#!/usr/bin/python
""" Vim Kick Pedal """

import os
import sys
import time
import evdev
import usb.core

VENDOR_ID = 0x04B4
PRODUCT_ID = 0x0002
GPIO_GET_CONFIG_CMD = 0xD8
GPIO_SET_CONFIG_CMD = 0xD9
GPIO_GET_VALUE_CMD = 0xDA
GPIO_SET_VALUE_CMD = 0xDB
GPIO_GET_LEN = 2
GPIO_SET_LEN = 1
DEVICE_TO_HOST = 0xC0
HOST_TO_DEVICE = 0x40
NOT_PRESSED = 0
PRESSED = 1
GPIO_PIN = 8
MONITOR_RATE = .25

###################################################################

class KickPedal(object):
    """ Object for interacting with the kick pedal itself """

    def __init__(self):
        if not os.geteuid() == 0:
            sys.exit("Must be run as root") # TODO: Make udev rule

        self.dev = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)
        if self.dev is None:
            raise ValueError("Cypress USB bridge not found")

        # TODO: Make udev rule
        if self.dev.is_kernel_driver_active(0) is True:
            self.dev.detach_kernel_driver(0)

        #self.dev.set_configuration() # TODO: Determine if this is correct

    def get_gpio(self, pin):
        """ Get gpio value of pin """
        ret = self.dev.ctrl_transfer(DEVICE_TO_HOST, GPIO_GET_VALUE_CMD, pin, 0, GPIO_GET_LEN)
        print(ret)
        assert ret[0] == 0
        return ret[1]

    # TODO: Figure this out
    #def set_gpio(self, pin, state):
    #    """ Set gpio value of pin """
    #    return
    #

#################################################################

class VimPedal(object):
    """ Uses the state of kick pedal to send keyboard commands """

    def __init__(self):
        self.pedal = KickPedal()
        self.state = self.pedal.get_gpio(GPIO_PIN)
        self.virtual_keyboard = evdev.UInput(events=None, name='vim-kick-pedal')

    def start(self):
        """ Start polling the pedal for new state """
        while True:
            if self.pedal_new_state():
                self.generate_keypress()
            time.sleep(MONITOR_RATE)

    def pedal_new_state(self):
        """ Return true if the pedal is in a new state """
        current_state = self.pedal.get_gpio(GPIO_PIN)
        if current_state != self.state:
            self.state = current_state
            return True

        return False

    def generate_keypress(self):
        """ Send a keypress depending on the new state """
        if self.state == PRESSED:
            self.send_keypress('KEY_I')
        else:
            self.send_keypress('KEY_ESC')

    def send_keypress(self, key):
        """ Send the actual keypress """
        # Send key down
        self.virtual_keyboard.write(evdev.ecodes.EV_KEY, evdev.ecodes.ecodes[key], 1)

        # Send key up
        self.virtual_keyboard.write(evdev.ecodes.EV_KEY, evdev.ecodes.ecodes[key], 0)

        # Fire write commands
        self.virtual_keyboard.syn()

########################################################

if __name__ == '__main__':
    pedal = VimPedal()
    pedal.start()
