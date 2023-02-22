let strip = neopixel.create(DigitalPin.P0, 300, NeoPixelMode.RGB)
strip.showRainbow(1, 180)
basic.forever(function () {
    strip.rotate(2)
    strip.show()
})
