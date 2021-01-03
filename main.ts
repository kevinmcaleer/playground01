input.buttonA.onEvent(ButtonEvent.Down, function on_button_a_down() {
    light.showAnimation(light.cometAnimation, 100)
    music.baDing.play()
    light.showAnimation(light.cometAnimation, 100)
})
input.buttonB.onEvent(ButtonEvent.Down, function on_button_b_down() {
    light.showAnimation(light.rainbowAnimation, 100)
    music.pewPew.play()
    music.pewPew.play()
    music.pewPew.play()
    light.showAnimation(light.rainbowAnimation, 100)
})
forever(function on_forever() {
    light.showAnimation(light.colorWipeAnimation, 100)
})
