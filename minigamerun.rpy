init 15 python:
    run_orgi_minigame_position = 0.0
    run_orgi_minigame_score = 0
    run_orgi_you_press_button = 0
    run_orgi_values = "She doesn't give a fuck."
    run_orgi_valuesbd = "{color=#950000}You're irritating her."
    run_orgi_valuesgd = "{color=#1e8e00}She's starting to get excited..."
    run_orgi_valuesgdt = "{color=#6e8e00}She loves it."
    run_orgi_difficulty = 1
    run_orgi_bar_speed = 100.0  # Speed of the point movement (pixels per second)
    run_orgi_last_time = 0.0    # Time of last update
    run_orgi_bar_width = 800    # Width of the bar in pixels

init:
    transform run_orgi_point_move(pos):
        subpixel True
        align(0.5, 0.2)
        xoffset pos - (run_orgi_bar_width / 2)

screen run_orgi_2_minigame:
    on "show" action Function(renpy.restart_interaction)
    timer 1.0 / 60.0 repeat True action Function(renpy.restart_interaction)  # Refresh screen 60 times per second

    if easymode:
        add "minigame/orgi_bar.png" align(0.5, 0.2)
    else:
        add "minigame/orgi_barhard.png" align(0.5, 0.2)

    python:
        current_time = renpy.get_game_runtime()
        delta_time = current_time - run_orgi_last_time00
        run_orgi_last_time = current_time

        run_orgi_minigame_position += run_orgi_bar_speed * delta_time * run_orgi_difficulty
        if run_orgi_minigame_position > run_orgi_bar_width:
            run_orgi_minigame_position = run_orgi_bar_width
            run_orgi_bar_speed = -run_orgi_bar_speed
            run_orgi_you_press_button = 0
        elif run_orgi_minigame_position < 0:
            run_orgi_minigame_position = 0
            run_orgi_bar_speed = -run_orgi_bar_speed
            run_orgi_you_press_button = 0

    add "minigame/orgi_point.png" at run_orgi_point_move(run_orgi_minigame_position)

    if not easymode:
        text "{size=-4}Difficulty: [run_orgi_difficulty:.1f]x" align(0.01, 0.02)
    if run_orgi_minigame_score > 0 and run_orgi_minigame_score < 3:
        text "[run_orgi_valuesgd]" align(0.5, 0.1)
    elif run_orgi_minigame_score < 0:
        text "[run_orgi_valuesbd]" align(0.5, 0.1)
    elif run_orgi_minigame_score >= 3:
        text "[run_orgi_valuesgdt]" align(0.5, 0.1)
    else:
        text "[run_orgi_values]" align(0.5, 0.1)

    if run_orgi_minigame_position <= 10 or run_orgi_minigame_position >= run_orgi_bar_width - 10:
        key ["K_SPACE", "mousedown_1"]:
            if run_orgi_you_press_button == 0:
                action [SetVariable("run_orgi_you_press_button", 1), Show("run_you_press_button_good"), Play("sound", "music/mon.mp3")]
            elif run_orgi_you_press_button == 1:
                if run_orgi_minigame_score < 4:
                    if easymode:
                        action [SetVariable("run_orgi_minigame_score", run_orgi_minigame_score + 1), SetVariable("run_orgi_you_press_button", 0), Show("run_you_press_button_good"), Play("sound", "music/mon.mp3")]
                    else:
                        action [SetVariable("run_orgi_minigame_score", run_orgi_minigame_score + 1), SetVariable("run_orgi_you_press_button", 0), SetVariable("run_orgi_difficulty", run_orgi_difficulty + 0.2), Show("run_you_press_button_good"), Play("sound", "music/mon.mp3")]
                else:
                    action Jump("nicoorgep5")
    else:
        key ["K_SPACE", "mousedown_1"] action [SetVariable("run_orgi_minigame_score", max(0, run_orgi_minigame_score - 1)), SetVariable("run_orgi_you_press_button", 0), Show("run_bad_button")]

screen run_you_press_button_good:
    text "{color=#1e8e00}Oooh...{/color}" at run_orgi_move_good
    timer 1.0 action Hide("run_you_press_button_good")

screen run_bad_button:
    text "{color=#950000}Oops...{/color}" at run_orgi_move_bad
    timer 1.0 action Hide("run_bad_button")

transform run_orgi_move_good:
    align(0.5,0.3)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0

transform run_orgi_move_bad:
    align(0.5,0.3)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0

label run_start_minigame:
    $ run_orgi_last_time = renpy.get_game_runtime()
    call screen run_orgi_2_minigame

label run_end_minigame:
    hide screen run_orgi_2_minigame
    $ renpy.pause(0.3)
    jump nicoorgep5