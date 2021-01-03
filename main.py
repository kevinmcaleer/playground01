def on_button_a_down():
    light.show_animation(light.comet_animation, 100)
    music.ba_ding.play()
    light.show_animation(light.comet_animation, 100)
input.button_a.on_event(ButtonEvent.DOWN, on_button_a_down)

def on_button_b_down():
    light.show_animation(light.rainbow_animation, 100)
    music.pew_pew.play()
    music.pew_pew.play()
    music.pew_pew.play()
    light.show_animation(light.rainbow_animation, 100)
input.button_b.on_event(ButtonEvent.DOWN, on_button_b_down)

def on_forever():
    light.show_animation(light.color_wipe_animation, 100)
forever(on_forever)
