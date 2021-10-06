# Clue Display and keyboard demo.
# Based off example code from Adafruit and arturo182.

import board
import terminalio
import displayio
from adafruit_clue import clue
import busio
from bbq10keyboard import BBQ10Keyboard, STATE_PRESS, STATE_RELEASE, STATE_LONG_PRESS
from adafruit_display_text import label

i2c = board.I2C()
kbd = BBQ10Keyboard(i2c)
kbd.backlight = 1

x_pos = 25
y_pos = 25

display = board.DISPLAY

splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(240, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x00FFFF #cyan

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(200, 200, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0xD3D3D3  # light grey
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)
splash.append(inner_sprite)

# Draw a label
#text_group = displayio.Group(scale=2, x=50, y=120)
#text = "Hello World!"
#text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00)
#text_group.append(text_area)  # Subgroup for text scaling
#splash.append(text_group)

while True:
    key_count = kbd.key_count
    if key_count > 0:
        key = kbd.key
        state = 'pressed'
        if key[0] == STATE_LONG_PRESS:
            state = 'held down'
        elif key[0] == STATE_RELEASE:
            state = 'released'

        if (state == 'pressed'):
            text_group = displayio.Group(scale=1, x=x_pos, y=y_pos)
            text = (key[1])
            text_area = label.Label(terminalio.FONT, text=text, color=0xFF0000)
            text_group.append(text_area)  # Subgroup for text scaling
            splash.append(text_group)

            x_pos = (x_pos + 8)
            if (x_pos > 200):
                x_pos = 25
                y_pos = (y_pos + 15)
