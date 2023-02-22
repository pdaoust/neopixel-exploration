strip: neopixel.Strip = None
strip.show_color(neopixel.colors(NeoPixelColors.RED))

def on_forever():
    global strip
    strip = neopixel.create(DigitalPin.P0, 24, NeoPixelMode.RGB)
basic.forever(on_forever)
