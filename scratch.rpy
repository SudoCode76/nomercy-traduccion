init python:
    import random

    def draw_scratch():
        chance = random.random()
        if chance < 0.6:
            return 0
        elif chance < 0.9:
            return 5
        else:
            return 35


screen scratch_screen():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text "Click!":
                xalign 0.5
            imagebutton:
                idle "Ep5/scratch_{0}_{1}.png".format(scratch_result, min(scratch_step + 1, 5))
                hover "Ep5/scratch_{0}_{1}.png".format(scratch_result, min(scratch_step + 1, 5))
                action If(scratch_step < 5,
                         SetVariable("scratch_step", scratch_step + 1),
                         Return())
                xalign 0.5

default scratch_result = 0
default scratch_step = 0

label scratch_card:
    $ scratch_result = draw_scratch()
    $ scratch_step = 0
    show screen scratch_screen

    $ ui.interact()

    hide screen scratch_screen

    if scratch_result == 0:
        "Nothing... Damn!"
    elif scratch_result == 5:
        $ money += 5
        "You won 5$!"
    else:
        $ money += 35
        "You won 35$!" with vpunch

    return