screen splash_settings():
    
    frame:

        align 0.5, 0.5
        left_margin 200
        right_margin 200
        top_margin 150
        bottom_margin 150

        left_padding 100
        right_padding 100
        top_padding 50
        bottom_padding 50

        vbox:

            xalign 0.5
            spacing 30

            label _("Accessibility Settings") xalign 0.5
            label _("These options can be changed again at any time in the menu.") xalign 0.5

            hbox:

                # xfill True
                xalign 0.5

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Toggles") xalign 0.5

                    textbutton _("Audio Titles") action ToggleVariable("persistent.sound_captions") alt "Toggle Sound Captions" xalign 0.5
                    textbutton _("Image Descriptions") action ToggleVariable("persistent.image_captions") alt "Toggle Image Descriptions" xalign 0.5
                    textbutton _("Screenshake") action ToggleField(persistent,"screenshake",true_value=True,false_value=False) alt "Toggle Screen Shake" xalign 0.5

                    ## Self-voicing does not work on smartphone devices, so this option only shows if the user is playing on a PC.
                    if renpy.variant("pc"):

                        textbutton _("Self-Voicing") action Preference("self voicing", "toggle") alt "Toggle Self-Voicing" xalign 0.5

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Typeface") xalign 0.5

                    textbutton _("NotoSans") action [gui.SetPreference("font", "gui/fonts/NotoSans-Regular.ttf"), SetVariable("typeface", "NotoSans"), gui.SetPreference("dialogue_spacing", 2)] alt "Change to NotoSans" xalign 0.5

                    textbutton _("DejaVuSans") action [gui.SetPreference("font", "DejaVuSans.ttf"), SetVariable("typeface", "DejaVuSans"), gui.SetPreference("dialogue_spacing", 2.01)] alt "Change to DejaVuSans" xalign 0.5

                    textbutton _("OpenDyslexic") action [gui.SetPreference("font", "_OpenDyslexic3-Regular.ttf"), SetVariable("typeface", "OpenDyslexic"), gui.SetPreference("dialogue_spacing", -4)]  alt "Change to OpenDyslexic" xalign 0.5
                    ## Note: Having so many actions set to a single radio button
                    ## will cause some of the preferences in the same category to appear
                    ## to be all selected, causing players some confusion. Some numbers
                    ## have been set to 2.01 to prevent this from happening.

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Text Color") xalign 0.5
                    
                    textbutton _("White") action gui.SetPreference("color", "#ffffff") alt "Change to White Text" xalign 0.5
                    textbutton _("Cream") action gui.SetPreference("color", "#FBF0D9") alt "Change to Cream Text" xalign 0.5
                    textbutton _("Black") action gui.SetPreference("color", "#000000") alt "Change to Black Text" xalign 0.5

            hbox:

                #xfill True
                xalign 0.5

                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Font Size") xalign 0.5

                    if renpy.variant("pc"):
                        textbutton _("Large") action gui.SetPreference("size", 33) alt "Change to Large Size Text" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("size", 31) alt "Change to Regular Size Text" xalign 0.5

                    elif renpy.variant("mobile"):

                        if typeface == "OpenDyslexic":
                            textbutton _("Large") action gui.SetPreference("phone_size", 32) xalign 0.5
                            textbutton _("Regular") action gui.SetPreference("phone_size", 30) xalign 0.5
                            ## Note: due to the unique nature of the OpenDyslexic font, it needs
                            ## to be just slightly smaller so as to not break the GUI

                        else:
                            textbutton _("Large") action gui.SetPreference("phone_size", 42) xalign 0.5
                            textbutton _("Regular") action gui.SetPreference("phone_size", 40) xalign 0.5
                
                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Textbox") xalign 0.5

                    if renpy.variant("pc"):

                        textbutton _("Black") action [gui.SetPreference("ADVtextbox", "gui/textbox_1.png"), gui.SetPreference("NVLtextbox", "gui/nvl_1.png")] alt "Change to Black Textbox" xalign 0.5
                        textbutton _("White") action [gui.SetPreference("ADVtextbox", "gui/textbox_2.png"), gui.SetPreference("NVLtextbox", "gui/nvl_2.png")]  alt "Change to White Textbox" xalign 0.5

                    elif renpy.variant("mobile"):

                        textbutton _("Black") action [gui.SetPreference("m_ADVtextbox", "gui/phone/textbox_1.png"), gui.SetPreference("m_NVLtextbox", "gui/phone/nvl_1.png")] xalign 0.5
                        textbutton _("White") action [gui.SetPreference("m_ADVtextbox", "gui/phone/textbox_2.png"), gui.SetPreference("m_NVLtextbox", "gui/phone/nvl_2.png")] xalign 0.5
            
                vbox:

                    spacing 5

                    style_prefix "radio"
                    label _("Line Spacing") xalign 0.5

                    if typeface == "OpenDyslexic":

                        textbutton _("Taller") action gui.SetPreference("dialogue_spacing", -2) alt "Change the height of the space between lines of dialogue" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("dialogue_spacing", -4) alt "Change the height of the space between lines of dialogue" xalign 0.5

                    elif typeface == "DejaVuSans":

                        textbutton _("Taller") action gui.SetPreference("dialogue_spacing", 4.01) alt "Change the height of the space between lines of dialogue" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("dialogue_spacing", 2.01) alt "Change the height of the space between lines of dialogue" xalign 0.5

                    else:

                        textbutton _("Taller") action gui.SetPreference("dialogue_spacing", 4) alt "Change the height of the space between lines of dialogue" xalign 0.5
                        textbutton _("Regular") action gui.SetPreference("dialogue_spacing", 2) alt "Change the height of the space between lines of dialogue" xalign 0.5
 
            textbutton _("Confirm") action Return() xalign 0.5


## These background buttons are 480x270
image room_button = im.FactorScale("bg/room.jpg", 0.25)
image office_button = im.FactorScale("bg/future_office.jpg", 0.25)
image beach_button = im.FactorScale("bg/sort_of_beautiful_beach_day.jpg", 0.25)
image bglock_button = "gui/button/bg_locked.jpg"

## These sprite buttons are 290x290
image ehappy_button = Crop((170, 245, 290, 290), "eileen happy")
image eneutral_button = Crop((170, 245, 290, 290), "eileen neutral")
image esurprised_button = Crop((170, 245, 290, 290), "eileen surprised")
image eupset_button = Crop((170, 245, 290, 290), "eileen upset")
image eangry_button = Crop((170, 245, 290, 290), "eileen angry")
image spritelock_button = "gui/button/sprite_locked.jpg"

init python:

    g_bg = Gallery()

    # Backgrounds for the BG Gallery
    g_bg.button("room")
    g_bg.unlock_image("room") 

    g_bg.button("office")
    g_bg.image("future_office")
    g_bg.unlock("future_office")

    g_bg.button("beach")
    g_bg.image("sort_of_beautiful_beach_day")
    g_bg.unlock("sort_of_beautiful_beach_day")

    # Sprites for the Sprite Gallery
    # We put a background in the first spot so Eileen isn't floating in a void.

    g_sprite = Gallery()

    g_sprite.button("eileen happy")
    g_sprite.unlock_image("room", "eileen happy")

    g_sprite.button("eileen neutral")
    g_sprite.unlock_image("room", "eileen neutral")

    g_sprite.button("eileen surprised")
    g_sprite.unlock_image("room", "eileen surprised")

    g_sprite.button("eileen upset")
    g_sprite.image("room", "eileen upset")
    g_sprite.unlock("room", "eileen upset")

    g_sprite.button("eileen angry")
    g_sprite.image("room", "eileen angry")
    g_sprite.unlock("room", "eileen angry")

    # The button used for locked images
    g_bg.locked_button = "bglock_button"
    g_sprite.locked_button = "spritelock_button"

    # The transition used when switching images.
    g_bg.transition = dissolve
    g_sprite.transition = dissolve

    # MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Add music files.
    mr.add("audio/music/Careless-Summer_Looping.mp3", always_unlocked=True)
    mr.add("audio/music/Future-Business_v001.mp3")
    mr.add("audio/music/Sculpture-Garden_Looping.mp3")
    mr.add("audio/music/The-Concrete-Bakes_Looping.mp3")

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.

screen extras_navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing



        textbutton _("Gallery") action ShowMenu("replay_gallery") alt "Gallery"




        textbutton _("Return") action Return() alt "Return"

## Extras Menu screen #######################################
##
## This is the same as the Game Menu screen, but just for the Extras.

screen extras_menu(title, scroll=None, yinitial=0.0):

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

    label title

    use extras_navigation


## Background Gallery screen ############################################################
##
## This is a simple screen that shows buttons that display a background.
## You can easily adapt this screen to make a CG or concept art screen.

screen bg_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Background Gallery"):

        grid 1 3:

            xfill True
            yfill True

            ## Call make_button to show a particular button.
            # add g_bg.make_button("background", "bg_button")

            add g_bg.make_button("room", "room_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("office", "office_button", xalign=0.5, yalign=0.5)
            add g_bg.make_button("beach", "beach_button", xalign=0.5, yalign=0.5)


## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.

screen replay_gallery():

    tag menu

    ## This use statement includes the extras_menu screen inside this one.
    use extras_menu("Gallery"):

        vbox:

            xalign 0.5
            yalign 0.5

            # The buttons that play each section.
            textbutton "Soon" action Replay("Soon")


            null height 20



