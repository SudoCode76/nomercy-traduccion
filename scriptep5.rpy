default toughguy = False
default achValid5 = 0
default nicsmoke = 0
default nicdomep5 = 4
default niclustep5 = 4
default smokesil = 0
default legsep5 = 0
default howareyouep5choice = 0
default smslust = 0
default smsnosleep_choice = 0
default smsthink_choice = 0
default nosmsaunt = 0
default cigthrow = False
default speedguy = 0
default selltommydrugs = 0
default shopclicked = False
default shopblindfold = False
default phonelive = True
default tommyep5call1 = False
default daddyep5call1 = False
default accountboosted = 0
default tommyaskyouep5 = False
default evewetdreamsscene = False
default tommyjoinsep5mtom = False
default mtommyep5enterdoor = False
default shoppackage = False
default tommymiddlefing = False
default tommyep5peeping = False
default shopalcoholep5weak = False
default shopalcoholep5strong = False
default shopsexyep5wear = False
default mtommyblindfoldon = False
default tommymomhas = 1
default tomscstat = 0
default tommydidntanswer = False
default tommylistentomusic = False
default tommyhelpwithcode = False
default mtomcinm = False
default mtomsharing = False
default mtomconface = False
default auntgetblindfold = False
default auntgetredwine = False
default auntgetwhitewine = False
default tommytellcodewhilecall = False
default auntep5love = False
default auntep5angry = False
default auntep5middle = False
default walletyours = 0
default showerdomnic = 0
default showerlustnic = 0
default cigcount = 0
default auntfinish = False
default auntnothing = False
default nicgetredwine = False
default nicgetsexylingerie = False
default nicgetwhitewine = False
default nicnormalwinescene = False
default nicangrywinescene = False
default winemerlot = False
default winecabernet = False
default garyep5call1 = False
default garyfriend = 0
default garrydidntbuy = True
default garrypumpmuscles = False
default nicdomrouteep5 = False
default scratchnumber = 0
default z3kr3t = False

define idle_time = 20.0

image scrolling_image = "Ep5/55002.png"

# Create a transform for the scrolling effect
transform scroll_up():
    ypos 0  # Start at the bottom of a 1080p screen
    linear 8.0 ypos -3240  # Move up over 6 seconds


label idle_message():
        hide screen idle_czek
        $ tomscstat = 1
        if not persistent.tomstat:
            show s3cr3ta1 at achievment with easeintop:
                    zoom 0.5
                    rotate_animation

            "S3CR3T 4CH13VM3NT{p}\"You are a true connoisseur of good music.\"."
            hide s3cr3ta1
            $ persistent.tomstat = True
        scene 52150a with dissolve
        stop sound
        t "Oops... too late."
        jump mtommydoormenu

screen idle_czek():
    timer idle_time action Jump("idle_message") repeat True


define n = Character("???", color="#1cfc03")

image ep5nick11 = Movie(channel="movie_dp", play = "images/Ep5/ep5nick11.webm", loop=False, image="500106")
image ep5nick12 = Movie(channel="movie_dp", play = "images/Ep5/ep5nick12.webm", loop=False, image="500107")
image ep5nick13 = Movie(channel="movie_dp", play = "images/Ep5/ep5nick13.webm")
image ep5nick14 = Movie(channel="movie_dp", play = "images/Ep5/ep5nick14.webm")
image ep5nick14a = Movie(channel="movie_dp", play = "images/Ep5/ep5nick14a.webm")
image ep5nick15 = Movie(channel="movie_dp", play = "images/Ep5/ep5nick15.webm")
image 5batk = Movie(channel="movie_dp", play = "images/Ep5/5batk.webm", loop=False, image="5batkimg")
image 5brew = Movie(channel="movie_dp", play = "images/Ep5/5brew.webm", loop=False, image="5b0033a")
image organ58 = Movie(channel="movie_dp", play = "images/Ep5/organ58.webm", loop=False, image="organ58img")
image nicoep5orgmov = Movie(channel="movie_dp", play = "images/Ep5/nicoep5orgmov.webm", loop=False, image="nicoorgfull")
image mccmep5sofa = Movie(channel="movie_dp", play = "images/Ep5/mccmep5sofa.webm", loop=False, image="epniccmfinalframe")
image cameramoveep51 = Movie(channel="movie_dp", play = "images/Ep5/cameramoveep51.webm", loop=False)
image mtomtomstart = Movie(channel="movie_dp", play = "images/Ep5/mtomtomstart.webm", loop=False, image="5035743")
image mtomtomcm = Movie(channel="movie_dp", play = "images/Ep5/mtomtomcm.webm", loop=False, image="50363")
image mtommccum = Movie(channel="movie_dp", play = "images/Ep5/mtommccum.webm", loop=False, image="mccummtom29")
image 5bbj = Movie(channel="movie_dp", play = "images/Ep5/5bbj.webm")
image cameramoveep52 = Movie(channel="movie_dp", play = "images/Ep5/cameramoveep52.webm")
image 5bbj2 = Movie(channel="movie_dp", play = "images/Ep5/5bbj2.webm")
image cigep5 = Movie(channel="movie_dp", play = "images/Ep5/cigep5.webm")
image anpho1 = Movie(channel="movie_dp", play = "images/Ep5/anpho1.webm")
image anpho2 = Movie(channel="movie_dp", play = "images/Ep5/anpho2.webm")
image morningmov = Movie(channel="movie_dp", play = "images/Ep5/morningmov.webm")
image mtomep5cam1 = Movie(channel="movie_dp", play = "images/Ep5/mtomep5cam1.webm")
image nicfing1 = Movie(channel="movie_dp", play = "images/Ep5/nicfing1.webm")
image nicfing2 = Movie(channel="movie_dp", play = "images/Ep5/nicfing2.webm")
image 50210anim = Movie(channel="movie_dp", play = "images/Ep5/50210anim.webm")
image nicbjcouch1 = Movie(channel="movie_dp", play = "images/Ep5/nicbjcouch1.webm")
image mtomep5sx1 = Movie(channel="movie_dp", play = "images/Ep5/mtomep5sx1.webm")
image mtomep5sx2 = Movie(channel="movie_dp", play = "images/Ep5/mtomep5sx2.webm")
image mtomep5cam1 = Movie(channel="movie_dp", play = "images/Ep5/mtomep5cam1.webm")
image mtomep5cam2 = Movie(channel="movie_dp", play = "images/Ep5/mtomep5cam2.webm")
image mtomtom = Movie(channel="movie_dp", play = "images/Ep5/mtomtom.webm")
image mtomtom2 = Movie(channel="movie_dp", play = "images/Ep5/mtomtom2.webm")
image mtomep5caress = Movie(channel="movie_dp", play = "images/Ep5/mtomep5caress.webm")
image mtomsolobjwithg = Movie(channel="movie_dp", play = "images/Ep5/mtomsolobjwithg.webm")
image mtomsolobjwithout = Movie(channel="movie_dp", play = "images/Ep5/mtomsolobjwithout.webm")
image mtomsolo = Movie(channel="movie_dp", play = "images/Ep5/mtomsolo.webm")
image mtomskside5ep = Movie(channel="movie_dp", play = "images/Ep5/mtomskside5ep.webm")
image mtomcminmoutwithout = Movie(channel="movie_dp", play = "images/Ep5/mtomcminmoutwithout.webm", loop=False, image="warga")
image mtomcminbf = Movie(channel="movie_dp", play = "images/Ep5/mtomcminbf.webm", loop=False, image="last")
image mtomcminglass = Movie(channel="movie_dp", play = "images/Ep5/mtomcminglass.webm", loop=False, image="last2")
image cofwithout = Movie(channel="movie_dp", play = "images/Ep5/cofwithout.webm", loop=False, image="50362cmwithoutfinal2")
image cofwithg = Movie(channel="movie_dp", play = "images/Ep5/cofwithg.webm", loop=False, image="50362withgfinal2")
image eveep5finalsuck = Movie(channel="movie_dp", play = "images/Ep5/eveep5finalsuck.webm")
image antnight = Movie(channel="movie_dp", play = "images/Ep5/antnight.webm", loop=False, image="antnighbj00")
image nicep5last1 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last1.webm", loop=False, image="nicep5last1_frame")
image nicep5last2 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last2.webm", loop=False, image="nicep5last2_frame")
image nicep5last4 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last4.webm", loop=False, image="nicep5last4_frame")
image nicep5last6 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last6.webm", loop=False, image="nicep5last6_frame")
image lastsleep = Movie(channel="movie_dp", play = "images/Ep5/lastsleep.webm", loop=False, image="lastsleep59")
image anep5lick2 = Movie(channel="movie_dp", play = "images/Ep5/anep5lick2.webm", loop=False, image="frameanlck")
image anep5lick4 = Movie(channel="movie_dp", play = "images/Ep5/anep5lick4.webm", loop=False, image="frameorg01")
image auntsxnocm = Movie(channel="movie_dp", play = "images/Ep5/auntsxnocm.webm", loop=False, image="auntsxnocm_frame")
image anep5grab = Movie(channel="movie_dp", play = "images/Ep5/anep5grab.webm", loop=False, image="anep5grab_frame")
image garryspace = Movie(channel="movie_dp", play = "images/Ep5/garryspace.webm", loop=False, image="garryover")
image antlick = Movie(channel="movie_dp", play = "images/Ep5/antlick.webm")
image antnight2 = Movie(channel="movie_dp", play = "images/Ep5/antnight2.webm")
image anep5lick1 = Movie(channel="movie_dp", play = "images/Ep5/anep5lick1.webm")
image anep5lick3 = Movie(channel="movie_dp", play = "images/Ep5/anep5lick3.webm")
image nicep5last3 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last3.webm")
image nicep5last3cam2 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last3cam2.webm")
image nicep5last5 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last5.webm")
image nicep5last7 = Movie(channel="movie_dp", play = "images/Ep5/nicep5last7.webm")
image anbjep5dom = Movie(channel="movie_dp", play = "images/Ep5/anbjep5dom.webm")
image anatitmsg = Movie(channel="movie_dp", play = "images/Ep5/anatitmsg.webm")
image anakiss = Movie(channel="movie_dp", play = "images/Ep5/anakiss.webm")
image anatitfk = Movie(channel="movie_dp", play = "images/Ep5/anatitfk.webm")
image anatitfk2 = Movie(channel="movie_dp", play = "images/Ep5/anatitfk2.webm")
image auntsxnoc = Movie(channel="movie_dp", play = "images/Ep5/auntsxnoc.webm")
image hjsxmov2 = Movie(channel="movie_dp", play = "images/Ep5/hjsxmov2.webm")
image hjpymov = Movie(channel="movie_dp", play = "images/Ep5/hjpymov.webm")
image garryworkout = Movie(channel="movie_dp", play = "images/Ep5/garryworkout.webm")




label episode5:
    if easymode:
        show text "Easy Mode points!"
        show image "images/Stats/Dom[nicdomep5].png" at statleft
        show image "images/Stats/Lust[niclustep5].png" at statright
        pause 1
        $niclustep5 += 2
        $nicdomep5 += 2
        show image "images/Stats/Dom[nicdomep5].png" at statleft
        show image "images/Stats/Lust[niclustep5].png" at statright
        pause 1
        hide text
    scene black with fade
    stop music fadeout 1.0
    play music "music/Forest.mp3"
    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 5" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Evening" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    if nicolelustending == True:
        $ niclustep5 = 5
        "You earned a bonus Lust point for kissing [woman_name]"
    if nicoledomending == True:
        $ nicdomep5 = 5
        "You earned a bonus Domination point for dominating [woman_name]"
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicdomep5].png"
    hide image "images/Stats/Lust[niclustep5].png"

    scene 5b000 with dissolve
    pause
    play sound "music/sliding.mp3"
    "{color=#ffa500}{i}*the sound of a sliding door*{/i}"
    $ renpy.pause(4, hard=True)
    scene 5b001 with dissolve
    pause
    scene 5b002 with dissolve
    play sound "music/lighter.mp3"
    "{color=#ffa500}{i}*the sound of a lighter*{/i}"
    scene 5b003 with dissolve
label ciggie:
    show cigep5 with dissolve
    $ renpy.pause(2, hard=True)
    if nicolelustending == True:
        show screen hint("She's confused after the kiss, maybe it's worth talking to her?\nI wonder if she'll have a cigarette with me...")
    elif nicoledomending == True:
        show screen hint("She's probably mad at me. I don't even know if trying to talk to her makes any sense.")

    menu:
            "{color=#FFD1DF}{i}*Offer her a cigarette*{/i}{/color}":
                    hide screen hint
                    $nicsmoke+= 1
                    jump cigofferep5

            "How are you?":
                    hide screen hint
                    jump howareyouep5

            "{color=#FFD1DF}{i}*Smoke in silence*{/i}{/color}":
                    hide screen hint
                    jump smokeinsilence

            "{color=#FFD1DF}{i}*Look at her legs*{/i}{/color}":
                    hide screen hint
                    jump lookatlegsep5

label lookatlegsep5:
    scene 5b0033 with dissolve
    $ legsep5 += 1
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i}I hope that soon they will lean on my shoulders..."
    jump ciggie

label cigofferep5:
    if nicsmoke == 1:
        e "Hey..."
        scene 5b005a with dissolve
        e "Want a smoke?"
        scene 5b005 with dissolve
        m "No..."
        scene 5b006 with dissolve
        e "Okay."
        scene 5b007 with dissolve
        "{color=#ffa500}{i}*the sound of taking a drag from a cigarette*{/i}"
        jump ciggie
    elif nicsmoke == 2:
        scene 5b005a with dissolve
        e "You sure?"
        e "It always helps when I'm having a bad day."
        m "..."
        if nicolelustep4 > 7:
            scene 5b005 with dissolve
            m "Ok..."
            scene 5b0010 with dissolve
            pause
            scene 5b0011 with dissolve
            "{color=#ffa500}{i}*the sound of taking a drag from a cigarette*{/i}"
            $ niclovebonusfactor += 1
            if nicoledomending == True:
                show screen hint("She's so dominated by me that I can say whatever I want to her. If I want to be rude...")
            else:
                show screen hint("I guess she's not so dominated by me that I can say whatever i want")
            menu:
                "I like it when you take something from me and put it in your mouth":
                    hide screen hint
                    if nicoledomending == True:
                        show image "images/Stats/Dom[nicdomep5].png" at statleft
                        show image "images/Stats/Lust[niclustep5].png" at statright
                        pause 1
                        $ nicdomep5 += 1
                        $ niclustep5 -= 1
                        show image "images/Stats/Dom[nicdomep5].png" at statleft
                        show image "images/Stats/Lust[niclustep5].png" at statright
                        with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicdomep5].png"
                        hide image "images/Stats/Lust[niclustep5].png"
                    else:
                        show image "images/Stats/Dom[nicdomep5].png" at statleft
                        show image "images/Stats/Lust[niclustep5].png" at statright
                        pause 1
                        $ niclustep5 -= 1
                        show image "images/Stats/Dom[nicdomep5].png" at statleft
                        show image "images/Stats/Lust[niclustep5].png" at statright
                        with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicdomep5].png"
                        hide image "images/Stats/Lust[niclustep5].png"
                "{color=#FFD1DF}{i}*Don't say anything*{/i}{/color}":
                    hide screen hint
                    pause

            scene 5b0012 with dissolve
            m "{color=#ffa500}{i}*Cough cough*{/i}"
            scene 5b0013 with dissolve
            m "It's not for me..."
            if not easymode:
                $ achValid5 += 1
                $ achievement.grant("Achiev16")
                $ achievement.sync()
                if not persistent.achievement16:
                         $ achievement.grant("Achiev16")
                         $ achievement.sync()
                         show Achiev16 at achievment with easeintop:
                                    zoom 0.5
                                    rotate_animation

                         "You have received the achievement!{p}{b}\"Smoking with cutie\".{/b}"
                         "Number of achievements earned in this chapter [achValid5]/8"
                         hide Achiev16
                         $ persistent.achievement16 = True
            show image "images/Stats/Dom[nicdomep5].png" at statleft
            show image "images/Stats/Lust[niclustep5].png" at statright
            pause 1
            $ niclustep5 += 1
            show image "images/Stats/Dom[nicdomep5].png" at statleft
            show image "images/Stats/Lust[niclustep5].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[nicdomep5].png"
            hide image "images/Stats/Lust[niclustep5].png"
            scene 5b0010 with dissolve
            jump ciggie
        elif nicolelustep4 <= 8:
            scene 5b005 with dissolve
            m "No..."
            jump ciggie
    elif nicsmoke >= 3:
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i}There’s no point in proposing again..."
            jump ciggie

label smokeinsilence:
    scene 5b0020 with dissolve
    "{color=#ffa500}{i}*the sound of taking a drag from a cigarette*{/i}"
    scene 5b0021 with dissolve
    if nicsmoke <= 1 and smokesil == 0:
        m "Could you go and smoke somewhere else?"
        scene 5b0021a with dissolve
        if easymode:
            menu:
                "No.{p}I’m the man of this house, and you can’t tell me what to do.\n{color=#3d85c6} +1 Dom Point":
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            pause 1
                            $ nicdomep5 += 1
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            with dissolve
                            pause 3
                            hide image "images/Stats/Dom[nicdomep5].png"
                            hide image "images/Stats/Lust[niclustep5].png"
                            $ smokesil += 1
                            jump ciggie

                "{color=#FFD1DF}{i}*Throw away the cigarette*{/i}{/color}":
                    jump throwcigep5

        else:
            menu:
                "No.{p}I’m the man of this house, and you can’t tell me what to do.":
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            pause 1
                            $ nicdomep5 += 1
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            with dissolve
                            pause 3
                            hide image "images/Stats/Dom[nicdomep5].png"
                            hide image "images/Stats/Lust[niclustep5].png"
                            $ smokesil += 1
                            jump ciggie

                "{color=#FFD1DF}{i}*Throw away the cigarette*{/i}{/color}":
                    jump throwcigep5


    if nicsmoke > 1 and smokesil >= 0:
        scene 5b0022 with dissolve
        m "You shouldn't smoke. It's not healthy for you."
        $ smokesil += 1

    if smokesil > 0:
        scene 5b006 with dissolve
        m "Just throw it away..."
        jump throwcigep5

label throwcigep5:
    $ cigthrow = True
    scene 5b0023 with dissolve
    pause 0.5
    scene 5b0023a with dissolve
    pause 0.5
    scene 5b0023b with dissolve
    pause 0.5
    scene 5b0023d with dissolve
    pause 0.5
    scene 5b0023e with dissolve
    pause 0.5
    scene 5b0023f with dissolve
    pause 0.5
    scene 5b0024 with dissolve
    e "Happy?"
    scene 5b0024a with dissolve
    pause 0.5
    scene 5b0024b with dissolve
    m "Very...{p}Thanks"
    jump howareyouep5v2

label howareyouep5:
    scene 5b0025 with dissolve
    e "How are you?"
    scene 5b0030 with dissolve
    m "What do you think?"

label howareyouep5v2:
    scene 5b0025 with dissolve
    show screen hint("I have to be careful here. Someone might see us... ")

    menu:
        "Wanna suck my cock?":
            hide screen hint
            scene 5b0031 with dissolve
            pause
            scene 5b0031a with dissolve
            m "Just go away [player_name]"
            scene 5b0031 with dissolve
            pause
            scene 5b0031a with dissolve
            m "You already got what you wanted today..."
            scene 5b0031 with dissolve
            e "I'll see you tomorrow, then...."
            label goodnightep5:
            e "Good night [woman_role]"
            label goodnightep5v2:
            scene 5b0032 with dissolve
            pause
            scene 5b0032b with dissolve
            m "Good night..."
            scene 5b0032 with dissolve
            pause
            scene 5b0031 with dissolve
            pause
            scene black with fade
            jump bedep5

        "You are beautiful [woman_role]":
            $ howareyouep5choice += 1
            if howareyouep5choice == 1:
                $ niclovebonusfactor += 1
                hide screen hint
                scene 5b0025 with dissolve
                pause
                scene 5b0032 with dissolve
                pause
                scene 5b0031 with dissolve
                if nicolelustending == True:
                            m "..."
                            scene 5b0031a with dissolve
                            m "Mhm..."
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            pause 1
                            $ niclustep5 += 1
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            with dissolve
                            pause 3
                            hide image "images/Stats/Dom[nicdomep5].png"
                            hide image "images/Stats/Lust[niclustep5].png"
                            jump howareyouep5v2
                else:
                            scene 5b0031a with dissolve
                            m "That doesn't sound very nice coming from you."
                            scene 5b0031 with dissolve
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            pause 1
                            $ niclustep5 -= 1
                            show image "images/Stats/Dom[nicdomep5].png" at statleft
                            show image "images/Stats/Lust[niclustep5].png" at statright
                            with dissolve
                            pause 3
                            hide image "images/Stats/Dom[nicdomep5].png"
                            hide image "images/Stats/Lust[niclustep5].png"
                            scene 5b0031a with dissolve
                            m "I wish you wouldn't talk to me like that."
                            jump howareyouep5v2
            else:
                 scene 5b0032b with dissolve
                 m "You already said that..."
                 scene 5b0032 with dissolve
                 pause
                 scene 5b0031 with dissolve
                 pause
                 jump howareyouep5v2

        "Are you drinking again?":
            hide screen hint
            scene 5b0033 with dissolve
            e "What kind of wine is it?"
            scene 5b0033a with dissolve
            pause
            scene 5b0033b with dissolve
            show screen hint("Good to know. I should remember.")
            m "Merlot..."
            hide screen hint with dissolve
            scene 5b0024b with dissolve
            m "Eve always brings me red wine when she gets it as a gift because she doesn’t like it."
            scene 5b0031a with dissolve
            if legsep5 > 0:
                m "I don't know why I'm telling you this... You're not even listening."
                scene 5b0024 with dissolve
                m "You've just been staring at my legs since you showed up."
                scene 5b0025 with dissolve
                pause
                scene 5b0024b with dissolve
                m "What do you want from me now?{p}Which sick fantasy of yours should I fulfill now?"
                show image "images/Stats/Dom[nicdomep5].png" at statleft
                show image "images/Stats/Lust[niclustep5].png" at statright
                pause 1
                $ nicdomep5 += 1
                show image "images/Stats/Dom[nicdomep5].png" at statleft
                show image "images/Stats/Lust[niclustep5].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[nicdomep5].png"
                hide image "images/Stats/Lust[niclustep5].png"
                scene 5b0031 with dissolve
                pause
                scene 5b0031a with dissolve
                m "Just go away..."
                scene 5b0031 with dissolve
                pause
                if not easymode:
                    show screen hint("This is a really BAD IDEA... but if you really have to...")
                    menu:
                                    "{color=#FFD1DF}{i}*Grab her head and force her to suck your dick. Fuck the neighbors and consequences*{/i}{/color}\n{color=#3d85c6}Normal Version Secret Scene":
                                        hide screen hint
                                        jump balconysuck

                                    "{color=#FFD1DF}{i}*Leave*{/i}{/color}":
                                        jump goodnightep5
            else:
                show image "images/Stats/Dom[nicdomep5].png" at statleft
                show image "images/Stats/Lust[niclustep5].png" at statright
                pause 1
                $ niclustep5 += 1
                show image "images/Stats/Dom[nicdomep5].png" at statleft
                show image "images/Stats/Lust[niclustep5].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[nicdomep5].png"
                hide image "images/Stats/Lust[niclustep5].png"


            scene 5b0024 with dissolve
            m "I have to go to sleep.{p}I have to get up early in the morning."
            scene 5b0031
            e "[woman_role]..."
            scene 5b0040 with dissolve
            show screen hint("I could try... If I was good to her before...")
            menu:
                "Good night":
                    hide screen hint
                    jump goodnightep5v2
                "I love you":
                    $ niclovebonusfactor += 1
                    hide screen hint
                    scene 5b0033a with dissolve
                    pause
                    if nicolelustending == True or niclustep5 >= 6:
                        show image "images/Stats/Dom[nicdomep5].png" at statleft
                        show image "images/Stats/Lust[niclustep5].png" at statright
                        pause 1
                        $ niclustep5 += 1
                        show image "images/Stats/Dom[nicdomep5].png" at statleft
                        show image "images/Stats/Lust[niclustep5].png" at statright
                        with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicdomep5].png"
                        hide image "images/Stats/Lust[niclustep5].png"
                        scene 5b0033b with dissolve
                        m "Good...{p}Good night [player_name]"
                        scene black with fade
                        jump bedep5
                    else:
                        jump goodnightep5v2

        "{color=#FFD1DF}{i}*Take a puff of a cigarette*{/i}{/color} {size=-8}(Req. Cigarette){/size}" if cigthrow == False:
            hide screen hint
            scene 5b0020 with dissolve
            "{color=#ffa500}{i}*the sound of taking a drag from a cigarette*{/i}"
            jump ciggie

        "{color=#FFD1DF}{i}*Take another cigarette*{/i}{/color} {size=-8}(Req. Cigarette throw){/size}*" if cigthrow == True:
            $ cigthrow = False
            $ cigcount += 1
            hide screen hint
            scene 5b002 with dissolve
            play sound "music/lighter.mp3"
            "{color=#ffa500}{i}*the sound of a lighter*{/i}"
            scene 5b0020 with dissolve
            "{color=#ffa500}{i}*The sound of taking a drag from a cigarette*{/i}"
            m "Really...?"
            jump ciggie

label balconysuck:

    show 5batk with vpunch
    $ renpy.pause(0.25, hard=True)
    show text "What are y..." with dissolve
    hide text with dissolve
    $ renpy.pause(0.25, hard=True)
    show text "[player_name]...!" with dissolve
    hide text with dissolve

    scene 5b0049 with dissolve
    e "Shh..."
    show 5bbj
    $ renpy.pause(2, hard=True)
    e "You have to be quiet, [woman_role]"
    pause
    e "Someone else will hear it...{p}How would you explain it to them?"
    pause
    e "Damn...{p}you're such a good cock swallower."
    pause
label c5bbj:
    hide 5bbj2
    show 5bbj
    pause
    menu (screen="rightchoice"):
        "Change view":
            jump c5bbj2
        "Continue":
            jump c5bbjend

label c5bbj2:
    hide 5bbj
    show 5bbj2
    pause
    menu (screen="rightchoice"):
        "Change view":
            jump c5bbj
        "Continue":
            jump c5bbjend

label c5bbjend:
    n "Neighbor...{p}is everything okay?"
    scene 5b0050 with dissolve
    e "Shit!"
    "{color=#A8E4A0}{i}{size=-3}The truth is that nothing like that happened on the balcony.{p}The risk was too high.{p}The only thing you did was...{/size}{/i}{/color}"
    show 5brew
    $ renpy.pause(2, hard=True)
    $ renpy.end_replay()
    jump goodnightep5

label bedep5:
    scene black with fade
    stop music fadeout 1.0
    show text "[player_name]'s room" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Late evening" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    scene bed0 with dissolve
    pause
    play sound "music/sms.mp3"
    "{color=#ffa500}{i}*sms sound*{/i}{/color}"
    play sound "music/sms.mp3"
    "{color=#ffa500}{i}*another sms sound*{/i}{/color}"
    scene bed1 with dissolve
    play music "music/Mat.wav"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What the fuck..."
    scene bed2 with dissolve
    pause
    scene bed3 with dissolve
    pause
    scene phone1 with dissolve
    e "I know this number.{p}[nicosister_role] Eve..."
    show screen hint("There's something going on. I should be direct. She definitely likes it.")

    if easymode:

        menu (screen="rightchoice"):
            "{color=#FFD1DF}{i}*Don't answer and go to sleep*":
                jump beforeep5dad
            "I'm not sleeping, did something happen?":
                jump smsnosleep
            "So you were thinking about me? \n{color=#3d85c6} +1":
                jump smsthinking

    else:
        menu (screen="rightchoice"):
            "{color=#FFD1DF}{i}*Don't answer and go to sleep*":
                jump beforeep5dad
            "I'm not sleeping, did something happen?":
                jump smsnosleep
            "So you were thinking about me?":
                jump smsthinking

label beforeep5dad:
    $ nosmsaunt =+ 1
    scene bed3 with dissolve
    pause
    scene bed2 with dissolve
    pause
    scene bed0
    pause
    scene black with fade
    jump ep5dad

label smsnosleep:
    $ smsnosleep_choice += 1
    scene phone1a with dissolve
    pause
    play sound "music/sms.mp3"
    scene phone2a with dissolve
    pause
    jump sms2talk

label smsthinking:
    $ smsthink_choice += 1
    $ smslust += 1
    scene phone1b with dissolve
    pause
    play sound "music/sms.mp3"
    scene phone2b with dissolve
    pause
    jump sms2talk

label sms2talk:

    if easymode:
        menu (screen="rightchoice"):
            "Sure, I'll stop by tomorrow.":
                jump smsstopby
            "Just talk?\n{color=#3d85c6} +1":
                jump smstalk

    else:
        menu (screen="rightchoice"):
            "Sure, I'll stop by tomorrow.":
                jump smsstopby
            "Just talk?":
                jump smstalk


label smstalk:
    $ smslust += 1
    if smsthink_choice == 1:
        scene phone2bb with dissolve
        pause
        play sound "music/sms.mp3"
        scene phone2bbb with dissolve
        pause
    else:
        scene phone2ab with dissolve
        pause
        play sound "music/sms.mp3"
        scene phone2aaa with dissolve
        pause
    jump sms3talk

label smsstopby:
    if smsthink_choice == 1:
        scene phone2ba with dissolve
        pause
    else:
        scene phone2aa with dissolve
        pause
    hide screen hint
    scene bed3 with dissolve
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i}Thank you!{p}See you tomorrow!"
    pause
    scene bed2 with dissolve
    pause
    scene bed0
    pause
    scene black with fade
    jump ep5dad

label smsstopby2:
    hide screen hint
    scene bed3 with dissolve
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i}Good Night!"
    pause
    scene bed2 with dissolve
    pause
    scene bed0
    pause
    scene black with fade
    jump ep5dad

label smsstopby3:
    hide screen hint
    scene bed3 with dissolve
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i} I know, I know, come see me tomorrow. I'm at home all day."
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i} Good night."
    pause
    scene bed2 with dissolve
    pause
    scene bed0
    pause
    scene black with fade
    jump ep5dad

label sms3talk:

    if easymode:
        menu (screen="rightchoice"):
            "What are you wearing?\n{color=#3d85c6} +1":
                jump smswhatuwear
            "If you want to talk, you can always count on me.":
                jump smsstopby3
    else:
        menu (screen="rightchoice"):
            "What are you wearing?":
                jump smswhatuwear
            "If you want to talk, you can always count on me.":
                jump smsstopby3

label smswhatuwear:
    $ smslust += 1
    if smsthink_choice == 1:
        scene phone2bbbb with dissolve
        pause
        play sound "music/sms.mp3"
        scene phone2bbbbb with dissolve
        pause
        play sound "music/sms.mp3"
        scene phone2bbbbbend with dissolve
        pause
    else:
        scene phone2aaaa with dissolve
        pause
        play sound "music/sms.mp3"
        scene phone2aaaaa with dissolve
        pause
        play sound "music/sms.mp3"
        scene phone2bbbbbend with dissolve
        pause


    if easymode:
        menu (screen="rightchoice"):
            "I will cum with pleasure to your house.\n{color=#3d85c6} +1":
                jump smskiss
            "Good night":
                jump smsstopby2
    else:
        menu (screen="rightchoice"):
            "I will cum with pleasure to your house.":
                jump smskiss
            "Good night":
                jump smsstopby2

label smskiss:
    hide screen hint
    scene bed3 with dissolve
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i} I just hope your finger slipped on the keyboard..."
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i} Good night [player_name]"

    scene bed2 with dissolve
    pause
    scene bed0
    pause
    scene black with fade
    if smslust > 2:
        $ evewetdreamsscene = True
        label bedep5scene:
        a "Ooooh...."
        label an1pho:
        show anpho1
        hide anpho2
        a "[player_name]..."
        pause
        menu (screen="leftchoice"):
            "Change view":
                jump an2pho
            "End":
                show organ58 with dissolve
                hide an1pho
                hide an2pho
                $ renpy.pause(3, hard=True)
                a "Ahh...."
                $ renpy.end_replay()
                jump ep5dad
        label an2pho:
        show anpho2
        hide anpho1
        pause
        menu (screen="leftchoice"):
            "Change view":
                jump an1pho
            "End":
                show organ58 with dissolve
                hide an1pho
                hide an2pho
                $ renpy.pause(3, hard=True)
                a "Ahh...."
                $ renpy.end_replay()
                jump ep5dad
        jump ep5dad
    else:
        jump ep5dad


label ep5dad:
    scene black with fade
    stop music fadeout 1.0
    play music "music/Mda.wav"
    show text "Meanwhile" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Somewhere outside the city" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    scene a511000 with dissolve
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Full. "
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I should be able to get there on a full tank."
    n "John."
    scene a511001 with dissolve
    scene a511002 with dissolve
    scene a511003 with dissolve
    d "Yes, Marco?"
    scene eatgr0 with dissolve
    r "{color=#ffa500}{i}*Smacking*{/i}{/color}"
    scene eatgr1 with dissolve
    scene eatgr2 with dissolve
    scene a510042 with dissolve
    r "The boys ask if you are going to the brothel with them."
    scene a511020 with dissolve
    r "It's Paul's birthday today.{p}He pays for everything."
    scene a511021 with dissolve
    scene a511022 with dissolve
    d "Nah.{p}You know me.{p}I never go to places like that."
    scene a510045 with dissolve
    r "That's what I told them."
    scene a510043 with dissolve
    scene eatgr2 with dissolve
    scene eatgr1 with dissolve
    scene eatgr0 with dissolve
    r "{color=#ffa500}{i}*Smacking*{/i}{/color}"
    d "I want to leave as early as possible to avoid wasting time. Maybe I can shorten the route by a day."
    scene a510041 with dissolve
    r "Sure."
    scene a511027 with dissolve
    r "How's [woman_name]?"
    r "Does she still look like time stopped for her in college?"
    scene a511026 with dissolve
    d "Beautiful, just like when I met her..."
    scene a511025 with dissolve
    r "No wonder you don't want to go with them.{p}If I had a wife like that, I would stay at home and take care of her all day long."
    r "Isn't she afraid without you in such a big house?"
    scene a511026 with dissolve
    d "Fortunately, there is one man in the house who watches over her."
    scene a510036 with dissolve
    r "Oh yeah, I forgot about your son.{p}What was his name?"
    d "[player_name]"
    scene a510043 with dissolve
    r "And how is the young man doing?"
    scene eatgr2 with dissolve
    scene eatgr1 with dissolve
    scene eatgr0 with dissolve
    scene a510041 with dissolve
    r "Calm as an old man?"
    scene a511025 with dissolve
    r "Can [woman_name] handle him alone?"
    scene a511026 with dissolve
    d "You know her.{p}Typical teacher."
    scene a511023 with dissolve
    d "If she gets mad, it's best not to be around her."
    scene a511025 with dissolve
    r "They are all like that...."
    scene a511023 with dissolve
    d "[player_name] is a good kid. Doesn't cause too many problems."
    d "Besides, he probably only has girls on his mind now."
    scene eatgr2 with dissolve
    scene eatgr1 with dissolve
    scene eatgr0 with dissolve
    r "{color=#ffa500}{i}*Smacking*{/i}{/color}"
    scene a510041 with dissolve
    r "I always wanted to have a son. I envy you that."
    scene a510046 with dissolve
    r "How about we introduce him to my daughter? She has now separated from her partner."
    scene a511021 with dissolve
    scene a511022 with dissolve
    d "No, no."
    scene a511021 with dissolve
    scene a511023 with dissolve
    d "This never works well.{p}Let him search for himself."
    scene a511020 with dissolve
    r "Great.{p}I'm going to bed. I also want to leave in the morning.{p}Good night"
    scene a511023 with dissolve
    d "Good night, Marco."
    scene black with fade


label morningep5:

    stop music fadeout 1.0
    play music "music/Mn2.mp3"
    show text "Next day" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Morning" at title2 with dissolve
    $ renpy.pause(2, hard=True)

    show morningmov
    $ renpy.pause(4, hard=True)
    scene 5000000 with dissolve
    pause 0.25
    scene 5000001 with dissolve
    pause 0.25
    scene 5000002 with dissolve
    e "{color=#ffa500}{i}*yawns*"
    scene 5000003 with dissolve
    e "I've barely woken up and I'm already tired."
    e "Time for a quick shower."
    scene 5000004 with dissolve
    play sound "music/shower.mp3"
    $ renpy.pause(1, hard=True)
    "{color=#ffa500}{i}*water sounds*"
    stop sound fadeout 1.0
    scene black with fade
    show text "Living room" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 50001 with dissolve
    e "Good morning"
    scene 50002 with dissolve
    pause
    scene 50003 with dissolve
    e "Are you leaving?"
    scene 50004 with dissolve
    m "I need to go to work.{p}It's monday."
    scene 50006 with dissolve
    e "Showing such a cleavage?{p}For all your horny students?"
    scene 50005 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She doesn't respond"
    scene 50007 with dissolve
    $ timeout_label = "strongwillpower"
    show screen hint("\n    I have to do something...") with dissolve

    if easymode:
        menu:
            "Stop her\n{color=#3d85c6} JUST DO IT":
                hide screen hint
                jump stopherep5
    else:
        menu:
            "Stop her":
                hide screen hint
                jump stopherep5


label strongwillpower:
    hide screen hint
    scene 50007a with dissolve
    pause 1
    scene 50007b with dissolve
    "{color=#A8E4A0}{i}{size=-3}She left..."
    "{color=#A8E4A0}{i}{size=-3}Uhm... Did you actually let her go?"
    menu:
        "Dude, I'm only interested in achievements.":
            "{color=#A8E4A0}{i}{size=-3} Ok..."
            "{color=#A8E4A0}{i}{size=-3} But you may even get two during this conversation!"
            "{color=#A8E4A0}{i}{size=-3} And an additional perk!"

            menu:
                    "Really? Okay, show me.":
                        jump stopherep5

        "Of course I am! I just wanted to see what would happen...":
            "{color=#A8E4A0}{i}{size=-3} Ok"
            jump stopherep5


label stopherep5:
    scene 50008 with vpunch
    e "Hey, wait."
    scene 50008a with dissolve
    m "Leave me alone, [player_name]."
    scene 50008b with dissolve
    m "I can't do this anymore"
    m "You've punished me enough, let's just go back to being a normal family."
    scene 50008c with dissolve
    m "I want to live a normal life and spend it with you like any other family."
    scene 50008b with dissolve
    m "Without having to avoid you out of fear of what you'll come up with next."
    scene 50008a with dissolve
    m "I'm sorry for everything, John and I haven't slept for a long time.{p}I had my own needs"
    m "I'm sorry I didn't think about you through all of this and that I hurt you."
    scene 50008d with dissolve
    e "Don't apologize, [woman_role]."
    e "I've always seen something more in you."
    scene 50010 with dissolve
    e "Your feminine face..."
    scene 50010a with dissolve
    e "Your sweet lips..."
    scene 50010b with dissolve
    e "Your little tits..."
    e "and that sexy ass..."
    scene 50010c with dissolve
    m "Stop."
    m "How do you imagine this? How do you even imagine our life together?"
    scene 50010d with dissolve
    e "That day when you came home a little drunk and we went all out...{p}It was a magical day for me"
    scene 50010e with dissolve
    e "Everything changed...{p}It was a bliss like nothing I'd ever felt before."
    e "I want you to feel that way too."
    scene 50010f with dissolve
    m "This is wrong.{p}What you're saying and doing is very wrong."
    scene 50010e with dissolve
    e "But for some reason, you don't resist it."
    scene 50010g with dissolve
    e "You let me do all this"
    scene 50010f with dissolve
    m "That's not true. What was I supposed to do? You're stronger, you made me do all of it."
    scene 50010a with dissolve
    m "Was I supposed to tell John everything?{p}I couldn't..."
    scene 50010 with dissolve
    m "I have my reasons for not doing it."
    scene 50010f with dissolve
    m "But if you don't come to your senses, I'll have no choice but to move out..."
    scene 50010d with dissolve
    e "And how will you explain it to dad?"
    scene 50010 with dissolve
    m "I don't know. This all feels like some kind of unreal dream."
    scene 50010b with dissolve
    e "For me, it's a beautiful dream"

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Kiss Her*{/i}{/color} \n{color=#3d85c6} Love path":
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    pause 1
                                    $ niclovebonusfactor += 3
                                    $ niclustep5 += 1
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    with dissolve
                                    pause 3
                                    hide image "images/Stats/Dom[nicdomep5].png"
                                    hide image "images/Stats/Lust[niclustep5].png"
                                    jump ep5kissone
            "{color=#FFD1DF}{i}*Unbutton her blouse.*{/i}{/color} \n{color=#3d85c6} Dom path":
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    pause 1
                                    $ nicdomep5 += 1
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    with dissolve
                                    pause 3
                                    hide image "images/Stats/Dom[nicdomep5].png"
                                    hide image "images/Stats/Lust[niclustep5].png"
                                    jump ep5choke

    else:
        menu:
            "{color=#FFD1DF}{i}*Kiss Her*{/i}{/color}":
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    pause 1
                                    $ niclovebonusfactor += 3
                                    $ niclustep5 += 1
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    with dissolve
                                    pause 3
                                    hide image "images/Stats/Dom[nicdomep5].png"
                                    hide image "images/Stats/Lust[niclustep5].png"
                                    jump ep5kissone
            "{color=#FFD1DF}{i}*Unbutton her blouse.*{/i}{/color}":
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    pause 1
                                    $ nicdomep5 += 1
                                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                                    show image "images/Stats/Lust[niclustep5].png" at statright
                                    with dissolve
                                    pause 3
                                    hide image "images/Stats/Dom[nicdomep5].png"
                                    hide image "images/Stats/Lust[niclustep5].png"
                                    jump ep5choke

label ep5kissone:
    scene 50008c with dissolve
    pause
    scene 50011 with dissolve
    m "WHAT THE..."
    scene 50011a with dissolve
    m "Don't..."
    m "I really have to go to work."
    jump photomentionep5


label ep5choke:
    scene 50008c with dissolve
    pause
    scene 50011button with dissolve
    m "WHAT THE..."
    scene 50011button2 with vpunch
    m "Don't..."
    scene 50011a with dissolve
    m "I really have to go to work."
    jump photomentionep5

label photomentionep5:
    scene 50008a with dissolve
    e "I'd like to show you something."
    scene 50012 with dissolve
    e "I found this photo."
    scene 50012a with dissolve
    m "Huh?"
    e "The night after the prom party."
    e "You and John were dating at the time, and this photo wasn't taken by him, but by your friend Lopez."
    scene 50013 with dissolve
    m "What...{p}How do you know about him...{p}Where did you get this photo?!"
    scene 50015 with dissolve
    e "Everything is on the Internet, although don't worry, no one will find it."
    scene 50014 with dissolve
    m "[player_name], I'm asking you.{p}If you love me, do something for me and forget about this photo."
    m "Delete it and don't ask about it again. I'm begging you."
    scene 50015 with dissolve
label ep5nicolereplayscene:

    if easymode:
        menu:
            "I'll consider it if you become my obedient bitch.\n{color=#3d85c6} Dom Path":
                jump obedientep5

            "If it's so important to you, I'll do it\n{color=#3d85c6} Love Path":
                $ niclovebonusfactor += 5
                jump willdeletephoto

    else:
        menu:
            "I'll consider it if you become my obedient bitch.":
                jump obedientep5

            "If it's so important to you, I'll do it":
                $ niclovebonusfactor += 5
                jump willdeletephoto

label willdeletephoto:
    scene 50030 with dissolve
    m "Thank you..."
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    pause 1
    $ niclustep5 += 1
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicdomep5].png"
    hide image "images/Stats/Lust[niclustep5].png"
    e "I already forgot about this photo."
    scene 50031 with dissolve
    m "What... What is that?"
    scene 50032 with dissolve
    e "Don't worry. It's just my little friend who responds to our cuddles."
    e "If you love me... will you do something for me?"
    m "I love you, that's why I won't do it, I can't."
    e "[woman_role], you cheated on your father from the very beginning, slept with other men and did it who knows how many times with strangers."
    e "Besides, we've already done this, and I agreed to delete this photo as soon as you asked me"
    m "Please don't talk about this photo anymore..."
    pause
    m "{color=#ffa500}{i}*She sighed*{/i}{/color}"
    m "Okay..."
    e "Hmm?"
    scene 500101 with dissolve
    e "Woo-hoo!"
    scene 500102 with dissolve
    m "But you have to hurry."
    scene 500103 with dissolve
    $ renpy.pause(1, hard=True)
    scene 500104 with dissolve
    $ renpy.pause(1, hard=True)
    scene 500105 with dissolve
    $ renpy.pause(1, hard=True)
    show ep5nick11 with dissolve:
        zoom 0.5
    $ renpy.pause(5, hard=True)
    scene 500106 with dissolve
    e "Now take it in your hand"
    show ep5nick12 with dissolve
    $ renpy.pause(3, hard=True)
    scene 500107 with dissolve
    e "Do your best"
    scene 500107a with dissolve
    m "If anyone saw what we were doing..."
    scene 500107 with dissolve
    e "Don't worry, there's no one here."
    show ep5nick13 with dissolve
    $ renpy.pause(2, hard=True)
    e "...Ooh..."
    $ renpy.pause(2, hard=True)
    e "Uhm... [woman_role]..."
    "{color=#A8E4A0}{i}{size=-3}She doesn't answer."
    e "Could you... blow me?"
    scene 500107a with dissolve
    m "No.{p}It's too much."
    show ep5nick13 with dissolve
    $ renpy.pause(2, hard=True)
    e "I think it will take some time then."
    $ renpy.pause(2, hard=True)
    m "..."
    m "....."
    scene 500107 with dissolve
    m "{color=#ffa500}{i}*She sighed*{/i}{/color}"
    m "..."
    scene 500107a with dissolve
    m "It's very uncomfortable here...{p}I have to take off my shoes."
    scene takeof1 with dissolve
    pause
    scene takeof2 with dissolve
    pause
    scene 500109 with dissolve
    $ renpy.pause(1, hard=True)
    scene 500109a with dissolve
    $ renpy.pause(1, hard=True)
    m "You deleted the photo when I asked you...{p}This one time I will do it, but you will never ask me to do it again."
label ep5nick14positive:
    hide ep5nick14a
    show ep5nick14
    $ renpy.pause(5, hard=True)
    menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Change view*":
            jump ep5nick14apositive
        "Can you lick my balls? {size=-8}(Req. 3 Lust){/size}" if niclustep5 > 6:
            jump ep5nick15viewppositive
        "{color=#FFD1DF}{i}*Continue*":
            jump ep5nick14stoppositive

label ep5nick15viewppositive:
     scene 50110z
     hide ep5nick14a
     hide ep5nick14
     scene 500109 with dissolve
     m "Uhm..."
     show ep5nick15 with dissolve
     $ renpy.pause(5, hard=True)
     menu (screen="rightchoice"):
         "Please suck me some more.":
             jump ep5nick14positive
         "{color=#FFD1DF}{i}*Continue*":
             jump ep5nick14stoppositive

label ep5nick14apositive:
     hide ep5nick14
     show ep5nick14a
     $ renpy.pause(5, hard=True)
     menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Change view*":
             jump ep5nick14positive
        "Can you lick my balls? {size=-8}(Req. 3 Lust){/size}" if niclustep5 > 6:
            jump ep5nick15viewppositive
        "{color=#FFD1DF}{i}*Continue*":
            jump ep5nick14stoppositive

     $ renpy.pause(5, hard=True)

label ep5nick14stoppositive:
     scene 500110 with dissolve
     m "I really need to go..."
     scene 500110a with dissolve
     m "I can't be late for work..."
     $ renpy.end_replay()
     scene 500110b with dissolve
     e "I understand but..."
     show screen hint("After what I did with her earlier, such simple sucking will not bring me to orgasm.")

     if easymode:
             menu:
                 "{color=#FFD1DF}{i}*Tell her to keep sucking.*{/i}{/color}{size=-8}(replay scene)":
                     hide screen hint
                     scene 500110c with dissolve
                     e "Go back to sucking."
                     jump ep5nick14view1
                 "You can go...\n{color=#3d85c6} Good for Love Path but no scene":
                     $ niclovebonusfactor += 3
                     hide screen hint
                     scene 500110b with dissolve
                     e "{color=#ffa500}{i}*A loud sigh.*{/i}{/color}"
                     e "Okay...go."
                     scene 50032 with dissolve
                     m "..."
                     m "Thanks."
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     pause 1
                     $ niclustep5 += 2
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     with dissolve
                     pause 3
                     hide image "images/Stats/Dom[nicdomep5].png"
                     hide image "images/Stats/Lust[niclustep5].png"
                     scene 50007a with dissolve
                     pause 1
                     scene 50007b with dissolve
                     pause 1
                     jump nicgooutep5

                 "{color=#FFD1DF}{i}*Grab her by the hair and take her to the sofa.* {/i}{/color}{size=-8}(Req. 2 Domination Points){/size}\n{color=#3d85c6} DOM PATH and you can get Speed Perk" if nicdomep5 > 5:
                     $ niclovebonusfactor -= 5
                     hide screen hint
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     pause 1
                     $ niclustep5 -= 3
                     $ nicdomep5 += 2
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     with dissolve
                     pause 3
                     hide image "images/Stats/Dom[nicdomep5].png"
                     hide image "images/Stats/Lust[niclustep5].png"
                     jump grabhairep5sofa
     else:
             menu:
                 "{color=#FFD1DF}{i}*Tell her to keep sucking.*{/i}{/color}{size=-8}(replay scene)":
                     hide screen hint
                     scene 500110c with dissolve
                     e "Go back to sucking."
                     jump ep5nick14view1
                 "You can go...":
                     $ niclovebonusfactor += 1
                     hide screen hint
                     scene 500110b with dissolve
                     e "{color=#ffa500}{i}*A loud sigh.*{/i}{/color}"
                     e "Okay...go."
                     scene 50032 with dissolve
                     m "..."
                     m "Thanks."
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     pause 1
                     $ niclustep5 += 2
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     with dissolve
                     pause 3
                     hide image "images/Stats/Dom[nicdomep5].png"
                     hide image "images/Stats/Lust[niclustep5].png"
                     scene 50007a with dissolve
                     pause 1
                     scene 50007b with dissolve
                     pause 1
                     jump nicgooutep5

                 "{color=#FFD1DF}{i}*Grab her by the hair and take her to the sofa.* {/i}{/color}{size=-8}(Req. 2 Domination Points){/size}" if nicdomep5 > 5:
                     $ niclovebonusfactor -= 5
                     hide screen hint
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     pause 1
                     $ niclustep5 -= 3
                     $ nicdomep5 += 2
                     show image "images/Stats/Dom[nicdomep5].png" at statleft
                     show image "images/Stats/Lust[niclustep5].png" at statright
                     with dissolve
                     pause 3
                     hide image "images/Stats/Dom[nicdomep5].png"
                     hide image "images/Stats/Lust[niclustep5].png"
                     jump grabhairep5sofa


label obedientep5:
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    pause 1
    $ nicdomep5 += 1
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicdomep5].png"
    hide image "images/Stats/Lust[niclustep5].png"
    m "..."
    e "And you know what I've been wondering?"
    e "I don't know if there's anything more exciting than you being late for class with your students because you had to suck my dick."
    m "[player_name]..."
    e "Do you want me to forget about this photo and not ask anyone else about it?"
    e "Show me what you can do with that mouth"
    m "Does the fact that I am your [woman_role] mean anything to you at all?"
    e "Huge{p}It turns me on even more."
    e "On your knees."
    scene 500101 with dissolve
    e "Hey, look at me"
    scene 500102 with dissolve
    e "Take my pants off"
    scene 500103 with dissolve
    $ renpy.pause(1, hard=True)
    scene 500104 with dissolve
    $ renpy.pause(1, hard=True)
    scene 500105 with dissolve
    $ renpy.pause(1, hard=True)
    show ep5nick11 with dissolve:
        zoom 0.5
    $ renpy.pause(5, hard=True)
    scene 500106 with dissolve
    e "Now take it in your hand!"
    show ep5nick12 with dissolve
    $ renpy.pause(3, hard=True)
    scene 500107 with dissolve
    e "Do your best..."
    scene 500107a with dissolve
    m "If anyone saw what you were doing..."
    scene 500107 with dissolve
    e "You mean what YOU are doing, not me.."
    e "Luckily for you, no one will see.{p}Suck it"
    show ep5nick13 with dissolve
    $ renpy.pause(2, hard=True)
    e "Your hand is very nice"
    e "But instead of wasting time, just pop it in your mouth already."
    scene 500107a with dissolve
    m "I have to take off my shoes..."
    e "Whatever."
    e "It would be better if you took off your pants too."
    scene takeof1 with dissolve
    pause
    scene takeof2 with dissolve
    pause
    scene 500109 with dissolve
    $ renpy.pause(1, hard=True)
    scene 500109a with dissolve
    $ renpy.pause(1, hard=True)

label ep5nick14view1:
    hide ep5nick14a
    show ep5nick14
    $ renpy.pause(5, hard=True)
    menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Change view*":
            jump ep5nick14view2
        "My balls need some of your attention, bitch.":
            jump ep5nick15view
        "{color=#FFD1DF}{i}*Continue*":
            jump ep5nick14stop

label ep5nick15view:
    scene 50110z
    hide ep5nick14a
    hide ep5nick14
    scene 500109 with dissolve
    m "Uhm..."
    show ep5nick15 with dissolve
    $ renpy.pause(5, hard=True)
    menu (screen="rightchoice"):
        "Suck it":
            scene 500110c with dissolve
            e "Go back to sucking."
            jump ep5nick14view1
        "{color=#FFD1DF}{i}*Continue*":
            jump ep5nick14stop

label ep5nick14view2:
    hide ep5nick14
    show ep5nick14a
    $ renpy.pause(5, hard=True)
    menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Change view*":
            jump ep5nick14view1
        "My balls need some of your attention, bitch.":
            jump ep5nick15view
        "{color=#FFD1DF}{i}*Continue*":
            jump ep5nick14stop

    $ renpy.pause(5, hard=True)

label ep5nick14stop:
    scene 500110 with dissolve
    m "I really need to go..."
    scene 500110a with dissolve
    m "I can't be late for work..."
    scene 500110b with dissolve
    e "You'll go... only when I cum"
    $ renpy.end_replay()
    show screen hint("Damn... I don't think I'm going to cum very quickly. She has to try harder or we have to finish.")

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Tell her to keep sucking.*{/i}{/color}{size=-8} (replay scene)":
                hide screen hint
                scene 500110c with dissolve
                e "Go back to sucking."
                jump ep5nick14view1
            "You can go...\n{color=#3d85c6} Love path but no scene":
                 $ niclovebonusfactor += 1
                 hide screen hint
                 scene 500110b with dissolve
                 e "{color=#ffa500}{i}*A loud sigh.*{/i}{/color}"
                 e "Okay...go."
                 scene 50032 with dissolve
                 m "..."
                 m "Thanks."
                 jump nicgooutep5
            "{color=#FFD1DF}{i}*Grab her by the hair and take her to the sofa.* {/i}{/color}{size=-8}(Req. 2 Domination Points){/size}\n{color=#3d85c6} DOM PATH and you can get Speed Perk" if nicdomep5 > 5:
                hide screen hint
                jump grabhairep5sofa

    else:
        menu:
            "{color=#FFD1DF}{i}*Tell her to keep sucking.*{/i}{/color}{size=-8} (replay scene)":
                hide screen hint
                scene 500110c with dissolve
                e "Go back to sucking."
                jump ep5nick14view1
            "You can go...":
                 $ niclovebonusfactor += 1
                 hide screen hint
                 scene 500110b with dissolve
                 e "{color=#ffa500}{i}*A loud sigh.*{/i}{/color}"
                 e "Okay...go."
                 scene 50032 with dissolve
                 m "..."
                 m "Thanks."
                 jump nicgooutep5
            "{color=#FFD1DF}{i}*Grab her by the hair and take her to the sofa.* {/i}{/color}{size=-8}(Req. 2 Domination Points){/size}" if nicdomep5 > 5:
                hide screen hint
                jump grabhairep5sofa

label grabhairep5sofa:
    scene 500110b with dissolve
    e "But I know how to help you."
    scene grab4 with dissolve
    scene grab5 with dissolve
    scene grab6 with dissolve
    scene grab7 with dissolve
    scene grab8 with dissolve
    scene grab9 with dissolve
    scene grab11 with dissolve
    e "Come here"
    scene 50203 with dissolve
    scene 50203a with dissolve
    scene 50203b with dissolve
    scene 50203c with dissolve
    scene 50203e with dissolve
    scene 50203f with dissolve
    e "Sit"
    scene 50204 with dissolve
    e "You won't need this."
    scene 50204a with dissolve
    m "What are you doing....?"
    scene 50204b with dissolve
    e "These pants only bother us."
    scene 50204c with dissolve
    scene jeans1 with dissolve
    scene jeans2 with dissolve
    scene jeans3 with dissolve
    m "[player_name] STOP"
    scene 50204cam with dissolve
    e "The more you struggle, the longer it will take."
    scene 50205 with dissolve
    e "I want to taste a little of you"
    scene 50205a with dissolve
    m "[player_name]!"
    scene 50205d with dissolve
    pause
    scene 50208 with dissolve
    e "I hope these aren't your favorite panties"
    scene 50208a with vpunch
    m "{color=#ffa500}{i}*Heavy breathing*"
    scene 50209 with dissolve
label nicfing2view:
    hide nicfing1
    show nicfing2 with dissolve
    $ renpy.pause(2, hard=True)
    menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Change view*":
            jump nicfing1view

        "{color=#FFD1DF}{i}*Continue*":
            jump afternickfing
label nicfing1view:
    hide nicfing2
    show nicfing1 with dissolve
    $ renpy.pause(2, hard=True)
    menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Change view*":
            jump nicfing2view

        "{color=#FFD1DF}{i}*Continue*":
            jump afternickfing

label afternickfing:
    m "{color=#ffa500}{i}*She starts panting faster and faster*"
    e "Oh no, no...{p}you won't cum that quickly."
    scene 50209x with dissolve
    e "Beautiful view"
    scene 50209y with dissolve
    pause
    scene 50209z with dissolve
    e "But you probably forgot about me..."
    scene 50209zz with dissolve
    scene 50209zzz with dissolve
    scene 50209zzz with dissolve
    scene 50209zzzz with dissolve
    scene 50209zzzzz with dissolve
    $ renpy.pause(1, hard=True)
    scene 50212 with dissolve
    e "I want to taste that pussy"
    scene 50212a with dissolve
    m "{color=#ffa500}{i}*She squealed*"
    scene 50209zfinal with dissolve
    "{color=#ffa500}{i}*Sucking sounds*"
    m "Ah..."
    show 50210anim with dissolve
    $ renpy.pause(2, hard=True)
    m "Oh..."
    menu (screen="rightchoice"):

        "{color=#FFD1DF}{i}*Continue*":
            jump nicep5down

label nicep5down:
    scene nicdown0 with dissolve
    if nicdomep5 > 5:
        e "Suck my cock, whore."
    elif niclustep5 > 5:
        e "Give me a good mouthful, honey."
    scene nicdown1 with dissolve
    scene nicdown2 with dissolve
    scene nicdown3 with dissolve
    scene nicdown4 with dissolve
    scene nicdown5 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Not again..."
    e "What are you waiting for?"
    e "If you don't want to be late, hurry up."
    scene nicdown6 with dissolve
    scene nicdown7 with dissolve
    scene nicdown8 with dissolve
    show nicbjcouch1 with dissolve
    "{color=#ffa500}{i}*Sucking sounds*"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ok [player_name], focus and do as they taught you on the internet"


    menu (screen="rightchoice"):

            "{color=#FFD1DF}{i}*Continue*":
                if _in_replay:
                    jump cameramovefail
                else:
                    jump orgep5game

label orgep5game:
    jump start_minigame

label cameramovefailquest:
    menu:
        "Try Again?"

        "Yes":
                $ orgi_minigame_bar = 90.0
                $ orgi_minigame_score = 0
                $ orgi_you_press_button = 0
                $ orgi_difficulty = 1
                jump start_minigame
        "No":
                jump cameramovefail

label nicoorgep5:
    $ niclovebonusfactor += 1
    if easymode:

        $ speedguy += 1
        "{color=#ffa500}*********************{/color}\nYou received the SPEED perk.\n{color=#ffa500}*********************{/color}"
    if not easymode:
        if orgi_difficulty > 2.1:
                $ achValid5 += 1
                $ speedguy += 1
                "{color=#ffa500}*********************{/color}\nYou received the SPEED perk.\n{color=#ffa500}*********************{/color}"
                $ achievement.grant("Achiev17")
                $ achievement.sync()
                if not persistent.achievement17:
                                         show Achiev17 at achievment with easeintop:
                                                    zoom 0.5
                                                    rotate_animation

                                         "You have received the achievement!{p}{b}\"Speedy Tongue!\".{/b}"
                                         "Number of achievements earned in this chapter [achValid5]/8"
                                         hide Achiev17
                                         $ persistent.achievement17 = True

        $ achValid5 += 1
        $ achievement.grant("Achiev18")
        $ achievement.sync()
        if not persistent.achievement18:
                             show Achiev18 at achievment with easeintop:
                                        zoom 0.5
                                        rotate_animation

                             "You have received the achievement!{p}{b}\"Fast...mouse?\".{/b}"
                             "Number of achievements earned in this chapter [achValid5]/8"
                             hide Achiev18
                             $ persistent.achievement18 = True
    hide nicbjcouch1
    show nicoep5orgmov with dissolve
    $ renpy.pause(12, hard=True)
    pause
    e "Im good, right [woman_role]?!"
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    pause 1
    $ niclustep5 += 2
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicdomep5].png"
    hide image "images/Stats/Lust[niclustep5].png"
    e "Don't stop sucking."
label cameramovefail:
    hide nicbjcouch1
    scene black with fade
    show cameramoveep51 with dissolve
    $ renpy.pause(8, hard=True)
    hide cameramoveep51
    show cameramoveep52
    pause
    e "I'm close..."
    hide cameramoveep52
    show nicbjcouch1
    e "Ahh..."
    show mccmep5sofa with dissolve
    $ maxmccumep7 += 1
    $ renpy.pause(3, hard=True)
    e "Daaaaamn"
    e "I fucking love your lips."
    stop music fadeout 1.0
    play music "music/Mnic.wav"
    scene nicendscene10 with fade
    e "Nice"
    $ renpy.end_replay()
    scene nicendscene11 with dissolve
    scene nicendscene12 with dissolve
    scene nicendscene13 with dissolve
    scene nicendscene14 with dissolve
    scene nicendscene15 with dissolve
    scene nicendscene16 with dissolve
    scene nicendscene17 with dissolve
    scene nicendscene18 with dissolve
    scene nicendscene19 with dissolve
    scene nicendscene20 with dissolve
    scene nicendscene21 with dissolve
    e "And how was it for you?"
    scene nicendscene22 with dissolve
    m "I need to go..."
    scene nicendscene23 with dissolve
    pause
    scene nicendscene25 with dissolve
    e "You should be more honest."
    scene nicendscene23 with dissolve
    e "If you don't like the way I do something, say so.{p}I will know for the future."
    scene nicendscene25 with dissolve
    e "I gave you quite a hard time because you're all sweaty."
    scene nicendscene23 with dissolve
    e "{color=#ffa500}{i}*giggling*{/i}{/color}"
    scene nicendscene25 with dissolve
    m "..."
    scene nicendscene24 with dissolve
    m "I have to change."


label nicgooutep5:
    scene black with fade
    show text "{i}[woman_name] left the room" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 50280 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ok... so what i should do now?"
    scene 50280a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I need to buy a few things, they will definitely come in handy. "
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It would also be a good idea to call Tommy and ask about the rest of the money."
    scene 50280 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I also have to visit my [nicosister_role] and ask what she knows about Lopez."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Maybe I should call my father?"


label ep5pathchoose:
    scene 50280a with dissolve
    if phonelive == True:
        show screen hint("I should call someone before I leave the house.")
    else:
        show screen hint("Time to go shopping.")
    menu:

        "{color=#FFD1DF}{i}*Go to the store*":
            jump storeep5

        "{color=#FFD1DF}{i}*Call Dad*{/i}{/color}{size=-8}(Req. Phone){/size}" if phonelive == True and daddyep5call1 == False:
            jump dadcallep5

        "{color=#FFD1DF}{i}*Call Tommy*{/i}{/color} {size=-8}(Req. Phone){/size}" if phonelive == True and tommyep5call1 == False:
            jump tommycallep5

        "{color=#FFD1DF}{i}*Call Gary*{/i}{/color} {size=-8}(Req. Phone){/size}" if phonelive == True and garyep5call1 == False:
            jump garycallep5




label boostaccep5:
                        $ phonelive = False
                        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Perfectly on time. I have 0$ for calls."
                        menu:
                            "Do you want to spend $25 and top up your phone account?"

                            "Yes {size=-6}{color=#e0d71d}25${/color}{/size}" if money >= 25:
                                $ money -= 25
                                play sound "music/buyshop.mp3"
                                $ accountboosted += 1
                                $ phonelive = True
                                jump ep5pathchoose
                            "No":
                                jump ep5pathchoose



label garycallep5:
    if phonelive == False:
        menu:
            "Do you want to spend $25 and top up your phone account?"

            "Yes {size=-6}{color=#e0d71d}25${/color}{/size}" if money >= 25:
                                        $ money -= 25
                                        play sound "music/buyshop.mp3"
                                        $ accountboosted += 1
                                        $ phonelive = True
                                        jump ep5pathchoose
            "No":
                                        jump ep5pathchoose

    elif phonelive:
        hide screen hint
        scene 50280b with dissolve
        if accountboosted == 0:
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn, 1$ left. I have enough for one phone call."
        scene 50280c with dissolve
        play sound "music/phonecall.mp3"
        "{color=#ffa500}{i}*Phone ringing*{/i}{/color}"
        $ renpy.pause(4, hard=True)
        $ garyep5call1 = True
        $ garyfriend += 1
        stop sound
        scene 50280g with dissolve
        p "Hey [player_name]"
        scene 50280d with dissolve
        e "I'm picking up the new 'game' today, if you know what I mean.{p}Interested?"
        scene 50280d with dissolve
        p "Always. Call me when you have them."
        scene 50280d with dissolve
        e "Ok... See You!"
        scene 50280 with dissolve
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I need to pick up a parcel from the store."
        if accountboosted == 0:
                  jump boostaccep5
        jump ep5pathchoose


label dadcallep5:
    hide screen hint
    scene 50280b with dissolve
    if accountboosted == 0:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn, 1$ left. I have enough for one phone call."
    scene 50280c with dissolve
    play sound "music/phonecall.mp3"
    "{color=#ffa500}{i}*Phone ringing*{/i}{/color}"
    $ renpy.pause(10, hard=True)

    if dadfriend > 0:
        $ daddyep5call1 = True
        stop sound
        d "Hey [player_name]!{p}What's up?"
        scene 50280d with dissolve
        e "Everything's fine, I'm just calling to ask how are you and when you're coming back"
        scene 50280g with dissolve
        d "I'll be back on Friday."
        d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} But if I manage to get there a little faster, I will surprise you on Thursday..."
        scene 50280c with dissolve
        d "On Friday, from what I heard, there is a match of our favorite team in our city."
        scene 50280f with dissolve
        e "Seriously?! And Conan will be playing?!"
        scene 50280e with dissolve
        d "Sure thing"
        scene 50280d with dissolve
        e "Then we're definitely going."
        scene 50280c with dissolve
        d "I have to go [player_name]. Say hello to your [woman_role] from me, will ya?."
        scene 50280d with dissolve
        e "Sure, have a good day."
        scene 50280b with dissolve
        if accountboosted == 0:
              jump boostaccep5
        jump ep5pathchoose

    else:
        stop sound
        scene 50280b with dissolve
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He didn't answer..."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Maybe he's mad at me..."
        jump ep5pathchoose


label tommycallep5:
    hide screen hint
    scene 50280b with dissolve
    if accountboosted == 0:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn, 1$ left. I have enough for one phone call."
    scene 50280c with dissolve
    play sound "music/phonecall.mp3"
    "{color=#ffa500}{i}*Phone ringing*{/i}{/color}"
    $ renpy.pause(10, hard=True)

    if tommyfriend > 0:
        $ tommyep5call1 = True
        $ tommyfriend += 1
        stop sound
        scene 50280e with dissolve
        t "Y...Yes?"
        scene 50280f with dissolve
        e "Sup Bro!"
        scene 50280g with dissolve
        t "Hey [player_name]"

        menu:
            "How's your mom doing?":
                if telltommy == True and mtommoney == 0 and tommymomsubmission > 1:
                    $ tommyaskyouep5 = True
                    scene 50280e with dissolve
                    t "[player_name]..."
                    t "I... I..."
                    t "I would like to talk to you about what happened..."
                    scene 50280d with dissolve
                    e "Mmmm...{p}Ok."
                    scene 50280e with dissolve
                    t "I...{p}I don't know how to say this..."
                    scene 50280f with dissolve
                    t "YOU ARE MY HERO, DUDE!"
                    t "I don't know how you did it...{p}But what I saw was...{p}Awesome!"
                    scene 50280d with dissolve
                    e "I thought you would be angry."
                    scene 50280i with dissolve
                    t "Never in my life, man.{p}I just wish I were in your place."
                    t "And this is what I would like to ask you..."
                    scene 50280e with dissolve
                    e "Huh?!"
                    scene 50280f with dissolve
                    e "You wanna fuck my [woman_role]?!"
                    scene 50280e with dissolve
                    t "NO NO MAN!"
                    scene 50280c with dissolve
                    t "I just want you to make my mom do the same to me."
                    scene 50280h with dissolve
                    e "..."
                    scene 50280d with dissolve
                    e "And how am I supposed to do it?"
                    scene 50280g with dissolve
                    t "I don't know man, you have to think of something.{i}She's home now."
                    t "I know she did it because she wanted to protect me from you."
                    t "Tell her that you and the boys will protect me, that I'm in no danger.{p}And you'll never offer me anything, and she'll believe it."
                    scene 50280e with dissolve
                    t "Maybe there's a way to do it so that she doesn't know it's me?!"
                    scene 50280i with dissolve
                    e "Ok, I'll try."
                    scene 50280g with dissolve
                    t "THANKS DUDE."
                    scene 50280c with dissolve
                    t "I'll text you the address."
                    scene 50280b with dissolve
                    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I didn't expect this "
                    if accountboosted == 0:
                        jump boostaccep5
                    jump ep5pathchoose
                else:
                    scene 50280c with dissolve
                    t "Why do you ask?"
                    t "What did my mother want from you anyway?"
                    scene 50280d with dissolve
                    e "Not now. I'll tell you when we meet.{p}Send me your address and prepare the money because I need it."
                    scene 50280c with dissolve
                    t "Ok, I'll send you a text soon. Cya."
                    scene 50280b with dissolve
                    if accountboosted == 0:
                        jump boostaccep5
                    jump ep5pathchoose

            "I need the rest of the money.":
                if telltommy == True and mtommoney == 0:
                                    scene 50280e with dissolve
                                    t "[player_name]..."
                                    t "I... I..."
                                    t "I would like to talk to you about what happened..."
                                    scene 50280d with dissolve
                                    e "Mmmm...{p}Ok."
                                    scene 50280c with dissolve
                                    t "Come to my place, I'll send you the address."
                                    scene 50280b with dissolve
                                    if accountboosted == 0:
                                        jump boostaccep5
                                    jump ep5pathchoose
                else:
                                    scene 50280c with dissolve
                                    t "Come to my place, I'll send you the address."
                                    scene 50280d with dissolve
                                    e "Great, Cya"
                                    if accountboosted == 0:
                                        jump boostaccep5
                                    jump ep5pathchoose


    else:
        stop sound
        scene 50280b with dissolve
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He didn't answer..."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Maybe he's mad at me..."
        jump ep5pathchoose

label storeep5:
    hide screen hint
    scene black with fade
    show text "General store in the city" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Afternoon" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    scene 52000 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I like this store. The owner probably has every possible thing someone would want to buy."

label shopep5storelist:
    scene 52000 with dissolve
    if easymode:
        show screen hint("EASYMODE: Blindfold for Threesome with Tommy, Red wine and lingerie for [woman_role], White wine for [nicosister_role]")
    else:
        show screen hint("I'll find many things here that will be useful to me... but what should I buy for whom?")
    show text "{font=LilitaOne.ttf}{color=#e0d71d}MONEY: [money]${/color}{/font}" at moneystat with dissolve
    menu (screen="leftchoice"):
        "Ask about something special for dates" if shopblindfold == False:
            hide screen hint
            if shopclicked == False:
                jump runrbr
            else:
                scene 52001 with dissolve
                s "Uhm.."
                scene 52002 with dissolve
                s "Do you mean some handcuffs or a whip??"
                scene 52003 with dissolve
                e "Erm... no?!{p}Something else."
                scene 52001 with dissolve
                s "Oh..."
                scene 52002 with dissolve
                s "Ok."
                scene 52003aba with dissolve
                s "A lot of people buy blindfolds.{p}To think of someone else..."
                scene 52003aba2 with dissolve
                s "I always think of my grandma."
                s "Beautiful woman."
                scene 52003aba4 with dissolve
                e "Hmm.."
                if tommyaskyouep5 == True:
                    e "This might help Tommy..."
                scene 52003aba with dissolve
                s "You want this?"
                s "Special price for you."
                scene 52003aba3 with dissolve
                s "35 bucks."
                scene 52003aba with dissolve
                s "Should I pack it?"
                scene 52003aba4 with dissolve
                if not easymode:
                    menu:
                        "Buy a night blindfold {size=-6}{color=#e0d71d}35${/color}{/size}" if money >= 35:
                            $ shopblindfold = True
                            $ money -= 35
                            play sound "music/buyshop.mp3"
                            scene 52003aba3 with dissolve
                            $ renpy.pause(1, hard=True)
                            jump shopep5storelist

                        "Look for something else.":
                            jump shopep5storelist
                else:
                    menu:
                        "Buy a night blindfold {size=-6}{color=#e0d71d}35${/color}{/size} \n{color=#3d85c6} Sharing Scene" if money >= 35:
                            $ shopblindfold = True
                            $ money -= 35
                            play sound "music/buyshop.mp3"
                            scene 52003aba3 with dissolve
                            $ renpy.pause(1, hard=True)
                            jump shopep5storelist

                        "Look for something else.":
                            jump shopep5storelist

        "Ask about some alcohol" if shopalcoholep5weak == False or shopalcoholep5strong == False:
            hide screen hint
            if shopclicked == False:
                jump runrbr
            else:
                scene 52001 with dissolve
                s "Uhm.."
                scene 52002 with dissolve
                s "Want some beer?{p}The shelves are full of it."
                scene 52003 with dissolve
                e "No, I'm looking for something stronger."
                scene 52001 with dissolve
                s "Oh..."
                scene 52002 with dissolve
                s "Date?"
                scene 52004 with dissolve
                s "When it comes to a romantic dinner with a girlfriend, I have something special."
                scene 52006wine with dissolve
                s "Two types of wine.{p}One white, weaker but delicious, and the other homemade red."
                s "But this red is very strong!"
                scene 52006wine2 with dissolve
                e "Hmm.."
                scene 52006wine with dissolve
                s "You want this?"
                scene 52006wine3 with dissolve
                s "Special price for you."
                scene 52006wine2 with dissolve
                s "$50 for white and $60 for red."
                scene 52006wine3 with dissolve
                s "Which one do you want?"
                scene 52006wine with dissolve
                label alcoholbuying:
                if not easymode:
                    menu:
                        "Buy a white wine {size=-6}{color=#e0d71d}50${/color}{/size}" if money >= 50 and shopalcoholep5weak == False :
                            $ shopalcoholep5weak = True
                            $ money -= 50
                            play sound "music/buyshop.mp3"
                            $ renpy.pause(1, hard=True)
                            jump alcoholbuying

                        "Buy a red wine {size=-6}{color=#e0d71d}60${/color}{/size}" if money >= 60 and shopalcoholep5strong == False :
                            $ shopalcoholep5strong = True
                            $ money -= 60
                            play sound "music/buyshop.mp3"
                            scene 52006red with dissolve
                            $ renpy.pause(1, hard=True)
                            s "As I said, this is homemade wine. I need to put some label on it. What kind do you want it to be there?"
                            hide screen hint
                            show screen hint("If only I remembered what [woman_name] was drinking on the balcony....")
                            scene 52006red2 with dissolve
                            menu:

                                "Merlot":
                                    hide screen hint
                                    $ winemerlot = True
                                    scene 52006red with dissolve
                                    s "Ok!"

                                "Cabernet Sauvignon":
                                    hide screen hint
                                    s "Ok!"
                                    scene 52006red with dissolve
                                    $ winecabernet = True
                            jump alcoholbuying

                        "Look for something else.":
                            jump shopep5storelist

                else:
                                    menu:
                                        "Buy a white wine {size=-6}{color=#e0d71d}50${/color}{/size} \n{color=#3d85c6} [nicosister_role] Scene" if money >= 50 and shopalcoholep5weak == False :
                                            $ shopalcoholep5weak = True
                                            $ money -= 50
                                            play sound "music/buyshop.mp3"
                                            $ renpy.pause(1, hard=True)
                                            jump alcoholbuying

                                        "Buy a red wine {size=-6}{color=#e0d71d}60${/color}{/size} \n{color=#3d85c6} [woman_name] Scene" if money >= 60 and shopalcoholep5strong == False :
                                            $ shopalcoholep5strong = True
                                            $ money -= 60
                                            play sound "music/buyshop.mp3"
                                            scene 52006red with dissolve
                                            $ renpy.pause(1, hard=True)
                                            s "As I said, this is homemade wine. I need to put some label on it. What kind do you want it to be there?"
                                            hide screen hint
                                            show screen hint("If only I remembered what [woman_name] was drinking on the balcony....")
                                            scene 52006red2 with dissolve
                                            menu:

                                                "Merlot \n{color=#3d85c6} [woman_name] Scene":
                                                    hide screen hint
                                                    $ winemerlot = True
                                                    scene 52006red with dissolve
                                                    s "Ok!"

                                                "Cabernet Sauvignon":
                                                    hide screen hint
                                                    s "Ok!"
                                                    scene 52006red with dissolve
                                                    $ winecabernet = True
                                            jump alcoholbuying

                                        "Look for something else.":
                                            jump shopep5storelist

            jump shopep5storelist

        "Ask about something sexy to wear" if shopsexyep5wear == False:
            scene 52000dres3 with dissolve
            s "You're lucky today!"
            scene 52000dres2 with dissolve
            s "Give me a moment."
            scene 52000dres with dissolve
            s "I have something like this."
            scene shopdress with dissolve
            e "And what is it?"
            s "Someone left it here once, and never came back for it in 2 years, so I kept it here just in case"
            e "I see."
            e "Do you think it'll fit?"
            s "I don't know, what size do you need?"
            e "How am I supposed to know!?"
            s "You're supposed to know that! What size does she look like?"
            e "Slim...Blonde..."
            s "It'll fit her, yeah..."
            e "..."
            e "And for a brunette?"
            s "Especially brunettes."
            e "Man, you'd say anything to make a sale..."
            s "If you say so... Shall I wrap it?"
            if not easymode:
                menu:
                        "Buy Sexy Lingerie {size=-6}{color=#e0d71d}60${/color}{/size}" if money >= 60:
                            $ shopsexyep5wear = True
                            $ money -= 60
                            play sound "music/buyshop.mp3"
                            e "There's no need to wrap it up"
                            $ renpy.pause(1, hard=True)
                            jump shopep5storelist

                        "Look for something else.":
                            jump shopep5storelist

            else:
                menu:
                        "Buy Sexy Lingerie {size=-6}{color=#e0d71d}60${/color}{/size} \n{color=#3d85c6} [woman_name] Scene" if money >= 60:
                            $ shopsexyep5wear = True
                            $ money -= 60
                            play sound "music/buyshop.mp3"
                            e "There's no need to wrap it up"
                            $ renpy.pause(1, hard=True)
                            jump shopep5storelist

                        "Look for something else.":
                            jump shopep5storelist

            jump shopep5storelist

        "Collect your package" if shoppackage == False:
            if shopclicked == False:
                jump runrbr
            else:
                hide screen hint
                show screen hint ("Legal drug delivery. Good thing no one has figured out yet to check packages sent from the same city.")
                scene 52003 with dissolve
                e "Did someone leave a package for me?"
                scene 52004a with dissolve
                s "Hmm... Let me see..."
                scene 52004 with dissolve
                s "Yeah... there's one for [player_name]"
                s "But for cash on delivery, you have to pay 30 dollars."
                menu:
                    "Pick up a package of drugs {size=-6}{color=#e0d71d}30${/color}{/size}" if money >= 30:
                        $ shoppackage = True
                        $ money -= 30
                        play sound "music/buyshop.mp3"
                        scene 52001a with dissolve
                        $ renpy.pause(1, hard=True)
                        hide screen hint
                        jump shopep5storelist

                    "Look for something else.":
                        hide screen hint
                        jump shopep5storelist

        "Buy a scratch for 2$" if money >= 2 and scratchnumber < 100:
            $ money -= 2
            $ scratchnumber += 1
            if scratchnumber >= 100:
                $ renpy.pause(1, hard=True)
                s "Oh, im very sorry but i don't have more..." with vpunch
                e "Damn!!"
                $ renpy.pause(1, hard=True)
                jump shopep5storelist
            call scratch_card
            jump shopep5storelist

        "Leave shop":
            jump aftershopdecision


label aftershopdecision:
    hide screen hint
    scene 52100 with dissolve
    e "Ok.. so what now?"

label aftershopping:
    hide screen hint
    menu:
        "{color=#FFD1DF}{i}*Return to the store*":
            jump shopep5storelist

        "{color=#FFD1DF}{i}*Visit Tommy*" if mtommyep5enterdoor == False:
            jump triptotommy

        "{color=#FFD1DF}{i}*Call Gary and sell him drugs*{/i}{/color} {size=-8}(Req. Phone, Drugs){/size}" if shoppackage and garrydidntbuy:
            jump garrycallworkout

        "{color=#FFD1DF}{i}*Take a bus to [nicosister_role]*{/i}{/color} {size=-6}{color=#e0d71d}10${/color}{/size}" if money >= 10 and auntfinish == False:
                    $ money -= 10
                    play sound "music/buyshop.mp3"
                    jump triptoaunt

        "{color=#FFD1DF}{i}*Return home*":
            jump triptohome

label garrycallworkout:
    if phonelive == False:
           menu:
               "Do you want to spend $25 and top up your phone account?"

               "Yes {size=-6}{color=#e0d71d}25${/color}{/size}" if money >= 25:
                       $ money -= 25
                       play sound "music/buyshop.mp3"
                       $ accountboosted += 1
                       $ phonelive = True
                       jump garrycallworkout
               "No":
                       jump sandboxep5menu

    elif phonelive:
            $ counter = 41

            while True:
                show garryworkout with dissolve
                show text "[counter]" at title2 with dissolve


                if counter >= 100:
                    jump garryisstrong

                $ counter += 1

                $ result = renpy.pause(0.50)

                if result:
                    "{color=#ffa500}{i}*Phone ringing*{/i}"
                    scene garrycall10 with dissolve
                    jump garryanswer
label garryisstrong:
    play sound "music/scouter.mp3"
    show garryspace
    $ renpy.pause(5, hard=True)
    scene garryover
    i "What does a scouter say about his power level?"
    j "I...IMPOSSIBLE!"
    j "It's OVER 9000!!" with vpunch
    i "WHAAT?!"
    $ z3kr3t = True
    i "We won't conquer Earth and fuck their girls if they're all like that.{p}We need to train more!!"
    if not persistent.gstwac:
            show gstwach at achievment with easeintop:
                    zoom 0.5
                    rotate_animation

            "S3CR3T 4CH13VM3NT{p}\"Garry saved the world!\"."
            hide gstwach
            $ persistent.gstwac = True
    scene garrycall10 with dissolve
    "{color=#ffa500}{i}*Phone ringing*{/i}"
    jump garryanswer

label garryanswer:
            p "Got anything for me?"
            e "Yeah...fresh delivery."
            p "Great, leave them in the usual spot. I'll send the money soon."
            show garryworkout with dissolve
            $ garrypumpmuscles = True
            $ garrydidntbuy = False
            $ money += 40
            show text "{color=#00ff00}{size=+15}+4 0 ${/color}" with dissolve
            with Pause(2)
            show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
            hide text with dissolve
            if accountboosted == 1:
                jump aftergarrycalldecision
            else:
                $ phonelive = False
                jump aftergarrycalldecision

label aftergarrycalldecision:
            menu:
                "{color=#FFD1DF}{i}*Return to the store*":
                    jump shopep5storelist

                "{color=#FFD1DF}{i}*Visit Tommy*" if mtommyep5enterdoor == False:
                    jump triptotommy

                "{color=#FFD1DF}{i}*Take a bus to [nicosister_role]*{/i}{/color} {size=-6}{color=#e0d71d}10${/color}{/size}" if money >= 10 and auntfinish == False:
                    $ money -= 10
                    play sound "music/buyshop.mp3"
                    jump triptoaunt

                "{color=#FFD1DF}{i}*Return home*" :
                    jump triptohome

label triptotommy:
    stop music fadeout 1.0
    play music "music/Mtom.wav"
    scene black with fade
    scene 52101 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I guess it's here."
    scene 52102 with dissolve
    scene 52102a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Quite a nice area."
    scene 52103a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hm hm hm...{p} He lives on the first floor..."
    scene 52103 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Someone hasn't closed the door"
    scene 52103b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Nice...{p} Maybe I can sneak in quietly."
    menu:
        "Come inside":
            jump tommyep5houseinside

        "Later":
            label outsidetommyhouse:
                hide screen hint
                scene 51000a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i}What now?"
                menu:
                    "{color=#FFD1DF}{i}*Go to Tommy's house*":
                        jump tommyep5houseinside

                    "{color=#FFD1DF}{i}*Return to the store*":
                        jump shopep5storelist

                    "{color=#FFD1DF}{i}*Call Gary and sell him drugs*{/i}{/color} {size=-8}(Req. Phone, Drugs){/size}" if shoppackage and garrydidntbuy:
                        jump garrycallworkout

                    "{color=#FFD1DF}{i}*Take a bus to [nicosister_role]*{/i}{/color} {size=-6}{color=#e0d71d}10${/color}{/size}" if money >= 10 and auntfinish == False:
                        $ money -= 10
                        play sound "music/buyshop.mp3"
                        jump triptoaunt

                    "{color=#FFD1DF}{i}*Return home*":
                        jump triptohome


label tommyep5houseinside:
    scene black with fade
    scene 52104 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This is his apartment"
    scene 52105 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Electric door lock?!"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Let me think..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} 3 keys look very worn...{p}{b}0{/b}... {b}1{/b}... and {b}4{/b}..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} and 1 and 0 are much more worn than number 4..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Neither Tommy nor his mother seem smart, so it can't be anything difficult..."

label mtommydoormenu:
    scene 52105 with dissolve
    hide screen hint
    show screen hint("It's probably some combination of 0, 1 and 4")
    menu:

        "{color=#FFD1DF}{i}*Try to break the code*{/i}{/color}":
            jump doorcode
        "{color=#FFD1DF}{i}*Call Tommy*{/i}{/color} {size=-8}(Req. Phone){/size}" if phonelive == True and tommydidntanswer == False:
            jump calltommyfordoor
        "{color=#FFD1DF}{i}*Leave*{/i}{/color}":
            jump outsidetommyhouse

label calltommyfordoor:
    hide screen hint
    stop music fadeout 1.0
    scene 52150 with dissolve
    t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} If you cut a sandwich in half, does it still count as one sandwich?"
    play sound "music/tommyphone.mp3"
    show screen idle_czek
    "{color=#ffa500}{i}*Phone ringing*{/i}"

label s3cr3tach:
    scene 52150a with dissolve
    t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh, I wonder who that is?"
    t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} [player_name]?"
    hide screen idle_czek
    if tommyfriend > 0:
        stop sound
        scene 52150b with dissolve
        t "What's up, [player_name]?"
        e "{i}{size=-2}*whispering*{/size}{/i} Give me the code to your apartment."
        if tommyaskyouep5 == True:
            scene 52150c with dissolve
            t "Uhm... but I'm not there."
            t "And my mom is at work now."
            e "{i}{size=-2}*whispering*{/size}{/i} Give me that code, I need to check something."
            t "Like what?"
            e "{i}{size=-2}*whispering*{/size}{/i} Give me the fucking code if you want me to help you."
            scene 52150b with dissolve
            t "Ok, ok. Chill...{p}It was..."
            t "1... and then 0 ... or 4... 0... and 1 and 4?"
            scene 52150d with dissolve
            t "Shit, I can't remember now "
            t "But it definitely starts with 101"
            $ tommytellcodewhilecall = True
            e "{i}{size=-2}*whispering*{/size}{/i} You seriously can't remember your door code?!?"
            scene 52150b with dissolve
            t "Hehe"
            t "Man, I have so many thoughts in my head that it's slipped my mind right now."
            t "For example, if you cut a sandwich..."
            scene 52150a with dissolve
            t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh..He hung up... "
            $ tommyhelpwithcode = True
            $ tommydidntanswer = True
            play music "music/Mtom.wav"
            jump mtommydoormenu
        else:
             scene 52150c with dissolve
             t "Uhm... but I'm not there."
             e "{i}{size=-2}*whispering*{/size}{/i} Give me that code, I need to check something."
             t "Like what?"
             e "{i}{size=-2}*whispering*{/size}{/i} Just give me the code."
             t "Uhm... just wait for me, I'll be there soon."
             scene 52150a with dissolve
             t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh..He hung up... "
             $ tommydidntanswer = True
             play music "music/Mtom.wav"
             jump mtommydoormenu
    else:
        scene 52150 with dissolve
        t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Fuck him."
        $ tommydidntanswer = True
        stop sound
        play music "music/Mtom.wav"
        jump mtommydoormenu


label doorcode:
    if itguy == 1 and not easymode:
            "PERK {color=#5ed42f}{b}ITGUY{/b}{/color}{p} I know these systems, the first digit is the floor number and the last is always 4."
            hide screen hint
            show screen hint("It's probably some combination of 0, 1 and 4...{p}The first digit is the floor number and the last is always 4.")
    if easymode:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Maybe just the apartment number?"

    if tommytellcodewhilecall == True:
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Tommy said that at the beginning there is '101'"

    $ codedoor = renpy.input("Enter 5 numbers to open the door. \n {i}(write your answer){/i}")
    $ codedoor = codedoor.strip() or "..."

    if codedoor.find("10104") != -1 or codedoor.find("10-104") != -1:
                jump dooropenep5

    else:
                jump doorclosed

label doorclosed:
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Nothing happened..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Lets try again!"

    menu:
        "Try Again?"

        "Yes":
                jump doorcode
        "No":
                jump mtommydoormenu

label dooropenep5:
    $ mtommyep5enterdoor = True
    hide screen hint
    play sound "music/dooropen.mp3"
    scene 52105a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Really?!"
    scene 52104 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Do they really have the apartment number as the access code?"
    scene black with fade
    pause
    scene 50305 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} And now quietly..."
    z "Yes, boss, I'm already on it."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Interesting..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Tommy's Mom is in the room right next to the door."
    z "I'm checking the documents now... I'll call you back once I find it..."
    z "Why so quiet? There's no one in the office but me today."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Someone might be lying here..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I wonder how she'll react when she sees me."
    scene 50305d with dissolve
    pause
    scene 50306 with vpunch
    z "WHA...!"
    scene 50306a with dissolve
    z "Uh, um..."
    scene 503052 with dissolve
    scene 503053 with dissolve
    scene 503054 with vpunch
    z "Nothing happened... I was just startled by the courier."
    scene 503055 with dissolve
    z "I'm really sorry, boss, but I have to hang up."
    scene 503055a with dissolve
    z "Of course, I'll take care of it as soon as possible."
    z "Alright, I'll talk to you later. Thanks, and goodbye!"
    scene 503055b with dissolve
    pause
    scene 50307 with dissolve
    z "WHAT THE FUCK ARE YOU DOING HERE?"
    scene 50307a with dissolve
    z "YOU NEED TO LEAVE NOW, OR I'LL CALL THE POLICE."
    scene 50308a with dissolve
    e "Is Tommy home?"
    scene 50308 with dissolve
    z "NO.{p}HOW DID YOU GET IN HERE?!"
    scene 50308a with dissolve
    e "Tommy gave me the code."
    scene 50309 with dissolve
    z "What?!... Why?"

    if mtommoney == 1:
        scene 50308a with dissolve
        e "Because it's a new week and I'm here for the next part."
        scene 50308 with dissolve
        z "Do you think I'll pay you every week?!"
        scene 50309 with dissolve
        e "Yes, because it's for your Tommy."
        scene 50308 with dissolve
        z "GET THE FUCK OUT OF HERE."
        scene 50310 with dissolve
        z "HELP! HELP!" with vpunch
        e "SHIT!"
        scene black with fade
        jump sandboxep5menu

    if tommymomsubmission > 1 and telltommy == False:
        scene 50311 with dissolve
        e "Because I really liked what you did and you should do it again for Tommy."
        jump part1part2

    if tommymomsubmission > 1 and telltommy == True:
        scene 50311 with dissolve
        e "Because he interrupted us earlier and we didn't finish."
        scene 50311a with dissolve
        z "Don't lie. Tommy definitely wouldn't do that."
        scene 50311d with dissolve
        z "Do you realize how difficult it was to talk to Tommy after all that?"
        scene 50311a with dissolve
        e "I'm sure you explained to him that it was all for his own good."
        e "You didn't do anything wrong there.{p}Just a handjob to an attractive friend."
        jump part1part2

    else:
        jump part1part2

label part1part2:
     scene 50311b with dissolve
     e "It doesn't matter why I'm here.{p}What's important is that I'm here because your Tommy's safety is in your hands."
     scene 50311c with dissolve
     e "And I want much more than last time..."
     scene 50311b with dissolve
     z "You’re sick."
     scene 50311d with dissolve
     z "Leave this apartment or I’ll start screaming."
     scene 50311e with dissolve
     e "You won’t do that because you know how it will end."
     scene 50311b with dissolve
     e "So instead of yelling...{p}I'll use your mouth for better purposes."
     scene 50311 with dissolve
     z "Wh....What?"
     scene 50311c with dissolve
     e "Besides, you seem to be in a hurry... you don't want your boss to find out you're not at work."
     scene 50311b with dissolve
     e "And Tommy will probably be back soon..."
     if tommymomsubmission > 1 and telltommy == True:
        scene 50311 with dissolve
        e "You probably don't want him to see us together again, or he might think he’ll have a new daddy, hehe."
     else:
        e "It might look strange if he sees us..."
     scene 50311d with dissolve
     z "You are a terrible person."
     scene 50311c with dissolve
     e "Decide quickly what we're doing.{p}Your boss will probably call soon..."
     scene 50311e with dissolve
     z "Fine."
     z "I’ll do the same thing I did last time. But Tommy must never find out."
     scene 50311c with dissolve
     e "Nah... "
     scene 50311c with dissolve
     e "You'll suck me off."

     menu:
        "{color=#FFD1DF}{i}*Take off her glasses*{/i}{/color}":
            jump takeoffglasses

        "{color=#FFD1DF}{i}*Leave the glasses on*{/i}{/color}":
            $ tommymomhas = 8
            jump leaveglasses

label leaveglasses:
         scene 50325wg with dissolve
         e "Now get on the bed"
         scene 50325wga with dissolve
         pause
         scene 50325wgb with dissolve
         pause
         jump mtombjep5withglass

label takeoffglasses:
     scene 50321 with dissolve
     e "You don't need these..."
     scene 50322 with dissolve
     e "Much better"

     if tommyep5call1 == True and shopblindfold == True:
            show screen hint ("If I cover her eyes, maybe I can somehow get Tommy in here...")
            menu:
                "{color=#FFD1DF}{i}Give her a blindfold":
                    $ tommymomhas = 3
                    $ shopblindfold = False
                    hide screen hint
                    jump giveblindfold

                "{color=#FFD1DF}{i}Tell her to get on the bed":
                    $ tommymomhas = 0
                    hide screen hint
                    jump mtombjep5withoutg

     elif shopblindfold == True:
            menu:
                "{color=#FFD1DF}{i}Give her a blindfold":
                    $ tommymomhas = 3
                    $ shopblindfold = False
                    hide screen hint
                    jump giveblindfold

                "{color=#FFD1DF}{i}Tell her to get on the bed":
                    $ tommymomhas = 0
                    hide screen hint
                    jump mtombjep5withoutg

     else:
            jump mtombjep5withoutg

label mtombjep5withglass:
     scene 50358bj_withglasses with dissolve
     e "You see... there's nothing to be afraid of."
     scene 50358bj_withglasses2 with dissolve
     e "Tommy's future is in your mouth hehe."
     scene 50358bj_withglasses3 with vpunch
     "{color=#A8E4A0}{i}{size=-3} If it weren't for you stuffing her mouth with your dick, she would probably scream."
label mtomsolobjwithgscene:
     hide mtomep5cam2
     show mtomsolobjwithg with dissolve
     $ renpy.pause(2, hard=True)
     menu (screen="rightchoice"):
        "Change view":
            jump solomtomcam2scenewithg
        "Continue":
            jump mtomtomep5withg

label solomtomcam2scenewithout:
     hide mtomsolobjwithout
     show mtomep5cam2 with dissolve
     $ renpy.pause(2, hard=True)
     menu (screen="rightchoice"):
        "Change view":
            jump mtomsolobjwithoutscene
        "Continue":
            jump mtomtomep5without

label solomtomcam2scenewithg:
     hide mtomsolobjwithg
     show mtomep5cam2 with dissolve
     $ renpy.pause(2, hard=True)
     menu (screen="rightchoice"):
        "Change view":
            jump mtomsolobjwithgscene
        "Continue":
            jump mtomtomep5withg

label mtombjep5withoutg:
     scene 50325withoutg with dissolve
     e "Now get on the bed"
     scene 50325withoutga with dissolve
     pause
     scene 50325withoutgb with dissolve
     pause
     scene 50358bj_withoutg with dissolve
     e "You see... there's nothing to be afraid of."
     scene 50358bj_withoutg2 with dissolve
     e "Tommy's future is in your mouth hehe."
     scene 50358bj_withoutg3 with vpunch
     "{color=#A8E4A0}{i}{size=-3} If it weren't for you stuffing her mouth with your dick, she would probably scream."
label mtomsolobjwithoutscene:
     hide mtomep5cam2
     show mtomsolobjwithout with dissolve
     $ renpy.pause(2, hard=True)
     menu (screen="rightchoice"):
        "Change view":
            jump solomtomcam2scenewithout
        "Continue":
            jump mtomtomep5without


label giveblindfold:
     $ mtommyblindfoldon = True
     scene 50323a with dissolve
     e "Put this on."
     scene 50323 with dissolve
     z "Why?"
     scene 50322 with dissolve
     e "I bought this especially for you.{p}So you don't have to look at me while you suck my cock..."
     scene 50324 with dissolve
     z "Uhm..."
     scene 50323 with dissolve
     z "Okay..."
     scene 50324a with dissolve
     "{color=#A8E4A0}{i}{size=-3}She put on a blindfold"
     scene 50325 with dissolve
     e "Now get on the bed"
     scene 50325a with dissolve
     pause
     scene 50325b with dissolve
     pause
label replayep5mtom3some:
     scene 50352 with dissolve
     e "You see... there's nothing to be afraid of."
     e "Tommy's future is in your mouth hehe."
     scene 50352a with dissolve
     z "*whispering softly* Just... do it.."

label mtomcam1bj:
     hide mtomep5cam2
     show mtomep5cam1 with dissolve
     $ renpy.pause(2, hard=True)

     menu (screen="rightchoice"):
        "Change view":
            jump mtomcam2bj
        "Continue":
            jump mtomtomep5

label mtomcam2bj:
     hide mtomep5cam1
     show mtomep5cam2 with dissolve
     $ renpy.pause(2, hard=True)

     menu (screen="rightchoice"):
        "Change view":
            jump mtomcam1bj
        "Continue":
            jump mtomtomep5

label mtomtomep5withg:
    scene 503530 with dissolve
    e "Hmm?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Interesting..."

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Signal him to come closer*{/i}{/color}\n{size=-8}(Req. Eyes covered with a blindfold){/size}" if mtommyblindfoldon == True:
                jump mtomshare
            "{color=#FFD1DF}{i}*Show him the middle finger*{/i}{/color}\n{color=#3d85c6} Tommy -1, A small number of points may block the next scenes with him.":
                scene 503532a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
                $ tommyfriend -= 1
                $ tommymiddlefing = True
                "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
                jump mtomblindfoldsolowithg
            "{color=#FFD1DF}{i}*Don't do anything*{/i}{/color}":
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You can watch as your mother serves me."
                $ tommyep5peeping = True
                jump mtomblindfoldsolowithg

    else:
        menu:
            "{color=#FFD1DF}{i}*Signal him to come closer*{/i}{/color}\n{size=-8}(Req. Eyes covered with a blindfold){/size}" if mtommyblindfoldon == True:
                jump mtomshare
            "{color=#FFD1DF}{i}*Show him the middle finger*{/i}{/color}":
                scene 503532a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
                $ tommyfriend -= 1
                $ tommymiddlefing = True
                "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
                jump mtomblindfoldsolowithg
            "{color=#FFD1DF}{i}*Don't do anything*{/i}{/color}":
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You can watch as your mother serves me."
                $ tommyep5peeping = True
                jump mtomblindfoldsolowithg

label mtomtomep5without:
    scene 503530 with dissolve
    e "Hmm?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Interesting..."

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Signal him to come closer*{/i}{/color}\n{size=-8}(Req. Eyes covered with a blindfold){/size}" if mtommyblindfoldon == True:
                jump mtomshare
            "{color=#FFD1DF}{i}*Show him the middle finger*{/i}{/color}\n{color=#3d85c6} Tommy -1":
                scene 503532a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
                $ tommyfriend -= 1
                $ tommymiddlefing = True
                "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
                jump mtomblindfoldsolowithout
            "{color=#FFD1DF}{i}*Don't do anything*{/i}{/color}":
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You can watch as your mother serves me."
                $ tommyep5peeping = True
                jump mtomblindfoldsolowithout

    else:
        menu:
            "{color=#FFD1DF}{i}*Signal him to come closer*{/i}{/color}\n{size=-8}(Req. Eyes covered with a blindfold){/size}" if mtommyblindfoldon == True:
                jump mtomshare
            "{color=#FFD1DF}{i}*Show him the middle finger*{/i}{/color}":
                scene 503532a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
                $ tommyfriend -= 1
                $ tommymiddlefing = True
                "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
                jump mtomblindfoldsolowithout
            "{color=#FFD1DF}{i}*Don't do anything*{/i}{/color}":
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You can watch as your mother serves me."
                $ tommyep5peeping = True
                jump mtomblindfoldsolowithout


label mtomblindfoldsolowithout:
     show mtomsolobjwithout with dissolve
     $ renpy.pause(3, hard=True)
     scene 50359 with vpunch
     e "I'm bored"
     scene 50359a with vpunch
     e "Time for the main course."
     scene 50359bwithoutglass3 with dissolve
     z "WHAT THE HELL!?"
     scene 50359cwithoutglass with dissolve
     e "You're in no danger."
     scene 50359bwithoutglass2 with dissolve
     z "I didn't agree to any of that."
     scene 50359bwithoutglass with dissolve
     e "I'll fuck you and leave."
label mtomtakeoffbf:
     $ tommymomhas = 0
     scene 50359bwithoutglass3 with dissolve
     z "LET ME GO!"
     scene 50359bwithoutglass2 with dissolve
     e "Remember you're doing this for Tommy."
     scene 50359bwithoutglass with dissolve
     e "All the boys in the neighborhood will protect him and he will be safe throughout his studies."
     scene 50359cwithoutglass with dissolve
     e "And I won't sell him any more shit."
     scene 50359bwithoutglass with dissolve
     z "You are the same age as my son.{p}This is sick."
     e "I promise your Tommy will be happy."
     scene 50359dwithoutglass with dissolve
     e "But I also have to be satisfied."
     scene 50359ewithoutglass with dissolve
     e "Damn Girl...{p}You don't even wear panties."
     scene 50359fwithoutglass with vpunch
     e "Lie down and stick your ass out."
     scene laymtom0 with dissolve
     z "Uhm..."
     scene 50331 with dissolve
     z "If you lie to me..."
     e "I won't do that..."
     scene v2final000 with vpunch
     "{color=#A8E4A0}{i}{size=-3}You grabbed her ass and pulled her down onto your cock.{/i}"
     show mtomsolo
     $ renpy.pause(3, hard=True)
     "{color=#A8E4A0}{i}{size=-3}Her wet pussy invites you deeper with each thrust.{/i}"
     pause
     "{color=#A8E4A0}{i}{size=-3}She doesn't even try to resist while you fuck her and treat her like a common whore.{/i}"
     e "Damn, you’ve got the perfect ass for this... So good to fuck from behind."
     "{color=#A8E4A0}{i}{size=-3}With each thrust, the sound of skin meeting skin grows louder, and her moans become more intense.{/i}"
     pause
     "{color=#A8E4A0}{i}{size=-3}You've managed to completely dominate this bitch, but you feel like you won't last much longer.{/i}"

     menu (screen="rightchoice"):
        "I want to cum on your face.":
            z "....{p}no...."
            hide mtomsolo
            scene mtomgetup with vpunch
            e "Come to me"
            jump mtomep5cmonface
        "I want to cum in your mouth":
            z "....{p}no...."
            jump mtomep5cminmouth

label mtomep5cmonface:
    show cofwithout with dissolve
    $ renpy.pause(15, hard=True)
    e "AAAAAAAHHHH FUCK"
    pause
    e "Looks like I'm your boss now."
    pause
    e "But don't worry, I'm good to my bitches."
    scene aftercmwithoutfinal with dissolve
    z "..."
    scene aftercmwithoutfinal2 with dissolve
    z "Leave..."
    $ renpy.end_replay()
    if not _in_replay:
        $ persistent.mtomep5cmonface = True
    jump aftercmimep5mtom


label mtomep5cminmouth:
    scene laymtom0 with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    scene laymtom1 with dissolve
    pause 0.25
    scene laymtom2 with dissolve
    pause 0.25
    scene laymtom3 with dissolve
    pause 0.25
    scene laymtom4 with dissolve
    pause 0.25
    scene laymtom5 with dissolve
    pause 0.25
    scene laymtom6 with dissolve
    pause 0.25
    scene laymtom7 with dissolve
    pause 0.25
    scene laymtom8 with dissolve
    pause 0.25
    scene laymtom9 with dissolve
    pause 0.25
    "{color=#A8E4A0}{i}{size=-3}You laid down next to her.{/i}"
    scene 50331 with dissolve
    e "Hey{p}Look at me."
    z "{color=#ffa500}{i}*She let out a soft moan.*{/i}{/color}"
    scene 50333 with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    e "My cock is covered in your juices, lick it."
    scene 50332 with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    z "I don't want to..."
    scene 50333 with dissolve
    e "You know what?"
    scene mtomcminmt with dissolve
    e "I'm not asking..."
    scene mtomcminmt2 with dissolve
    e "I deserve a reward for fucking you so hard."
    scene mtomcminmt3 with dissolve
    $ timeout_label = "mtommyep5afterkiss"
    $ timeout = 0.5
    menu:

        "{color=#FFD1DF}{i}Kiss her":
            scene mtomcminmt4 with dissolve
            "{color=#A8E4A0}{i}{size=-3}You took the opportunity and kissed her on the lips, but she was so tired that she didn't kiss you back."
            if not easymode and not _in_replay:
                $ achValid5 += 1
                $ achievement.grant("Achiev19")
                $ achievement.sync()
                if not persistent.achievement19:

                                             show Achiev19 at achievment with easeintop:
                                                        zoom 0.5
                                                        rotate_animation

                                             "You have received the achievement!{p}{b}\"Instant reaction!\".{/b}"
                                             "Number of achievements earned in this chapter [achValid5]/8"
                                             hide Achiev19
                                             $ persistent.achievement19 = True
            scene mtomcminmt3 with dissolve
            e "Now suck me"
            scene mtomcminmt2 with dissolve
            pause 0.25

label mtommyep5afterkiss:
    $ tommymomhas = 0
    scene mtomcminmt5 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She obediently leaned against your stomach and took your cock into her mouth while you began to pleasure her with your finger."
    show mtomskside5ep with dissolve
    "{color=#A8E4A0}{i}{size=-3}The amount of her pussy juices dripping onto your hand could mean that she either hasn't done it in a while or she's really turned on by the whole situation...{/i}"
    e "I wonder what your husband would say if he saw what you're doing with my dick right now."
    e "Sucking off your son's friend."
    "{color=#A8E4A0}{i}{size=-3}She didn't answer, either ignoring your words or being too busy with your cock."
    e "Don't you dare take it out of your mouth now"
    e "Ahh...."
    if tommymomhas == 0:
        hide mtomskside5ep
        show mtomcminmoutwithout with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalwithout with dissolve
        e "Thanks"
        jump aftercmimep5mtom

    elif tommymomhas == 3:
        hide mtomskside5ep
        show mtomcminbf with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalbf with dissolve
        e "Thanks"
        jump aftercmimep5mtom

    elif tommymomhas == 8:
        hide mtomskside5ep
        show mtomcminglass with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalwithg with dissolve
        e "Thanks"
        jump aftercmimep5mtom

label aftercmimep5mtom:
    $ maxmccumep7 += 1
    if not _in_replay:
        $ persistent.mtomcinm = True
    scene black with Fade(2.0, 1.0, 2.0)
    e "I have to drop by more often because I see we have a great connection."
    z "...{p}...what?"
    "{color=#A8E4A0}{i}{size=-3} You left the apartment."
    $ renpy.end_replay()
    jump aftersxmtomep5


label mtomblindfoldsolowithg:
     show mtomsolobjwithg with dissolve
     $ renpy.pause(3, hard=True)
     scene 50359 with vpunch
     e "I'm bored"
     scene 50359a with vpunch
     e "Time for the main course."
     scene 50359withg0a with dissolve
     z "WHAT THE HELL?!"
     scene 50359withg0a with dissolve
     e "You're in no danger."
     scene 50359withg0c with dissolve
     z "I didn't agree to any of that."
     scene 50359withg0d with dissolve
     e "I'll fuck you and leave."
     scene 50359withg0a with dissolve
     z "LET ME GO!"
     scene 50359withg0e with dissolve
     e "Remember you're doing this for Tommy."
     scene 50359withg0f with dissolve
     e "All the boys in the neighborhood will protect him and he will be safe throughout his studies."
     scene 50359withg0g with dissolve
     e "And I won't sell him any more shit."
     z "You are the same age as my son.{p}This is sick."
     e "I promise your Tommy will be happy."
     scene 50359withg0next with dissolve
     e "But I also have to be satisfied."
     scene 50359withg0next2 with vpunch
     e "Damn Girl...{p}You don't even wear panties."
     scene 50359withg3 with vpunch
     e "Lie down and stick your ass out."
     scene laymtom0 with dissolve
     z "Uhm..."
     scene 50331 with dissolve
     z "If you lie to me..."
     e "I won't do that..."
     scene v2final000 with vpunch
     "{color=#A8E4A0}{i}{size=-3}You grabbed her ass and pulled her down onto your cock.{/i}"
     show mtomsolo
     $ renpy.pause(3, hard=True)
     "{color=#A8E4A0}{i}{size=-3}Her wet pussy invites you deeper with each thrust.{/i}"
     pause
     "{color=#A8E4A0}{i}{size=-3}She doesn't even try to resist while you fuck her and treat her like a common whore.{/i}"
     e "Damn, you’ve got the perfect ass for this... So good to fuck from behind."
     "{color=#A8E4A0}{i}{size=-3}With each thrust, the sound of skin meeting skin grows louder, and her moans become more intense.{/i}"
     pause
     "{color=#A8E4A0}{i}{size=-3}You've managed to completely dominate this bitch, but you feel like you won't last much longer.{/i}"

     menu (screen="rightchoice"):
        "I want to cum on your face.":
            z "....{p}no...."
            hide mtomsolo
            scene mtomgetup with vpunch
            e "Come to me"
            jump mtomep5cmonfacewithg
        "I want to cum in your mouth":
            z "....{p}no...."
            jump mtomep5cminmouthwithg

label mtomep5cmonfacewithg:
    show cofwithg with dissolve
    $ renpy.pause(15, hard=True)
    e "AAAAAAAHHHH FUCK"
    pause
    e "Looks like I'm your boss now."
    pause
    e "But don't worry, I'm good to my bitches."
    scene 50362aftercmglass1 with dissolve
    z "..."
    scene aftercmglassfinal2 with dissolve
    z "Leave..."
    if not _in_replay:
        $ persistent.mtomep5cmonface = True
    jump aftercmimep5mtom

label mtomep5cminmouthwithg:
    scene laymtom0 with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    scene laymtom1 with dissolve
    pause 0.25
    scene laymtom2 with dissolve
    pause 0.25
    scene laymtom3 with dissolve
    pause 0.25
    scene laymtom4 with dissolve
    pause 0.25
    scene laymtom5 with dissolve
    pause 0.25
    scene laymtom6 with dissolve
    pause 0.25
    scene laymtom7 with dissolve
    pause 0.25
    scene laymtom8 with dissolve
    pause 0.25
    scene laymtom9 with dissolve
    pause 0.25
    "{color=#A8E4A0}{i}{size=-3}You laid down next to her.{/i}"
    scene 50331 with dissolve
    e "Hey{p}Look at me."
    z "{color=#ffa500}{i}*She let out a soft moan.*{/i}{/color}"
    scene 50333_glass with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    e "My cock is covered in your juices, lick it."
    scene 50332_glass with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    z "I don't want to..."
    scene 50333_glass with dissolve
    e "You know what?"
    scene mtomcminmt with dissolve
    e "I'm not asking..."
    scene mtomcminmt2 with dissolve
    e "I deserve a reward for fucking you so hard."
    scene mtomcminmt3glass with dissolve
    $ timeout_label = "mtommyep5afterkisswithg"
    $ timeout = 0.5
    menu:

        "{color=#FFD1DF}{i}Kiss her":
            scene mtomcminmt4glass with dissolve
            "{color=#A8E4A0}{i}{size=-3}You took the opportunity and kissed her on the lips, but she was so tired that she didn't kiss you back."
            if not easymode:
                $ achValid5 += 1
                $ achievement.grant("Achiev19")
                $ achievement.sync()
                if not persistent.achievement19:
                                             show Achiev19 at achievment with easeintop:
                                                        zoom 0.5
                                                        rotate_animation

                                             "You have received the achievement!{p}{b}\"Instant reaction!\".{/b}"
                                             "Number of achievements earned in this chapter [achValid5]/8"
                                             hide Achiev19
                                             $ persistent.achievement19 = True
            scene mtomcminmt3glass with dissolve
            e "Now suck me"

label mtommyep5afterkisswithg:
    $ tommymomhas = 8
    scene mtomcminmt2 with dissolve
    pause 0.25
    scene mtomcminmt5 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She obediently leaned against your stomach and took your cock into her mouth while you began to pleasure her with your finger."
    show mtomskside5ep with dissolve
    "{color=#A8E4A0}{i}{size=-3}The amount of her pussy juices dripping onto your hand could mean that she either hasn't done it in a while or she's really turned on by the whole situation...{/i}"
    e "I wonder what your husband would say if he saw what you're doing with my dick right now."
    e "Sucking off your son's friend."
    "{color=#A8E4A0}{i}{size=-3}She didn't answer, either ignoring your words or being too busy with your cock."
    e "Don't you dare take it out of your mouth now"
    e "Ahh...."
    if tommymomhas == 0:
        hide mtomskside5ep
        show mtomcminmoutwithout with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalwithout with dissolve
        e "Thanks"
        jump aftercmimep5mtom

    elif tommymomhas == 3:
        hide mtomskside5ep
        show mtomcminbf with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalbf with dissolve
        e "Thanks"
        jump aftercmimep5mtom

    elif tommymomhas == 8:
        hide mtomskside5ep
        show mtomcminglass with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalwithg with dissolve
        e "Thanks"
        jump aftercmimep5mtom

label mtomblindfoldsolo:
     show mtomep5cam1 with dissolve
     $ renpy.pause(3, hard=True)
     scene 50359 with vpunch
     e "I'm bored"
     scene 50359a with vpunch
     e "Time for the main course."
     scene 50359withbf0a with dissolve
     z "WHAT THE HELL?!"
     scene 50359withbf0 with dissolve
     e "You're in no danger."
     scene 50359withbf0a with dissolve
     z "I didn't agree to any of that."
     scene 50359withbftakeoff with dissolve
     $ timeout_label = "mtomtakeoffbf"
     $ timeout = 2
     menu:
        "Don't take off the blindfold":
            scene 50359withbftakeoff2 with dissolve
            e "I like it..{p}If you want me to finish quickly then leave it on."
     scene 50359withbf0a with dissolve
     e "I'll fuck you and leave."
     scene 50359withbf0c with dissolve
     z "LET ME GO!"
     scene 50359withbf0b with dissolve
     e "Remember you're doing this for Tommy."
     scene 50359withbf0 with dissolve
     e "All the boys in the neighborhood will protect him and he will be safe throughout his studies."
     scene 50359withbf0d with dissolve
     e "And I won't sell him any more shit."
     scene 50359withbf0e with dissolve
     z "You are the same age as my son.{p}This is sick."
     e "I promise your Tommy will be happy."
     scene 50359withbf0g with dissolve
     e "But I also have to be satisfied."
     scene 50359withbf0z with vpunch
     e "Damn Girl...{p}You don't even wear panties."
     z "..."
     z "Please...{p}...use a condom."
     scene 50359withbf3 with vpunch
     e "Lie down and stick your ass out."
     scene laymtom0 with dissolve
     z "Uhm..."
     scene 50331 with dissolve
     z "If you lie to me..."
     e "I won't do that..."
     scene v2final000 with vpunch
     "{color=#A8E4A0}{i}{size=-3}You grabbed her ass and pulled her down onto your cock.{/i}"
     show mtomsolo
     $ renpy.pause(3, hard=True)
     "{color=#A8E4A0}{i}{size=-3}Her wet pussy invites you deeper with each thrust.{/i}"
     pause
     "{color=#A8E4A0}{i}{size=-3}She doesn't even try to resist while you fuck her and treat her like a common whore.{/i}"
     e "Damn, you’ve got the perfect ass for this... So good to fuck from behind."
     "{color=#A8E4A0}{i}{size=-3}With each thrust, the sound of skin meeting skin grows louder, and her moans become more intense.{/i}"
     pause
     "{color=#A8E4A0}{i}{size=-3}You've managed to completely dominate this bitch, but you feel like you won't last much longer.{/i}"

     menu (screen="rightchoice"):
        "I want to cum on your face.":
            z "....{p}no...."
            jump mtomep5cmonfacewithbf
        "I want to cum in your mouth":
            z "....{p}no...."
            jump mtomep5cminmouthwithbf

label mtomep5cmonfacewithbf:
    hide mtomsolo
    scene mtomgetup with vpunch
    e "Come to me"
    scene bgout0 with dissolve
    e "You won't need this anymore"
    scene bgout1 with dissolve
    pause
    scene bgout2 with dissolve
    pause
    jump mtomep5cmonface


label mtomep5cminmouthwithbf:
    scene laymtom0 with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    scene laymtom1 with dissolve
    pause 0.25
    scene laymtom2 with dissolve
    pause 0.25
    scene laymtom3 with dissolve
    pause 0.25
    scene laymtom4 with dissolve
    pause 0.25
    scene laymtom5 with dissolve
    pause 0.25
    scene laymtom6 with dissolve
    pause 0.25
    scene laymtom7 with dissolve
    pause 0.25
    scene laymtom8 with dissolve
    pause 0.25
    scene laymtom9 with dissolve
    pause 0.25
    "{color=#A8E4A0}{i}{size=-3}You laid down next to her.{/i}"
    scene 50331 with dissolve
    e "Hey{p}Look at me."
    z "{color=#ffa500}{i}*She let out a soft moan.*{/i}{/color}"
    scene 50333_blindf with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    e "My cock is covered in your juices, lick it."
    scene 50332_blindf with dissolve
    z "{color=#ffa500}{i}*She is breathing heavily*{/i}{/color}"
    z "I don't want to..."
    scene 50333 with dissolve
    e "You know what?"
    scene mtomcminmt with dissolve
    e "I'm not asking..."
    scene mtomcminmt2 with dissolve
    e "I deserve a reward for fucking you so hard."
    scene mtomcminmt3bf with dissolve
    $ timeout_label = "mtommyep5afterkisswithbf"
    $ timeout = 0.5
    menu:

        "{color=#FFD1DF}{i}Kiss her":
            scene mtomcminmt4bf with dissolve
            "{color=#A8E4A0}{i}{size=-3}You took the opportunity and kissed her on the lips, but she was so tired that she didn't kiss you back."
            if not easymode:
                $ achValid5 += 1
                $ achievement.grant("Achiev19")
                $ achievement.sync()
                if not persistent.achievement19:
                                             show Achiev19 at achievment with easeintop:
                                                        zoom 0.5
                                                        rotate_animation

                                             "You have received the achievement!{p}{b}\"Instant reaction!\".{/b}"
                                             "Number of achievements earned in this chapter [achValid5]/8"
                                             hide Achiev19
                                             $ persistent.achievement19 = True
            scene mtomcminmt3bf with dissolve
            e "Now suck me"
            scene mtomcminmt2 with dissolve
            pause 0.25

label mtommyep5afterkisswithbf:
    $ tommymomhas = 3
    scene mtomcminmt5 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She obediently leaned against your stomach and took your cock into her mouth while you began to pleasure her with your finger."
    show mtomskside5ep with dissolve
    "{color=#A8E4A0}{i}{size=-3}The amount of her pussy juices dripping onto your hand could mean that she either hasn't done it in a while or she's really turned on by the whole situation...{/i}"
    e "I wonder what your husband would say if he saw what you're doing with my dick right now."
    e "Sucking off your son's friend."
    "{color=#A8E4A0}{i}{size=-3}She didn't answer, either ignoring your words or being too busy with your cock."
    e "Don't you dare take it out of your mouth now"
    e "Ahh...."
    if tommymomhas == 0:
        hide mtomskside5ep
        show mtomcminmoutwithout with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalwithout with dissolve
        e "Thanks"
        jump aftercmimep5mtom

    elif tommymomhas == 3:
        hide mtomskside5ep
        show mtomcminbf with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalbf with dissolve
        e "Thanks"
        jump aftercmimep5mtom

    elif tommymomhas == 8:
        hide mtomskside5ep
        show mtomcminglass with dissolve
        $ renpy.pause(9, hard=True)
        e "Oh...."
        scene mtomfinalwithg with dissolve
        e "Thanks"
        jump aftercmimep5mtom

label mtomtomep5:
    scene 503530 with dissolve
    e "Hmm?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Interesting..."

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Signal him to come closer*{/i}{/color}\n{size=-8}(Req. Eyes covered with a blindfold){/size}" if mtommyblindfoldon == True:
                jump mtomshare
            "{color=#FFD1DF}{i}*Show him the middle finger*{/i}{/color}\n{color=#3d85c6} Tommy -2 and you won't get any money from him":
                scene 503532a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
                $ tommyfriend -= 2
                $ tommymiddlefing = True
                "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
                jump mtomblindfoldsolo
            "{color=#FFD1DF}{i}*Don't do anything*{/i}{/color}":
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You can watch as your mother serves me."
                $ tommyep5peeping = True
                jump mtomblindfoldsolo

    else:
        menu:
            "{color=#FFD1DF}{i}*Signal him to come closer*{/i}{/color}\n{size=-8}(Req. Eyes covered with a blindfold){/size}" if mtommyblindfoldon == True:
                jump mtomshare
            "{color=#FFD1DF}{i}*Show him the middle finger*{/i}{/color}":
                scene 503532a with dissolve
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
                $ tommyfriend -= 2
                $ tommymiddlefing = True
                "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
                jump mtomblindfoldsolo
            "{color=#FFD1DF}{i}*Don't do anything*{/i}{/color}":
                e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You can watch as your mother serves me."
                $ tommyep5peeping = True
                jump mtomblindfoldsolo

label mtomfuck:
    scene 503532a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
    jump mtomshare

label mtomshare:
    $ tommyjoinsep5mtom = True
    scene 503531 with dissolve
    scene 503532 with dissolve
    pause
    scene 50352 with dissolve
    e "Give me a moment, girl."
    scene 503532walk with dissolve
    e "I have to take off my shirt because I'm sweating."
    scene 503532walk2 with dissolve
    pause
    scene 50354 with dissolve
    pause 2
    scene 503541 with dissolve
    pause 0.25
    scene 503542 with dissolve
    pause 0.25
    scene 503543 with dissolve
    pause
    scene 50355 with dissolve
    z "What's happening?!"
    scene 50355a with vpunch
    pause
    scene 50355b with dissolve
    scene 50356 with dissolve
    show mtomtomstart with dissolve
    $ renpy.pause(2, hard=True)
    scene 5035743 with dissolve
    z "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Strange..."
    z "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Has he suddenly become smaller?!"
label mtomtom2view:
    hide mtomtom2
    show mtomtom with dissolve
    $ renpy.pause(2, hard=True)

    menu (screen="rightchoice"):
        "Change view":
            jump mtomtom1view
        "Continue":
            jump mtomtomnextep5step

label mtomtom1view:
    hide mtomtom
    show mtomtom2 with dissolve
    $ renpy.pause(2, hard=True)

    menu (screen="rightchoice"):
        "Change view":
            jump mtomtom2view
        "Continue":
            jump mtomtomnextep5step

label mtomtomnextep5step:
    scene 50360 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Another video for my collection."
    scene 50360a with dissolve
    pause
    scene 50360b with dissolve
    z "MMMMMMMMMMMMM"
    scene 50360c with dissolve
    z "WHAT THE HELL?!"
    scene 50360d with dissolve
    e "Don't worry. I came with a friend."
    scene 50360e with dissolve
    z "I didn't agree to any of that."
    z "I DON'T WANT TO!"
    scene 50360d with dissolve
    e "You're in no danger."
    e "Just do your job and we'll be gone soon."
    scene 50360e with dissolve
    z "Let me go."
    scene 50360d with dissolve
    e "Remember you're doing this for Tommy."
    e "All the boys in the neighborhood will protect him and he will be safe throughout his studies."
    scene 50360e with dissolve
    e "But these boys want to get something out of it too."
    z "Uhm..."
    z "You should have told me"
    scene 50360d with dissolve
    e "That you'll have to suck more than one dick?"
    e "I think you knew that well."
    e "But hey..."
    e "I promise your Tommy will be happy."
    scene 50360f with dissolve
    z "Aww.."
    e "But I also have to be satisfied."
    scene 50360e with dissolve
    z "Uhm..."
    z "If you lie to me..."
    scene 50360f with dissolve
    e "I won't do that..."
    scene 50360g with dissolve
    e "Because you will be very nice to us."
    e "And stick out your sexy ass for me now."
    scene 50360h with dissolve
    e "Damn Girl...{p}You don't even wear panties."
    e "It's time for you to see what reward caring mommies receive."
label mtomep5sx:
    show mtomep5sx1 with dissolve
    $ renpy.pause(2, hard=True)
    e "Fucking great."
    e "Ohhh."

label mtomep5sx2:
    hide mtomep5sx1
    show mtomep5sx2 with dissolve
    $ renpy.pause(2, hard=True)

    menu (screen="rightchoice"):
        "Change view":
            jump mtomep5sx1
        "Finish":
            jump mtomtomendpart

label mtomep5sx1:
    hide mtomep5sx2
    show mtomep5sx1 with dissolve
    $ renpy.pause(2, hard=True)

    menu (screen="rightchoice"):
        "Change view":
            jump mtomep5sx2
        "Finish":
            jump mtomtomendpart

label mtomtomendpart:
    hide mtomep5sx2
    hide mtomep5sx1
    scene 50362 with dissolve
    t "Ehm..."
    scene 50362a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What the hell?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He wants to take my place?"
    show mtomep5sx1 with dissolve
    e "Nah Bro.{p}That bitch is mine."
    $ renpy.pause(5, hard=True)
    hide mtomep5sx1
    show mtomtomcm
    t "Oooh...."
    e "Yeah...{p}Fill her mouth."
    $ renpy.pause(6, hard=True)
    e "Swallow that, you slut"
    play sound "music/cough.mp3"
    z "{color=#ffa500}{i}*Cough*{/i}"
    z "{color=#ffa500}{i}*Spit*{/i}"
    e "Why did you spit it out?!"

    menu:
        "{color=#FFD1DF}{i}*Cum on her face*{/i}{/color}":
            jump mtommccum1
        "{color=#FFD1DF}{i}*Cum in her pussy*{/i}{/color}":
            jump mtommccum2

label mtommccum1:
    scene 50364cof1 with dissolve
    e "Come here"
    z "UUHH"
    scene 50364cof2 with dissolve
    pause
    scene 50364cof3 with dissolve
    "{color=#A8E4A0}{i}{size=-3}You showed Tommy it was time for him to get out of here.{/size}{/i}{/color}"
    scene v2cofwithbf00 with dissolve
    pause
    scene bgout0 with dissolve
    e "You won't need this anymore"
    scene bgout1 with dissolve
    pause
    scene bgout2 with dissolve
    pause
    jump mtomep5cmonface

label mtommccum2:
    scene 50364 with dissolve
    e "Come here"
    z "UUHH"
    show mtommccum
    e "OH FUCK."
    scene 50365 with dissolve
    e "..."
    show mtomep5caress with dissolve
    e "It was super nice..."
    z "Just leave..."
    e "You didn't even object when I cummed inside you."
    z "..."
    e "Do you want me to fill you with cum more often?"
    z "Get out..."
    e "Ok ok... my little whore."
    $ renpy.end_replay()
    scene black with fade
    if not _in_replay:
        $ persistent.mtomsharing = True
    show text "You left the apartment, leaving Tommy's mom exhausted on the bed." at title with dissolve
    $ renpy.pause(2, hard=True)
    jump aftersxmtomep5

label aftersxmtomep5:
    scene 51000 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} That was good..."
    scene 51000a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What should I do now?"
    if tommyjoinsep5mtom == True or tommyep5peeping == True:
        if tommyjoinsep5mtom == True:
            $ tommyfriend += 2
        elif tommyep5peeping == True:
            $ tommyfriend += 1
        scene 51001 with dissolve
        t "[player_name]!!!!"
        scene 51001a with dissolve
        t "You're my hero, dude."
        scene 51001b with vpunch
        t "Let me hug you"
        e "Take your hands off."
        scene 51001c with dissolve
        t "Oh.. sorry. I've never been more excited in my life than I am right now."
        if tommyjoinsep5mtom == True:
            scene 51001d with dissolve
            t "You're my best friend, [player_name]!{p}No one has ever done anything like that for me in my life."
        elif tommyep5peeping == True:
             scene 51001d with dissolve
             t "I'm really glad you let me watch."
        scene 510013 with dissolve
        e "Uhm... Sure."
        scene 510014 with dissolve
        e "You can always count on me in such matters..."
        scene 510015 with dissolve
        t "I know, man.{p}We absolutely have to do this again, and now you have to let me have some fun too!"
        scene 510014 with dissolve
        e "Yeah... sure."
        scene 510015 with dissolve
        t "I still have some business for you..."
        if tommypaylater == True:
                t "First, your money.{p}Thanks for waiting."
                $ money += 150
                show text "{color=#00ff00}{size=+15}+1 5 0 ${/color}" with dissolve
                with Pause(2)
                show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
                hide text with dissolve
        else:
                t "First, your money.{p}Thanks for waiting."
                $ money += 35
                show text "{color=#00ff00}{size=+15}+3 5 ${/color}" with dissolve
                with Pause(2)
                show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
                hide text with dissolve
        t "And tell me... do you have anything to smoke or something stronger?"


        show screen hint("I promised Tommy's mom I wouldn't sell him anything else... But money always comes in handy.")
        if easymode:
            menu:
                "Nothing... sorry.":
                    hide screen hint
                    $ tommyfriend -= 2
                    t "Man... really?!"
                    t "That's definitely not true. I need to get something, man."
                    e "I don't have.. maybe tomorrow."

                "{color=#FFD1DF}{i}*Sell him soft drugs*{/i}{/color}{color=#00ff00} +20${/color} {size=-8}(Req. Drugs){/size}\n{color=#3d85c6} Different Ending" if shoppackage == True:
                    hide screen hint
                    $ selltommydrugs += 1
                    $ tommyfriend += 1
                    e "Mhm..."
                    scene 510016 with dissolve
                    pause 1
                    scene 510017 with dissolve
                    pause 1
                    scene 510018 with dissolve
                    pause 1
                    $ money += 20
                    show text "{color=#00ff00}{size=+15}+2 0 ${/color}" with dissolve
                    with Pause(2)
                    show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
                    hide text with dissolve
                    scene 510019 with dissolve
                    e "Not a word to anyone."
                    t "Sure man.{p}Thanks.{p}See you later."
                    jump sandboxep5menu

                "{color=#FFD1DF}{i}*Sell him hard drugs*{/i}{/color}{color=#00ff00} +50${/color} {size=-8}(Req. Drugs){/size}\n{color=#3d85c6} Different Ending" if shoppackage == True:
                    hide screen hint
                    $ tommyfriend += 2
                    $ selltommydrugs += 2
                    e "Mhm..."
                    scene 510016 with dissolve
                    pause 1
                    scene 510017 with dissolve
                    pause 1
                    scene 510018 with dissolve
                    pause 1
                    $ money += 50
                    show text "{color=#00ff00}{size=+15}+5 0 ${/color}" with dissolve
                    with Pause(2)
                    show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
                    hide text with dissolve
                    scene 510019 with dissolve
                    e "Not a word to anyone."
                    t "Sure man.{p}Thanks.{p}See you later."
                    jump sandboxep5menu
        else:
            menu:
                "Nothing... sorry.":
                    hide screen hint
                    $ tommyfriend -= 2
                    t "Man... really?!"
                    t "That's definitely not true. I need to get something, man."
                    e "I don't have.. maybe tomorrow."

                "{color=#FFD1DF}{i}*Sell him soft drugs*{/i}{/color}{color=#00ff00} +20${/color} {size=-8}(Req. Drugs){/size}" if shoppackage == True:
                    hide screen hint
                    $ selltommydrugs += 1
                    $ tommyfriend += 1
                    e "Mhm..."
                    scene 510016 with dissolve
                    pause 1
                    scene 510017 with dissolve
                    pause 1
                    scene 510018 with dissolve
                    pause 1
                    $ money += 20
                    show text "{color=#00ff00}{size=+15}+2 0 ${/color}" with dissolve
                    with Pause(2)
                    show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
                    hide text with dissolve
                    scene 510019 with dissolve
                    e "Not a word to anyone."
                    t "Sure man.{p}Thanks.{p}See you later."
                    jump sandboxep5menu

                "{color=#FFD1DF}{i}*Sell him hard drugs*{/i}{/color}{color=#00ff00} +50${/color} {size=-8}(Req. Drugs){/size}" if shoppackage == True:
                    hide screen hint
                    $ tommyfriend += 2
                    $ selltommydrugs += 2
                    e "Mhm..."
                    scene 510016 with dissolve
                    pause 1
                    scene 510017 with dissolve
                    pause 1
                    scene 510018 with dissolve
                    pause 1
                    $ money += 50
                    show text "{color=#00ff00}{size=+15}+5 0 ${/color}" with dissolve
                    with Pause(2)
                    show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
                    hide text with dissolve
                    scene 510019 with dissolve
                    e "Not a word to anyone."
                    t "Sure man.{p}Thanks.{p}See you later."
                    jump sandboxep5menu
    else:
        jump sandboxep5menu


label sandboxep5menu:
        if persistent.mtomcinm == True and persistent.mtomsharing == True and persistent.mtomep5cmonface == True and not easymode:

            $ achValid5 += 1
            $ achievement.grant("Achiev20")
            $ achievement.sync()
            if not persistent.achievement20:
                                         show Achiev20 at achievment with easeintop:
                                                    zoom 0.5
                                                    rotate_animation

                                         "You have received the achievement!{p}{b}\"You must be a fan of Tommy's mom... You checked out all the scenes with her.\"{/b}"
                                         "Number of achievements earned in this chapter [achValid5]/8"
                                         hide Achiev20
                                         $ persistent.achievement20 = True
        scene 51000a with Dissolve(2.0)
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What should I do now?"

        if mtommyep5enterdoor == True:
            menu:
                "{color=#FFD1DF}{i}*Return to the store*":
                    jump shopep5storelist

                "{color=#FFD1DF}{i}*Take a bus to [nicosister_role]*{/i}{/color} {size=-6}{color=#e0d71d}10${/color}{/size}" if money >= 10 and auntfinish == False:
                    $ money -= 10
                    play sound "music/buyshop.mp3"
                    jump triptoaunt

                "{color=#FFD1DF}{i}*Call Gary and sell him drugs*{/i}{/color} {size=-8}(Req. Phone, Drugs){/size}" if shoppackage and garrydidntbuy:
                            jump garrycallworkout

                "{color=#FFD1DF}{i}*Return home*":
                    jump triptohome

        else:
            menu:
                "{color=#FFD1DF}{i}*Return to the store*":
                    jump shopep5storelist

                "{color=#FFD1DF}{i}*Visit Tommy*" if mtommyep5enterdoor == False:
                    jump triptotommy

                "{color=#FFD1DF}{i}*Take a bus to [nicosister_role]*{/i}{/color} {size=-6}{color=#e0d71d}10${/color}{/size}" if money >= 10 and auntfinish == False:
                    $ money -= 10
                    play sound "music/buyshop.mp3"
                    jump triptoaunt

                "{color=#FFD1DF}{i}*Call Gary and sell him drugs*{/i}{/color} {size=-8}(Req. Phone, Drugs){/size}" if shoppackage and garrydidntbuy:
                            jump garrycallworkout

                "{color=#FFD1DF}{i}*Return home*":
                    jump triptohome


label triptoaunt:
     scene black with fade
     stop music fadeout 1.0
     play music "music/Mat.wav"
     show text "{size=+5}20 minutes later{/size}" with dissolve
     $ renpy.pause(2, hard=True)
     hide text with dissolve
     scene ep4door with Dissolve(2.0)
     e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Alright, here I am..."
     e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hope it's not a trap and she secretly wants to kill me, or something..."
     play sound "music/dooropen.mp3"
     scene 50100 with Dissolve(2.0)
     a "H-Hello? Oh! It's you, [player_name]... Uh... How are you doing?"
     e "Well, curious. I wanna know what you wanted to say."
     scene 50101 with dissolve
     a "Oh... You mean, about last time..."
     scene 50101a with dissolve
     e "Yeah, that's literally why you called me... "
     scene 50101 with dissolve
     a "Alright... Look..."
     scene 50102 with dissolve
     e "Go on..."
     scene 50102a with dissolve
     pause
     scene 50102b with dissolve
     pause
     scene talkaunt0 with dissolve
     a "I'm not mad at you, alright?"
     scene talkaunt1 with dissolve
     a "I get it, you're young, horny, stupid..."
     scene talkaunt2 with dissolve
     a "And we all do stupid things. I've been your age too."
     scene talkaunt3 with dissolve
     e "Does that mean you tried to pick up old men?"
     scene 50105 with dissolve
     a "Excuse me?{p}Does that mean you're calling me old?"
     scene 50105a with dissolve
     e "...Yeah. Old but hot"
     scene 50106 with dissolve
     a "Mmm... You silly boy."
     scene 50106a with dissolve
     a "Okay, I forgive you, alright?"
     scene 50106 with dissolve
     e "You forgive me? About what, exactly?"
     scene 50107 with dissolve
     a "For being weird around me, and considering me a fucking PROSTITUTE."
     scene 50107a with dissolve
     a "I'm your [nicosister_role]. Don't you ever forget that..."
     scene 50106 with dissolve
     e "You don't have to forgive me, because I know you've never been actually mad about it.{p}I said the truth. You're stupid hot, alright?"
     scene 50107 with dissolve
     a "I know you said the truth, but... you know, it's not... normal!"
     scene 50106 with dissolve
     e "It's not normal for [nicosister_role]s to be your level of hot either."
     scene 50106a with dissolve
     a "Tsk... Alright, you win. I'm letting that slip... Just because I like the ego boost..."
     scene 50107 with dissolve
     a "...You're bold. I like that..."
     scene 50108 with dissolve
     e "So you like me? Now that's weird."
     scene talkaunt2 with dissolve
     a "Whatever... At least that's done and out now. Phew..."
     scene 50109 with dissolve
     a "*Hiccup*{p}Oops!"
     scene 50109a with dissolve
     a "Sorry..."
     scene 50106 with dissolve
     e "...Have you been drinking today?"
     scene 50106a with dissolve
     a "Perhaps I had a little glass of wine while I was preparing for the shower... Fancy."
     scene 50106 with dissolve
     e "So that's why you're so forgiving today..."
     scene 50107 with dissolve
     a "Hey, I just love a good wine, you know me... I like treating myself."
     if shopalcoholep5weak == True or shopalcoholep5strong == True or shopblindfold == True:
        e "Speaking of which!... I almost forgot! I brought you this..."
        label giveauntiegifts:
            scene 50106 with dissolve

            if easymode:
                menu:
                    "{color=#FFD1DF}{i}Give her White Wine{/i}{/color}{size=-8} (Req. White Wine){/size}\n{color=#3d85c6} Only this, but you can give a blindfold for a short scene" if shopalcoholep5weak == True:
                        $ auntgetwhitewine = True
                        $ shopalcoholep5weak = False
                        jump giveauntwhitewine
                    "{color=#FFD1DF}{i}Give her Red Wine{/i}{/color}{size=-8} (Req. Red Wine){/size} " if shopalcoholep5strong == True:
                        $ auntgetredwine = True
                        $ shopalcoholep5strong = False
                        jump giveauntredwine
                    "{color=#FFD1DF}{i}Give her Blindfold{/i}{/color}{size=-8} (Req. Blindfold){/size} " if shopblindfold == True:
                        $ auntgetblindfold = True
                        $ shopblindfold = False
                        jump giveauntblindfold
                    "{color=#FFD1DF}{i}Continue":
                        $ auntfinish = True
                        jump eveburrito

            else:
                menu:
                    "{color=#FFD1DF}{i}Give her White Wine{/i}{/color}{size=-8} (Req. White Wine){/size} " if shopalcoholep5weak == True:
                        $ auntgetwhitewine = True
                        $ shopalcoholep5weak = False
                        jump giveauntwhitewine
                    "{color=#FFD1DF}{i}Give her Red Wine{/i}{/color}{size=-8} (Req. Red Wine){/size} " if shopalcoholep5strong == True:
                        $ auntgetredwine = True
                        $ shopalcoholep5strong = False
                        jump giveauntredwine
                    "{color=#FFD1DF}{i}Give her Blindfold{/i}{/color}{size=-8} (Req. Blindfold){/size} " if shopblindfold == True:
                        $ auntgetblindfold = True
                        $ shopblindfold = False
                        jump giveauntblindfold
                    "{color=#FFD1DF}{i}Continue":
                        $ auntfinish = True
                        jump eveburrito

label giveauntblindfold:
    scene 50110b with dissolve
    a "Oh, and this!? Oh no!"
    scene 50111b with dissolve
    a "I hope you’re not trying to kidnap me!"
    scene 50112b with dissolve
    e "W-What!? No!{p}Hahaha... {p}Well, unless you want me to.."
    scene 50113b with dissolve
    a "Give me that..."
    scene 50114b with dissolve
    a "W-What do you want from me!?"
    scene 50114ba with dissolve
    a "I can’t see a thing! Stay back!"
    scene 50115b with dissolve
    e "Oh! I’m going to do everything to you, and when I’m done... I’ll set you free."
    scene 50116b with dissolve
    a "Oh... You’re so bad."
    jump giveauntiegifts

label giveauntwhitewine:
    scene 50110w with dissolve
    e "...White wine!"
    scene 50111w with dissolve
    a "Oh, thank you!"
    scene 50112w with dissolve
    a "You really know me well, you little devil!"
    scene 50113w with dissolve
    e "Well, I like spoiling you. And I know you love being spoiled. I think this is the brand you like."
    scene 50112w with dissolve
    a "Oh god, you're such a charmer, stop it! Or I might end up falling for you."
    jump giveauntiegifts

label giveauntredwine:
    scene 50110r with dissolve
    e "...Red wine!"
    scene 50111r with dissolve
    a "Red wine... How... thoughtful of you! Thanks..."
    scene 50113r with dissolve
    e "Hey, don’t mention it..."
    scene 50112r with dissolve
    a "I hope you didn’t spend too much."
    scene 50113r with dissolve
    e "Pfft... That’s no problem."
    jump giveauntiegifts

label eveburrito:
    scene 50107 with dissolve
    a "Well, I should get dressed, as you can see, I’m wrapped in towels like a MILF burrito... You know what I mean?"
    scene 50106 with dissolve
    e "Heh... Just the kind of burrito I like..."
    scene 50107 with dissolve
    e "Tsk... You’re such a dummy... Anyway, let me get dressed, I won’t be long."
    show screen hint("I guess I should stop her from getting dressed...right?") with dissolve
    menu:

        "{color=#FFD1DF}{i}Stop her":
            hide screen hint
            jump nodresseve

label eveclotheson:

label nodresseve:
    scene 50106 with dissolve
    e "Nah, you don't have to.{p}I actually wanted to ask you something quick and then head out."
    scene 50106a with dissolve
    a "Oh, well..."
    if auntgetwhitewine == True:
        scene 50107 with dissolve
        a "Maybe we could open that white wine you brought, don’t you think?"
        scene 50106 with dissolve
        e "Thanks, but...{p}I don’t drink wine."
        scene 50120 with dissolve
        a "Damn, you’re such a buzzkill... Well, I hope you don’t mind if I have a little."
        scene 50121 with dissolve
        e "Me? A buzzkill? Let me prove you I'm not..."
        scene 50122 with dissolve
        e "I'll take my shirt off just so you don't feel out of place."
        scene 50122a with dissolve
        a "Great... Now I have a half-naked man in my house and a wine bottle. This is dangerous."
        scene 50123 with dissolve
        e "Hey, I'm not that dangerous!"
        e "Let me pour you a glass while I'm at it."
        scene 50122a with dissolve
        a "Come..."
        scene 50124 with dissolve
        "{color=#A8E4A0}{i}{size=-3} She opened the bottle and came to you with a glass."
        scene black with fade
        scene 50125 with dissolve
        a "You’ve got good pouring technique... Don’t kid me, you’re a natural drinker."
        scene 50125a with dissolve
        e "Nah... I just like doing everything one hundred percent... It’s part of who I am."
        scene 50125b with dissolve
        a "Watch your words, young man, you tend to leave things open to interpretation..."
        scene 50125drink1 with dissolve
        pause
        scene 50125drink2talk with dissolve
        e "Tsk... That’s what she said!"
        scene 50127 with dissolve
        a "Hahaha... Oh, you’re such a clever guy..."
        scene 50125 with dissolve
        e "Yeah... I’m afraid if I had some of that wine you’re drinking, I’d get way too drunk, way too fast."
        scene 50125b with dissolve
        a "Well... I don’t know how much you paid for it, but... Damn, it’s strong.."
        scene 50125a with dissolve
        e "Oh, and before I forget... I've got something to ask you."
        scene 50125b with dissolve
        a "Hope it's not asking me out."
        scene 50125drink2 with dissolve
        e "Not yet..."
        scene 50127 with dissolve
        a "...What?"
        scene 50125drink2talk with dissolve
        e "Nothing...heh..."
        scene 50126 with dissolve
        e "Here, look at this photo."
        scene 50126a with dissolve
        a "[player_name]! This is your [woman_role] almost naked! Where did you get this from!?"
        scene 50126b with dissolve
        e "That doesn't matter! What does matter is that I have good reasons to believe Lopez and her spent the night at a hotel together after prom..."
        scene 50127 with dissolve
        a "...Hm... Well, that dress is indeed the one she used for prom, but... She never really used it ever again... What a shame. She looked fantastic on it."
        scene 50125a with dissolve
        e "That's... weird. Do you think they were together that night?"
        scene 50125b with dissolve
        a "I’ll be honest with you... I don’t remember much from that night... But..."
        scene 50125drink1 with dissolve
        pause
        scene 50125drink2talk with dissolve
        e "But...?"
        scene 50127 with dissolve
        a "...But what I do know for sure is that he and your [woman_role] argued after being together, or well, that's what she told me"
        scene 50125a with dissolve
        e "They argued? I wonder about what."
        scene 50125b with dissolve
        a "No clue. But it must've been something tough, since after that very night they did cut off all contact."
        a "Well... it was their last day of school so it's a 'fuck all' thing."
        scene 50125a with dissolve
        e "Come on, that’s no excuse, lots of people meet again after high school... That’s normal."
        scene 50125b with dissolve
        a "Yeah, but not if you’ve had a big fight... It’s like the argument drove them apart for good."
        scene 50125drink2 with dissolve
        e "Hmm... I see... So, you’re saying they never saw each other again after a fight?"
        scene 50127 with dissolve
        a "Yeah... I think so... Resentment builds up quickly. It can really tear people apart."
        scene 50125a with dissolve
        e "Yeah... I guess..."
        jump auntwinedrink

    else:
            scene 50106a with dissolve
            a "Hope it's not asking me out."
            scene 50108 with dissolve
            e "Not yet..."
            scene 50107 with dissolve
            a "...What?"
            scene 50106 with dissolve
            e "Nothing...heh..."
            scene 50140 with dissolve
            e "Here, look at this photo."
            scene 50140a with dissolve
            a "[player_name]! This is your [woman_role] almost naked! Where did you get this from!?"
            scene 50140b with dissolve
            e "That doesn't matter! What does matter is that I have good reasons to believe Lopez and her spent the night at a hotel together after prom..."
            scene 50140 with dissolve
            a "...Hm..."
            scene 50140a with dissolve
            a "Well, that dress is indeed the one she used for prom, but... She never really used it ever again... What a shame. She looked fantastic on it."
            scene 50140b with dissolve
            e "That's... weird. Do you think they were together that night?"
            scene 50141 with dissolve
            a "I’ll be honest with you... I don’t remember much from that night... But..."
            scene 50141a with dissolve
            e "But...?"
            scene 50141 with dissolve
            a "...But what I do know for sure is that he and your [woman_role] argued after being together, or well, that's what she told me"
            scene 50141a with dissolve
            e "They argued? I wonder about what."
            scene 50142 with dissolve
            a "No clue. But it must've been something tough, since after that very night they did cut off all contact."
            scene 50141 with dissolve
            a "Well... it was their last day of school so it's a 'fuck all' thing."
            scene 50141a with dissolve
            e "Come on, that’s no excuse, lots of people meet again after high school... That’s normal."
            scene 50142 with dissolve
            a "Yeah, but not if you’ve had a big fight... It’s like the argument drove them apart for good."
            scene 50142a with dissolve
            e "Hmm... I see... So, you’re saying they never saw each other again after a fight?"
            scene 50141 with dissolve
            a "Yeah... I think so... Resentment builds up quickly. It can really tear people apart."
            scene 50142a with dissolve
            e "Yeah... I guess..."
            e "Well, that’s all I needed to know... Thank, I guess. You weren't of much help anyways."
            scene 50143 with dissolve
            a "Hey, it's not my fault! I can't know it all, you jerk!"
            scene 50143a with dissolve
            e "You're her sister! She's supposed to trust you every secret. That's how women work!"
            scene 50143 with dissolve
            a "You're a man, and you don't know ANYTHING about women! Ugh. Fuck off."
            $ auntnothing = True
            jump auntdoorleaves


label auntwinedrink:
    scene 50128 with dissolve
    a "Whew... Are you sure this stuff isn’t made with vodka or something? It kicks like a kangaroo."
    scene 50128a with dissolve
    a "*Yawn*"
    scene 50128b with dissolve
    e "Hey, that tattoo? I’ve never seen it before."
    scene 50129 with dissolve
    a "Hohoho... this one?"
    scene 50129a with dissolve
    e "Damn, that’s a badass tattoo...{p}Whorey... I like it."
    scene 50129b with dissolve
    a "Whorey!? Y-You think so...?"
    scene 50129c with dissolve
    e "Yeah... it suits you. You're a big whore anyway."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She's totally drunk."
    scene 50131 with dissolve
    a "You’re... bold... but I don’t mind.{p}*Hiccup*{p}Not one bit..."
    "{color=#A8E4A0}{i}{size=-3} You kneel in front of her, spreading her legs slightly, taking off her towel with your hand."
    "{color=#A8E4A0}{i}{size=-3} Eve shivers but doesn’t resist, biting her lip as your head dips between her thighs."
    scene 50130a with dissolve
    a "W-What are you doing? *Hiccup*"
    scene cmlickframe with dissolve
    e "Just relax... I’m gonna make you feel real good..."
    show anep5lick1 with dissolve
    "{color=#A8E4A0}{i}{size=-3} The first touch of your tongue makes her gasp, her hips shifting slightly as you begin to work."
    a "Ngh... Watch that tongue..."
    "{color=#A8E4A0}{i}{size=-3} The taste of her grows stronger as you flick and lap at her clit, her moans soft at first but growing louder as you suck and tease her sensitive spots."
    a "Oh...{p}f-fuck...{p}you're so... G-Goood."
    "{color=#A8E4A0}{i}{size=-3} You take one of your fingers to her mouth, they slide up to her mouth, pressing one against her lips."
    show anep5lick2
    $ renpy.pause(4, hard=True)
    e "Suck on it, you cope-drinking slut... pretend it's my big fat cock."
    scene frameanlck
    show anep5lick3
    "{color=#A8E4A0}{i}{size=-3} She doesn’t hesitate, taking your finger into her mouth, her lips closing around it as she begins to suck."
    e "Mmm... There's something addictive about your old-hag pussy. "
    "{color=#A8E4A0}{i}{size=-3} Muffled from your finger, she suck on it while blushing harder, ashamed of the words that came out of your mouth"
    e "What's the matter? Can't talk? Yeah, you can't. Keep sucking my finger, hag."
    "{color=#A8E4A0}{i}{size=-3} Her moans become muffled, her body shaking as your fingers works faster, harder, until she’s trembling."
    scene frameorg00 with dissolve
    a "Oh god... f-fuck... I’m gonna... cum... So fast!"
    show anep5lick4 with dissolve
    $ renpy.pause(1, hard=True)
    scene frameorg01
    "{color=#A8E4A0}{i}{size=-3} Her body shakes as she cums on your mouth, and you keep going, licking until her hips finally relax, and she lets out a satisfied sigh."
    "{color=#A8E4A0}{i}{size=-3} Slowly, you pull back, wiping your mouth with the back of your hand as you stand up, a satisfied grin on your face."
    scene 53105 with dissolve
    e "That was fun..."
    scene 53106 with dissolve
    e "But..."
    scene 53107 with dissolve
    e "I'm too worked up to stop now..."
    scene 53108 with dissolve
    e "I want the full course! I want your mouth on my cock NOW! And you better make me nut."
    "{color=#A8E4A0}{i}{size=-3} You started unzipping your pants' fly, as you position yourself in front of her ready to fuck her throat."
    scene antpantdown3 with dissolve
    pause
    scene antpantdown4 with dissolve
    a "W-Wait... I’m... I’m too tired..."
    scene antpantdown5 with dissolve
    a "I'm not an eager young girl anymore."
    scene antpantdown6 with dissolve
    e "What!? Come on, I just made you cum."
    scene antpantdown7 with dissolve
    e "Now it's my turn, you selfish bitch!"
    scene ansckfinal00 with dissolve
    a "...I know but... I could pass out. You wouldn't like that... would you? Plus... You'd make my mouth sore."
    scene ansckfinal10 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Deep inside, you knew you had no problem with that, but if you said you didn't, you'd probably end up spoiling her mood.-"
    scene ansckfinal15 with dissolve
    a "Maybe... not today... okay? N-Next time."
    $ renpy.end_replay()
    show screen hint("Being nice to her might pay off... but I'm so horny...")

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Force her to continue*\n{color=#3d85c6} Additional scene but end her path":
                hide screen hint
                jump forceeveep5
            "Sure\n{color=#3d85c6} Longer scene with Eve!":
                hide screen hint
                jump lethergoeveep5
    else:
        menu:
            "{color=#FFD1DF}{i}*Force her to continue*":
                hide screen hint
                jump forceeveep5
            "Sure":
                hide screen hint
                jump lethergoeveep5

label forceeveep5:
    scene ansckfinal21 with dissolve
    pause 0.25
    scene ansckfinal22 with dissolve
    pause 0.25
    scene ansckfinal24 with dissolve
    pause 0.25
    scene ansckfinal25 with dissolve
    pause 0.25
    scene ansckfinal26 with dissolve
    pause 0.25
    scene ansckfinal27 with dissolve
    pause 0.25
    scene ansckfinal28 with dissolve
    pause 0.25
    scene ansckfinal29 with dissolve
    pause 0.25
    scene ansckfinal30 with dissolve
    pause 0.25
    "{color=#A8E4A0}{i}{size=-3} You grab her hair, pulling her closer as she gasps in surprise. Before she can say another word, you push your cock against her lips."
    show anbjep5dom
    e "Shut your stupid mouth up, whore.{p}I know how much you want to get that cute throat fucked by a young cock."
    "{color=#A8E4A0}{i}{size=-3} She hesitates, but doesn’t fight you, her lips parting as you slide your pulsing cock into her mouth, sliding it in quickly-"
    "{color=#A8E4A0}{i}{size=-3} Her eyes close as she begins to suck, slowly at first, then picking up the pace as you thrust your meat deeper into her throat, bulging it.-"
    e "Yeah... just like that...{p}Gag on that meat.{p}Do the only thing you're good for, cheap wine drinking cock sucker."
    "{color=#A8E4A0}{i}{size=-3} Her hands grip your thighs as you fuck her mouth deep and good, your hips moving faster, harder.-"
    "{color=#A8E4A0}{i}{size=-3} You can feel yourself getting close, her tongue swirling around your shaft as you push her deeper onto you.-"
    e "I’m gonna cum all up in your mouth, hope you don't mind..."
    scene 53149 with vpunch
    $ maxmccumep7 += 1
    play sound "music/cman.mp3"
    "{color=#A8E4A0}{i}{size=-3} With one final thrust, you stick your balls to her chin and blast her mouth with a thick load of cum that bathes her mouth's wall.-"
    scene 53150 with vpunch
    scene 53150 with Dissolve(2.0)
    e "Mmm... You're gonna be tasting my cum for a week now, you cock hungry slut."
    e "So nice..." with vpunch
    scene 53151 with dissolve
    a "Uhm..."
    scene 53152 with dissolve
    pause
    scene 53153 with dissolve
    a "Uhm..."
    scene 53154 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She pulls back, coughing your fluids out, wiping her mouth with her hand."
    scene 53155 with dissolve
    a "I may taste your cum but at least I've paid off my debt, right? Ha ha..."
    a "*Coughs*"
    scene 53156 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You tuck yourself back in, smirking as you watch her."
    e "I wanna do it again soon.{p}Perhaps even make it an regular thing."
    scene 53155 with dissolve
    a "I will think about it..."
    scene 53156 with dissolve
    pause
    scene 53155 with dissolve
    a "You should go now..."
    $ renpy.end_replay()
    scene black with Fade(2.0, 1.0, 2.0)
label auntdoorleaves:
    scene black with Fade(2.0, 1.0, 2.0)
    pause
    scene ep4door with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What should I do now?"

    if mtommyep5enterdoor == True:
            menu:
                "{color=#FFD1DF}{i}*Return to the store*":
                    jump shopep5storelist

                "{color=#FFD1DF}{i}*Call Gary and sell him drugs*{/i}{/color} {size=-8}(Req. Phone, Drugs){/size}" if shoppackage and garrydidntbuy:
                    jump garrycallworkout

                "{color=#FFD1DF}{i}*Return home*":
                    jump triptohome

    else:
            menu:
                "{color=#FFD1DF}{i}*Return to the store*":
                    jump shopep5storelist

                "{color=#FFD1DF}{i}*Visit Tommy*":
                    jump triptotommy

                "{color=#FFD1DF}{i}*Call Gary and sell him drugs*{/i}{/color} {size=-8}(Req. Phone, Drugs){/size}" if shoppackage and garrydidntbuy:
                    jump garrycallworkout

                "{color=#FFD1DF}{i}*Return home*":
                    jump triptohome


label lethergoeveep5:
    scene 53108 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You sigh and pull your pants back up, zipping them as you sit back down on the couch."
    e "Fine... I guess you’ve earned a break. Can't be milking the cow dry."
    scene 53109 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She giggles softly, leaning back against the couch"
    a "Mhm... Oh, look at the time..."
    scene 53110 with dissolve
    a "It’s getting late... why don’t you stay the night? We can watch a movie or something... just relax."
    menu:
        "Nah, I really should get going.":
            jump auntdoorleaves

        "Okay...":
            jump eveningwitheve


label eveningwitheve:
    stop music fadeout 1.0
    play music "music/ctrls.wav"
    scene black with Fade(2.0, 1.0, 2.0)
    pause
    "{color=#A8E4A0}{i}{size=-3} You are lying on the bed, waiting for Eve"
    "{color=#A8E4A0}{i}{size=-3} You hear the soft click of the bathroom door opening, and Eve steps out, dressed in a long, oversized T-shirt that barely reaches her thighs."
    scene 53200 with dissolve
    pause
    scene 53201 with dissolve
    a "I usually sleep naked, so...{p}sorry for not having any normal 'jamas."
    scene 53202 with dissolve
    e "That doesn't seem to be a problem for me, though."
    scene 53203 with dissolve
    a "So, what are we watching?"
    scene 53204 with dissolve
    e "You pick..."
    scene 53204_1 with dissolve
    a "Nahhh, you choose. I’m not picky."
    scene 5320205 with dissolve
    pause
    scene 5320206 with dissolve
    pause
    scene 5320207 with dissolve
    pause
    scene 5320208 with dissolve
    pause
    scene 53204a with dissolve
    pause
    scene 5320314 with dissolve
    pause
    scene 5320409 with dissolve
    e "Alright...{p}What about a...{p}drama?"
    scene 5320410 with dissolve
    a "I mean... They're good, but life's already a big drama.{p}Plus, it's late, I don't like thinking that much"
    scene 5320411 with dissolve
    pause
    scene 5320314 with dissolve
    pause
    scene 5320313 with dissolve
    e "So... how about a 90’s action movie?"
    scene 5320412 with dissolve
    e "Those are neat."
    scene 5320410 with dissolve
    a "Great, now you're calling me old again."
    scene 5320409 with dissolve
    e "Old? Nah, just... classic. Like a fine wine."
    scene 5320411 with dissolve
    a "Haha...{p}You sure you can handle something that...{p}mature?"
    scene 5320409 with dissolve
    e "I don't know, wanna find out?"
    scene 5320412 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She smirked, and bit on her lip playfully."
    "{color=#A8E4A0}{i}{size=-3} You turn and click on a 90s action movie from the 'Old but Gold' catalogue, then it began to play."
    scene 5320412aa with dissolve
    "{color=#A8E4A0}{i}{size=-3} After a few minutes of playing, you can’t help but feel the heavy, warm sensation of Eve’s breasts resting on your back, like pillows that should be used for exactly that."
    "{color=#A8E4A0}{i}{size=-3} Every time she breathed, her breasts shifted slightly, and you could feel her nipples harden as your lungs expanded, pressing your back against her tits."
    scene 532050 with dissolve
    pause
    scene 53206 with vpunch
    e "Much better"
    scene 53206a with dissolve
    "{color=#A8E4A0}{i}{size=-3} At one point, you glance over, your eyes drawn to her cleavage, which peeks from under the loose neckline of her T-shirt."
    scene 53206b with dissolve
    pause
    scene 53206c with dissolve
    a "What? Did I distract you? I thought you liked the movie."
    scene 53207 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Instead of answering, your hand slides up her shoulder, gently pulling down one of the straps of her shirt"
    scene 53207a with dissolve
    e "No... I just happen to love tits more than movies."
    scene 53207b with dissolve
    "{color=#A8E4A0}{i}{size=-3} You exposed her left breast, soft and inviting, and you begin to massage it, your thumb brushing against her nipple, feeling it harden under your touch."
    show anatitmsg with dissolve
    e "God, it's so soft... Who would've known that you'd have such good milkers, you fat bitch?"
    a "I'm not fat!"
    e "You're just fat breasted, then."
    scene 53208 with dissolve
    show anakiss with dissolve
    "{color=#A8E4A0}{i}{size=-3} You pull her for a kiss, giving her a passionate, warm kiss."
    $ renpy.pause(3, hard=True)
    scene 53207b with dissolve
    e "Mmm... Bet they're good for fucking."
    show anatitmsg with dissolve
    a "Y-You mean... a tittyfuck?"
    e "...D'uh... Yeah!"
    a "Damn, and here I just wanted to cuddle..."
    e "Fuck cuddling... Now I want to wrap my dick with those baby feeders..."
    scene 53208 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her excitement caused her to start kissing you again."
    show anakiss with dissolve
    "{color=#A8E4A0}{i}{size=-3} Your mouths opening to each other as your tongues coil and stick together, swapping saliva, mixing fluids."
    scene 53207b with dissolve
    a "Okay...{p}Fuck, this is terribly wrong..."
    e "It's not if you enjoy it. I can see it in your face."
    a "Quiet now."
    scene 53209 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She begins taking her ripped tee off..."
    scene 53209a with dissolve
    "{color=#A8E4A0}{i}{size=-3}...swiftly sliding it down like a broken dress..."
    scene 53209b with dissolve
    "{color=#A8E4A0}{i}{size=-3}...until her chest is completely naked."
    scene 53210 with dissolve
    e "You look so fine...{p}Who would've thought a MILF like you would actually melt for a guy like me."
    e "Just like in your favorite porn."
    scene 53210a with dissolve
    a "[player_name]!{p}You're not very forgiving, are you..."
    scene 53211 with dissolve
    e "You're the one packing those meaty MILFY tits. It's all on you, and now I want them wrapped around my cock."
    e "Go ahead, take my cock out. You're dying for it."
    scene 53212 with dissolve
    a "Uhm..."
    scene 53213 with dissolve
    pause 0.25
    scene 53213a with dissolve
    pause 0.25
    scene 53214 with dissolve
    pause 0.25
    scene 53215 with vpunch
    a "Lie down."
    scene 53216 with dissolve
    pause 0.25
    scene 53216a with dissolve
    a "I haven't thanked you yet for fixing my computer..."
    scene 53217 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She positions herself on top of you, wrapping her tits together around your cock, clumsily, not fully sandwiching it, lacking the tightness you wanted."
    show anatitfk with dissolve
    e "You are very obedient.{p}I like it."
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3} Her movements were slow and unsure, and you could feel yourself getting frustrated."
    e "Ugh, when I said I wanted a titty fuck, I really meant it! Let me do it for you... Bring those fat tits over here."
    scene 53222 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Without waiting any longer, you reached down and grabbed her tits yourself, squeezing them tighter around your shaft, pumping them stronger and faster as she moved up and down."
    show anatitfk2 with dissolve
    "{color=#A8E4A0}{i}{size=-3} The difference was immediate, your cock sliding between them with a fast beat, feeling how it glued itself to her sweaty chest skin."
    "{color=#A8E4A0}{i}{size=-3} You watch as she presses and wraps her tits together, sandwiching your cock tight."
    e "These tits were made for me to fuck them... That's for sure."
    "{color=#A8E4A0}{i}{size=-3} Your [nicosister_role] gasped, her face even redder, trying to keep up with your pace."
    a "D-Do they fit... right?"
    show anep5grab with dissolve
    "{color=#A8E4A0}{i}{size=-3} You didn’t answer with words. Instead, you grabbed the back of her head, pulling her towards your cock, forcing her closer to the action, her lips just inches away."
    e "Yeah... Perfect."
    scene anep5grab_frame with dissolve
    show eveep5finalsuck with dissolve
    pause
    e "D-Dear god, that's one good cock sucker right there..."
    pause
    a "Mpfpfh!"
    "{color=#A8E4A0}{i}{size=-3} Bobbing her head up and down, sucking and milking that cock, she seems careless of anything else beside your cock and her mouth."
    pause
    e "Yeah... just like that...{p}Gag on that meat.{p}Do the only thing you're good for, cheap wine drinking cock sucker."
    pause
    "{color=#A8E4A0}{i}{size=-3} She clearly knew what she was doing, and damn, sucking dick was one of her favorite things."
    pause
    scene asdfg10 with vpunch
    "{color=#A8E4A0}{i}{size=-3} She vacuum-sealed her lips on your dick, causing you to quickly nut all into her mouth."
    scene aftercm10 with vpunch
    $ maxmccumep7 += 1
    e "Mmm... I just came! Fuck! I didn't even feel it... Fuck!"
    scene aftercm10 with dissolve
    pause 0.1
    scene aftercm11 with dissolve
    pause 0.1
    scene aftercm12 with dissolve
    pause 0.1
    scene aftercm13 with dissolve
    pause 0.1
    scene aftercm14 with dissolve
    pause 0.1
    scene aftercm15 with dissolve
    pause 0.1
    scene aftercm16 with dissolve
    pause 0.1
    scene aftercm17 with dissolve
    pause 0.1
    scene aftercm18 with dissolve
    pause 0.1
    scene aftercm19 with dissolve
    e "Perhaps you can't jerk a dick with your tits, but damn you can suck it."
    scene 53240 with dissolve
    pause
    scene 53240a with dissolve
    play sound "music/gulp.mp3"
    "*Gulp*"
    scene 53240 with dissolve
    pause
    scene 53240b with dissolve
    a "You were right about grown women, dear...{p}You've still got a lot to learn from one, that's for sure..."
    $ renpy.end_replay()
    scene 53240d with dissolve
    e "For real... But now I should get going."
    scene 53240e with dissolve
    a "W-What? No! I thought we would watch a movie together... Come on... Stay with me!"
    scene 53240d with dissolve
    show screen hint ("If I want to do something else today, I can't stay... although I'm sure she won't be happy with this answer.")

    if easymode:
            menu:
                "Nah, I really should get going.":
                    hide screen hint
                    scene 53240a with dissolve
                    a "*Sighs*..."
                    scene 53240e with dissolve
                    a "Okay, I guess I can't stop you... You know the way out."
                    scene 53240d with dissolve
                    e "Was a real pleasure to use your mouth and tits."
                    scene 53240b with dissolve
                    a "You may have a good dick but you're weird. Ugh."
                    $ auntep5middle = True
                    jump auntdoorleaves

                "I couldn't care less about what you want to do. I just wanted you to blow me.\n{color=#3d85c6} End her path":
                    hide screen hint
                    scene 53240e with dissolve
                    a "E-Excuse me!?"
                    scene 53240d with dissolve
                    e "What? You got a problem?"
                    scene 53240e with dissolve
                    a "You just wanted to use me."
                    scene 53240d with dissolve
                    e "You said it best. Just wanted to use your fat tits. I don't see the problem since you ended up loving it."
                    scene 53240e with dissolve
                    a "W-Well... I can't lie, I love that cock... B-But you're just nutting and leaving! You can't do that!"
                    scene 53240d with dissolve
                    e "I'm not your boyfriend. And if you want that kind of shit, you could probably get one."
                    scene 53240a with dissolve
                    e "Won't be a hard task with a blowjob-mouth like yours. Bitch, you can really suck it."
                    scene 53240c with dissolve
                    a "S-Screw you, [player_name]!{p}Get lost."
                    e "Whatever, bitch. I'm out."
                    $ auntep5angry = True
                    jump auntdoorleaves

                "Okay... I might just stay.\n{color=#3d85c6} Additional scene, but no scene with [woman_role]":
                    jump staywitheveaunt

    else:
            menu:
                "Nah, I really should get going.":
                    hide screen hint
                    scene 53240a with dissolve
                    a "*Sighs*..."
                    scene 53240e with dissolve
                    a "Okay, I guess I can't stop you... You know the way out."
                    scene 53240d with dissolve
                    e "Was a real pleasure to use your mouth and tits."
                    scene 53240b with dissolve
                    a "You may have a good dick but you're weird. Ugh."
                    $ auntep5middle = True
                    jump auntdoorleaves

                "I couldn't care less about what you want to do. I just wanted you to blow me.":
                    hide screen hint
                    scene 53240e with dissolve
                    a "E-Excuse me!?"
                    scene 53240d with dissolve
                    e "What? You got a problem?"
                    scene 53240e with dissolve
                    a "You just wanted to use me."
                    scene 53240d with dissolve
                    e "You said it best. Just wanted to use your fat tits. I don't see the problem since you ended up loving it."
                    scene 53240e with dissolve
                    a "W-Well... I can't lie, I love that cock... B-But you're just nutting and leaving! You can't do that!"
                    scene 53240d with dissolve
                    e "I'm not your boyfriend. And if you want that kind of shit, you could probably get one."
                    scene 53240a with dissolve
                    e "Won't be a hard task with a blowjob-mouth like yours. Bitch, you can really suck it."
                    scene 53240c with dissolve
                    a "S-Screw you, [player_name]!{p}Get lost."
                    e "Whatever, bitch. I'm out."
                    $ auntep5angry = True
                    jump auntdoorleaves

                "Okay... I might just stay.":
                    jump staywitheveaunt




label staywitheveaunt:
            hide screen hint
            scene 53240e with dissolve
            a "Thank you! Thank you... I really, really wanted to spend the night with a boy."
            scene 53240d with dissolve
            e "Any boy?"
            scene 53240b with dissolve
            a "Eh... Well... You. The only boy I want."
            scene 53240d with dissolve
            e "That's much better... Alright, I'll just hit the pause button..."
            scene 53240b with dissolve
            a "Such a charmer..."
            $ auntep5love = True
            scene 53280 with Dissolve(3.0)
            "{color=#A8E4A0}{i}{size=-3} You both settle into the bed, watching the rest of the movie together in silence, not really knowing any context of the movie, just picturing it together, just to slowly fall asleep with it in the background."
label nighteve:
            scene black with fade
            stop music fadeout 1.0
            show text "Few hours later" at title with dissolve
            $ renpy.pause(2, hard=True)
            hide text with dissolve
            show antnight with dissolve
            show text "It was late at night, and in your sleep, you could feel a wetness on your cock,\n along with a pressure moving up and down" at narratortalk with dissolve
            $ renpy.pause(5, hard=True)
            hide text with dissolve
            show text "Panting and soft moans filled your ears" at narratortalk with dissolve
            $ renpy.pause(5, hard=True)
            hide text with dissolve
            show text "As you slowly opened your eyes, waking up, you realized something was happening... " at narratortalk with dissolve
            $ renpy.pause(7, hard=True)
            hide text with dissolve
            show text "Your MILF clearly hadn’t had enough and was taking advantage of you and your young cock being there." at narratortalk with dissolve
            $ renpy.pause(5, hard=True)
            hide text with dissolve
            show text "She was sucking you, jerking you off with her right hand, breathing heavily, trying not to choke.\nShe was really giving it her all, because she was a horny, mature slut starving for cock. For your cock." at narratortalk with dissolve
            $ renpy.pause(8, hard=True)
            hide text with dissolve
            show text "You fully opened your eyes, and without saying a word, you just enjoyed the way she’d woken you up in the best way possible: with a good sloppy blowjob." at narratortalk with dissolve
            $ renpy.pause(5, hard=True)
            hide text with dissolve
            show antnight2 with dissolve
            pause
            scene 53285 with dissolve
            e "Mmm....{p}You won't give up on any dick lying next to you."
            show antlick with dissolve
            $ renpy.pause(3, hard=True)
            pause
            scene 53286 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Eve doesn’t even answer. Instead, she climbs on top of you, positioning herself in the cowgirl position. "
            scene 53286a with dissolve
            e "Oh... I see..."
            scene 53286a with dissolve
            "{color=#A8E4A0}{i}{size=-3} She lowers herself onto you slowly, positioning her pussy on top of your throbbing horny cock, and shoves it in as her body shudders with pleasure. "
            show auntsxnoc
            pause
            "{color=#A8E4A0}{i}{size=-3} She can't stop bouncing and bouncing on your cock. Something inside of her was quickly broken by the mix of alcohol and depraved sex."
            pause
            "{color=#A8E4A0}{i}{size=-3} Each smack of her hips felt heavy, and intense. She'd lift her hips so high in the air that your dick would come out, just for her to smash it down and into her wet, warm cunt every time."
            a "Mmm... Good God..."
            e "Jeez... Tight fit for a fat cock like mine. Fits like a glove. You were made for me."
            a "Ah... S-Sure... W-Whatever... Oh..."
            pause
            e "You know you want it all inside, young virile sperm up your milfy pussy."
            a "Fuck YES... Oh!"
            show auntsxnocm
            "{color=#A8E4A0}{i}{size=-3} You can feel how she's gently holding her weight with her palms on your firm chest, as with one final thrust, you empty your balls inside of her, feeling how your dick pulsates inside, sticking your cum into her walls."
            $ renpy.pause(3, hard=True)
            pause
            scene 53287 with dissolve
            $ maxmccumep7 += 1
            e "You have a really nice pussy."
            a "Shut up..."
            "{color=#A8E4A0}{i}{size=-3} You lie there gasping and moaning, your breathing slowing as the room falls into silence once again."
            scene black with Fade(2.0, 1.0, 2.0)
            $ renpy.end_replay()
            if not easymode:
                        $ achValid5 += 1
                        $ achievement.grant("Achiev23")
                        $ achievement.sync()
                        if not persistent.achievement23:
                                                     show Achiev23 at achievment with easeintop:
                                                                zoom 0.5
                                                                rotate_animation

                                                     "You have received the achievement!{p}{b}\"It was a date!\"{/b}"
                                                     "Number of achievements earned in this chapter [achValid5]/8"
                                                     hide Achiev23
                                                     $ persistent.achievement23 = True
            jump endpart1



label triptohome:
    scene black with fade
    show text "After walking for a while, you finally arrive home." at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    if givemoneyep4 == False:
        "{color=#A8E4A0}{i}{size=-3} After opening the door, you realized the house was eerily quiet and dark."
        scene nopower01 with dissolve
        e "Hello? {p}Is anyone here?"
        e "Candles? How romantic."
        scene black with fade
        "{color=#A8E4A0}{i}{size=-3} You went upstairs, hoping to find your [woman_role], but you couldn’t find her."
        e "[woman_name]?{p}Where are you?"
        scene 0001 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You approached her bedroom door, but when you reached for the handle to turn it and go in, you realized it was locked."
        e "Locked!? Why?"
        m "There's no power.{p}They cut it off for non-payment..."
        e "Damn..."
        m "It should be working again tomorrow. I had to beg them to turn it back on until John comes back, and somehow it worked."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn, I could have given her the money like my father asked... But I'll probably use it later..."
        "{color=#A8E4A0}{i}{size=-3} Avoiding further confrontation, with your energy drained from the day, you went to your room and collapsed onto the bed, ready to sleep like a log."
        show text "{font=LilitaOne.ttf}{color=#e0d71d}MONEY: [money]${/color}{/font}" at moneystat with dissolve
        menu:
            "If you still have $500 left - you can change your decision and give [woman_name] the money to pay the bill... or use it in the next episode."
            "Give 500$" if money >= 500:
                hide text
                $ givemoneyep4 = True
                $ dadfriend += 2
                $ money -= 500
                jump electricityhome
            "No, I want to keep them.":
                hide text
                "Ok!"
                jump endpart1

    else:
      label electricityhome:
        "{color=#A8E4A0}{i}{size=-3} After opening the front door, you finally stepped into your home, feeling the peace that your -broken- home offered."
        e "Hello... I’m back..."
        "{color=#A8E4A0}{i}{size=-3} To your surprise, [woman_role] wasn’t in the living room, though this didn’t worry you — she could easily be in her room."
        "{color=#A8E4A0}{i}{size=-3} Just as you set foot on the stairs, you heard the sound of the shower running like a waterfall."
label ep5showernic:
        if _in_replay:
            $ nicdomep5 = 8
            $ niclustep5 = 8
        scene 55000 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You kneel by the door, eyes locked on the keyhole."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I can't see anything...{p}But why the fuck am I looking through this keyhole?"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I love my life..."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} ...and John, who still hasn't fixed the lock so I can visit his wife while she's taking a shower hehe..."
        show scrolling_image at scroll_up
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Mmm... I can't understand how Dad let such a hot bitch unattended for a while...{p}Just look at that."
        scene 55002a with dissolve
        pause
        scene 55002b with dissolve
        "{color=#A8E4A0}{i}{size=-3} [woman_name] stands under the shower, her back to you, unaware of your entrance."
        scene 55003 with dissolve
        "{color=#A8E4A0}{i}{size=-3} Water streams down her body, outlining her fine curves."
        scene 55003a with dissolve
        "{color=#A8E4A0}{i}{size=-3} You don't bother hiding your intentions, your eyes fixed on her naked, wet body, as your hand moves to your cock."
        scene 55003b with dissolve
        pause
        scene 55003c with dissolve
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Alright... This is peak."
        "{color=#A8E4A0}{i}{size=-3} You start stroking yourself, slowly at first, watching the water drip from her full breasts and slide down her thighs."
        "{color=#A8E4A0}{i}{size=-3} But then she turns around, her eyes widening when she sees you standing there, your cock in your hand."
        scene 55003d with vpunch
        "{color=#A8E4A0}{i}{size=-3} She flinches in surprise and quickly crouches down, covering herself with her hands."
        m "[player_name]!? Ugh...!{p}You're jacking off!"
        scene 55003d3 with dissolve
        e "Hey, uh... I just got home... and well..."
        scene 55003d2 with dissolve
        m "And well...?"
        scene 55003d3 with dissolve
        e "I was a bit... pent up.{p}I caught you showering, and said 'Why not?'"
        scene 55003d with dissolve
        e "Now that you've made me get my dick out... You gave me an idea."
        scene 55003d3 with dissolve
        m "What now..."
        scene 55003d2 with dissolve
        e "How about you...{p}pose for me while I beat my meat to you?"
        scene 55003pose2 with dissolve
        "{color=#A8E4A0}{i}{size=-3} Her hands move to her chest, as she rejects the idea, disgusted."
        scene 55003pose with dissolve
        m "No way!{p}Ugh...{p}I'm not doing that!..."
        scene 55003pose2 with dissolve
        if easymode:
            menu:
                "Oh, come on. I’m not asking for much. You’re already here... you look great. What’s the harm?\n{color=#3d85c6} +1 Lust Point":
                    jump loveshower

                "Tough talk for a cheating hotwife that has no choice other than submitting to her [player_role]'s demands. Chop chop.\n{color=#3d85c6} +1 Dom Point":
                    jump domshower
        else:
            menu:
                "Oh, come on. I’m not asking for much. You’re already here... you look great. What’s the harm?":
                    jump loveshower

                "Tough talk for a cheating hotwife that has no choice other than submitting to her [player_role]'s demands. Chop chop.":
                    jump domshower


label loveshower:
        if not _in_replay:
            show image "images/Stats/Dom[nicdomep5].png" at statleft
            show image "images/Stats/Lust[niclustep5].png" at statright
            pause 1
            $ niclustep5 += 1
            show image "images/Stats/Dom[nicdomep5].png" at statleft
            show image "images/Stats/Lust[niclustep5].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[nicdomep5].png"
            hide image "images/Stats/Lust[niclustep5].png"
        "{color=#A8E4A0}{i}{size=-3} [woman_name] tightens her grip over her chest, clearly disgusted and trying to resist."
        scene 55003pose with dissolve
        m "I’m not a toy! Or a slut!{p}I’m your [woman_role]!{p}You can’t just do this."
        scene 55003pose2 with dissolve
        e "You say that... but you’re still standing there, aren’t you?{p}You haven’t walked away."
        scene 55003pose with dissolve
        m "S-So what!?"
        scene 55003pose2 with dissolve
        e "That's because deep down, I think you know you like this."
        scene 55003pose with dissolve
        m "What are you even talking about?{p}I don’t like this. You’re just..."
        scene 55003pose2 with dissolve
        e "I’m just saying what you won’t admit. You know you’re beautiful. And you know I can’t take my eyes off you. So, why not enjoy it?"
        scene 55003pose3 with dissolve
        "{color=#A8E4A0}{i}{size=-3} She looks away, trying not to show her disgust."
        scene 55003pose2 with dissolve
        e "Come on... I know you feel this. You’re not just some boring housewife. You’re stunning. Pose for me. Show me you know it."
        $ showerlustnic += 1
label lustprysnic:
              "{color=#A8E4A0}{i}{size=-3} [woman_name] bites her lip, still resisting, but you can see her defenses crumbling bit by bit... "
              scene pose09 with dissolve
              scene pose14 with dissolve
              scene pose15 with dissolve
              scene pose16 with dissolve
              scene pose17 with dissolve
              "{color=#A8E4A0}{i}{size=-3} Slowly, she lowers her arms, the water continuing to run down her body."
              scene pose25 with dissolve
              "{color=#A8E4A0}{i}{size=-3} Her posture is tense, but after a long moment, she finally turns slightly, exposing her chest to you, showing off her precious tits."
              e "There you go... Look at that.{p}You’ve got a body worth showing off... So-fucking-HOT."
              "{color=#A8E4A0}{i}{size=-3} Her face flushes, but she doesn’t speak. "
              e "Come closer to me... I want to look at your lovely tits up close, but don't splash me."
              scene pose30 with dissolve
              "{color=#A8E4A0}{i}{size=-3} Complying to your orders, she took two steps, and shyly showed her breasts to you, almost sticking them against the glass."
              scene pose31 with dissolve
              e "That’s more like it. You see? You look amazing, such a shame you've been lowballing yourself with my dad."
              e "You’ve done well. Get yourself out when you’re ready. I’ll be waiting outside."
              scene pose31left with dissolve
              "{color=#A8E4A0}{i}{size=-3} You leave the bathroom, letting your [woman_role] alone for a minute."
              $ renpy.end_replay()
              $ showerlustnic += 1
              jump ep5aftershower

label domshower:
        show image "images/Stats/Dom[nicdomep5].png" at statleft
        show image "images/Stats/Lust[niclustep5].png" at statright
        pause 1
        $ nicdomep5 += 1
        show image "images/Stats/Dom[nicdomep5].png" at statleft
        show image "images/Stats/Lust[niclustep5].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[nicdomep5].png"
        hide image "images/Stats/Lust[niclustep5].png"
        scene 55003pose with dissolve
        m "I’m not a toy! Or a slut!? I'm your [woman_role]!{p}You just... don't seem to understand that..."
        scene 55003pose2 with dissolve
        e "You say you're not a slut, yet you’re still here, aren’t you?"
        scene 55003pose with dissolve
        m "...And?"
        scene 55003pose2 with dissolve
        e "You haven’t walked away, haven’t called for help...{p}Perhaps not because you KNOW you can't do shit about it, but you actually like it. "
        scene 55003pose with dissolve
        m "...{p}What are you even saying!?"
        scene 55003pose2 with dissolve
        e "I'm saying that you're a good slut, and you will do what a good slut does and pose for me."
        scene 55003pose3 with dissolve
        "{color=#A8E4A0}{i}{size=-3} [woman_name] clenches her jaw, refusing to look back at you."
        scene 55003pose2 with dissolve
        e "Come on...{p}Now.{p}Pose for me. Do what I say."
        $ showerdomnic += 1
label domprysnic:
            "{color=#A8E4A0}{i}{size=-3} She sighs, you can see her shaking slightly, still resisting, but she knows there’s no escape from this. "
            scene pose09 with dissolve
            scene pose14 with dissolve
            scene pose15 with dissolve
            scene pose16 with dissolve
            scene pose17 with dissolve

            "{color=#A8E4A0}{i}{size=-3} Slowly, she lowers her arms. The water continues to cascade down her body, and after a long moment, she finally turns slightly, enough for you to see her tits up close, her arms hanging limply by her sides."
            scene pose25 with dissolve
            m "You've got no limits, I can't believe how depraved you've turned out to be..."
            e "Sh..."
            "{color=#A8E4A0}{i}{size=-3} [woman_name] hesitates again, her face showing disgust over you."
            "{color=#A8E4A0}{i}{size=-3} She looks away from you, exposing her full body to you under the running water."
            "{color=#A8E4A0}{i}{size=-3} The curves of her hips, the swell of her breasts, her flat stomach... all on display."
            "{color=#A8E4A0}{i}{size=-3} Her face is tense, disgusted, but she doesn’t look at you"
            e "I want to see them better, come on, come on."
            "{color=#A8E4A0}{i}{size=-3} Her lips tighten as she hesitates, her arms twitching, as if she wants to refuse."
            scene pose30 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Her nipples, still stiff from the heat, stand out against her skin as the water continues to flow over her."
            e "Funny..."
            e "I told you to show me your tits up close...{p}and you just did so..."
            scene pose31 with dissolve
            e "...That's exactly how obedient I want you to be..."
            e "Obedient enough to get on your knees now and vacuum-seal your lips around my dick..."
            scene pose30 with dissolve
            e "...And suck on it until you can feel my cum stick all over your throat..."
            e "You would just do it...{p}Because you are good [woman_role]."
            scene pose31 with dissolve
            e "And you want to suck your [player_role]'s cock."
            scene pose30 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Looking around, guilty of her thoughts, she took a step back and bit her inner lip without opening her mouth in a sign of doubt and self disapproval."
            scene pose40 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Nonetheless, after a brief moment of doubt, she kneeled down under the water, reaching up to your throbbing cock, ready to begin sucking."
            scene pose41 with dissolve
            e "Fucking hell... Good girl...{p}But nah, I don't wanna do it here."
            e "I was just curious how quickly you would get on your knees to blow me."
            e "I'll be waiting for you in your room... Bye."
            scene pose42 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Without looking back at her, you turn and leave the bathroom, leaving her kneeling naked under the water."
            $ renpy.end_replay()
            $ showerdomnic += 1
            jump ep5aftershower

label ep5aftershower:
        scene black with Fade(2.0, 1.0, 2.0)
        scene 55100bed with Dissolve(2.0)
        "{color=#A8E4A0}{i}{size=-3} You lay back on the bed, listening to the sound of a hair dryer."
        scene 55100bed1 with dissolve
        "{color=#A8E4A0}{i}{size=-3} Moments later, [woman_name] steps out of the bathroom, wrapped tightly in her towel."
        "{color=#A8E4A0}{i}{size=-3} She hesitates at the door, her eyes meeting yours, a blush creeping up her cheeks"
        scene 55100bed2 with dissolve
        m "Can I have some privacy?"
        scene 55100bed3 with dissolve
        pause
        scene 55100bed4 with dissolve

        if easymode:
            menu:
                    "Look, I can't be more straight with you. I just can't get enough of you.\n{color=#3d85c6} +1 Lust Point":
                        jump aftershowerep5lust


                    "You’ve been such good little slut, doing what I asked.\n{color=#3d85c6} +1 Dom Point":
                        jump aftershowerep5dom
        else:
            menu:
                    "Look, I can't be more straight with you. I just can't get enough of you.":
                        jump aftershowerep5lust


                    "You’ve been such good little slut, doing what I asked.":
                        jump aftershowerep5dom


label aftershowerep5lust:
    scene nicaftshow0 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her blush deepens, and she looks away, clearly uncomfortable but not angry."
    scene nicaftshow4 with dissolve
    m "...Thanks, I guess."
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    pause 1
    $ niclustep5 += 1
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicdomep5].png"
    hide image "images/Stats/Lust[niclustep5].png"
    scene nicaftshow0 with dissolve
    e "How about we just take it easy tonight? Let’s watch some TV together... Nothing else, just TV and chill."
    scene nicaftshow9a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her shoulders loosen slightly, and she looks at the floor, clearly not having many options to choose."
    scene nicaftshow9b with dissolve
    m "... Do I have a choice?"
    scene nicaftshow9 with dissolve
    e "I don't know, do you?"
    scene nicaftshow9c with dissolve
    m "Ugh... Fine."
    jump giftep5nic

label aftershowerep5dom:
    scene nicaftshow3 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She tenses, her body stiff as she tightens the towel around herself, avoiding your eyes."
    scene nicaftshow5 with dissolve
    m "W-What do you want from me now?"
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    pause 1
    $ nicdomep5 += 1
    show image "images/Stats/Dom[nicdomep5].png" at statleft
    show image "images/Stats/Lust[niclustep5].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicdomep5].png"
    hide image "images/Stats/Lust[niclustep5].png"
    e "Well...{p}I feel like watching TV, with you. Just like a couple would do, right?"
    scene nicaftshow1 with dissolve
    m "We. Are. NOT.{p}A couple."
    scene nicaftshow7 with dissolve
    e "Oh but we will be.{p}Trust me on that."
    jump giftep5nic

label giftep5nic:
    scene nicaftshow9a with dissolve
    if shopalcoholep5weak == True or shopalcoholep5strong == True:
        e "Oh, I've got something for you."
label giftep5nicask:
        scene nicaftshow9a with dissolve

        if easymode:
            menu:
                    "{color=#FFD1DF}{i}Give her Sexy Lingerie{/i}{/color}{size=-8} (Req. Sexy Lingerie){/size}\n{color=#3d85c6} Needed for the final scene" if shopsexyep5wear == True:
                        $ nicgetsexylingerie = True
                        $ shopsexyep5wear = False
                        jump giveniclingerie

                    "{color=#FFD1DF}{i}Give her White Wine{/i}{/color}{size=-8} (Req. White Wine){/size} " if shopalcoholep5weak == True:
                        $ nicgetwhitewine = True
                        $ shopalcoholep5weak = False
                        jump givenicwhitewine

                    "{color=#FFD1DF}{i}Give her Red Wine{/i}{/color}{size=-8} (Req. Red Wine){/size}\n{color=#3d85c6} Needed for the final scene" if shopalcoholep5strong == True:
                        $ nicgetredwine = True
                        $ shopalcoholep5strong = False
                        jump givenicredwine

                    "Continue":
                        jump nicep5tv

        else:
            menu:
                    "{color=#FFD1DF}{i}Give her Sexy Lingerie{/i}{/color}{size=-8} (Req. Sexy Lingerie){/size} " if shopsexyep5wear == True:
                        $ nicgetsexylingerie = True
                        $ shopsexyep5wear = False
                        jump giveniclingerie

                    "{color=#FFD1DF}{i}Give her White Wine{/i}{/color}{size=-8} (Req. White Wine){/size} " if shopalcoholep5weak == True:
                        $ nicgetwhitewine = True
                        $ shopalcoholep5weak = False
                        jump givenicwhitewine

                    "{color=#FFD1DF}{i}Give her Red Wine{/i}{/color}{size=-8} (Req. Red Wine){/size} " if shopalcoholep5strong == True:
                        $ nicgetredwine = True
                        $ shopalcoholep5strong = False
                        jump givenicredwine

                    "Continue":
                        jump nicep5tv

label giveniclingerie:
        scene 55200 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You hand her the lingerie set you got for her."
        e "Thought you’d look great in this. Go on, put it on."
        scene 55200b with dissolve
        "{color=#A8E4A0}{i}{size=-3} She hesitates, blushing, but her resistance is soft."
        scene 55200a with dissolve
        m "...I’m not walking around in this. I hope you don’t expect me to parade around like some kind of trophy or something."
        scene 55200b with dissolve
        e "But you are my trophy..."
        scene 55200c with dissolve
        e "Chill the fuck down. If you're going to bitch that much, you could just put that robe of yours over it and that's it."
        scene 55200 with dissolve
        m "Uhm..."
        jump giftep5nicask

label givenicwhitewine:
        scene 55200white with dissolve
        "{color=#A8E4A0}{i}{size=-3} You grab a bottle of white wine, holding it, grinning."
        e "Got you some wine. White wine, figured it’d be nice."
        scene 55200white2 with dissolve
        "{color=#A8E4A0}{i}{size=-3} [woman_name]’s disappointment is clear, though she stays quiet, not wanting to push back too much."
        e "Come on, it's probably the tastiest white liquid you've ever had in your mouth."
        scene 55200white3 with dissolve
        m "Ugh... You're such a dickhead."
        jump giftep5nicask


label givenicredwine:
        scene 55200red with dissolve
        "{color=#A8E4A0}{i}{size=-3} You hand her the red wine bottle."
        if winemerlot == True:
            scene 55200redgood with dissolve
            e "I brought something to make tonight even better... Merlot. I know you love this thing."
            "{color=#A8E4A0}{i}{size=-3} Your [woman_role] seems less enthusiastic, though the gift is appreciated."
            scene 55200redgood2 with dissolve
            m "Oh... Merlot... It’s good."
            scene 55200redgood with dissolve
            e "It sure makes any bad movie more bearable."
            jump giftep5nicask
        else:
            scene 55200redbad with dissolve
            m "Thanks, but I usually prefer Merlot..."
            scene 55200redbad2 with dissolve
            e "Shit.{p}Well, it’s the thought that counts, right?"
            scene 55200redbad with dissolve
            m "Yeah... thanks for the thought."
            jump giftep5nicask

label nicep5tv:
        stop music fadeout 1.0
        play music "Music/Mnicdat.mp3"
        scene 55300 with dissolve
        e "I'll wait for you in the living room."
        scene black with Fade(2.0, 1.0, 2.0)
        "{color=#A8E4A0}{i}{size=-3} Without having a long wait, you still got eager to see her there, growing weary of waiting, until footsteps approached from the hall."

        if nicgetsexylingerie == False:
            jump nicpyj
        if nicgetsexylingerie == True:
            scene 50500sx with dissolve
            "{color=#A8E4A0}{i}{size=-3} [woman_name] steps into the room, wearing the outfit you gave her."
            "{color=#A8E4A0}{i}{size=-3} It clings to her body, accentuating every curve, though her posture remains stiff, unsafe."
            scene 50501sx00 with dissolve
            $ renpy.pause(0.25, hard=True)
            scene 50501sx01 with dissolve
            scene 50501sx02 with dissolve
            scene 50501sx03 with dissolve
            scene 50501sx04 with dissolve
            scene 50501sx05 with dissolve
            scene 50501sx06 with dissolve
            scene 50501sx07 with dissolve
            scene 50501sx08 with dissolve
            $ renpy.pause(0.25, hard=True)
            scene 50501sx09 with dissolve
            scene 50501sx10 with dissolve
            scene 50501sx11 with dissolve
            scene 50501sx12 with dissolve
            scene 50501sx13 with dissolve
            scene 50501sx14 with dissolve
            scene 50501sx15 with dissolve
            scene 50501sx16 with dissolve
            scene 50501sx17 with dissolve
            scene 50501sx18 with dissolve
            scene 50501sx19 with dissolve
            scene 50501sx20 with dissolve
            e "Looking fine like good wine..."
            scene 50501sx21 with dissolve
            $ renpy.pause(0.25, hard=True)
            scene 50501sx22 with dissolve
            scene 50501sx23 with dissolve
            scene 50501sx24 with dissolve
            m "...You think so?"
            scene 50501sx25 with dissolve
            scene 50501sx26 with dissolve
            scene 50501sx27 with dissolve
            e "Oh come on, sit next to me. No need to be afraid of me."
            "{color=#A8E4A0}{i}{size=-3} [woman_name] looks at you, but after a moment of hesitation, she shifts over. "
            scene black with fade
            scene 57000a with dissolve
            "{color=#A8E4A0}{i}{size=-3} As soon as she sits down beside you, you place your head on her thigh, resting on her."
            "{color=#A8E4A0}{i}{size=-3} The movie menu pops up on the screen, a selection of films you could choose from."
            scene 57000moviepicksx with dissolve
            "{color=#A8E4A0}{i}{size=-3} You casually navigate the options as [woman_name] lies beside you, tense from having you so close to her private bits."
            scene 57002apick with dissolve
            e "How about you pick a movie for me? I'm too tired."
            scene 57001apick with dissolve
            m "Mhm..."
            scene 570007 with dissolve
            "{color=#A8E4A0}{i}{size=-3} After choosing something to watch out of the online catalogue, she hits 'play' and pants lightly."
            scene 570006 with dissolve
            "{color=#A8E4A0}{i}{size=-3} The movie begins, as the TV reflects on your eyes as you watch it together."
            "{color=#A8E4A0}{i}{size=-3} For a few minutes, neither of you speaks, but the silence feels heavy, weighted by the unspoken discomfort between you caused by her."
            scene 570002 with dissolve
            e "I can feel you're tense... Hmm..."
            if nicgetredwine == True and winemerlot == True:
                scene 56000sxdrinkpass with dissolve
                e "That's why I've poured a glass of Merlot for you"
                "{color=#A8E4A0}{i}{size=-3} She hesitates, her eyes flicking from the glass to you, and then back again."
                scene 56000sxdrink0 with dissolve
                "{color=#A8E4A0}{i}{size=-3} After a moment, she reaches out and takes it from you."
                scene 56000sxdrink1 with dissolve
                "{color=#A8E4A0}{i}{size=-3} She brings it to her lips, taking a slow sip."
                scene 56000sxdrink0 with dissolve
                m "At least it’s Merlot... Cheers."
                jump redwinedrinking
            elif nicgetredwine and winecabernet == True:
                scene 56000sxdrinkpass with dissolve
                e "That's why I've poured a glass of your red wine for you"
                "{color=#A8E4A0}{i}{size=-3} She hesitates, her eyes flicking from the glass to you, and then back again."
                scene 56000sxdrink0 with dissolve
                "{color=#A8E4A0}{i}{size=-3} After a moment, she reaches out and takes it from the table."
                scene 56000sxdrink1 with dissolve
                "{color=#A8E4A0}{i}{size=-3} She brings it to her lips, taking a slow sip."
                scene 56000sxdrink0 with dissolve
                m "Not bad for a wine that isn't Merlot."
                jump redwinedrinking
            elif nicgetwhitewine == True:
                scene 57002apick with dissolve
                e "That's why I've poured a glass of your white wine for you"
                scene 57001apicktalk with dissolve
                m "Why did you get white? You know I don’t like it..."
                scene 57001a with dissolve
                "{color=#A8E4A0}{i}{size=-3} She looks at the wine disappointed of your choice in wine."
                scene 57002a with dissolve
                e "It’s still wine, isn’t it? Come on, just drink it."
                scene 570007 with dissolve
                "{color=#A8E4A0}{i}{size=-3} [woman_name] bites her lip, looking away from you, her body tense but unmoving."
                "{color=#A8E4A0}{i}{size=-3} There’s no fight in her words, just exhaustion."
                scene 570003 with dissolve
                m "I don’t want it... Please. Just... leave it."
                scene 57002a with dissolve
                e "Just drink it! It's the same thing!"
                scene 570002 with dissolve
                m "It's not!"
                scene 570007 with dissolve
                e "Alright, You know what? Fuck your wine. I only wanted you drunk enough so I can fuck your guts."
                scene 570005 with dissolve
                m "Ugh! That's it. I've had enough of you today."
                scene black with Fade(2.0, 1.0, 2.0)
                "{color=#A8E4A0}{i}{size=-3} She stands up, and leaves you on your own after being disrespected."
                e "Women."
                $ nicangrywinescene = True
                jump endpart1
            else:
                jump nowinedrinking

        label redwinedrinking:
            "{color=#A8E4A0}{i}{size=-3} The movie drags on, the two of you barely paying attention to what’s happening on screen."
            scene 56000sxdrinkask with dissolve
            m "Are you... Enjoying it?"
            scene 56000sxdrinkresp with dissolve
            e "Hm? I thought you weren't even going to watch it. And now you care about if I'm watching it?"
            scene 56000sxdrinkask with dissolve
            m "I'm just asking..."
            scene 56000sxdrink1 with dissolve
            e "Yeah... At least the girls are hot..."
            e "Yet... You're better than any of them."
            scene 56000sxdrinkask with dissolve
            m "Yeah... Sure..."
            scene 56000sxdrinkresp with dissolve
            e "They might be younger but they ain't as hot as you. Trust me, you're fucking hot."
            scene 56000sxdrink1 with dissolve
            "{color=#A8E4A0}{i}{size=-3} She blushes deeply, not knowing how to react, as she sips on her glass of wine."
            scene 56000sxdrinkask with dissolve
            m "*Hip* ...Thanks."

            menu:

                "Ask for a favor {size=-8}(Req. Red Wine){/size}" if nicgetredwine == True:
                  label sxfavor:
                    scene 56000hjsx with dissolve
                    e "Do me a favor..."
                    scene 56000hjsx1 with dissolve
                    pause
                    scene 56000hjsx2 with dissolve
                    "{color=#A8E4A0}{i}{size=-3} [woman_name] looks at you, her eyes narrowing slightly, as she blushes and notices you being completely naked."
                    scene 56000hjsx3 with dissolve
                    m "W-What are you doing!? Are you kidding me!? Right now!?"
                    scene 56000hjsx4 with dissolve
                    e "I want you to stroke my dick while I watch the movie... Do it."
                    "{color=#A8E4A0}{i}{size=-3} [woman_name]’s expression tightens, but she doesn’t leave. "
                    scene testhj00 with dissolve
                    "{color=#A8E4A0}{i}{size=-3} There’s a long pause before she reaches down, her hand moving over your shorts, her movements mechanical, distant."
                    show hjsxmov2
                    pause
                    "{color=#A8E4A0}{i}{size=-3} Her body stays in the same position, still lying on her side as she halfheartedly obeys your request. "
                    pause
                    "{color=#A8E4A0}{i}{size=-3} It’s clear she isn’t into it, since she looks only motivated by the content of her glass."
                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                    show image "images/Stats/Lust[niclustep5].png" at statright
                    pause 1
                    $ nicdomep5 += 1
                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                    show image "images/Stats/Lust[niclustep5].png" at statright
                    with dissolve
                    pause 3
                    hide image "images/Stats/Dom[nicdomep5].png"
                    hide image "images/Stats/Lust[niclustep5].png"

                    pause
                    scene 56000sxcm with vpunch
                    "{color=#A8E4A0}{i}{size=-3} You lean back, letting out a satisfied groan as you cum-shot away your load."
                    $ maxmccumep7 += 1
                    scene 56000sxcm with vpunch
                    e "Oh... fuck..."
                    scene 56000sxcmwipe with dissolve
                    "{color=#A8E4A0}{i}{size=-3} The silence after is thick, uncomfortable."
                    "{color=#A8E4A0}{i}{size=-3} [woman_name] pulls her hand away, wiping it on her thigh without a word."
                    scene 56000sxcmafter with dissolve
                    m "I guess that's it... *Hip*"
                    $ renpy.end_replay()
                    scene 56000sxcmafter2 with dissolve
                    e "Shit, you're drunk. Are you sure you can walk upstairs on your own?"
                    scene 56000sxcmafter with dissolve
                    m "I'm not a granny. I'll go to sleep... You do whatever you want... *Hip*"
                    scene 56000sxcmafter2 with dissolve
                    e "Oh, mind your words."
                    if nicgetredwine == True and winemerlot == True:
                        scene black with Fade(2.0, 1.0, 2.0)
                        "{color=#A8E4A0}{i}{size=-3} Tipsy, she stands up, picks up the bottle of Merlot, and left you on your own at the living room."
                        jump finalep5
                    elif nicgetredwine == True and winecabernet == True:
                        scene black with Fade(2.0, 1.0, 2.0)
                        "{color=#A8E4A0}{i}{size=-3} Tipsy, she walked upstairs to her room, and left you on your own with the Cabernet bottle at the living room."
                        jump endpart1

                "Continue watching":
                    $ niclovebonusfactor += 4
                    jump continuewatching

        label nowinedrinking:
                scene 570006 with dissolve
                "{color=#A8E4A0}{i}{size=-3} After what it seemed at eternity later, the movie finally winds down, as the credits roll across the screen"
                scene 570005 with dissolve
                m "I guess that's it..."
                scene 570002 with dissolve
                e "Do you want me to help you get to the bedroom?"
                scene 570003 with dissolve
                m "I'm not a granny. I'll go to sleep..."
                scene 570007 with dissolve
                e "Oh ok... Goodnight..."
                scene black with Fade(2.0, 1.0, 2.0)
                "{color=#A8E4A0}{i}{size=-3} She walked upstairs to her room, and left you on your own at the living room."
                $ nicnormalwinescene = True
                jump endpart1

        label continuewatching:
            scene 56000sxdrink0 with dissolve
            "{color=#A8E4A0}{i}{size=-3} After what it seemed at eternity later, the movie finally winds down, as the credits roll across the screen."
            scene 56000sxdrink1 with dissolve
            m "I guess that's it... *Hip*"
            e "Shit, you're drunk. Are you sure you can walk upstairs on your own?"
            m "I'm not a granny. I'll go to sleep... You do whatever you want... *Hip*"
            e "Oh, mind your words."
            if nicgetredwine == True and winemerlot == True:
                "{color=#A8E4A0}{i}{size=-3} Tipsy, she stands up, picks up the bottle of Merlot, and left you on your own at the living room."
                scene black with fade
                jump finalep5
            elif nicgetredwine == True and winecabernet == True:
                "{color=#A8E4A0}{i}{size=-3} Tipsy, she walked upstairs to her room, and left you on your own with the Cabernet bottle at the living room."
                jump endpart1



label nicpyj:
        if nicgetsexylingerie == False:
            scene 50500py with dissolve
            "{color=#A8E4A0}{i}{size=-3} [woman_name] enters, dressed in a pair of John’s oversized pajamas. "
            "{color=#A8E4A0}{i}{size=-3} They hang loose on her frame, swallowing her form in the thick fabric. "
            "{color=#A8E4A0}{i}{size=-3} She pauses in the doorway, looking at you with a blank expression, then walks over to the couch. "
            scene 5050100 with dissolve
            $ renpy.pause(0.25, hard=True)
            scene 5050101 with dissolve
            scene 5050102 with dissolve
            scene 5050103 with dissolve
            scene 5050104 with dissolve
            scene 5050105 with dissolve
            scene 5050106 with dissolve
            scene 5050107 with dissolve
            scene 5050108 with dissolve
            scene 5050109 with dissolve
            scene 5050110 with dissolve
            scene 5050111 with dissolve
            $ renpy.pause(0.25, hard=True)
            scene 5050112 with dissolve
            scene 5050113 with dissolve
            scene 5050114 with dissolve
            scene 5050115 with dissolve
            scene 5050116 with dissolve
            scene 5050117 with dissolve
            scene 5050118 with dissolve
            scene 5050119 with dissolve
            scene 5050120 with dissolve
            m "So?"
            "{color=#A8E4A0}{i}{size=-3} Her tone is flat, uninterested, as she settles into the cushions, her eyes locked into you."
            e "Oh come on, sit next to me. No need to be afraid of me."
            "{color=#A8E4A0}{i}{size=-3} [woman_name] looks at you, but after a moment of hesitation, she shifts over. "
            scene black with fade
            scene 57000apy with dissolve
            "{color=#A8E4A0}{i}{size=-3} As soon as she sits down beside you, you place your head on her thigh, resting on her."
            "{color=#A8E4A0}{i}{size=-3} The movie menu pops up on the screen, a selection of films you could choose from."
            scene 57000moviepickpy with dissolve
            "{color=#A8E4A0}{i}{size=-3} You casually navigate the options as [woman_name] lies beside you, tense from having you so close to her private bits."
            scene 57002apickpy with dissolve
            e "How about you pick a movie for me? I'm too tired."
            scene 57001apickpy with dissolve
            m "Mhm..."
            scene 57000apy with dissolve
            "{color=#A8E4A0}{i}{size=-3} After choosing something to watch out of the online catalogue, she hits 'play' and pants lightly."
            scene 57pyj6 with dissolve
            "{color=#A8E4A0}{i}{size=-3} The movie begins, as the TV reflects on your eyes as you watch it together."
            "{color=#A8E4A0}{i}{size=-3} For a few minutes, neither of you speaks, but the silence feels heavy, weighted by the unspoken discomfort between you caused by her."
            scene 57pyj2 with dissolve
            e "I can feel you're tense... Hmm..."
            if nicgetredwine == True and winemerlot == True:
                scene 56000pydrinkpass with dissolve
                e "That's why I've poured a glass of Merlot for you"
                "{color=#A8E4A0}{i}{size=-3} She hesitates, her eyes flicking from the glass to you, and then back again."
                scene 56000drink with dissolve
                "{color=#A8E4A0}{i}{size=-3} After a moment, she reaches out and takes it from you."
                scene 56000drink2 with dissolve
                "{color=#A8E4A0}{i}{size=-3} She brings it to her lips, taking a slow sip."
                scene 56000drink3 with dissolve
                m "At least it’s Merlot... Cheers."
                jump pyredwinedrinking
            elif nicgetredwine and winecabernet == True:
                scene 56000pydrinkpass with dissolve
                e "That's why I've poured a glass of your red wine for you"
                "{color=#A8E4A0}{i}{size=-3} She hesitates, her eyes flicking from the glass to you, and then back again."
                scene 56000drink with dissolve
                "{color=#A8E4A0}{i}{size=-3} After a moment, she reaches out and takes it from the table."
                scene 56000drink2 with dissolve
                "{color=#A8E4A0}{i}{size=-3} She brings it to her lips, taking a slow sip."
                scene 56000drink3 with dissolve
                m "Not bad for a wine that isn't Merlot."
                jump pyredwinedrinking
            elif nicgetwhitewine == True:
                scene 57002apickpy with dissolve
                e "That's why I've poured a glass of your white wine for you"
                scene 57001apickpy with dissolve
                m "Why did you get white? You know I don’t like it..."
                scene 57pyj1 with dissolve
                "{color=#A8E4A0}{i}{size=-3} She looks at the wine disappointed of your choice in wine."
                scene 57pyj2 with dissolve
                e "It’s still wine, isn’t it? Come on, just drink it."
                scene 57pyj1 with dissolve
                "{color=#A8E4A0}{i}{size=-3} [woman_name] bites her lip, looking away from you, her body tense but unmoving."
                "{color=#A8E4A0}{i}{size=-3} There’s no fight in her words, just exhaustion."
                scene 57pyj5 with dissolve
                m "I don’t want it... Please. Just... leave it."
                scene 57pyj2 with dissolve
                e "Just drink it! It's the same thing!"
                scene 57pyj5 with dissolve
                m "It's not!"
                scene 57pyj2 with dissolve
                e "Alright, You know what? Fuck your wine. I only wanted you drunk enough so I can fuck your guts."
                scene 57pyj9 with dissolve
                m "Ugh! That's it. I've had enough of you today."
                scene black with Fade(2.0, 1.0, 2.0)
                "{color=#A8E4A0}{i}{size=-3} She stands up, and leaves you on your own after being disrespected."
                e "Women."
                $ nicangrywinescene = True
                jump endpart1
            else:
                jump pynowinedrinking

        label pyredwinedrinking:
            scene 56000drink with dissolve
            "{color=#A8E4A0}{i}{size=-3} The movie drags on, the two of you barely paying attention to what’s happening on screen."
            scene 56000drink3 with dissolve
            m "Are you... Enjoying it?"
            scene 56000drink2 with dissolve
            e "Hm? I thought you weren't even going to watch it. And now you care about if I'm watching it?"
            scene 56000drink3 with dissolve
            m "I'm just asking..."
            scene 56000pymcresp with dissolve
            e "Yeah... At least the girls are hot..."
            e "Yet... You're better than any of them."
            scene 56000drink3 with dissolve
            m "Yeah... Sure..."
            scene 56000pymcresp with dissolve
            e "They might be younger but they ain't as hot as you. Trust me, you're fucking hot."
            scene 56000drink with dissolve
            "{color=#A8E4A0}{i}{size=-3} She blushes deeply, not knowing how to react, as she sips on her glass of wine."
            scene 56000drink3 with dissolve
            m "*Hip* ...Thanks."

            menu:

                "Ask for a favor {size=-8}(Req. Red Wine){/size}" if nicgetredwine == True:
                  label pysxfavor:
                    scene 56000hjpy with dissolve
                    e "Do me a favor..."
                    scene 56000hjpy1 with dissolve
                    pause
                    scene 56000hjpy2 with dissolve
                    "{color=#A8E4A0}{i}{size=-3} [woman_name] looks at you, her eyes narrowing slightly, as she blushes and notices you being completely naked."
                    scene 56000hjpy3 with dissolve
                    m "W-What are you doing!? Are you kidding me!? Right now!?"
                    scene 56000hjpy4 with dissolve
                    e "I want you to stroke my dick while I watch the movie... Do it."
                    "{color=#A8E4A0}{i}{size=-3} [woman_name]’s expression tightens, but she doesn’t leave. "
                    scene testhjpy00 with dissolve
                    "{color=#A8E4A0}{i}{size=-3} There’s a long pause before she reaches down, her hand moving over your shorts, her movements mechanical, distant."
                    show hjpymov
                    pause
                    "{color=#A8E4A0}{i}{size=-3} Her body stays in the same position, still lying on her side as she halfheartedly obeys your request. "
                    pause
                    "{color=#A8E4A0}{i}{size=-3} It’s clear she isn’t into it, since she looks only motivated by the content of her glass."
                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                    show image "images/Stats/Lust[niclustep5].png" at statright
                    pause 1
                    $ nicdomep5 += 1
                    show image "images/Stats/Dom[nicdomep5].png" at statleft
                    show image "images/Stats/Lust[niclustep5].png" at statright
                    with dissolve
                    pause 3
                    hide image "images/Stats/Dom[nicdomep5].png"
                    hide image "images/Stats/Lust[niclustep5].png"

                    pause
                    scene 56000pycm with vpunch
                    "{color=#A8E4A0}{i}{size=-3} You lean back, letting out a satisfied groan as you cum-shot away your load."
                    $ maxmccumep7 += 1
                    scene 56000pycm with vpunch
                    e "Oh... fuck..."
                    scene 56000pycmwipe with dissolve
                    "{color=#A8E4A0}{i}{size=-3} The silence after is thick, uncomfortable."
                    "{color=#A8E4A0}{i}{size=-3} [woman_name] pulls her hand away, wiping it on her thigh without a word."
                    scene 56000pycmafter with dissolve
                    m "I guess that's it... *Hip*"
                    $ renpy.end_replay()
                    scene 56000pycmafter2 with dissolve
                    e "Shit, you're drunk. Are you sure you can walk upstairs on your own?"
                    scene 56000pycmafter with dissolve
                    m "I'm not a granny. I'll go to sleep... You do whatever you want... *Hip*"
                    scene 56000pycmafter2 with dissolve
                    e "Oh, mind your words."
                    if nicgetredwine == True and winemerlot == True:
                        scene black with Fade(2.0, 1.0, 2.0)
                        "{color=#A8E4A0}{i}{size=-3} Tipsy, she stands up, picks up the bottle of Merlot, and left you on your own at the living room."
                        "{color=#A8E4A0}{i}{size=-3} You returned to your room."
                        "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                        jump endpart1
                    elif nicgetredwine == True and winecabernet == True:
                        scene black with Fade(2.0, 1.0, 2.0)
                        "{color=#A8E4A0}{i}{size=-3} Tipsy, she walked upstairs to her room, and left you on your own with the Cabernet bottle at the living room."
                        scene black with fade
                        "{color=#A8E4A0}{i}{size=-3} You returned to your room."
                        "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                        jump endpart1

                "Continue watching":
                    $ niclovebonusfactor += 4
                    jump pycontinuewatching

        label pynowinedrinking:
                scene 57000apy with dissolve
                "{color=#A8E4A0}{i}{size=-3} After what it seemed at eternity later, the movie finally winds down, as the credits roll across the screen"
                scene 57pyj5 with dissolve
                m "I guess that's it..."
                scene 57pyj2 with dissolve
                e "Do you want me to help you get to the bedroom?"
                scene 57pyj5 with dissolve
                m "I'm not a granny. I'll go to sleep..."
                scene 57pyj2 with dissolve
                e "Oh ok... Goodnight..."
                scene black with Fade(2.0, 1.0, 2.0)
                "{color=#A8E4A0}{i}{size=-3} She walked upstairs to her room, and left you on your own at the living room."
                $ nicnormalwinescene = True
                jump endpart1

        label pycontinuewatching:
            scene 56000drink with dissolve
            "{color=#A8E4A0}{i}{size=-3} After what it seemed at eternity later, the movie finally winds down, as the credits roll across the screen."
            scene 56000drink2 with dissolve
            m "I guess that's it... *Hip*"
            e "Shit, you're drunk. Are you sure you can walk upstairs on your own?"
            scene 56000drink with dissolve
            m "I'm not a granny. I'll go to sleep... You do whatever you want... *Hip*"
            e "Oh, mind your words."
            if nicgetredwine == True and winemerlot == True:
                "{color=#A8E4A0}{i}{size=-3} Tipsy, she stands up, picks up the bottle of Merlot, and left you on your own at the living room."
                scene black with fade
                "{color=#A8E4A0}{i}{size=-3} You returned to your room."
                "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                jump endpart1
            elif nicgetredwine == True and winecabernet == True:
                "{color=#A8E4A0}{i}{size=-3} Tipsy, she walked upstairs to her room, and left you on your own with the Cabernet bottle at the living room."
                scene black with fade
                "{color=#A8E4A0}{i}{size=-3} You returned to your room."
                "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                jump endpart1





label finalep5:
    "{color=#A8E4A0}{i}{size=-3} After a while of watching TV, you didn't hear any more activity from [woman_name]'s room."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Sounds like she fell asleep."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Alcohol can do miracles on women, that's facts."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Perhaps I should go and check up on her... Hehe."
    scene 0001 with dissolve

    if easymode:
        menu:

            "{color=#FFD1DF}{i}*Open the door*{/i}{/color} {size=-8} (Req. 6 Lust Points or 6 Domination Points){/size}\n{color=#3d85c6} Dom Path" if niclustep5 > 9 or nicdomep5 > 9:
                if not easymode:
                            $ achValid5 += 1
                            $ achievement.grant("Achiev24")
                            $ achievement.sync()
                            if not persistent.achievement24:
                                                         show Achiev24 at achievment with easeintop:
                                                                    zoom 0.5
                                                                    rotate_animation

                                                         "You have received the achievement!{p}{b}\"Score 6 points in Episode 5\"{/b}"
                                                         "Number of achievements earned in this chapter [achValid5]/8"
                                                         hide Achiev24
                                                         $ persistent.achievement24 = True
                jump opendoorfinal

            "{color=#FFD1DF}{i}*Try to break the lock*{/i}{/color} {color=#00ff00}10\%\ chance{/color}":
                $ dooropenep5final = renpy.random.randint(1, 100)
                if dooropenep5final >= 90:
                    show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
                    with Pause(2)
                    hide text with dissolve
                    jump opendoorfinal
                else:
                    show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
                    with Pause(2)
                    hide text with dissolve
                    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn... I can't open this door."
                    "{color=#A8E4A0}{i}{size=-3} Without looking back, you returned to your room."
                    "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                    jump endpart1

            "She is tired and drunk. Let her rest.\n{color=#3d85c6} Love Path":
                    $ niclovebonusfactor += 5
                    "{color=#A8E4A0}{i}{size=-3} What a lovely [player_role]..."
                    "{color=#A8E4A0}{i}{size=-3} Without looking back, you returned to your room."
                    "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                    jump endpart1

    else:
        menu:

            "{color=#FFD1DF}{i}*Open the door*{/i}{/color} {size=-8} (Req. 6 Lust Points or 6 Domination Points){/size}" if niclustep5 > 9 or nicdomep5 > 9:
                if not easymode:
                            $ achValid5 += 1
                            $ achievement.grant("Achiev24")
                            $ achievement.sync()
                            if not persistent.achievement24:
                                                         show Achiev24 at achievment with easeintop:
                                                                    zoom 0.5
                                                                    rotate_animation

                                                         "You have received the achievement!{p}{b}\"Score 6 points in Episode 5\"{/b}"
                                                         "Number of achievements earned in this chapter [achValid5]/8"
                                                         hide Achiev24
                                                         $ persistent.achievement24 = True
                jump opendoorfinal

            "{color=#FFD1DF}{i}*Try to break the lock*{/i}{/color} {color=#00ff00}10\%\ chance{/color}":
                $ dooropenep5final = renpy.random.randint(1, 100)
                if dooropenep5final >= 90:
                    show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
                    with Pause(2)
                    hide text with dissolve
                    jump opendoorfinal
                else:
                    show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
                    with Pause(2)
                    hide text with dissolve
                    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn... I can't open this door."
                    "{color=#A8E4A0}{i}{size=-3} Without looking back, you returned to your room."
                    "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                    jump endpart1

            "She is tired and drunk. Let her rest.":
                    $ niclovebonusfactor += 5
                    "{color=#A8E4A0}{i}{size=-3} What a lovely [player_role]..."
                    "{color=#A8E4A0}{i}{size=-3} Without looking back, you returned to your room."
                    "{color=#A8E4A0}{i}{size=-3} Once there, you threw yourself onto the bed, and finally had what you’ve been craving for: A good nap."
                    jump endpart1


label opendoorfinal:
    $ niclovebonusfactor -= 10
    stop music fadeout 1.0
    scene 56000a with dissolve
    "{color=#A8E4A0}{i}{size=-3} You open the door quietly, stepping inside. She’s lying on her back, completely passed out."
    scene 56000b with dissolve
    "{color=#A8E4A0}{i}{size=-3} There was an empty bottle of Merlot on the bedside table."
    scene 56000c with dissolve
    "{color=#A8E4A0}{i}{size=-3} She’s sprawled out under a blanket, her chest rising and falling as she sleeps, her mouth slightly open, lips parted just enough to tease."
    scene 56000d with dissolve
    "{color=#A8E4A0}{i}{size=-3} You pull the blanket away, exposing her naked skin."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What a fucking sight..."
    scene 56001 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her legs are slightly parted, and it’s all the invitation you need."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Mmm… I feel like I arrived just in time..."
    scene 56003 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Crawling onto the bed, you watch her body shift slightly under your weight, but she stays asleep: drunk and vulnerable beneath you."
    scene 560051 with dissolve
    pause
    scene 560052 with dissolve
    play sound "music/kiss1.mp3"
    "{color=#ffa500}{i}*the sound of a kiss*{/i}{/color}"
    scene 560053 with dissolve
    pause
    scene 560054 with dissolve
    play sound "music/kiss2.mp3"
    "{color=#ffa500}{i}*the sound of a kiss*{/i}{/color}"
    scene 560055 with dissolve
    pause
    scene 560056 with dissolve
    play sound "music/kiss3.mp3"
    "{color=#ffa500}{i}*the sound of a kiss*{/i}{/color}"
    "{color=#A8E4A0}{i}{size=-3} She stirs, her eyes opening briefly, but she’s too out of it to register what’s happening."
    scene 560057 with dissolve
    m "[player_name]... what...{p}what are you..."
    scene 56006 with dissolve
    e "Sh... Sh... Stay still, kitty. I’m gonna take care of you."
    scene 56006a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Slowly, you take her panties off, sliding down her legs, at the same time your hands tease her skin as they move all the way down."
    scene 56006b with dissolve
    pause
    scene 56007 with dissolve
    m "No...{p}please... s-stop..."
    scene 56008 with dissolve
    pause
    scene 560081 with dissolve
    pause
    scene 560082 with dissolve
    show nicep5last1 with dissolve
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3} Without waiting for more of a response, you push your fat cock inside her, her body instinctively responding to the penetration even though she’s still barely conscious."
    scene nicep5last1_frame with dissolve
    "{color=#A8E4A0}{i}{size=-3} She lets out a soft, barely audible gasp, her legs twitching slightly as you fill her with your cock, pushing it in. "
    show nicep5last2 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You lean down, kissing her gently on the lips."
    scene 56009aframe with dissolve
    m "P-Please... don’t..."
    show nicep5last3 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Interrupting her speech, you kiss her again, this time more passionately and sloppy"
    pause
    "{color=#A8E4A0}{i}{size=-3} Her body responds despite her shame, her hips shifting slightly in time with your movements. You can feel her warm tight pussy walls tightening around your eager cock, drawing you deeper, sucking you in."
label camnicep5last3:
    hide nicep5last3cam2
    show nicep5last3
    pause
    menu (screen="rightlowchoice"):
        "Change view":
            jump cam2nicep5last3
        "Continue":
            hide nicep5last3
            jump camnicep5last4

label cam2nicep5last3:
    hide nicep5last3
    show nicep5last3cam2
    pause
    menu (screen="rightlowchoice"):
        "Change view":
            jump camnicep5last3
        "Continue":
            hide nicep5last3cam2
            jump camnicep5last4

label camnicep5last4:
    show nicep5last4 with dissolve
    $ renpy.pause(1, hard=True)
    e "Mmm, enough... Steady, now... Relax."
    m "Please... stop... {p}I can’t... I hate you for this..."
    e "Hate it? You’re fucking soaking! You’re just fighting hard to not admit it."
    scene finaldomi01 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi02 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi03 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi04 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi05 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi06 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi07 with dissolve
    $ renpy.pause(0.1, hard=True)
    scene finaldomi08 with dissolve
    $ renpy.pause(0.25, hard=True)
    show nicep5last5 with dissolve
    $ renpy.pause(1, hard=True)
    e "Her wet, tight pussy grips you harder with every thrust, pulling you deeper into her, and you know you’ve got her right where you want her."
    $ renpy.pause(1, hard=True)
    e "That’s right. Fucking take it. You were made for this. You’re nothing but a little cumdump for me."
    m "N-No... stop... please..."
    e "Don’t worry. I’ll stop after leaving a good bellyful of cum."
    "{color=#A8E4A0}{i}{size=-3} The sound of your hips slapping against hers are the only thing to be heard, her sobs mixing with the wet sounds of your cock stretching her tight walls."
    e "You feel that? I’m gonna fucking cum inside you, and there’s nothing you can do about it. You’re mine now."
    m "No... please...{p}Don’t...{p}I can’t... I..."
    scene ep5lastcmfinal00 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Ignoring her, you thrust deeper, your cock throbbing inside her as you finally cum."
    show nicep5last6
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3} With a final, brutal thrust, you bury yourself deep inside her, spilling your load."
    scene v2ep5lastcmfinal37 with dissolve
    show nicep5last7
    "{color=#A8E4A0}{i}{size=-3} The hot rush of cum fills her, and her body shakes as you keep pounding into her..."
    "{color=#A8E4A0}{i}{size=-3} ...pushing your cum as deep as it’ll go."
    "{color=#A8E4A0}{i}{size=-3} [woman_name] lets out a soft, defeated whimper, her body limp beneath you, completely exhausted."
    scene lastsleep49 with dissolve
    e "Hope my cum stains your sheets when you wake up and it had rolled out of your pussy."
    show lastsleep
    "{color=#A8E4A0}{i}{size=-3} She turns her face away, tears still streaming down her cheeks, too ashamed and tired to say anything."
    m "I...{p}I just want to sleep..."
    scene 56013 with dissolve
    e "Yeah? Me too.{p}We’ll sleep together like this... with you full of my cum."
    "{color=#A8E4A0}{i}{size=-3} She doesn’t respond, her breathing slowing as she drifts off again."
    "{color=#A8E4A0}{i}{size=-3} Without saying another word, both of you quickly found kissing the sheets asleep."
    "{color=#A8E4A0}{i}{size=-3} You’ve done it. You’ve fucked her to sleep. And the only thing you could do is for her to remember it when she wakes up."
    $ maxmccumep7 += 1
    $ nicdomrouteep5 = True
    $ renpy.end_replay()
    scene black with Fade(2.0, 1.0, 2.0)
    if not easymode:
            $ achValid5 += 1
            $ achievement.grant("Achiev22")
            $ achievement.sync()
            if not persistent.achievement22:
                                         show Achiev22 at achievment with easeintop:
                                                    zoom 0.5
                                                    rotate_animation

                                         "You have received the achievement!{p}{b}\"YOU DID IT, BRO. YOU DID IT!\"{/b}"
                                         "Number of achievements earned in this chapter [achValid5]/8"
                                         hide Achiev22
                                         $ persistent.achievement22 = True
    jump endpart1



label runrbr:
    hide screen hint
    hide text
    $ shopclicked = True
    y "HELP" with vpunch
    y "THIEF!!" with vpunch
    e "What's going on there?"
    $ timeout_label = "shopep5storelist"
    $ timeout = 2
    menu:

        "{color=#FFD1DF}{i}*Check what's happening":
            scene robber1 with dissolve
            pause
            jump robberep5
        "{color=#FFD1DF}{i}*Stay in the store":
            jump shopep5storelist


label robberep5:
    scene robber2 with dissolve
    y "THAT GUY JUST ROBBED ME!"
    $ timeout_label = "norobber"
    $ timeout = 2
    menu:

        "{color=#FFD1DF}{i}*Start chasing the thief*{/i}{/color} {size=-8}(Req.{b}SPEED{/b}){/size}" if speedguy > 0 :
            jump chasingtherobber
        "He's already too far away...":
            jump norobber

label norobber:
        scene robber2 with dissolve
        e "I'm sorry, but he's too far away..."
        scene robber3 with dissolve
        y "Oh..{p}SCREW YOU!"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ugh... old hag."
        e "Time to go back."
        jump shopep5storelist

label chasingtherobber:
            scene robber4 with dissolve
            scene robber5 with dissolve
            scene robber4a with dissolve
            scene robber5a with dissolve
            scene robber6 with dissolve
            scene robber7 with dissolve
            scene robber12 with dissolve
            "{color=#A8E4A0}{i}{size=-3} The thief, seeing that you were catching up to him, threw the stolen purse on the ground."
            scene robber12a with dissolve
            scene robber12b with dissolve
            n "Fuck you!"
            scene robber13 with dissolve
            jump walletchoice

label walletchoice:
            show screen hint("I don't think anyone sees me...")

            if easymode:
                menu:
                    "{color=#FFD1DF}{i}*Pick up the purse from the ground and take some money from it* {color=#00ff00} +123${/color}\n{color=#3d85c6} Dad -2":
                         hide screen hint
                         scene black with Fade(2.0, 1.0, 2.0)
                         $ money += 123
                         show text "{color=#00ff00}{size=+15}+1 2 3 ${/color}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         scene black with Fade(2.0, 1.0, 2.0)
                         "{color=#A8E4A0}{i}{size=-3} After several minutes, when everyone had already dispersed, you returned to the store."
                         $ dadfriend -= 2
                         $ walletyours += 1
                         jump shopep5storelist

                    "{color=#FFD1DF}{i}*Give it back to the old woman*\n{color=#3d85c6} Dad +2":
                         hide screen hint
                         scene black with Fade(2.0, 1.0, 2.0)
                         pause 1
                         scene robber10 with dissolve
                         e "Excuse me, I believe this is yours."
                         scene robber11 with dissolve
                         y "Oh thank you, [player_name]!{p}Here, this is for you for your help."
                         e "Ah... You're welcome."
                         scene black with Fade(2.0, 1.0, 2.0)
                         $ money += 40
                         show text "{color=#00ff00}{size=+15}+4 0 ${/color}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} How did she know my name...?"
                         $ dadfriend += 2
                         $ walletyours -= 1
                         jump shopep5storelist

            else:
                menu:
                    "{color=#FFD1DF}{i}*Pick up the purse from the ground and take some money from it* {color=#00ff00} +123${/color} ":
                         hide screen hint
                         scene black with Fade(2.0, 1.0, 2.0)
                         $ money += 123
                         show text "{color=#00ff00}{size=+15}+1 2 3 ${/color}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         scene black with Fade(2.0, 1.0, 2.0)
                         "{color=#A8E4A0}{i}{size=-3} After several minutes, when everyone had already dispersed, you returned to the store."
                         $ dadfriend -= 2
                         $ walletyours += 1
                         jump shopep5storelist

                    "{color=#FFD1DF}{i}*Give it back to the old woman*":
                         hide screen hint
                         scene black with Fade(2.0, 1.0, 2.0)
                         pause 1
                         scene robber10 with dissolve
                         e "Excuse me, I believe this is yours."
                         scene robber11 with dissolve
                         y "Oh thank you, [player_name]!{p}Here, this is for you for your help."
                         e "Ah... You're welcome."
                         scene black with Fade(2.0, 1.0, 2.0)
                         $ money += 40
                         show text "{color=#00ff00}{size=+15}+4 0 ${/color}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}" with dissolve
                         with Pause(2)
                         hide text with dissolve
                         e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} How did she know my name...?"
                         $ dadfriend += 2
                         $ walletyours -= 1
                         jump shopep5storelist

label endpart1:
    stop music fadeout 1.0
    play music "music/Redem.mp3"
    scene black with Fade(2.0, 1.0, 2.0)
    show text "Location unknown" with Fade(2.0, 1.0, 2.0)
    $ renpy.pause(2, hard=True)
    scene police01 with dissolve
    pause
    play sound "music/message.mp3"
    scene police02
    pause
    scene police03 with dissolve
    pause
    play sound "music/mouse.mp3"
    scene police04
    pause
    play sound "music/mouse.mp3"
    scene police05 with dissolve
    pause
    scene police06 with dissolve
    pause
    scene police07 with dissolve
    pause
    scene police08 with dissolve
    pause
    scene police09
    play sound "music/mouse.mp3"
    pause
    play sound "music/keyboard.mp3"
    scene police10 with dissolve
    pause
    play sound "music/scary.mp3"
    scene police11 with dissolve
    scene black with Fade(4.0, 1.0, 2.0)

    show text "{size=+5}End of Chapter 5{/size}" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)

    jump statsep5

label statsep5:

     $ achVall = achValid + achValid2 + achValid3 + achValid4 + achValid5
     if not easymode:
         "So far you have achieved {b}[achVall]{/b} out of 24 available achievements!"
         if tomscstat == 1 and not z3kr3t:
            "...and 1 out of 2 s3cr3t achievements...:-)"
         elif z3kr3t and tomscstat == 0:
            "...and 1 out of 2 s3cr3t achievements...:-)"
         elif z3kr3t and tomscstat == 1:
            "...and 2 out of 2 s3cr3t achievements...:-)"
     else:
         "You did not receive any achievements because you are playing in easy mode."
     if itguy >= 1 and speedguy >= 1:
        "Learned Perks: 3/3{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
     elif itguy >= 1 and speedguy == 0:
        "Learned Perks: 2/3{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}"
     elif itguy == 0 and speedguy >= 1:
        "Learned Perks: 2/3{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
     else:
        "Learned Perks: 1/3{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}"
     $ renpy.pause(2, hard=True)
     jump episode6










