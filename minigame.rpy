init 15 python:
    orgi_minigame_bar = 90.0
    orgi_minigame_score = 0
    orgi_you_press_button = 0
    orgi_values = "She doesnt give a fuck."
    orgi_valuesbd = "{color=#950000}You're irritating her."
    orgi_valuesgd = "{color=#1e8e00}She's starting to get excited..."
    orgi_valuesgdt = "{color=#6e8e00}She loves it."
    orgi_difficulty = 1
    orgi_bar_speed = 90.0
    orgi_last_time = 0.0

init:
    transform orgi_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,0.12)
        rotate frp

screen orgi_2_minigame:
    on "show" action Function(renpy.restart_interaction)
    timer 1.0 / 60.0 repeat True action Function(renpy.restart_interaction)

    if easymode:
        add "minigame/orgi_bar.png" align(0.5,0.2)
    else:
        add "minigame/orgi_barhard.png" align(0.5,0.2)

    python:
        current_time = renpy.get_game_runtime()
        delta_time = current_time - orgi_last_time
        orgi_last_time = current_time

        orgi_minigame_bar += orgi_bar_speed * delta_time * orgi_difficulty
        if orgi_minigame_bar > 90:
            orgi_minigame_bar = 90
            orgi_bar_speed = -orgi_bar_speed
            orgi_you_press_button = 0
        elif orgi_minigame_bar < -90:
            orgi_minigame_bar = -90
            orgi_bar_speed = -orgi_bar_speed
            orgi_you_press_button = 0

    add "minigame/orgi_point.png" at orgi_point_move(orgi_minigame_bar)

    if not easymode:
        text "{size=+2}Difficulty: [orgi_difficulty:.1f]x" align(0.5,0.01)
        text "{size=-2}GAIN SPEED PERK\nComplete with difficulty 2.2x+{/size}" align(0.01,0.95)
    if orgi_minigame_score > 0 and orgi_minigame_score < 3:
        text "[orgi_valuesgd]" align(0.5,0.1)
    elif orgi_minigame_score < 0:
        text "[orgi_valuesbd]" align(0.5,0.1)
    elif orgi_minigame_score >= 3:
        text "[orgi_valuesgdt]" align(0.5,0.1)
    else:
        text "[orgi_values]" align(0.5,0.1)

    if easymode:
        if orgi_minigame_bar >= -14 and orgi_minigame_bar <= 14:
            key ["K_SPACE","mousedown_1"]:
                if orgi_you_press_button == 0:
                    if orgi_minigame_score < 4:
                        action [SetVariable("orgi_minigame_score", orgi_minigame_score +  1), SetVariable("orgi_you_press_button", orgi_you_press_button + 1), Show("you_press_button_good"), Play("sound", "music/mon.mp3")]
                    else:
                        action Jump("nicoorgep5")
                elif orgi_you_press_button == 1:
                    action SetVariable("orgi_minigame_score", orgi_minigame_score + 0)
        else:
           key ["K_SPACE","mousedown_1"] action [SetVariable("orgi_minigame_score", 0), Show("bad_button")]

    else:
        if orgi_minigame_bar >= -7 and orgi_minigame_bar <= 7:
            key ["K_SPACE","mousedown_1"]:
                if orgi_you_press_button == 0:
                    if orgi_minigame_score < 4 and orgi_minigame_score >= -2:
                        action [SetVariable("orgi_minigame_score", orgi_minigame_score +  1), SetVariable("orgi_you_press_button", orgi_you_press_button + 1), SetVariable("orgi_difficulty", orgi_difficulty +  0.2), Show("you_press_button_good"), Play("sound", "music/mon.mp3")]
                    elif orgi_minigame_score < -2:
                        action Jump("cameramovefailquest")
                    else:
                        action Jump("nicoorgep5")
                elif orgi_you_press_button == 1:
                    if orgi_minigame_score < -2:
                        action Jump("cameramovefailquest")
                    else:
                        action SetVariable("orgi_minigame_score", orgi_minigame_score + 0)
        else:
            key ["K_SPACE","mousedown_1"]:
                action [SetVariable("orgi_minigame_score", orgi_minigame_score-2), Show("bad_button"), If(orgi_minigame_score < 0, Jump("cameramovefailquest"))]

screen you_press_button_good:
    text "{color=#1e8e00}Oooh...{/color}" at orgi_move_good
    timer 1.0 action Hide("you_press_button_good")

screen bad_button:
    text "{color=#950000}Oops...{/color}" at orgi_move_bad
    timer 1.0 action Hide("bad_button")

transform orgi_move_good:
    align(0.5,0.3)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0

transform orgi_move_bad:
    align(0.5,0.3)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0

label start_minigame:
    $ orgi_last_time = renpy.get_game_runtime()
    call screen orgi_2_minigame

label end_minigame:
    hide screen orgi_2_minigame
    $ renpy.pause(0.3)
    jump nicoorgep5