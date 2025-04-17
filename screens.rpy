################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
define centered = Character(None, what_style="centered_text", window_style="centered_window", window_background=None)

screen say(who, what):
    style_prefix "say"

    window:

        background Transform(style.window.background, alpha=persistent.say_window_alpha)
        ### IMPORTANT: The Transform() is holding the window background, and the alpha variable ties to our say window alpha

        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
                background None

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

default persistent.say_window_alpha = 1.0

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height 
    background None

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background None
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    line_spacing gui.preference("dialogue_spacing", 3)

screen hint(texthint):
    frame:
        background "images/Stats/Perk2.png"
        xalign 0
        yalign 0.1
        has vbox:
            xmaximum 0.15
            xpos 0.25
            text "{font=Jost.ttf}{size=-10}{color=#000}{i}{p}"
            text "{font=Jost.ttf}{size=-10}{color=#FFF}{i}[texthint!i]"


## Input screen ################################################################


screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################

define gui.game_menu_background = "MainBackground.png"

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            $ badge = i.kwargs.get("badge", None)
            textbutton i.caption:
                if i.args:
                     text_color i.args[0]
                insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                action [SensitiveIf( i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]
                if badge:
                                foreground Transform("badge " + badge, xpos=30, yalign=1.0)
    if timeout_label is not None:
        bar: #Creates a bar that drains as time runs out
            xalign 0.5
            ypos 980
            xsize 340
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
        timer timeout action [SetVariable("timeout", 8), SetVariable("timeout_label", None), Jump(timeout_label)]


screen rightchoice(items):
                             style_prefix "choice"
                             vbox:
                                 xalign 1.0
                                 for i in items:
                                     $ badge = i.kwargs.get("badge", None)
                                     textbutton i.caption:
                                         if i.args:
                                              text_color i.args[0]
                                         insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                                         action [SensitiveIf( i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]
                                         if badge:
                                                         foreground Transform("badge " + badge, xpos=30, yalign=1.0)
                             if timeout_label is not None:
                                 bar:
                                     xalign 0.5
                                     ypos 980
                                     xsize 340
                                     value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
                                 timer timeout action [SetVariable("timeout", 8), SetVariable("timeout_label", None), Jump(timeout_label)]


screen finalchoice(items):
                             style_prefix "choice"
                             vbox:
                                 xalign 1.0
                                 yalign 0.9
                                 xsize 240
                                 for i in items:
                                     textbutton i.caption:
                                         xsize 240
                                         if i.args:
                                              text_color i.args[0]
                                         insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                                         action [SensitiveIf( i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]


screen rightlowchoice(items):
                             style_prefix "choice"
                             vbox:
                                 xalign 1.0
                                 yalign 0.9
                                 for i in items:
                                     $ badge = i.kwargs.get("badge", None)
                                     textbutton i.caption:
                                         if i.args:
                                              text_color i.args[0]
                                         insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                                         action [SensitiveIf( i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]
                                         if badge:
                                                         foreground Transform("badge " + badge, xpos=30, yalign=1.0)
                             if timeout_label is not None:
                                 bar:
                                     xalign 0.5
                                     ypos 980
                                     xsize 340
                                     value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
                                 timer timeout action [SetVariable("timeout", 8), SetVariable("timeout_label", None), Jump(timeout_label)]

screen leftchoice(items):
                             style_prefix "choice"
                             vbox:
                                 xalign 0.1
                                 for i in items:
                                     $ badge = i.kwargs.get("badge", None)
                                     textbutton i.caption:
                                         if i.args:
                                              text_color i.args[0]
                                         insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                                         action [SensitiveIf( i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]
                                         if badge:
                                                         foreground Transform("badge " + badge, xpos=30, yalign=1.0)
                             if timeout_label is not None:
                                 bar:
                                     xalign 0.5
                                     ypos 980
                                     xsize 340
                                     value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
                                 timer timeout action [SetVariable("timeout", 8), SetVariable("timeout_label", None), Jump(timeout_label)]

screen tvchoice(items):
                             style_prefix "choice"
                             vbox:
                                 xalign 0.5
                                 yalign 0.1
                                 for i in items:
                                     $ badge = i.kwargs.get("badge", None)
                                     textbutton i.caption:
                                         if i.args:
                                              text_color i.args[0]
                                         insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                                         action [SensitiveIf( i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]
                                         if badge:
                                                         foreground Transform("badge " + badge, xpos=30, yalign=1.0)
                             if timeout_label is not None:
                                 bar:
                                     xalign 0.5
                                     ypos 980
                                     xsize 340
                                     value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
                                 timer timeout action [SetVariable("timeout", 8), SetVariable("timeout_label", None), Jump(timeout_label)]

screen fight(items):
    python:
        random_xalign = store._fight_menu_position['x']
        random_yalign = store._fight_menu_position['y']

    style_prefix "choice"
    vbox:
        xalign random_xalign
        yalign random_yalign
        for i in items:
            $ badge = i.kwargs.get("badge", None)
            textbutton i.caption:
                if i.args:
                    text_color i.args[0]
                background Frame("images/Ep6/border.png", Borders(10, 10, 10, 10))
                hover_background Frame("images/Ep6/border_hover.png", Borders(10, 10, 10, 10))
                insensitive_background Frame("gui/button/choice_insensitive.png", Borders(5, 5, 5, 5))
                action [SensitiveIf(i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]
                if badge:
                    foreground Transform(badge, xpos=0.5)

    if timeout_label is not None:
        bar:
            xalign 0.5
            ypos 980
            xsize 340
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
        timer timeout action [SetVariable("timeout", 8), SetVariable("timeout_label", None), Jump(timeout_label)]


screen dance(items):
    python:
        # Pobranie wcześniej ustawionej pozycji menu
        random_xalign2 = store._dance_menu_position['x']
        random_yalign2 = store._dance_menu_position['y']

    style_prefix "choice"
    vbox:
        xalign random_xalign2
        yalign random_yalign2
        for i in items:
            textbutton i.caption:
                if i.args:
                    text_color i.args[0]
                action [SensitiveIf(i.action), SetVariable("timeout", 8), SetVariable("timeout_label", None), i.action]

    if timeout_label is not None:
        bar:
            xalign 0.5
            ypos 980
            xsize 340
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=timeout)
        timer timeout action [SetVariable("timeout", 2), SetVariable("timeout_label", None), Jump(timeout_label)]






## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 805
    yanchor 0.7

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    font "Staatliches.ttf"


style fight_vbox is vbox
style fight_button is fightbutton
style fight_button_text is fightbutton_text

style fight_vbox:
    xalign 0.5
    ypos 805
    yanchor 0.7

    spacing gui.choice_spacing

style fight_button is default:
    properties gui.button_properties("fight_button")

style fight_button_text is default:
    properties gui.button_text_properties("fight_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.

        hbox:
            style_group "quick"

            xalign 0.5
            yalign 1.0

            ## https://www.renpy.org/doc/html/self_voicing.html#creator-concerns
            # imagebutton auto "foo.png" action None() alt "foo"
            textbutton _("Back") action Rollback() alt "Back"
            textbutton _("History") action ShowMenu('history') alt "History"
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) alt "Skip"
            textbutton _("Auto") action Preference("auto-forward", "toggle") alt "Auto"
            textbutton _("Save") action ShowMenu('save') alt "Save"
            textbutton _("Q.Save") action QuickSave() alt "Quick Save"
            textbutton _("Q.Load") action QuickLoad() alt "Quick Load"
            textbutton _("Options") action ShowMenu('preferences') alt "Options"

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################


init python:
    config.movie_mixer = "sfx"

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("{size=+8}Start") action Start() alt "Start"

        else:

            textbutton _("Save") action ShowMenu("save") alt "Save"

        textbutton _("Load") action ShowMenu("load") alt "Load"

        textbutton _("Settings") action ShowMenu("preferences") alt "Preferences"

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True) alt "End Replay"

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu() alt "Main Menu"


        if main_menu:

            textbutton _("Gallery") action ShowMenu("replay_gallery") alt "Extras"
            textbutton _("Achievements") action ShowMenu("achievements_screen") alt "Achievements"
#             textbutton _("{color=#00FFFF}STEAM WISHLIST") action OpenURL ("https://store.steampowered.com/app/3299570/No_Mercy/") alt "Website" at pulse_blue
#             textbutton _("{color=f00}Patreon") action OpenURL ("https://www.patreon.com/zerat") alt "Patreon"
#             textbutton _("{color=#79b6c9}SubscribeStar") action OpenURL ("https://subscribestar.adult/zeratgames") alt "SubscribeStar"
            textbutton _("YouTube") action OpenURL ("https://www.youtube.com/@ZeratGames") alt "YouTube"
            textbutton _("Website") action OpenURL ("https://zeratgames.com") alt "Website"


        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu) alt "Quit"

transform pulse_blue:
    linear 1.0 matrixcolor TintMatrix("#89FFFF")
    linear 1.0 matrixcolor TintMatrix("#111116")
    repeat

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation
    ### Note: I *personally* always separate the navigation of the main menu
    ### and the game menu so the main menu can be more flexible in design. To
    ### do so, comment out "use navigation" and put your buttons in using a vbox
    ### or hbox, or however you want to lay those out.


    if gui.show_name:

        vbox:

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty

style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True



style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################


screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180


style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            ## Standard Preferences
            hbox:

                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window") alt "Set Display to Windowed"
                        textbutton _("Fullscreen") action Preference("display", "fullscreen") alt "Set Display to Full Screen"

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable") alt "Disable Rollback Side"
                    textbutton _("Left") action Preference("rollback side", "left") alt "Set Rollback Side to Left"
                    textbutton _("Right") action Preference("rollback side", "right") alt "Set Rollback Side to Right"

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle") alt "Skip Unseen Text"
                    label _("Font")
                    textbutton _("{font=Jost.ttf}Jost (default)") action  gui.SetPreference("font", "Jost.ttf")
                    textbutton _("{font=Staatliches.ttf}Staatliches") action gui.SetPreference("font", "Staatliches.ttf")
                    textbutton _("{font=LilitaOne.ttf}LilitaOne") action  gui.SetPreference("font", "LilitaOne.ttf")


            null height (4 * gui.pref_spacing)


          

                ## This shows Ren'Py's built-in accessibility menu. This can also be displayed by pressing "A" on the keyboard when playing on a PC. As this option can break the way the game is displayed and also does not support translation as of the latest Ren'Py build, you may want to hide the option.
                # textbutton _("More Options...") action Show("_accessibility")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            alt "Mute All"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

## History screen ##############################################################
##


init python:
    if preferences.get_mixer("music") != 0.75:  # So we don't erase the player's preference
        preferences.set_mixer("music", 0.75)

screen history():

    tag menu

    predict False

    frame:

        style_prefix "history"

        label _("History")

        left_margin 200
        right_margin 200
        top_margin 50
        bottom_margin 50

        left_padding 50
        right_padding 100
        top_padding 150
        bottom_padding 100

        vpgrid:

            cols 1
            yinitial 1.0

            draggable True
            mousewheel True
            scrollbars "vertical"

            for h in _history_list:

                window:

                    ## This lays things out properly if history_height is None.
                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"

                            ## Take the color of the who text from the Character, if
                            ## set.
                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what

            if not _history_list:

                text "The dialogue history is empty." line_spacing 10


        textbutton _("Return") action Return() yalign 1.1 xalign 1.0 alt "Return"


define gui.history_allow_tags =  { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    color "#ffffff"

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    ypos -100
    size gui.label_text_size




################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action alt "Yes"
                textbutton _("No") action no_action alt "No"

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"
    color gui.accent_color

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color gui.accent_color


# Achievki
screen achievements_screen():
    tag menu
    vbox:
        xalign 0.5
        spacing 10
        text "ACHIEVEMENTS" size 50 xalign 0.5 font "AbrilFatface.ttf"

        grid 8 4:
            spacing 30

            for i in range(1,33):

                    if getattr(persistent, "achievement{}".format(i), False):
                        add "Achiev{}".format(i) xysize (200,200)
                    else:
                        add "Achiev{}_lock".format(i) xysize (200,200)



        hbox:
                xalign 0.5
                textbutton "Back" action Return() style "menu_button" background "#000"
                if getattr(persistent, "tomstat", True) or getattr(persistent, "gstwac", True):
                        spacing 50
                        textbutton "Secret Achievements" action ShowMenu("achievements_secret") style "menu_button" background "#000" xalign 0.9

screen achievements_secret():
     tag menu
     vbox:
         xalign 0.5
         spacing 10
         text "SECRET ACHIEVEMENTS" size 50 xalign 0.5 font "AbrilFatface.ttf"

         grid 3 3:
            spacing 30
            if getattr(persistent, "tomstat", True):
                add "s3cr3ta1" xysize (200,200)
            if getattr(persistent, "gstwac", True):
                add "gstw" xysize (200,200)

         hbox:
                xalign 0.5
                textbutton "Back" action ShowMenu("achievements_screen") style "menu_button" background "#000"

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:

#         background Transform(style.nvl_window.background, alpha=persistent.say_window_alpha)
        ### IMPORTANT: The Transform() is holding the window background, and the alpha variable ties to our say window alpha

        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    # background "gui/nvl.png"
    background gui.preference("NVLtextbox", "gui/nvl_1.png")
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Prefs") action ShowMenu("preferences")


style say_dialogue:
    variant "small"
    size gui.preference("phone_size", 40)

style window:
    variant "small"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background gui.preference("m_NVLtextbox", "gui/phone/nvl_1.png") #"gui/phone/nvl.png"

style main_menu_frame:
    variant "small"

style game_menu_outer_frame:
    variant "small"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
