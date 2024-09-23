# Scroll library - use this for scrolling

# SPDX-FileCopyrightText: 2020 Jeff Epler for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# This example implements a simple two line scroller using
# Adafruit_CircuitPython_Display_Text. Each line has its own color
# and it is possible to modify the example to use other fonts and non-standard
# characters.

import adafruit_display_text.label
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio

# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()

# This next call creates the RGB Matrix object itself. It has the given width
# and height. bit_depth can range from 1 to 6; higher numbers allow more color
# shades to be displayed, but increase memory usage and slow down your Python
# code. If you just want to show primary colors plus black and white, use 1.
# Otherwise, try 3, 4 and 5 to see which effect you like best.
#
# Updated to work with Matrix Potal M4
# If you have a matrix with a different width or height, change that too.
# If you have a 16x32 display, try with just a single line of text.
matrix = rgbmatrix.RGBMatrix(
    width=64, bit_depth=4,
    rgb_pins=[
        board.MTX_R1,
        board.MTX_G1,
        board.MTX_B1,
        board.MTX_R2,
        board.MTX_G2,
        board.MTX_B2
    ],
    addr_pins=[
        board.MTX_ADDRA,
        board.MTX_ADDRB,
        board.MTX_ADDRC,
        board.MTX_ADDRD
    ],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE
)


# Associate the RGB matrix with a Display so that we can use displayio features
# Updated to work for Matrix Portal M4
display = framebufferio.FramebufferDisplay(matrix)

# Create two lines of text to scroll. Besides changing the text, you can also
# customize the color and font (using Adafruit_CircuitPython_Bitmap_Font).
# To keep this demo simple, we just used the built-in font.
# The Y coordinates of the two lines were chosen so that they looked good
# but if you change the font you might find that other values work better.
def scroll_line1(line_text):
    line = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0xff0000,
        text=line_text)
    line.x = display.width
    line.y = 8
    return line

def scroll_line2(line_text):
    line = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=0x0080ff,
        text=line_text)
    line.x = display.width
    line.y = 24
    return line

# Put each line of text into a Group, then show that group.
def scroll_display(line1, line2):
    g = displayio.Group()
    g.append(line1)
    g.append(line2)
    display.root_group = g
    return display

# This function will scoot one label a pixel to the left and send it back to
# the far right if it's gone all the way off screen. This goes in a function
# because we'll do exactly the same thing with line1 and line2 below.
def scroll(line):
    line.x = line.x - 1
    line_width = line.bounding_box[2]
    if line.x < -line_width:
        line.x = display.width

# This function scrolls lines backwards.  Try switching which function is
# called for line2 below!
def reverse_scroll(line):
    line.x = line.x + 1
    line_width = line.bounding_box[2]
    if line.x >= display.width:
        line.x = -line_width


# The code below should be copied and used in your main program. It is commented out below to prevent infinite loops

# Scroll some text
# Do this first
#line1 = scroll_text.scroll_line1("This is a test") # Define the first line
#line2 = scroll_text.scroll_line2("Whoa Kenzo look at this!") # Define the 2nd line
#display = scroll_text.scroll_display(line1, line2) # create a display object
#while True:
#    scroll_text.scroll(line1) # These two lines call the scroll function
#    scroll_text.scroll(line2)
    #reverse_scroll(line2)
#    display.refresh(minimum_frames_per_second=0)

