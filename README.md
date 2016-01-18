# Vim Kick Pedal
[![License](http://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

This project allows you to enter and exit VIM's insert mode using a rock band pedal! Similar to Alexander Levchuk's [project](https://github.com/alevchuk/vim-clutch). 


## Materials

### Required materials:
+ PSOC 4 prototyping kit: $4 + shipping

These can be bought from multiple sources. I got mine from [Cypress](http://www.cypress.com/documentation/development-kitsboards/psoc-4-cy8ckit-049-4xxx-prototyping-kits), but you might get a better deal on shipping elsewhere. We will only be using the usb to serial bridge so you can use the rest of the prototyping kit for another project.
+ Rock Band pedal (Or a similar pedal)

I found my rock band pedal at a thrift shop for $2. Many other pedals could work though since the implementation works by reading a GPIO.

+ Through hole resistors (I use a 220 Ohm resistor)
+ Through hole LED

### Optional materials:
+ USB cable

The USB cable can be used to ensure the prototyping kit doesn't easily fall out of a USB port. It also an easy way to extend the length of your vim pedal. I had Male USB 2.0 type A cable with a broken connector on one side that I used. 
+ Female Stereo cable

This cable makes it easy to plug the Rock Band pedal in to the prototyping board. It also extends the cable on the pedal.


## Equipment

+ Soldering Iron and Solder

## Hardware Setup

TODO: Schematic / pictures

## Software Setup

TODO: Need a udev rule

## License

This project is MIT licensed. Read [LICENSE.md](LICENSE.md) for more details on the MIT license.
