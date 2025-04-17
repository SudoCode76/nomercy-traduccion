default domep6 = 4
default lustep6 = 4
default easyfight = 0
default ep6alcohol = 0
default mohito1 = False
default mohito2 = False
default tequila1 = False
default tequila2 = False
default slaptoilet = 0
default achValid6 = 0
default slapach = False
default dancepoints = 0
default dancepoints2 = 0
default dancepoints3 = 0
default fail_dance = 0
default fail_dance2 = 0
default textcar_index = 0
default ep6car = False
default ringplay = 0
default speedsaver = False
default endingnothing = False
default endingdomino = False
default endinglove = False
default tommygethismm = False
default mcdrugsexmtom = False
default sleepwithout = False
default askaboutntr = False
default ntrep6 = False
default tommyalreadycall = False
default visitpolice = False
default ringbellstat = 0
default doorknockstat = 0
default dadalreadycall = False



image movie1 = Movie(channel="movie_dp", play = "images/Ep6/movie1.webm")
image movie2 = Movie(channel="movie_dp", play = "images/Ep6/movie2.webm")
image movie3 = Movie(channel="movie_dp", play = "images/Ep6/movie3.webm")
image movie4 = Movie(channel="movie_dp", play = "images/Ep6/movie4.webm")
image movie5 = Movie(channel="movie_dp", play = "images/Ep6/movie5.webm")
image toiletep6 = Movie(channel="movie_dp", play = "images/Ep6/toiletep6.webm")
image toiletblowcam1 = Movie(channel="movie_dp", play = "images/Ep6/toiletblowcam1.webm")
image toiletblowcam2 = Movie(channel="movie_dp", play = "images/Ep6/toiletblowcam2.webm")
image toiletblowcam3 = Movie(channel="movie_dp", play = "images/Ep6/toiletblowcam3.webm")
image toiletblowcam4 = Movie(channel="movie_dp", play = "images/Ep6/toiletblowcam4.webm")
image niccarlick = Movie(channel="movie_dp", play = "images/Ep6/niccarlick.webm")
image niccarcl1 = Movie(channel="movie_dp", play = "images/Ep6/niccarcl1.webm")
image niccarbj1 = Movie(channel="movie_dp", play = "images/Ep6/niccarbj1.webm")
image niccarbj2 = Movie(channel="movie_dp", play = "images/Ep6/niccarbj2.webm")
image cmmtom = Movie(channel="movie_dp", play = "images/Ep6/cmmtom.webm")
image mtomdrgsex = Movie(channel="movie_dp", play = "images/Ep6/mtomdrgsex.webm")
image antep6fc = Movie(channel="movie_dp", play = "images/Ep6/antep6fc.webm")
image antep6sck = Movie(channel="movie_dp", play = "images/Ep6/antep6sck.webm")
image clubdancing = Movie(channel="movie_dp", play = "images/Ep6/clubdancing.webm")
image slapep6 = Movie(channel="movie_dp", play = "images/Ep6/slapep6.webm")
image befcmtoil = Movie(channel="movie_dp", play = "images/Ep6/befcmtoil.webm")
image nicdance1 = Movie(channel="movie_dp", play = "images/Ep6/nicdance1.webm")
image nicdance2 = Movie(channel="movie_dp", play = "images/Ep6/nicdance2.webm")
image mtomtomsck1 = Movie(channel="movie_dp", play = "images/Ep6/mtomtomsck1.webm")
image mtomtomsck2 = Movie(channel="movie_dp", play = "images/Ep6/mtomtomsck2.webm")
image mtomtomsck3 = Movie(channel="movie_dp", play = "images/Ep6/mtomtomsck3.webm")
image nicfckinside = Movie(channel="movie_dp", play = "images/Ep6/nicfckinside.webm")
image nicfckinside2 = Movie(channel="movie_dp", play = "images/Ep6/nicfckinside2.webm")
image cmintoil = Movie(channel="movie_dp", play = "images/Ep6/cmintoil.webm", loop=False, image="cmins54")
image antfkstart = Movie(channel="movie_dp", play = "images/Ep6/antfkstart.webm", loop=False, image="antfkstart_frame")
image cmtoiletback = Movie(channel="movie_dp", play = "images/Ep6/cmtoiletback.webm", loop=False, image="cmonb_frame")
image cminsep6 = Movie(channel="movie_dp", play = "images/Ep6/cminsep6.webm", loop=False, image="cmins_frame")
image ep6morning1 = Movie(channel="movie_dp", play = "images/Ep6/ep6morning1.webm", loop=False, image="eyes_frame")
image ep6morning2 = Movie(channel="movie_dp", play = "images/Ep6/ep6morning2.webm", loop=False, image="60000")

init python:
    import random

    if not hasattr(store, "_fight_menu_position"):
        store._fight_menu_position = {'x': 0.5, 'y': 0.5}

    if not hasattr(store, "_dance_menu_position"):
        store._dance_menu_position = {'x': 0.5, 'y': 0.5}

    def set_fight_menu_position():
        store._fight_menu_position = {
            'x': random.random(),
            'y': random.random() * 0.9
        }

    def set_dance_menu_position():
        store._dance_menu_position = {
            'x': random.random(),
            'y': random.random() * 0.9
        }

transform delicate_movement:
    anchor (0.5, 0.5)
    pos (0.5, 0.5)

    ease 6.0 pos (0.52, 0.5)
    ease 6.0 pos (0.48, 0.5)
    ease 6.0 pos (0.50, 0.5)
    repeat

image my_scene = "Ep6/60000.jpg"

label episode6:
    if easymode:
        show text "Easy Mode points!"
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        pause 1
        $lustep6 += 2
        $domep6 += 2
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        pause 1
        hide text
    scene black with dissolve
    stop music fadeout 1.0
    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 6" at title with dissolve
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    if nicgetredwine == True and winemerlot == True and nicgetsexylingerie == True and persistent.achievement22 == True and nicdomrouteep5 == True:
        show text "Due to your decisions in previous episodes, your [woman_role] feels completely dominated by you." at title with dissolve
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        pause 1
        $ domep6 += 3
        $ lustep6 -= 2
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[domep6].png"
        hide image "images/Stats/Lust[lustep6].png"
        hide text with dissolve
        jump ep6morning1
    elif niclovebonusfactor > 9 and niclovebonusfactor < 20 and nicdomrouteep5 == False:
        show text "Due to your decisions in previous episodes, your [woman_role] feels loved by you." at title with dissolve
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        pause 1
        $ lustep6 += 1
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[domep6].png"
        hide image "images/Stats/Lust[lustep6].png"
        hide text with dissolve
        jump routecheckep6
    elif niclovebonusfactor >= 20 and nicdomrouteep5 == False:
        show text "Due to your decisions in previous episodes, your [woman_role] feels really loved by you." at title with dissolve
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        pause 1
        $ lustep6 += 2
        show image "images/Stats/Dom[domep6].png" at statleft
        show image "images/Stats/Lust[lustep6].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[domep6].png"
        hide image "images/Stats/Lust[lustep6].png"
        hide text with dissolve
        jump routecheckep6

label routecheckep6:
    scene black with dissolve
    if auntep5love == True:
            jump aftermorningep6
    elif nicdomrouteep5 == True:
            jump ep6morning1
    elif nicdomrouteep5 == False:
            jump aftermorningep6

label ep6morning1:
    show ep6morning1
    $ renpy.pause(3, hard=True)
    "{color=#A8E4A0}{i}{size=-3} You open your eyes after a confusing night, although, it might have been more confusing for [woman_name]."
    "{color=#A8E4A0}{i}{size=-3} Your mind is as groggy as your heavy eyelids, which struggle to stay open, while your eyes are fixed on the ceiling."
    scene eyes_frame
    e "Hmphf..."
    show ep6morning2 with dissolve
    $ renpy.pause(7, hard=True)
    play music "music/Morning.wav"
    show my_scene at delicate_movement with dissolve:
        zoom 1.05
    "{color=#A8E4A0}{i}{size=-3} You swallow a bit of saliva, and as you yawn without opening your mouth, you turn your head to find the confirmation you needed: You hadn't hallucinated last night."
    "{color=#A8E4A0}{i}{size=-3} The sight is strange and a bit unsettling. [woman_name] is staring at you expressionlessly, as if she had recently lost her soul."
    e "Hey...{p}Uhm...{p}Good morning?"
    "{color=#A8E4A0}{i}{size=-3} Nothing comes out of her mouth, not even a breath."
    e "What's wrong?{p}All good?"
    "{color=#A8E4A0}{i}{size=-3} She is silent, and perhaps for the first time, you feel a bit of fear as your back chills and your hair stands on end."
    scene 60000 with dissolve
    e "Oh, well..."
    scene 60001 with dissolve
    m "What do you think?"
    scene 60000 with dissolve
    e "Well...{p}you should be... satisfied."
    scene 60002 with dissolve
    "{color=#A8E4A0}{i}{size=-3} It was after you said that when her face shifted, frowning, while stabbing you with her frustrated look, with eyeliner-dried tears that went down her eyes."
    scene 60002a with dissolve
    m "Oh, you think so?"
    scene 60002b with dissolve
    m "Satisfied?"
    scene 60002 with dissolve
    e "I guess so, after all, your moans didn't lie, you enjoyed it as much as I did."
    e "It's not like you stopped me anyway, right?"
    scene 60001 with dissolve
    m "Please, just... Ugh..."
    scene 60000 with dissolve
    e "Seriously, I don't get what's wrong with you.{p}I thought you'd be glad that we finally did it."
    scene 60001 with dissolve
    m "Glad?"
    scene 60002a with dissolve
    m "You crossed the ONLY line you shouldn't have crossed with me."
    scene 60002b with dissolve
    m "This..."
    scene 60002a with dissolve
    m "All of this is just FUCKED. Not right at all!"
    scene 60002 with dissolve
    e "Not right? Ah, come on... We had a blast, didn't we? You were fucking loving it."
    scene 60003 with dissolve
    "{color=#A8E4A0}{i}{size=-3} [woman_name]'s face reddens, as her eyes burned with anger."
    scene 60003a with dissolve
    m "Loving it? I was fucking wasted, [player_name]!"
    m "I didn't know what the hell I was doing!"
    scene 60003 with dissolve
    e "Oh, please. You knew exactly what you were doing. You wanted it. You just can't fucking admit it to yourself because you're too afraid of finally being happy with me."
    scene 60001 with dissolve
    m "No... I didn't... I can't..."
    scene 60000 with dissolve

    if easymode:
        menu (screen="rightchoice"):
            "Well... You did, to me...":
                jump morningtalkq1
            "Perhaps I did it better than my dad has ever did, like in every other aspect aswell.\n{color=#3d85c6} Dad -1":
                $ dadfriend -= 1
                jump morningtalkq1

    else:
        menu (screen="rightchoice"):
            "Well... You did, to me...":
                jump morningtalkq1
            "Perhaps I did it better than my dad has ever did, like in every other aspect aswell.":
                $ dadfriend -= 1
                jump morningtalkq1

label morningtalkq1:
    scene 60004 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her gaze darting to the door. She remembers locking it last night, but now she's not so sure. Her brow furrows in confusion and fear."
    scene 60004a with dissolve
    m "I locked it... I know I did..."
    m "How did you...? I locked the door..."
    scene 60002 with dissolve

    if easymode:
        menu (screen="rightchoice"):
            "Do you think so? To me it was an open invitation from you.":
                jump morningtalkq2
            "Nope. You didn’t. You were basically just asking for me to fuck you.\n{color=#3d85c6} +1 Dom Point":
                                show image "images/Stats/Dom[domep6].png" at statleft
                                show image "images/Stats/Lust[lustep6].png" at statright
                                pause 1
                                $ domep6 += 1
                                show image "images/Stats/Dom[domep6].png" at statleft
                                show image "images/Stats/Lust[lustep6].png" at statright
                                with dissolve
                                pause 3
                                hide image "images/Stats/Dom[domep6].png"
                                hide image "images/Stats/Lust[lustep6].png"
                                jump morningtalkq2
    else:
        menu (screen="rightchoice"):
            "Do you think so? To me it was an open invitation from you.":
                jump morningtalkq2
            "Nope. You didn’t. You were basically just asking for me to fuck you.":
                                show image "images/Stats/Dom[domep6].png" at statleft
                                show image "images/Stats/Lust[lustep6].png" at statright
                                pause 1
                                $ domep6 += 1
                                show image "images/Stats/Dom[domep6].png" at statleft
                                show image "images/Stats/Lust[lustep6].png" at statright
                                with dissolve
                                pause 3
                                hide image "images/Stats/Dom[domep6].png"
                                hide image "images/Stats/Lust[lustep6].png"
                                jump morningtalkq2


label morningtalkq2:
    scene 60002a with dissolve
    m "W-What!? No!"
    scene 60002 with dissolve
    e "So I just walked in, and did what I had to."
    scene 60001 with dissolve
    m "I... I need to think... This is too much..."
    scene 60000 with dissolve

    if easymode:
        menu (screen="rightchoice"):
             "I didn’t want you to feel used...\n{color=#3d85c6} Love points":
                                 $ niclovebonusfactor += 1
                                 jump morningtalklust
             "The only thing you need to do is to quit bitching and date me.\n{color=#3d85c6} Dom points":
                                 jump morningtalkdom
    else:
        menu (screen="rightchoice"):
             "I didn’t want you to feel used...":
                                 $ niclovebonusfactor += 1
                                 jump morningtalklust
             "The only thing you need to do is to quit bitching and date me.":
                                 jump morningtalkdom


label morningtalkdom:
    scene 60003 with dissolve
    "{color=#A8E4A0}{i}{size=-3} [woman_name]'s breath hitches, as she's already annoyed, yet, she felt like the events from last night might have made you trip over your usual 'just threatening' ways, into something worse."
    scene 60005 with dissolve
    pause
    scene 60001 with dissolve
    m "I... I need to think... This is too much... Please, just..."
    scene 60000 with dissolve
    e "Bitch, you sound like a broken record."
    scene 60002a with dissolve
    m "Don't call me that! Ugh. I just... don't want you saying things like that out loud."
    scene 60002 with dissolve
    e "Why's that? You can't handle the truth? If you didn't like it, then why didn't you just leave? Just admit it!"
    scene 60001 with dissolve
    m "No... I didn't... I can't..."
    if easymode:
        menu (screen="rightchoice"):
             "{color=#FFD1DF}{i}*Choke her*{/i}{/color}\n{color=#3d85c6} +2 Dom points, -2 Lust points":
                                 jump grabchin
             "{color=#FFD1DF}{i}*Remain silent*{/i}{/color}\n{color=#3d85c6} +1 Dom Point":
                                 jump silentmornep6
    else:
        menu (screen="rightchoice"):
             "{color=#FFD1DF}{i}*Choke her*{/i}{/color}":
                                 jump grabchin
             "{color=#FFD1DF}{i}*Remain silent*{/i}{/color}":
                                 jump silentmornep6

label silentmornep6:
    scene 60005 with dissolve
    pause
    scene 60001 with dissolve
    m "I need air... Air... I... We’ll talk later."
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    pause 1
    $ domep6 += 1
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[domep6].png"
    hide image "images/Stats/Lust[lustep6].png"
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} She stands up quickly. She looks back at you one last time before walking out of the room, leaving you alone in the bed."
    jump aftermorningep6

label grabchin:
    scene 60006 with vpunch
    "{color=#A8E4A0}{i}{size=-3} You sigh, but quickly put your hand on her neck."
    e "Look at me. I'm getting tired of this cat and mouse bullshit. I want you to finally swallow it."
    scene 60006a with dissolve
    "{color=#A8E4A0}{i}{size=-3} She bites her lip, trying to look away, scared of your tight grip on her chin."
    scene 60006b with dissolve
    m "B-Back off! Ugh!"
    scene 60006e with dissolve
    e "Say it..."
    scene 60006c with dissolve
    m "Say what?!"
    scene 60006a with dissolve
    e "Say that you liked getting fucked by me last night. Come on."
    scene 60006b with dissolve
    m " F-Fuck... Ugh... Alright... I..."
    scene 60006c with dissolve
    e "You what!?"
    scene 60006e with dissolve
    m "...L-Lo... Fuck, I-I can’t, s-sorry, sorry."
    scene 60007 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You release her chin, and she takes a deep breath, her body tense."
    e "Ugh... Whatever."
    scene 60007a with dissolve
    m "I need air... Air... I..."
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    pause 1
    $ domep6 += 2
    $ lustep6 -= 2
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[domep6].png"
    hide image "images/Stats/Lust[lustep6].png"
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} She stands up quickly. She looks back at you one last time before walking out of the room, leaving you alone in the bed."
    jump aftermorningep6

label morningtalklust:
    scene 60002a with dissolve
    m "I don’t care what you’ve got to say...I should just report you to the cops, for fuck’s sake!"
    scene 60002 with dissolve
    e "No! You can’t."
    scene 60002b with dissolve
    m "Oh no? Why?!"
    scene 60002 with dissolve
    e "Because I just... I fucking care about you, alright? I couldn't help myself."
    scene 60005 with dissolve
    "{color=#A8E4A0}{i}{size=-3} [woman_name] looks down."
    scene 60001 with dissolve
    m "You care about me? This is how you show it? By taking advantage of me when I'm drunk off my ass?"
    scene 60005 with dissolve
    e "I know it might sound fucked up-"
    scene 60002b with dissolve
    m "It was fucked up! Are you kidding me?!"
    scene 60002 with dissolve
    e "Okay! Okay... Chill... I just... love you. I can't help how I feel. Just give me a break! Just for once think about you and me..."
    scene 60005 with dissolve
    "{color=#A8E4A0}{i}{size=-3} [woman_name] shakes her head, tears streaming down her face."
    scene 60001 with dissolve
    m "I don't know... I need time to think... I can't just forget what you did..."
    scene 60000 with dissolve
    e "...I guess you gotta do what you gotta do... Just don’t lock me out. You’re the only woman I want..."
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    pause 1
    $ lustep6 += 2
    $ domep6 -= 1
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[domep6].png"
    hide image "images/Stats/Lust[lustep6].png"
    "{color=#A8E4A0}{i}{size=-3} [woman_name] sighs, her gaze distant and lost."
    scene 60001 with dissolve
    m "I... I need to be alone for a bit. I need some air."
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} She stands up quickly. She looks back at you one last time before walking out of the room, leaving you alone in the bed."
    jump aftermorningep6

label aftermorningep6:
    scene 65000 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Okay, what should I do today..."
    scene 65000b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It would be good to learn more about Lopez... but no one here wants to talk."
    scene 65000 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Actually, there's an old policeman living in the neighborhood. If Lopez was some shady character, he might know something or be able to check."
    scene 65000a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I could also use some money, maybe I'll take my [woman_role] out tonight. If I rent a nice car, she'd definitely like it... and maybe... hehe."
    if shoppackage == True:
        scene 65000 with dissolve
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I have some drugs left, I need to sell them to someone."
    jump evecameep6


label evecameep6:
    play sound "music/ring.mp3"
    "{color=#A8E4A0}{i}{size=-3} Ding dong..."
    scene 65001 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hm? Who can it be now?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I don’t think [woman_name] ordered anything."
    scene 65002 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Swiftly, you hurried up to the door. You leaned, sticking your right eye onto the peephole, close enough to focus and see what was in front of you behind your very door."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Eve? What is she doing here?"
    "{color=#A8E4A0}{i}{size=-3} You lowered your vision, and peeked her chest, scanning it fully, as you melted watching her melons."
    scene 65002a with dissolve
    a "Hey! Who is it?! It’s me, Eve!"
    scene black with Fade(2.0, 1.0, 1.0)
    play sound "music/dooropen.mp3"
    e "Come on in!"
    if auntep5angry == True:
        a "Oh... It's you... I thought you were at university.{p}Tell [woman_name] to call me."
        e "Uhm... okay..."
        jump ep6choosepath
    e "You want to talk with [woman_name]? Sit with me, she will probably come down soon."
    scene ep6anttalk8 with dissolve
    stop music fadeout 1.0
    play music "music/ctrls.wav"
    a "Hey... How is it?"
    scene ep6anttalk9 with dissolve
    e "Chillin’, chillin’..."
    scene ep6anttalk8 with dissolve
    a "So, from what I’ve heard your managing things now around your house..."
    scene ep6anttalk7 with dissolve
    e "Well I’ve been doing so for a while, now... You know, even before from when we last met."
    scene ep6anttalk6 with dissolve
    a "I know, I mean, likeee... Turning into the “man of the house”."
    scene ep6anttalk7 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She bit her lip as she finished that sentence."
    e "That’s one way of seeing it... I think I am, yeah."
    e "Well, I'll go get your sister downstairs... It seemed like she didn't even care about you coming to visit her. I should teach her some respect."
    scene ep6anttalk8 with dissolve
    a "Damn! You’ve gotten quite bossy, young man!"
    scene ep6anttalk7 with dissolve
    e "Hey, I’m a man of my word. When I said I run the house, I really meant it."
label evereplayep6:
    scene 65011 with dissolve
    a "Stay..."
    "{color=#A8E4A0}{i}{size=-3} Your [nicosister_role] hand suddenly brushed against your hot and throbbing bulge, as she smirked."
    scene anttalkgrab10 with dissolve
    a "Mngh... Looks like you really are the man of the house now, aren’t you? Feeling quite solid there."
    scene 65012 with dissolve
    e "You know it. Always ready for action..."
    scene anttalkgrab12 with dissolve
    a "But you know, like, being the man of the house doesn’t mean you have to limit yourself to just one pussy, does it?"
    scene 65012 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You chuckled, playing along with her teasing."
    e "Hey, I’m an equal opportunity ass-banger."
    scene 65012a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Just as you were about to say more, you heard footsteps coming down the stairs. Quickly, you both pulled your hands away from each other, trying to look as casual as possible."
    scene 65016 with dissolve
    m "Hey, what’s going on down here?"
    scene 65017 with dissolve
    a "Oh, hey [woman_name]! Just catching up with your... man of the house."
    scene 65018 with dissolve
    "{color=#A8E4A0}{i}{size=-3} [woman_name] smiled awkwardly, and walked over to the couch, greeting your [nicosister_role] warmly."
    scene 65019 with dissolve
    m "It’s so good to see you! Can I get you some coffee?"
    scene 65019a with dissolve
    a "That would be lovely, thank you."
    scene 65016 with dissolve
    "{color=#A8E4A0}{i}{size=-3} [woman_name] headed to the kitchen counter, only to find that there was no coffee left."
    m "Oh, shoot. Looks like we’re out. Let me check the attic; I think we might have some stored up there."
    scene ep6anttalk9 with dissolve
    "{color=#A8E4A0}{i}{size=-3} As soon as she left the room, you and your [nicosister_role] exchanged a glance and burst into nervous laughter."
    scene ep6anttalk8 with dissolve
    a "That was close!"
    scene 65013 with vpunch
    "{color=#A8E4A0}{i}{size=-3} Before you could say anything, your [nicosister_role] quickly straddled you, her lips pressing against yours in a hungry, wet kiss."
    scene 65014 with dissolve
    e "It would be nice if those lips were on something else now..."
    scene 65014a with dissolve
    a "How about a risky quickie? I can feel you’re already hard for me."
    scene 65014 with dissolve
    e "Huh? What is it with you?! I know you, you’re pretty loud."
    scene 65014b with dissolve
    a "Chill... I’ll try my best to keep my mouth shut."
    scene 65014 with dissolve
    e "I can make your mouth shut with something big."
    scene 65014a with dissolve
    a "I want you to fuck me from behind, hard and f-fast."
    scene 65014 with dissolve
    e "I have a feeling you came over for me to fuck your guts."
    scene 65014b with dissolve
    a "You wouldn’t be wrong... Mngh..."
    menu:

        "{color=#FFD1DF}{i}*Fuck her from behind*":
            jump ep6antsx

        "{color=#FFD1DF}{i}*Just grab her head and make her suck your dick*":
            jump ep6antscks

label ep6antscks:
    scene 65014 with dissolve
    e "Hm... I’m feeling like getting blew."
    scene 65014b with dissolve
    a "Mngh... Lucky stud, I’m feeling like sucking some young dick..."
    scene 65015a with dissolve
    e "It’s your lucky day, then... Get to sucking!"
    scene 65015b with dissolve
    "{color=#A8E4A0}{i}{size=-3} You guided her to sit beside you on the couch, your hand gently but firmly grasping the back of her head."
    scene 65015c with dissolve
    "{color=#A8E4A0}{i}{size=-3} You undid your pants, freeing your hard, throbbing dick, and guided her head down."
    scene antsckstart with dissolve
    e "Open wide, [nicosister_role]... Show me what that slutty cougar mouth can do."
    show antep6sck with dissolve
    "{color=#A8E4A0}{i}{size=-3} She complied, her lips parting as she took you into her warm, wet slutty mouth."
    "{color=#A8E4A0}{i}{size=-3} You could feel her tongue swirling around your shaft while she swallowed your girth, her saliva coating you, making you slick and ready. "
    e "Mngh... That’s right... Good pace too..."
    "{color=#A8E4A0}{i}{size=-3} She bobbed her head up and down, her lips tight around you, her cheeks hollowing out as she sucked you eagerly."
    "{color=#A8E4A0}{i}{size=-3} Her saliva dripped down your shaft, coating your balls every time she lifted her bobbing head up."
    e "Fuck, yeah... Just like that. You’re such a good little cock sucker, aren’t you?"
    a "Mngh... Mff!"
    e "Yeah yeah... Can’t talk with a dick in your mouth..."
    a "Mmmph... Mmmph..."
    "{color=#A8E4A0}{i}{size=-3} Her moans were muffled, her eyes watering as she took your dick deeper, her saliva dripping down her chin, making a sloppy mess on your balls."
    e "Fuck, I’m gonna nut... Fuhhhck... "
    a "Mppgh!"
    e "You’re gonna swallow every last drop, understand?"
    "{color=#A8E4A0}{i}{size=-3} She nodded as best she could, her mouth still stuffed full of your dick."
    scene antsckend with vpunch
    "{color=#A8E4A0}{i}{size=-3} You could feel your orgasm hitting, your body tensing and your balls lifting as you came inside of her mouth, your hot cum shooting into her facial hole, coating her tongue, her throat."
    scene antsckend1 with vpunch
    $ maxmccumep7 += 1
    a "Oghhh!"
    scene antsckend2 with vpunch
    e "That’s riiiight... Good girl..."
    play sound "music/gulp.mp3"
    "{color=#A8E4A0}{i}{size=-3} She swallowed eagerly, her throat working as she took every last drop."
    scene 65015after with dissolve
    "{color=#A8E4A0}{i}{size=-3} You pulled out, your dick still glistening with her saliva, a satisfied smile on her face. "
    scene 65015after2 with dissolve
    scene 65015after3 with dissolve
    play sound "music/gulp.mp3"
    pause
    scene 65015after4 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She licked her lips, swallowed the last of your cum, her eyes never leaving yours."
    a "Mmm... That was... surprisingly sweet..."
    e "You’re welcome, hag."
    $ renpy.end_replay()
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} You both quickly composed yourselves, adjusting your clothes just as [woman_name] walked back into the room."
    m "Found some beans! I’ll be right back with the coffee."
    e "That’s good for you two, but I’m gonna bounce back to my room... You girls have fun together."
    "{color=#A8E4A0}{i}{size=-3} You made your way up to your room, as you gazed at your blushing and slightly disheveled Eve, winking at her."
    jump ep6choosepath

label ep6antsx:
    scene 65020 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She quickly took off her skirt, exposing her glistening, wet pussy."
    "{color=#A8E4A0}{i}{size=-3} You took a moment to admire her tight, pink entrance before pressing your thick, hard dick into her."
    show antfkstart with dissolve
    "{color=#A8E4A0}{i}{size=-3} You started slow, feeling her tightness envelop you, her wetness coating your shaft. You could feel her pussy pulsing, eager for more."
    scene antfkstart_frame with dissolve
    a "Mngh!"
    show antep6fc
    e "Hey! Shut it, hoe"
    a "O-Oh... Okay..."
    "{color=#A8E4A0}{i}{size=-3} You picked up the pace, your hips moving faster and harder, your balls slapping against her clit with each thrust, making it hard for her not to burst into tears of pleasure and loud moans."
    "{color=#A8E4A0}{i}{size=-3} Her moans were muffled, but you could feel her body responding to yours, her back arching, her ass pressing back against you."
    a "Fuck, yes! Just like that! Fuck m-!"
    e "I told you to SHUT IT."
    a "Mngh... S-Sor-RY!"
    "{color=#A8E4A0}{i}{size=-3} Your grip on her shirt tightening as you pounded into her, as the sound of your balls slapping her thighs echoed."
    "{color=#A8E4A0}{i}{size=-3} You could feel her pussy clenching around you, her body tensing as her orgasm hit."
    a "Ohhh f-fuck!"
    scene v2aunt061 with vpunch
    e "Finally, with a hard powerful thrust, you came deep up her retracted womb, feeling how it shoot webs into her tight cunt"
    $ maxmccumep7 += 1
    scene v2aunt062 with vpunch
    e "AAAgh..."
    scene v2aunt063 with vpunch
    a "Fuck, yes..."
    scene 65020aftercm with dissolve
    a "That was GOOD..."
    $ renpy.end_replay()
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} You both quickly composed yourselves, adjusting your clothes just as [woman_name] walked back into the room."
    m "Found some beans! I’ll be right back with the coffee."
    e "That’s good for you two, but I’m gonna bounce back to my room... You girls have fun together."
    "{color=#A8E4A0}{i}{size=-3} You made your way up to your room, as you gazed at your blushing and slightly disheveled Eve, winking at her."
    jump ep6choosepath


label ep6choosepath:

    if askaboutntr == False:
        $ askaboutntr = True
        "There may be a scene with NTR (but not involving the main character) later in the game. Do you want it not to happen?"
        menu:
                "NTR is good":
                     $ ntrep6 = True

                "No no... bitches are mine":
                     $ ntrep6 = False

label roomsbxhub:
    scene 61111a with dissolve
    show text "{font=LilitaOne.ttf}{color=#e0d71d}MONEY: [money]${/color}{/font}" at moneystat with dissolve
    menu:
            "{color=#FFD1DF}{i}*Call Tommy* {/i}{/color}" if tommyalreadycall == False:
                    hide text with dissolve
                    jump calltommyep6

            "{color=#FFD1DF}{i}*Call Dad* {/i}{/color}" if dadalreadycall == False:
                    hide text with dissolve
                    jump calldadep6

            "{color=#FFD1DF}{i}*Rent a car*{size=-8}(Req. 50$){/size}" if money > 49 and ep6car == False:
                     hide text with dissolve
                     jump rentacarep6

            "{color=#FFD1DF}{i}*Visit police officer*" if visitpolice == False:
                     hide text with dissolve
                     scene black with fade
                     jump visitpoliceep6

            "{color=#FFD1DF}{i}*Invite Nicole on a date tonight* {size=-8}(Req. Car and 50$){/size}"  if ep6car == True and money > 49:
                hide text with dissolve
                jump eveningep6talkafterfck

            "{color=#FFD1DF}{i}*Go to sleep*":
                jump sleependepisode


label calldadep6:
    if walletyours <= 0:
            scene 61111 with dissolve
            play sound "music/phonecall.mp3"
            pause 3
            stop sound
            scene 61111b with dissolve
            e "Hey, dad!"
            scene 61111 with dissolve
            d "Hey, son. How's it going?"
            if easymode:
                menu:
                    "Chat normally\n {color=#3d85c6} Dad +1":
                                scene 61111b with dissolve
                                "{color=#A8E4A0}{i}{size=-3} It was just a regular chat with my dad, talking about random stuff... but I'm sure he appreciated that I called him. {i}{size=-3}{/color}"
                                $ dadfriend += 1
                                scene 61111 with dissolve
                                d "It was nice talking to you. See you."

                    "Ask for money\n {color=#3d85c6} Dad -1 point ":
                        scene 61111b with dissolve
                        e "Dad, I need some money."
                        scene 61111 with dissolve
                        d "How much do you need?"

            else:
                menu:
                    "Chat normally":
                        scene 61111b with dissolve
                        "{color=#A8E4A0}{i}{size=-3} It was just a regular chat with my dad, talking about random stuff... but I'm sure he appreciated that I called him. {i}{size=-3}{/color}"
                        $ dadfriend += 1
                        scene 61111 with dissolve
                        d "It was nice talking to you. See you."

                    "Ask for money":
                        scene 61111b with dissolve
                        e "Dad, I need some money."
                        scene 61111 with dissolve
                        d "How much do you need?"

                        menu:
                            "50 dollars":
                                if dadfriend >= 0:
                                    scene 61111b with dissolve
                                    e "I need 50 dollars."
                                    scene 61111 with dissolve
                                    d "50 dollars? Alright, but that's a lot. You always want more! Fine, take it."
                                    $ dadfriend -= 1
                                    scene 61111b with dissolve
                                    e "Thanks, dad!"
                                    $ money += 50
                                else:
                                    scene 61111b with dissolve
                                    e "I need 50 dollars."
                                    scene 61111 with dissolve
                                    d "What? You want money again, and our relationship is like this? You always want more cash!"
                                    scene 61111b with dissolve
                                    e "But... please..."
                                    scene 61111 with dissolve
                                    d "No way. I've had enough of your requests!"

                            "100 dollars":
                                if dadfriend >= 0:
                                    scene 61111b with dissolve
                                    e "I need 100 dollars."
                                    scene 61111 with dissolve
                                    d "100 dollars?! Do you have any idea how much that is?!"
                                    d "Always with the money! But... fine, here you go. Don’t come asking for this much again!"
                                    $ dadfriend -= 2
                                    scene 61111b with dissolve
                                    e "Thanks, dad!"
                                    $ money += 100

                                else:
                                    scene 61111b with dissolve
                                    e "I need 100 dollars."
                                    scene 61111 with dissolve
                                    d "100 dollars?! How many times do I have to tell you that I won't give you that much money?!"
                                    scene 61111b with dissolve
                                    e "Please... I really need it."
                                    scene 61111 with dissolve
                                    d "This isn’t an emergency! You’re not getting a dime!"




            $ dadalreadycall = True
            jump roomsbxhub
    else:
        scene 61111 with dissolve
        play sound "music/phonecall.mp3"
        pause
        "..."
        stop sound
        d "It's good that you're calling, we need to talk."
        scene 61111b with dissolve
        e "What’s up?"
        scene 61111 with dissolve
        d "I just got a call from Mrs. Thompson…"
        scene 61111b with dissolve
        e "Who’s that?!"
        scene 61111 with dissolve
        d "Remember that woman whose purse was taken by a crook and you stopped him?"
        scene 61111b with dissolve
        e "Oh... that one!"
        scene 61111 with dissolve
        d "Well, she knows you took it."
        scene 61111b with dissolve
        e "So what? What’s it to you?"
        scene 61111 with dissolve
        d "What’s it to me? She’s our neighbor, [player_name]! She knew me, and she knows you. How could you do something like this?"
        scene 61111b with dissolve
        e "Whatever, it’s just a purse."
        scene 61111 with dissolve
        d "Just a purse? You’re a thief, [player_name]. I didn’t raise you to be a criminal. I raised you to be a good man! And do good deeds!"
        scene 61111b with dissolve
        e "Yeah, yeah, save the lecture. I don’t need it."
        scene 61111 with dissolve
        d "You need more than a lecture. You need to grow up and take responsibility for your actions. I’m disappointed in you."
        scene 61111b with dissolve
        e "Disappointed? Fuck off, man. I do what I want."
        "{color=#A8E4A0}{i}{size=-3} You hung up."
        $ dadalreadycall = True
        jump roomsbxhub


label visitpoliceep6:
    play music "music/plcof.mp3"
    scene plcman00 with Dissolve(2.0)
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} So... this is the place..."
    scene plcman01 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I hope this oldhead is at home."
    scene plcman02 with dissolve
    play sound "music/knock.mp3"
    scene plcman03 with dissolve
    pause 0.1
    scene plcman04
    pause 0.1
    scene plcman03
    pause 0.1
    scene plcman04
    pause 0.1
    scene plcman05 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You reached for the door, and with a hefty couple of knocks on the door, you made yourself present."
    $ renpy.pause(4, hard=True)
    e "Hm..."
    scene plcman06 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Right after that, you noticed a doorbell there, perhaps, it would be a better idea to ring it."
label doorchoicepolice:
    if ringbellstat == 10:
        jump plcangry
    elif doorknockstat == 3:
        jump plcoming
    else:
        menu:
            "Ring the bell":
                scene plcman07_05 with dissolve
                play sound "music/ring.mp3"
                scene plcman07_06 with dissolve
                scene plcman07_05 with dissolve
                $ ringbellstat += 1
                jump doorchoicepolice
            "Knock again":
                play sound "music/knock.mp3"
                scene plcman03 with dissolve
                pause 0.1
                scene plcman04
                pause 0.1
                scene plcman03
                pause 0.1
                scene plcman04
                pause 0.1
                $ doorknockstat += 1
                jump doorchoicepolice

label plcangry:
       r "SHUT YOUR ASS UP OR I'LL SHOOT" with vpunch
       jump oldmantalks

label plcoming:
       r "I’m coming!"
       jump oldmantalks

label oldmantalks:
    "{color=#A8E4A0}{i}{size=-3} Door suddenly open"
    scene plcman08_07 with dissolve
    r "Who are you...? What do you want?"
    scene plcman08_06 with dissolve
    e "Hey, chill out man! You sound really worked up..."
    scene plcman08_07 with dissolve
    r "Who the fuck are you, what do you want?!"
    scene plcman08_08 with dissolve
    r "I’ve told you fucker I don’t want no home insurance."
    scene plcman08_07 with dissolve
    r "This whole place is built out of bricks and plaster, not paper and wood! It’s NOT going to burn d-"
    scene plcman08_09 with dissolve
    e "What the fuck are you talking about? I’m not an insurance salesman."
    scene plcman08_08 with dissolve
    r "Oh... Well...In that case..."
    scene plcman08_09 with dissolve
    e "Look, I’m [player_name], and I’m just a neighbor who wants to know a bit about something that happened a while ago and nobody wants to talk about it."
    scene plcman08_08 with dissolve
    r "You mean the civil rights movements or something...?"
    scene plcman08_06 with dissolve
    e "What? No...{p}It’s about a local case, a disappearance."
    scene plcman08_10 with dissolve
    r "Huh?"
    scene plcman08_08 with dissolve
    r "What are you, then, a private investigator?"
    scene plcman08_09 with dissolve
    e "Do I look like a private investigator?"
    scene plcman08_08 with dissolve
    r "Not at all..."
    scene plcman08_10 with dissolve
    r "Hm..."
    scene plcman08_08 with dissolve
    r "Well, in that case, come inside."
    scene black with Fade(2.0, 1.0, 1.0)
    scene plcinside0 with dissolve
    e "The last name is Lopez."
    scene plcinside1 with dissolve
    scene plcinside2 with dissolve
    scene plcinside3 with dissolve
    scene plcinside4 with dissolve
    scene plcinside5 with dissolve
    scene plcinside6 with dissolve
    r "Hm... Lopez... Lopez..."
    scene plcinside7 with dissolve
    r "You mean last name?"
    scene plcinside4 with dissolve
    e "No...?"
    scene plcinside11_09 with dissolve
    r "There is no such name as Lopez.{p}It's a last name or a nickname."
    scene plcinside11_10 with dissolve
    e "Huh?"
    scene plcinside7 with dissolve
    r "...It does ring a bell now that I think about it..."
    scene plcinside8 with dissolve
    scene plcinside9 with dissolve
    e "Oh, does it?"
    scene plcinside11_09 with dissolve
    r "Yeah... The pizza parlor guy."
    scene plcinside11_10 with dissolve
    e "What? No... I don’t think so..."
    scene plcinside11_09 with dissolve
    r "...How would I know? I mean, I was in the bureau for missing people in the police back in the day... If you happen to have a picture of him..."
    scene plcinside11_10 with dissolve
    e "I do, hold on."
    "{color=#A8E4A0}{i}{size=-3} You took your phone out of your pocket, and opened up the gallery, and started scrolling until you found the picture of Lopez."
    scene plcinside11_11 with dissolve
    e "Here, this is the guy..."
    scene plcinside11_12 with dissolve
    r "Hold on, let me see it up close."
    scene plcinside11_13 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Without asking for it, he snatched your phone off your hand and gave it a closer inspection, holding it really close to his face and frowning."
    scene plcinside11_14 with dissolve
    r "Yeah... No..."
    scene plcinside11_13 with dissolve
    e "What you mean? You were a cop back then, you must know something."
    scene plcinside12_22 with dissolve
    r "I never said I wasn’t, I’m saying that I could throw you a bone if you sent the picture, but whatever you do with it it’s none of my business, and you didn’t get it from me."
    scene plcinside11_14 with dissolve
    r "By the way, who are those two ladies in the picture?"
    scene plcinside11_13 with dissolve
    menu:
        "It’s my [woman_role] and my [nicosister_role]... Why?":
            scene plcinside11_14 with dissolve
            r "Oh, it’s nothing..."
            jump polqest

        "Noneofya.":
            scene plcinside12_23 with dissolve
            r "Huh?"
            scene plcinside12_24 with dissolve
            e "None of ya’ business"
            scene plcinside12_22 with dissolve
            r "Okay, smartass. Whatever..."
            jump polqest

label polqest:
    scene plcinside11_13 with dissolve
    e "Alright... So...what’s next?"
    scene plcinside11_14 with dissolve
    r "Send me that photo."
    scene plcinside12_22 with dissolve
    r "Alright, I know the file name. I still have the records from my operational days. Just give me a day or two. I’ll send you some field notes or whatever there is available in my docs."
    scene plcinside12_24 with dissolve
    e "Here’s my number just in case..."
    scene plcinside12_22 with dissolve
    r "Alright... Now bounce. I’ve got work to do..."
    scene plcoutside with dissolve
    "{color=#A8E4A0}{i}{size=-3} He slammed the door shut, and left you by yourself: You had done it again. And this time you had an ally who seemed to be real."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This oldhead better have what I’m looking for, otherwise all of this would’ve been a waste of time."
    scene black with Fade(2.0, 1.0, 1.0)
    $ visitpolice = True
    jump roomsbxhub

label sleependepisode:
    if tommygethismm == False or mtommoney == 1:
        scene black with fade
        $ sleepwithout = True
        "{color=#A8E4A0}{i}{size=-3} You decided to end the day without any evening adventures. And that's good! Time to get some sleep!"
        jump endchapter6
    elif tommygethismm == True:
        scene black with fade
        "{color=#A8E4A0}{i}{size=-3} You decided to end the day without any evening adventures. And that's good! Time to get some sleep!"
        "Or not"
        "{color=#A8E4A0}{i}{size=-3} You didn’t want to sleep at all. You weren’t tired. Yet, you didn’t really know what to do instead."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I need to respect my loyal customers. I received an order and I have to fulfill it."
        e "You swung your legs out of bed and stuffed the small bag of pills you had prepared earlier into your pocket. You knew Tommy's place wasn't far, and you had the door code memorized from previous visits."
        scene 60990 with dissolve
        "{color=#A8E4A0}{i}{size=-3} Just like that, you reached the apartment complex and walked into the corridor where Tommy’s apartment door was at."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hm... What was the code again?"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh... Right"
        "{color=#A8E4A0}{i}{size=-3} You punched in the door code, the lock clicking open with a soft beep."
        scene 60991 with dissolve
        "{color=#A8E4A0}{i}{size=-3} As you walked into the living room, you were greeted by an unexpected sight. [tommywoman_role] was passed out on the couch."
        scene 60991a with dissolve
        "{color=#A8E4A0}{i}{size=-3} Tommy was sleeping in a nearby chair, his head lolled to the side, soft snores escaping his lips."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hm? What happened here?"
        scene 60991 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You walked over to the couch and reached out, roughly shaking [tommywoman_role] to rouse her from her drug-induced slumber."
        scene 60992 with vpunch
        e "Hey... Junkie... Wake the fuck up"
        scene 60992b with dissolve
        "{color=#A8E4A0}{i}{size=-3} Her eyes fluttered open, her gaze unfocused and glassy. She looked up at you, a slow smile spreading across her face as recognition dawned in her eyes."
        scene 60992a with dissolve
        z "Mmm? It's you again!"
        scene 60992b with dissolve
        e "Me? Yeah... you look like shit."
        scene 60992a with dissolve
        z "Mmm... Uhm...  Do you have any more...?"
        scene 60992b with dissolve
        e "More what?"
        scene 60992a with dissolve
        z "You know... the good stuff... More p-pills..."
        scene 60992b with dissolve
        e "Nah, sorry, bitch. I'm all out."
        scene 60992c with dissolve
        "{color=#A8E4A0}{i}{size=-3} Her face fell in dissappointment."
label mtomreplaynight:
        scene 60992d with dissolve
        z "C-Come on... I’ll make it up for you... I know you have more!"
        scene 60992e with dissolve
        play sound "music/belt.mp3"
        "{color=#A8E4A0}{i}{size=-3} She reached for your belt, her fingers fumbling with the buckle as she tried to unfasten it."
        e "Oh... You’re quick... You clearly know what to do..."
        scene 60992g with dissolve
        z "Y-Yes... Another sloppy?!"
        scene 60992e with dissolve
        e "Another one? Oh..."
        if tommywomanshort_role in ["Mom", "mom", "Mother", "mother"]:
            "{color=#A8E4A0}{i}{size=-3} That’s when you realized what just happened. She blew her own son off, perhaps under the influence of your drugs having him mistaken for another man..."
        else:
            "{color=#A8E4A0}{i}{size=-3} That’s when you realized what just happened. She gave Tommy a blowjob, perhaps under the influence of your drugs having him mistaken for another man..."
        scene 60992f with dissolve
        e "I don’t want no sloppy... You better give me something better..."
        "{color=#A8E4A0}{i}{size=-3} Her eyes widened in surprise, a flush spreading across her cheeks as she realized what you were implying. She looked up at you, her breath hitching in her throat as she nodded slowly."
        scene 60992h with dissolve
        z "Okay... okay..."
        scene 60992i with dissolve
        e "Do you know what I want, right?"
        scene 60992h with dissolve
        z "Y-You wanna fuck... Me... Right?"
        scene 60992i with dissolve
        e "You want the pills, I want to fuck the shit out of that junkie-pussy of yours."
        scene 60992h with dissolve
        z "Oh... Oh my..."
        scene 60992i with dissolve
        play sound "music/belt.mp3"
        "{color=#A8E4A0}{i}{size=-3} You laid down on the couch, unbuckling your belt and sliding your pants down your legs."
        scene 60997 with dissolve
        "{color=#A8E4A0}{i}{size=-3} Your legs spread wide, your cock already hard and throbbing with ready for her to hop on it and ride as if her life depended on it."
        e "Go on, show me how much you want to get high again. Show me how down you wanna bend for another pill."
        scene 60995 with dissolve
        "{color=#A8E4A0}{i}{size=-3} She walked over to you, her hips swaying seductively as she climbed onto you, straddling you. She placed her hands on her thighs, her knees on either side of your hips, her pussy hovering just above your cock."
        if tommywomanshort_role in ["Mom", "mom", "Mother", "mother"]:
            e "You don’t even care about your son being right beside us you nasty freak? You ain’t got no shame."
        else:
            e "You don’t even care about Tommy being right beside us you nasty freak? You ain’t got no shame."
        z "Mngh... I... Don’t..."
        e "I fucking know it. Only thing you’ve got is a pussy tight enough to keep my dick entertained."
        e "Now, lower yourself onto me. Slowly."
        scene 60995a with vpunch
        "{color=#A8E4A0}{i}{size=-3} She did as you commanded, slowly lowering her pussy onto you, as it slowly began to slide in."
        scene mtomsecret120 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You could feel her wetness, her heat pounding through her cunt, as she enveloped your dick, her tight pussy gripping your cock like a vice."
        show mtomdrgsex
        "{color=#A8E4A0}{i}{size=-3} She began to move, her hips rolling as she lifted herself up and down, her pussy sliding along your shaft. You could feel her juices coating your hard cock as her pussy began to throb on your dick like a vibrating onahole that was made for you to finally use it."
        "{color=#A8E4A0}{i}{size=-3} You looked up at her, your eyes filled with lust and disdain as you watched her tits bounce with each thrust against her sweater. She was loving the dick more than the drugs that awaited her afterwards."
        e "Move that shit up... Up and down..."
        z "Mngh..."
        e "Ride it, or I might end up not giving you shit... I feel like scamming a bitch today..."
        z "P-Please d-don’t!!!"
        "{color=#A8E4A0}{i}{size=-3} She picked up the pace, her body moving with desperate urgency as she rode your cock."
        "{color=#A8E4A0}{i}{size=-3} You could see her nails digging further against her thighs, her breath coming in short as the only thing she wanted now is to cum all over with your dick shoved up to her uterus. "
        e "Only way for you to get the pills is by taking my nut up your cunt..."
        z "Oh god... yes... yes, please..."
        scene mtomsecret194 with vpunch
        "{color=#A8E4A0}{i}{size=-3} her body convulsing as her orgasm hit. You could feel her pussy clenching around you, her juices flowing as she came hard, as her moaning didn’t seem to wake Tommy up."
        z "Ooh..."
        e "Mngh... My turn...."
        e "If you want your prize, you better eat this nasty nut and not spill a fucking drop."
        scene v2cmmtom01 with dissolve
        "{color=#A8E4A0}{i}{size=-3} She kneeled right before you in front of you and you stood jerking your cock in front of her, as she opened her mouth wide."
        "{color=#A8E4A0}{i}{size=-3} Her make up was completely ruined, and you could see a smile forming on her mindless face as your pressed your dick against her tongue."
        e "Here it comes..."
        show cmmtom
        "{color=#A8E4A0}{i}{size=-3} And just like that, you started pumping your thick white sperm-shot right into her mouth, filling her taste buds with the taste of your cum."
        e "Yeah... T-Take it all, bitch."
        scene 60998a with dissolve
        "{color=#A8E4A0}{i}{size=-3} You looked down at her, a satisfied smirk playing on your lips as you realized you had gotten exactly what you wanted."
        "{color=#A8E4A0}{i}{size=-3} Especially when you see a huge amount of your cum flowing out of her mouth."
        scene 60998b with dissolve
        e "Do you want your candy? Then you have to swallow it together with my sperm."
        scene 60998c with dissolve
        e "Suck it."
        scene 60998d with dissolve
        "{color=#A8E4A0}{i}{size=-3} She moaned softly as the pill began to dissolve in her mouth, mixing with the huge amount of your cum."
        scene 60998e with dissolve
        pause
        scene 60998f with dissolve
        e "That's it. Now buzz off, Imma get going. "
        scene 60999 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You stood up and put on your pants, watching one last time as [tommywoman_role] slowly began to drift away..."
        $ mcdrugsexmtom = True
        $ renpy.end_replay()
        if not easymode:
                    $ achValid6 += 1
                    $ achievement.grant("Achiev26")
                    $ achievement.sync()
                    if not persistent.achievement26:
                                                 show Achiev26 at achievment with easeintop:
                                                            zoom 0.5
                                                            rotate_animation

                                                 "You have received the achievement!{p}{b}\"Night Stalker\"{/b}"
                                                 "Number of achievements earned in this chapter [achValid6]/4"
                                                 hide Achiev26
                                                 $ persistent.achievement26 = True
        scene black with Fade(2.0, 1.0, 1.0)
        jump endchapter6

label rentacarep6:
    scene 61111a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hm... Perhaps it’d be a good idea to get a ride for tonight."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I mean, I could probably take a cab for the two of us but... if anything pops up I’ll need a car to hop in."
    play sound "music/phonecall.mp3"
    pause
    "..."
    stop sound
    u "Hello! This is Lando’s Rentos! How may I help you?"
    scene 61111b with dissolve
    e "Hey, name’s [player_name]... Look, I’m having a date tonight"
    scene 61111 with dissolve
    u "Mhm"
    scene 61111b with dissolve
    e "And well, I need to impress a ‘special’ girl."
    scene 61111 with dissolve
    u "Oh, well, in that case I could offer you an SUV... Actually, I’m right in front of a big Yotota right now."
    scene 61111b with dissolve
    e "Hey, that will do."
    u "Alright, then! The cost per day is... $45 and the delivery fee is $5. You’ll receive it with a tank full of gas, and you gotta bring it back full."
    scene 61111b with dissolve
    e "Got it... When will you be dropping it by?"
    scene 61111 with dissolve
    u "Well, considering our drivers are busy… I could get it ready and delivered by the evening."
    scene 61111b with dissolve
    e "Sounds good to me."
    scene 61111 with dissolve
    u "Alright, thank you for choos-"
    scene 61111b with dissolve
    e "Yeah yeah, see you."
    $ money -= 50
    play sound "music/buyshop.mp3"
    $ ep6car = True
    jump ep6choosepath

label calltommyep6:
    $ tommyalreadycall = True
    if selltommydrugs > 1 and tommyfriend > 1 :
        play sound "music/phonecall.mp3"
        scene 61111 with dissolve
        jump tommyaftersellingdrg
    else:
        play sound "music/phonecall.mp3"
        scene 61111 with dissolve
        jump tommyaftersellingwd


label tommyaftersellingwd:
    scene black with Fade(2.0, 1.0, 1.0)
    stop music
    play music "music/Mtom.wav"
    if tommymrolegive == False:
        $ tommywomanshort_role = renpy.input("Tommy lives with his... \n {i}(Enter for 'Stepmom or write 'Mom' or something else.){/i}", )
        $ tommywoman_role = "Tommy's " + (tommywomanshort_role.strip() if tommywomanshort_role.strip() else "Stepmom")
        $ tommywomanshort_role = tommywomanshort_role.strip() if tommywomanshort_role.strip() else "Stepmom"
        $ tommymrolegive = True
        $ persistent.tommywoman_role = tommywoman_role
        $ persistent.tRole = tommywoman_role
    scene 60702 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy walked into the house, with his mind clouded from being busy all day."
    "{color=#A8E4A0}{i}{size=-3} The day seemed to be pretty chill, but as soon as he stepped inside, he knew something was up."
    t "Hey, [tommywomanshort_role]. What's up?"
    scene 60702a with dissolve
    z "Thomas..."
    scene 60702b with dissolve
    z "We need to talk."
    scene 60703 with dissolve
    t "Huh?! About what?"
    scene 60703a with dissolve
    z "I found something in your room."
    scene 60704 with dissolve
    z "Weed, Tommy...."
    scene 60704b with dissolve
    z "What are you doing with your life?!"
    scene 60704a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy felt a knot form in his stomach. He had been careful, or so he thought. He tried to play it cool, shrugging off her concern."
    "{color=#A8E4A0}{i}{size=-3} But at the same time his world began to crumble, his phone buzzed."
    stop music
    play sound "music/tommyphone.mp3"
    t "Ugh, one second..."
    stop sound
    "{color=#A8E4A0}{i}{size=-3} Tommy quickly dismissed the call."
    play music "music/Mtom.wav"
    scene 60705 with dissolve
    t "[tommywomanshort_role], it’s not what you think..."
    scene 60705a with dissolve
    scene 60705b with dissolve
    z "Don’t lie to me, Tommy. I’m your [tommywomanshort_role], and I’m worried about you."
    scene 60705c with dissolve
    t "Come on!"
    scene 60705d with dissolve
    t "I’m not lying!"
    scene 60706a with dissolve
    z "...Tommy, I found a big bag of weed under your bed. What are you doing with this stuff?"
    scene 60706 with dissolve
    t "Uh... I..."
    scene 60706a with dissolve
    z "Are you selling this?"
    scene 60706 with dissolve
    t "Uh... Okay...{p}It's not mine!"
    scene 60706b with dissolve
    z "Don’t bullshit me, Tommy!"
    scene 60706 with dissolve
    t "Oh, come on! You don’t need to worry. I’ve got everything under control."
    scene 60706b with dissolve
    z "Under control? Tommy, drugs are dangerous!"
    scene 60706 with dissolve
    t "It's WEED. Not drugs!"
    scene 60709 with dissolve
    z "I don’t want to see you ruin your life, not after ALL I’ve invested in you. I’ve seen what drugs can do to people."
    scene 60706c with dissolve
    t "[tommywomanshort_role], seriously, I’m fine. You don’t need to worry about me."
    scene 60709a with dissolve
    if tommywomanshort_role in ["Mom", "mom", "Mother", "mother"]:
        z "I can't help but worry! You are my son!"
    else:
        z "I can’t help but worry! You are the closest person to me!"
    scene 60709d with dissolve
    t "I know! I... I’m sorry..."
    scene 60709a with dissolve
    z "Look... Uh... I don’t know where to start..."
    scene 60709c with dissolve
    z "...When I was your age, I made some mistakes too. I experimented with drugs, and it almost ruined my life."
    scene 60709b with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy raised an eyebrow, surprised by her admission. He had never heard this story before."
    t "You did drugs?"
    scene 60709a with dissolve
    z "Look! I was young and stupid!"
    scene 60706 with dissolve
    t "Just like me?"
    scene 60706b with dissolve
    z "Mhm. Thought I could handle it, but it got out of control, real quick. I don’t want the same thing to happen to you. Drugs can take over your life before you even realize it."
    scene 60706c with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy sighed, feeling a pang of guilt in his stomach. He knew he couldn’t keep lying to her."
    t "Okay... "
    scene 60709d with dissolve
    z "Uhm..."
    scene 60709c with dissolve
    z "Yes..."
    scene 60710hug with dissolve
    z "Come give me a hug and promise me you'll take care of yourself."
    scene black with Fade(2.0, 1.0, 1.0)
    t "Sure..."
    t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Nice tits..."
    if tommyfriend > 1:
        t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I need to order more weed from [player_name] instantly..."
        t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's best to send him the money right away."
        $ money += 50
        play sound "music/buyshop.mp3"
        show text "{color=#00ff00}{size=+15}+5 0 ${/color}" with dissolve
        with Pause(2)
        show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
        hide text with dissolve
    jump ep6choosepath

label tommyaftersellingdrg:
    scene black with Fade(2.0, 1.0, 1.0)
    stop music
    play music "music/Mtom.wav"
    if tommymrolegive == False:
        $ tommywomanshort_role = renpy.input("Tommy lives with his... \n {i}(Enter for 'Stepmom or write 'Mom' or something else.){/i}", )
        $ tommywoman_role = "Tommy's " + (tommywomanshort_role.strip() if tommywomanshort_role.strip() else "Stepmom")
        $ tommywomanshort_role = tommywomanshort_role.strip() if tommywomanshort_role.strip() else "Stepmom"
        $ tommymrolegive = True
        $ persistent.tommywoman_role = tommywoman_role
        $ persistent.tRole = tommywoman_role
    scene 60702 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy walked into the house, with his mind clouded from being busy all day."
    "{color=#A8E4A0}{i}{size=-3} The day seemed to be pretty chill, but as soon as he stepped inside, he knew something was up."
    t "Hey, [tommywomanshort_role]. What's up?"
    scene 60702a with dissolve
    z "Thomas..."
    scene 60702b with dissolve
    z "We need to talk."
    scene 60703 with dissolve
    t "Huh?! About what?"
    scene 60703a with dissolve
    z "I found something in your room."
    scene 60704 with dissolve
    z "Drugs, Tommy...."
    scene 60704b with dissolve
    z "What are you doing with your life?!"
    scene 60704a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy felt a knot form in his stomach. He had been careful, or so he thought. He tried to play it cool, shrugging off her concern."
    "{color=#A8E4A0}{i}{size=-3} But at the same time his world began to crumble, his phone buzzed."
    stop music
    play sound "music/tommyphone.mp3"
    t "Ugh, one second..."
    stop sound
    "{color=#A8E4A0}{i}{size=-3} Tommy quickly dismissed the call."
    play music "music/Mtom.wav"
    scene 60705 with dissolve
    t "[tommywomanshort_role], it’s not what you think...{p}I don’t do drugs."
    scene 60705a with dissolve
    scene 60705b with dissolve
    z "Don’t lie to me, Tommy. I’m your [tommywomanshort_role], and I’m worried about you."
    scene 60705c with dissolve
    t "Come on!"
    scene 60705d with dissolve
    t "I’m not lying!"
    scene 60706a with dissolve
    z "...Tommy, first I found a bag of weed and NOW some pills in your room. What are you doing with this stuff?"
    scene 60706 with dissolve
    t "Uh... I..."
    scene 60706a with dissolve
    z "What?"
    scene 60706 with dissolve
    t "Uh... Okay...{p}They’re not mine!"
    scene 60706b with dissolve
    z "Don’t bullshit me, Tommy!"
    scene 60706 with dissolve
    t "Oh, come on! You don’t need to worry. I’ve got everything under control."
    scene 60706b with dissolve
    z "Under control? Tommy, drugs are dangerous!"
    scene 60706 with dissolve
    t "Fuck, I KNOW!"
    scene 60709 with dissolve
    z "I don’t want to see you ruin your life, not after ALL I’ve invested in you. I’ve seen what drugs can do to people."
    scene 60706c with dissolve
    t "[tommywomanshort_role], seriously, I’m fine. You don’t need to worry about me."
    scene 60709a with dissolve
    if tommywomanshort_role in ["Mom", "mom", "Mother", "mother"]:
        z "I can't help but worry! You are my son!"
    else:
        z "I can’t help but worry! You are the closest person to me!"
    scene 60709d with dissolve
    t "I know! I... I’m sorry..."
    scene 60709a with dissolve
    z "Look... Uh... I don’t know where to start..."
    scene 60709c with dissolve
    z "...When I was your age, I made some mistakes too. I experimented with drugs, and it almost ruined my life."
    scene 60709b with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy raised an eyebrow, surprised by her admission. He had never heard this story before."
    t "You did drugs?"
    scene 60709a with dissolve
    z "Look! I was young and stupid!"
    scene 60706 with dissolve
    t "Just like me?"
    scene 60706b with dissolve
    z "Mhm. Thought I could handle it, but it got out of control, real quick. I don’t want the same thing to happen to you. Drugs can take over your life before you even realize it."
    scene 60706c with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy sighed, feeling a pang of guilt in his stomach. He knew he couldn’t keep lying to her."
    t "Okay... I might have bought some drugs..."
    scene 60709d with dissolve
    z "Uhm..."
    scene 60709c with dissolve
    z "Yes..."
    scene 60710 with dissolve
    z "You’re right."
    scene 60710a with dissolve
    z "And here they are."
    scene 60711 with dissolve
    "{color=#A8E4A0}{i}{size=-3} His [tommywomanshort_role] opened the bottle and took out one pill, examining it carefully."
    scene 60712 with dissolve
    pause
    scene 60712a with dissolve
    z "Wait a minute... W-what are these?"
    scene 60712 with dissolve
    t "They’re just... they help me relax."
    scene 60712a with dissolve
    z "Oh god, these are dangerous. Do you know what’s in these?"
    scene 60712 with dissolve
    t "I... I don’t know. They just help me chill out."
    "{color=#A8E4A0}{i}{size=-3} His mom looked at the pill, her expression almost drooly, as she contemplated the same pills that made her an addict back in her days."
    scene 60713 with vpunch
    "{color=#A8E4A0}{i}{size=-3} Before Tommy could stop her, she popped the pill into her mouth and swallowed it. Tommy’s eyes widened in shock."
    scene 60713a with dissolve
    t "[tommywomanshort_role], what are you doing?!"
    scene 60713b with dissolve
    pause
    scene 60714 with dissolve
    z "Hey! You said these help you relax, right?"
    scene 60714a with dissolve
    t "Yeah... So?"
    scene 60714 with dissolve
    z "So now I’m gonna make sure these actually work and they’re not some kind of ecstasy pills that could end up killing you!"
    z "If something happens to me, you'll learn a lesson."
    scene 60714a with dissolve
    t "Oh, shit!"
    scene 60714b with dissolve
    "{color=#A8E4A0}{i}{size=-3} Tommy quickly took the bottle from her and hid it. His mom sat on the chair, her expression turning distant as the drug started to take effect."
    scene 60714c with dissolve
    z "Are you good?!"
    scene black with Fade(2.0, 1.0, 1.0)
    z "[tommywomanshort_role]?!"
    pause
    if ntrep6 == True:
        jump mtomgoep6
    else:
        $ tommygethismm = True
        "{color=#A8E4A0}{i}{size=-3} She fell asleep."
        t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I need to order more drugs from [player_name] instantly..."
        t "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's best to send him the money right away."
        $ money += 100
        play sound "music/buyshop.mp3"
        show text "{color=#00ff00}{size=+15}+1 0 0 ${/color}" with dissolve
        with Pause(2)
        show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
        hide text with dissolve
        jump ep6choosepath

label mtomgoep6:
    scene 60714d with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} After a few minutes, her eyes glazed over, and she looked at Tommy with a strange smile."
    z "Yeah...I feel good. Can I have another one?"
    scene 60714e with dissolve
    t "[tommywomanshort_role], no! You can’t have any more. It’s not safe."
    scene 60714d with dissolve
    z "C-Come on, I’m like... Floating... I wanna keep feeling it a little longer. It’s been so long since I felt like this."
    scene 60714e with dissolve
    t "[tommywomanshort_role], I can’t give you any more! It’s not right!"
    scene 60714f with dissolve
    z "I... C-Come on! I’ve not felt this good in years!"
    scene 60714g with dissolve
    t "N-No! Whatever it’s done to you, it’s not the same thing it does to me when it hits! Stop!"
    scene 60714i02 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She stood up and walked over to Tommy"
    z "I just want another pill! Sell me another one, god damnit!"
    t "Wha...Whaat?"
    scene 60714i03 with dissolve
    z "C-Come on, You greedy bastard..."
    z "What do you want?! 30$? 50$? Whatever, just... come on!"
    t "Cool it down! What's going on with you?! I don't want your money! [tommywomanshort_role] wake up!"
label replaytommyep6:
    scene 60715 with dissolve
    z "I... F-Fine...{p}I see you want me to beg for it..."
    scene 60715a with dissolve
    z "F-Fine..."
    scene 60715b with dissolve
    z "I'll blow your dick..."
    scene 60715c with dissolve
    "{color=#A8E4A0}{i}{size=-3} He watched in shocked arousal as she reached for his belt, unbuckling it quickly before pulling down his zipper. His cock sprang free, already hard and throbbing with anticipation."
    t "[tommywomanshort_role]?"
    scene 60715d with dissolve
    z "Stop pretending, L-Lopez! You pervert."
    scene 60715e with dissolve
    z "Getting your dick sucked by hungry girls is the only thing you want..."
    scene 60715f with dissolve
    "{color=#A8E4A0}{i}{size=-3} Before Tommy could react, his [tommywomanshort_role] knelt down in front of him, her eyes filled with a hungry intensity that sent a jolt straight to his fat dick."
    t "Are you really going to blow me for a fucking pill?"
    scene 60716 with vpunch
    $ renpy.pause(0.5, hard=True)
    scene 60716a with dissolve
    $ renpy.pause(0.5, hard=True)
    scene 60716b with dissolve
    $ renpy.pause(0.5, hard=True)
    scene 60716c with dissolve
    $ renpy.pause(0.5, hard=True)
    scene 60716d with dissolve
    $ renpy.pause(0.5, hard=True)
    scene 60717 with dissolve
    z "Uhm..."
    scene 60717a with dissolve
    $ renpy.pause(0.5, hard=True)
    scene 60717b with dissolve
    $ renpy.pause(0.5, hard=True)
    scene mtomsck1 with dissolve
    t "Oh fuck, [tommywomanshort_role]... You’re too far gone..."
    show mtomtomsck1
    $ renpy.pause(3, hard=True)
    "{color=#A8E4A0}{i}{size=-3} She didn’t seem to care about his protests, her head bobbing up and down as she sucked him eagerly. Her tongue swirled around his shaft while it was inside, licking and teasing every sensitive spot of his white veiny cock."
    show mtomtomsck2
    pause
    "{color=#A8E4A0}{i}{size=-3} He could feel her saliva coating his dick, making her movements slick and smooth, truly better than all those times he’s jerked off to the though of getting a blowjob by the hottest porn star he could think of."
    t "[tommywomanshort_role]... oh god, your mouth feels so good..."
    show mtomtomsck3
    "{color=#A8E4A0}{i}{size=-3} He looked down at her, watching as she took him deeper, her lips stretching wide to accommodate his thickness. She replied to his compliments by breathing harder through her nose, huffing faster."
    if tommywomanshort_role in ["Mom", "mom", "Mother", "mother"]:
        "{color=#A8E4A0}{i}{size=-3} She moaned softly, carelessly, not knowing she was blowing her own son for drugs. He couldn’t help but grip her hair tightly, guiding her movements as she sucked him harder."
    else:
        "{color=#A8E4A0}{i}{size=-3} She moaned softly, carelessly, not knowing that she was giving her sweet Tommy a blowjob for drugs. He couldn’t help but grip her hair tightly, guiding her movements as she sucked him harder."
    t "Fuck, [tommywomanshort_role]... you’re so good at this..."
    "{color=#A8E4A0}{i}{size=-3} She pulled back slightly, her tongue flicking against the sensitive tip of his cock before taking him deep again. He could feel his climax building, his balls drawing up tight as she brought him closer to the edge."
    t "I’m gonna cum... You better stop..."
    "{color=#A8E4A0}{i}{size=-3} But she didn’t stop. Instead, she increased her pace, her head moving faster as she sucked him with renewed vigor, doing it all for the pills that once drove her crazy."
    scene ckmtom18 with vpunch
    t "Oh fuck, [tommywomanshort_role]... S-Shiiittt..."
    scene ckmtom19 with vpunch
    $ renpy.pause(0.5, hard=True)
    scene ckmtom20 with vpunch
    $ renpy.pause(0.5, hard=True)
    scene ckmtom21 with vpunch
    "{color=#A8E4A0}{i}{size=-3} His body tensed as his orgasm hit, his cock pulsing as he came hard, filling her mouth with his hot cum."
    scene 60718 with dissolve
    t "Oh god, [tommywomanshort_role]... that was fucking... Good..."
    scene 60718a with dissolve
    "{color=#A8E4A0}{i}{size=-3} She looked up at him, her eyes filled with satisfaction as she swallowed almost every last drop"
    z "There, that wasn’t so bad, was it? Now, how about that pill?"
    $ tommygethismm = True
    "{color=#A8E4A0}{i}{size=-3} Tommy, still reeling from getting blown by his own [tommywomanshort_role], hesitated. He knew giving her more drugs was a bad idea, but the pleasure she had just given him clouded his judgment."
    scene black with Fade(2.0, 1.0, 2.0)
    "{color=#A8E4A0}{i}{size=-3} But the look in her eyes, the desperation, was too much for him to bear. He reached for the bottle and pulled out a pill, handing her another one."
    "{color=#A8E4A0}{i}{size=-3} ..and he took one for himself.."
    $ renpy.end_replay()
    "{color=#ffa500}{i}*Phone ringing*{/i}{/color}"
    play sound "music/phonecall.mp3"
    t "{i}[player_name]?"
    "{i}The person you are trying to call is unavailable. Please leave a message."
    t "{i}Hey man! I need more of these...you know what. I'm sending you the money immediately, please bring it quickly!"

    $ money += 100
    play sound "music/buyshop.mp3"
    show text "{color=#00ff00}{size=+15}+1 0 0 ${/color}" with dissolve
    with Pause(2)
    show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
    hide text with dissolve
    if not easymode:
                $ achValid6 += 1
                $ achievement.grant("Achiev25")
                $ achievement.sync()
                if not persistent.achievement25:
                                             show Achiev25 at achievment with easeintop:
                                                        zoom 0.5
                                                        rotate_animation

                                             "You have received the achievement!{p}{b}\"What a trip!\"{/b}"
                                             "Number of achievements earned in this chapter [achValid6]/4"
                                             hide Achiev25
                                             $ persistent.achievement25 = True

    jump ep6choosepath

label eveningep6talkafterfck:
    stop music
    play music "music/Mnic.wav"
    scene 68000 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You thought she would’ve left the house, but you found her in her bedroom, doing some makeup."
    scene 68001 with dissolve
    e "Hey..."
    scene 68001a with dissolve
    m "Hi, I guess..."
    scene 68002 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She seemed a bit more relieved, but still stressed overall."
    scene 68002a with dissolve
    e "Well..."
    scene 68003 with dissolve
    e "Are you feeling better?"
    scene 68003a with dissolve
    m "Does it matter?"
    scene 68003 with dissolve
    e "It should matter to you."
    scene 68004 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She sighed before answering, rolling her eyes in disinterest at the conversation."
    scene 68004a with dissolve
    m "Whatever..."
    scene 68005 with dissolve
    m "...Think I’m gonna go out tonight..."
    scene 68005a with dissolve
    m "I need some time for myself after all."
    scene 68005b with dissolve
    show screen hint ("I can either be firm or try to convince her...")

    if easymode:
        menu:

            "With whose permission?\n{color=#3d85c6} +1 Dom Point, -1 Lust Point":
                hide screen hint
                jump whosepermission

            "If you needed any time, that time should be spent together.\n{color=#3d85c6} +1 Lust Point, +1 Dom Point":
                hide screen hint
                jump spacelove

    else:
        menu:

            "With whose permission?":
                hide screen hint
                jump whosepermission

            "If you needed any time, that time should be spent together.":
                hide screen hint
                jump spacelove

label whosepermission:
    scene 68006 with dissolve
    m "Mine!"
    scene 68006a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her eyes widened as she frowned, not expecting that reply from you."
    e "That would be valid IF you didn’t happen to be mine. Too bad, you gotta ask me first."
    scene 68007 with dissolve
    m "Excuse me?!"
    scene 6801mctalk with dissolve
    e "You’ve heard me."
    scene 6801mclisten with dissolve
    m "Yes, I know, but... ugh."
    scene 6801mctalk with dissolve
    e "What’s the matter? You want to go out, you just gotta ask for permission to your superior."
    scene 68008 with dissolve
    m "My superior?"
    scene 68008a with dissolve
    e "Come on, do you really want to get me on my bad side?! I’m just telling you nicely."
    scene 68008 with dissolve
    m "N-No... Just."
    scene 68008a with dissolve
    e "Oh, so you don’t need to be reminded. You already know it! Good to know…"
    scene 6801mclisten with dissolve
    m "Ugh! Just... Quit it!"
    scene 6801mctalk with dissolve
    e "It’s not that hard, you just gotta ask..."
    scene 68010 with dissolve
    m "Please don’t make me say it..."
    scene 68010a with dissolve
    e "Do you have a choice?"
    scene 68011 with dissolve
    m "You’ve already said that countless of times, please, just...{p}Can you be a normal person once?"
    scene 68011a with dissolve
    e "I’m not suggesting you anything. You’re going for it yourself. If you happened to be normal, then you would’ve taken it as a joke. But nope, you’re far too gone."
    scene 68012 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She swallowed her own spit, trying to hold back any rage, as she looked down and back up to your eyes."
    scene 68012a with dissolve
    m "Can I please, please go out... tonight...?"
    scene 68012 with dissolve
    e "Hmm...{p}Okay."
    scene 68013 with dissolve
    m "...Allright..."
    scene 68013 with dissolve
    e "With me."
    scene 68014 with dissolve
    m "W-What? No!"
    scene 68014a with dissolve
    m "I mean, please! I just want some SPACE for myself! Come on..."
    scene 68015 with dissolve
    e "Do you think I’m stupid and I don’t know the kind of creeps that happen to accumulate there? I’m going there with you, and that’s it."
    scene 68016 with dissolve
    m "B-But... Ugh... People will think I’m dating you... I’ll be seen as a hungry cougar or something."
    scene 68016a with dissolve
    e "And aren't we dating at all? Come on, we've even gone all the way together..."
    scene 68016 with dissolve
    m "N-No... We're not... Stop it..."
    scene 6801mctalk with dissolve
    e "Come on, you don't even believe that. You know you love the idea of going out together and pretending for one night that you're not some pathetic old [woman_role] fucking her [player_role]."
    scene 6801mclisten with dissolve
    m "Nobody knows that, only you..."
    scene 68016a with dissolve
    e "What?"
    scene 68017 with dissolve
    m "Ugh! Look, whatever you’re trying to do here just... Cut it. You’ve already done-fucked everything we were..."
    scene 68017a with dissolve
    m "Now we’re something... Ugh... Terrible."
    "{color=#A8E4A0}{i}{size=-3} Her subconscious had spoken, and she gave herself away. It seemed like she was convincing herself that you were her partner, or at least that's what you believed."
    e "Terrible for you, at least for now... So, what's it gonna be, hm? Are we going, or are you gonna stay here and rot?"
    scene 68017 with dissolve
    m "I don't want to, but... I don't see any other way out of this. We could go... But you need to behave like a normal person in public! For just... once!"
    scene 68015 with dissolve
    e "You don’t think I could behave? [woman_name], I can be anything If I want to, you just gotta ask for it..."
    scene 68005ak with dissolve
    m "I know you can... Just please, please... If we’re going out, I need people to think you’re not a weirdo."
    scene 68005k with dissolve
    e "Like if I cared what they thought."
    scene 68006k with dissolve
    m "But I do!"
    scene 68005k with dissolve
    e "Jeez, It’s not like if they’re even going to remember your ass after the pass out in their bed after getting back home."
    scene 68006k with dissolve
    m "That’s not the point. You WILL behave, period..."
    scene 68005bk with dissolve
    e "I’ll behave as long as you ask for it."
    scene 68006k with dissolve
    m "[player_name]!"
    scene 68005bk with dissolve
    e "Go on... You know what to do."
    scene 68008k with dissolve
    m "Will you... Will you please BEHAVE tonight?"
    scene 68008ak with dissolve
    e "Hm???"
    scene 68008k with dissolve
    m "Please?"
    scene 68007ak with dissolve
    e "Great, that's what I wanted to hear... I’ll try."
    scene 68007bk with dissolve
    m "Phew... Okay..."
    scene 68007ak with dissolve
    e "So, see you tonight, wear a nice dress that shows off that pretty ass and tits of yours. Bye."
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    pause 1
    $ domep6 += 1
    $ lustep6 -= 1
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[domep6].png"
    hide image "images/Stats/Lust[lustep6].png"
    hide text with dissolve
    scene black with Fade(2.0, 1.0, 1.0)
    $ renpy.pause(1, hard=True)
    jump goingtoclub

label spacelove:
    scene 68004a with dissolve
    m "[player_name], please... I just need some time alone, don’t start with that..."
    scene 68005b with dissolve
    e "Alone? You think being alone is going to solve anything?! You need to be with me... After all, we need a bit more of touch..."
    scene 68007 with dissolve
    m "I can't... I can't talk about ‘us’... I need to clear my head."
    scene 68007a with dissolve
    e "I know, but why do it alone? You know how it is nowadays, it’s dodgy everywhere... You can clear your head with me. I promise, I'll behave... And take care of you."
    scene 68008 with dissolve
    m "Yeah like if your word had any worth…"
    scene 6801mctalk with dissolve
    e "Hey, I think I can keep my dick in my pants... And others’ too."
    scene 68011 with dissolve
    m "Are you sure about that? Please."
    scene 68014a with dissolve
    e "Like, come on, I won't do anything to ruin your fun. Just give me a chance!"
    scene 68006k with dissolve
    m "A chance for what? For you to just blow it all up in public? Even if I agreed I’d still regret it shortly after."
    scene 68005bk with dissolve
    e "You wouldn’t regret it if I happened to be a gentleman in public with you, shit, even the man you  need..."
    scene 68017a with dissolve
    m "I don’t need a man... I need some space, and love, for fuck’s sake!"
    e "I can give you love!"
    scene 68017 with dissolve
    m "You don’t have any idea of what 'love' really means."
    scene 68015 with dissolve
    e "Come on, I want to make things right. I promise I'll behave with you and show you the love you deserve..."
    scene 68006k with dissolve
    m "You can start showing it right now by SWEARING you won’t try anything with me..."
    scene 68005bk with dissolve
    e "Okay! Okay... I won't try anything. Just let me be there with you. Let me show you that I can be trusted!..."
    scene 68008k with dissolve
    m "I... I don’t know... Are you sure? Don’t want you backing up once we’re there or anything..."
    scene 68008ak with dissolve
    e "I am... Come on, let’s go out together..."
    scene 68005ak with dissolve
    m "Okay... But if you break your promise, I swear..."
    scene 6801mctalk with dissolve
    e "I’ll try my best..."
    scene 68013 with dissolve
    m "Okay... FINE. Let's go out tonight. But you better keep your word..."
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    pause 1
    $ domep6 -= 1
    $ lustep6 += 1
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[domep6].png"
    hide image "images/Stats/Lust[lustep6].png"
    hide text with dissolve
    scene black with Fade(2.0, 1.0, 1.0)
    $ renpy.pause(1, hard=True)
    jump goingtoclub

label goingtoclub:
    stop music
    scene black with Fade(2.0, 1.0, 1.0)
    show text "Evening" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 68500 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You slouched on the couch, glancing at your watch every few minutes. [woman_name] was taking forever to get ready for the club, and you were certainly anxious."
    "{color=#A8E4A0}{i}{size=-3} Finally, you heard her heels clicking down the stairs."
    scene 68501a with dissolve
    "{color=#A8E4A0}{i}{size=-3} She looked hot in a tight, shimmering dress that showed off all her curves. Her hair and makeup were on point."
    scene 68501 with dissolve
    m "Hey... I’m ready."
    scene 68501a with dissolve
    e "Damn, you look fucking great."
    "{color=#A8E4A0}{i}{size=-3} [woman_name] smiled, slightly pleased with the compliment, yet awkward."
    scene 68501 with dissolve
    m "Yeah... Thanks?..."
    scene 68501a with dissolve
    e "You’re welcome..."
    scene 68501 with dissolve
    m "So, we’re taking a cab?"
    scene 68501a with dissolve
    e "Nah, I’ve got something way better planned. Come with me"
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} You took her hand and led her to the front door."
    scene 68502 with dissolve
    m "What’s this?"
    e "A car. D’uh."
    m "...Smartass. Although, I don’t see why you rented a car..."
    e "Hey, I thought it’d be lame to just go to one of the local clubs. So, I’ve got something better in mind."
    m "Really? Where are we going?"
    scene 68503 with dissolve
    e "The only nice club you’ve probably been taken to in your lifetime."
    scene 68504 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You opened the passenger door for her, and she slid in, her dress riding up a bit, giving you a nice view of her thighs."
    scene black with Fade(2.0, 1.0, 1.0)
    show text "As you started the engine, the lifted SUV purred to life, and you pulled out of the driveway, heading onto the open road."
    $ renpy.pause(3, hard=True)
    hide text with dissolve

    scene 69200car with dissolve
    e "Here we are..."
    e "Forest Club."
    scene 69001talk9 with dissolve
    e "Everything okay?"
    scene 69001talk2 with dissolve
    m "Yeah..."
    scene 69001talk0 with dissolve
    pause
    scene 69001talk1 with dissolve
    m "Can I..."
    scene 69001talk2 with dissolve
    m "Ask you for a favor?"
    scene 69001talk0 with dissolve
    e "What is it?"
    scene 69001talk9 with dissolve
    m "Please don’t make no stupid moves..."
    scene 69002d with dissolve
    e "And why’s that?"
    scene 69002b with dissolve
    m "Because I’ve agreed to give you one last chance."
    scene 69001talk5 with dissolve
    e "Relax, after all, I just wanted to get out of the same four walls too"
    e "I know you like clubbing."
    scene 69001talk1 with dissolve
    e "So chill, take a break. Just worry about busting a few moves on the dancefloor, I guess."

    if easymode:
        menu:
            "Just remember, I’ll be watching you. Don’t try anything funny with other guys.\n{color=#3d85c6} +1 Dom Point":
                scene 69002c with dissolve
                m "Ugh.."
                scene 69002b with dissolve
                m "We haven’t even left the car yet and you’re already being a dick"
                scene 69002c with dissolve
                e "Complain all you want, but the only dick in this car is the one you love to guzzle"
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ domep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                e "Let's go."
            "Gotta give it to you, you look hot in that dress.\n{color=#3d85c6} +1 Lust Point":
                scene 69002 with dissolve
                e "You’re probably the best looking woman I know."
                scene 69002d with dissolve
                m "Oh, t-thank you… That’s sweet."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                scene 69002 with dissolve
                e "Let's go."

    else:
        menu:
            "Just remember, I’ll be watching you. Don’t try anything funny with other guys.":
                scene 69002c with dissolve
                m "Ugh.."
                scene 69002b with dissolve
                m "We haven’t even left the car yet and you’re already being a dick"
                scene 69002c with dissolve
                e "Complain all you want, but the only dick in this car is the one you love to guzzle"
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ domep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                e "Let's go."
            "Gotta give it to you, you look hot in that dress.":
                scene 69002 with dissolve
                e "You’re probably the best looking woman I know."
                scene 69002d with dissolve
                m "Oh, t-thank you… That’s sweet."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                scene 69002 with dissolve
                e "Let's go."


    if easymode:

        menu:
            "{color=#FFD1DF}{i}*Open the door for her*{/i}{/color}\n{color=#3d85c6} +1 Lust Point":
                scene 69002d with dissolve
                e "Wait... I'll open the door for you."
                scene 69003 with dissolve
                e "Take my hand."
                m "Damn, it’s good to know you can still be a gentleman..."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                jump ep6clubentrance

            "{color=#FFD1DF}{i}*Wait until she gets out on her own to watch*{/i}{/color}\n{color=#3d85c6} +1 Dom Point":
                scene 69003a with dissolve
                pause
                scene 69003b with dissolve
                e "Can’t get enough of that ass."
                m "[player_name]! I said no weird moves, okay?!"
                e "Yeah yeah, whatever."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ domep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                jump ep6clubentrance

    else:
        menu:
            "{color=#FFD1DF}{i}*Open the door for her*{/i}{/color}":
                scene 69002d with dissolve
                e "Wait... I'll open the door for you."
                scene 69003 with dissolve
                e "Take my hand."
                m "Damn, it’s good to know you can still be a gentleman..."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                jump ep6clubentrance

            "{color=#FFD1DF}{i}*Wait until she gets out on her own to watch*{/i}{/color}":
                scene 69003a with dissolve
                pause
                scene 69003b with dissolve
                e "Can’t get enough of that ass."
                m "[player_name]! I said no weird moves, okay?!"
                e "Yeah yeah, whatever."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ domep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                jump ep6clubentrance

label ep6clubentrance:
    play music "music/musicclub1.mp3"
    scene black with Fade(2.0, 1.0, 1.0)
    show text "Forest Club" at title with dissolve
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3}Hurrying your pace, you walked inside of the club, but you’re stopped right at the entrance by the bouncer."
    scene 69049 with dissolve
    b "Good night to yall, I’ll need some ID."
    scene 69049a with dissolve
    b "Nah, not for you. You’re way above the age.{p}It’s him, gotta make sure."
    scene 69049c with dissolve
    e "Man, do you think I’m not over 18?"
    b "Come on, people can disguise their age real easy. Let me see that ID."
    e "Here, have it."
    scene 690491 with dissolve
    b "Hm...Alright. You’re good, son."
    b "Have fun while inside."
    scene 69049d with dissolve
    e "With a chick like her... it’s kind of hard not to."
    scene 690491 with dissolve
    b "Alright, now for my curiosity, I wanna see her ID."
    scene 69049a with dissolve
    m "Uhm... Here..."
    scene 69049c with dissolve
    b "Alright.. let’s see..."
    b "Shit!"
    m "W-What?!"
    scene 69049 with dissolve
    b "37?! Maaaan, what a legend. You really did pull a milf."
    scene 69049d with dissolve
    e "Believe me, now?!"
    scene 69049 with dissolve
    b "Man, you're one lucky bastard. She's a fine mommy, ain't she?"

    if easymode:
        menu:
            "Yeah, she's a real MILF. Keeps me young, if you know what I mean.\n{color=#3d85c6} +1 Lust Point":
                scene 69049d with dissolve
                b "I bet she does. Take care of her inside."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                e "Oh, I will"
                scene black with Fade(2.0, 1.0, 1.0)
                jump clubinside

            "You bet she is. Isn't that right, bubble butt?{color=#FFD1DF}{i}*Slap her ass*{/i}{/color}\n{color=#3d85c6} +1 Dom Point":
                scene 69049d with dissolve
                "{color=#A8E4A0}{i}{size=-3} With force, you smacked her asscheeks."
                scene 69049e with vpunch
                m "Ow! [player_name]!"
                scene 69049d with dissolve
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ domep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                b "Man, you’re slick."
                scene black with Fade(2.0, 1.0, 1.0)
                jump clubinside
    else:
        menu:
            "Yeah, she's a real MILF. Keeps me young, if you know what I mean.":
                scene 69049d with dissolve
                b "I bet she does. Take care of her inside."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                e "Oh, I will"
                scene black with Fade(2.0, 1.0, 1.0)
                jump clubinside

            "You bet she is. Isn't that right, bubble butt?{color=#FFD1DF}{i}*Slap her ass*{/i}{/color}":
                scene 69049d with dissolve
                "{color=#A8E4A0}{i}{size=-3} With force, you smacked her asscheeks."
                scene 69049e with vpunch
                m "Ow! [player_name]!"
                scene 69049d with dissolve
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ domep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
                b "Man, you’re slick."
                scene black with Fade(2.0, 1.0, 1.0)
                jump clubinside

label clubinside:
    show clubdancing with dissolve
    "{color=#A8E4A0}{i}{size=-3}Once inside, you looked around, scanning for a seat, as you stared at the multitude with her on your side."
    e "You like the place, right?"
    m "Yeah, it's rather posh... But it’s nice. Been here a few times."
    "{color=#A8E4A0}{i}{size=-3} You take a seat with her on the nearest couch."
    scene 69060e with dissolve
    e "Man, I’m thirsty!"
    scene 69060f with dissolve
    m "Thought it’d be just me..."
    scene 69060h with dissolve
    e "Since I’m feeling like sharing today, I’ll go get US some drinks going on"
    scene 69060g with dissolve
    m "Well, I... I appreciate it!"
    scene 69060c with dissolve
    m "I just hope there aren't too many people at the bar"
    scene 69060h with dissolve
    e "Don't worry, lady."
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3}You reached for the bar, where the bartender attended you."
    scene 69060bar with dissolve
    f "Yo, what can I get you?"
    show screen hint ("I have to get her drunk... but I can't overdo it...")

    if easymode:
        menu:
            "One tequila drink. Make it double and a beer.\n{color=#3d85c6} You need to buy one tequila and one mojito":
                scene 69060bar2 with dissolve
                hide screen hint
                f "Strong drink!"
                f "Coming right up."
                $ tequila1 = True
                $ ep6alcohol += 3

            "One mojito and a beer.\n{color=#3d85c6} +1 Lust Point":
                scene 69060bar2 with dissolve
                hide screen hint
                f "Sure thing, buddy."
                $ mohito1 = True
                $ ep6alcohol += 1

    else:
        menu:
            "One tequila drink. Make it double and a beer.":
                scene 69060bar2 with dissolve
                hide screen hint
                f "Strong drink!"
                f "Coming right up."
                $ tequila1 = True
                $ ep6alcohol += 3

            "One mojito and a beer.":
                scene 69060bar2 with dissolve
                hide screen hint
                f "Sure thing, buddy."
                $ mohito1 = True
                $ ep6alcohol += 1

    scene black with Fade(2.0, 1.0, 1.0)
    scene 69061 with dissolve
    "{color=#A8E4A0}{i}{size=-3}You made your way back to the couch, handing her the drink she wanted"
    scene 69061b with dissolve
    m "Thanks..."
    if mohito1:
            scene 69063b with dissolve
            "{color=#A8E4A0}{i}{size=-3} She took a big sip of her drink"
            scene 69061b with dissolve
            m "I really like this"
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            pause 1
            $ lustep6 += 1
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[domep6].png"
            hide image "images/Stats/Lust[lustep6].png"
            hide text with dissolve
    scene 69061 with dissolve
    e "Here you go... Come on, let's drink up"
    scene 69063b with dissolve
    "{color=#A8E4A0}{i}{size=-3}In a lousy attempt to cheer her up further, you clinked your glasses together, right before chugging them down."
    e "Phew... There’s something extra in these..."
    scene 69061b with dissolve
    m "Of course there’s going to be something extra if you drink it in one sip, you maniac!"
    scene 69061 with dissolve
    e "Come on, let's dance... I’m already heated up."
    scene 69062 with dissolve
    m "What? You and me?"
    scene 69062a with dissolve
    m "No way!"
    scene 69063b with dissolve
    e "Hey, I came all the way here to take you for a spin down at the dancefloor. The least you could do is accept."
    scene 69063c with dissolve
    m "Ugh... Whatever, it’s not like people are going to remember us after all... Let's go."
    scene 69063b with dissolve
    e "That’s my girl."
    scene black with Fade(2.0, 1.0, 1.0)
    show nicdance1 with dissolve
    e "You're pretty good at this..."
    show text "You have to dance! Choose the moves that appear on the screen."
    $ dancetut = "Ep6/dancetut.png"
    show image dancetut at title2
    pause
    hide image dancetut
    hide text
    show text "You don't have to be good at dancing... but [woman_name] will definitely like it!"
    pause
    hide text
label nicdancingfirst:

    $ set_dance_menu_position()


    $ current_image = renpy.random.choice([
        "Ep6/lefthand.png",
        "Ep6/righthand.png",
        "Ep6/leftfoot.png",
        "Ep6/rightfoot.png"
    ])


    show image current_image at title with dissolve
    $ timeout_label = "faildance1"
    $ timeout = 2

    menu (screen="dance"):
        "Left Hand":
            if current_image == 'Ep6/lefthand.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints += 1
                jump check_points
            else:
                jump faildance1
        "Right Hand":
            if current_image == 'Ep6/righthand.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints += 1
                jump check_points
            else:
                jump faildance1
        "Left Foot":
            if current_image == 'Ep6/leftfoot.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints += 1
                jump check_points
            else:
                jump faildance1
        "Right Foot":
            if current_image == 'Ep6/rightfoot.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints += 1
                jump check_points
            else:
                jump faildance1

label faildance1:
    hide image current_image
    $ fail_dance += 1
    if fail_dance >= 2:
        if speedguy >= 1 and speedsaver == False:
            show text "Ooops!...One more try cause you got SPEED perk!"
            $ speedsaver = True
            hide text
            jump nicdancingfirst
        else:
            jump faildancefin1
    $ dancepoints = 0
    show text "Ooops!...One more try!"
    pause
    hide text
    jump nicdancingfirst

label faildancefin1:
    hide image current_image
    m "Oh [player_name]... I thought'd you are a better dancer haha"
    jump afterdance1

label check_points:
    if dancepoints >= 5:
        jump dance1gamewin
    else:
        jump nicdancingfirst

label dance1gamewin:
            hide image current_image
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            pause 1
            $ niclovebonusfactor += 1
            $ lustep6 += 1
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[domep6].png"
            hide image "images/Stats/Lust[lustep6].png"
            hide text with dissolve
            y "Look at that babe with that guy."
            y "She's got to be twice his age!"

label afterdance1:
    e "Let's get back to the sofas"
    m "Sure!"
    scene black with Fade(2.0, 1.0, 1.0)
    stop music fadeout 1.0
    play music "music/musicclub2.mp3"
    scene 69060a with dissolve
    "{color=#A8E4A0}{i}{size=-3} After busting a couple of moves, you finally returned to your seat, breathing hard."
    e "You're pretty good at this... Who would’ve thought those legs could do much more than just scissor-opening."
    scene 69060b with dissolve
    m "Ugh! What?! S-Shut up."
    scene 69060e with dissolve
    e "Chill, it’s not like anyone will hear us with the music being this loud!"
    scene 69060c with dissolve
    m "...I think you’re right... Ugh, I need another drink."
    e "On my way!"
    scene 69060bar with dissolve
    "{color=#A8E4A0}{i}{size=-3} You headed back to the bar, and with one hand on the counter you got the bartender’s attention."
    f "Back again for more? What can I get you this time?"
    show screen hint ("I have to get her drunk... but I can't overdo it...")
    menu:

        "One tequila drink. Make it double and a beer.":
            scene 69060bar2 with dissolve
            hide screen hint
            f "You got it."
            f "This will be strong! Don't drink too much of it..."
            $ tequila2 = True
            $ ep6alcohol += 3

        "One mojito and a beer.":
            scene 69060bar2 with dissolve
            hide screen hint
            f "Coming right up."
            $ mohito2 = True
            $ ep6alcohol += 1

    scene 69060e with dissolve
    "{color=#A8E4A0}{i}{size=-3} Rushing, with both drinks in hand, you return to the couch."
    e "Here, your drink lady..."
    scene 69060f with dissolve
    m "Are you sure you’re not putting anything in these drinks?"
    scene 69060h with dissolve
    e "Eh, why would I do that?"
    scene 69060g with dissolve
    m "It wouldn’t be odd."
    scene 69060a with dissolve
    e "You’re asking way too many out of place questions."
    scene 69060g with dissolve
    m "Nevermind... I might be tripping... Pass me that."
    scene 69060h with dissolve
    e "Ah ah ah, this time you gotta ask for it."
    scene 69060 with dissolve
    m "Can you... not?"
    scene 69060a with dissolve
    e "You want the drink or not?"
    scene 69064 with dissolve
    m "...Please? Can I have the drink?"
    scene 69065 with dissolve
    e "Hm... Sure. Here. Good girl."
    if ep6alcohol >=4:
        scene 69064a with dissolve
        "{color=#A8E4A0}{i}{size=-3}You both take a sip, and she starts to look a bit more relaxed, as she huffs a bit of air after the shot."
        if mohito2:
                scene 69063b with dissolve
                "{color=#A8E4A0}{i}{size=-3} She took a big sip of her drink"
                scene 69061b with dissolve
                m "I really like this"
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
        scene 69064b with dissolve
        e "Are you tipsy yet?"
        scene 69065a with dissolve
        m "Yeah, I thiiink... *hic* so..."
        scene 69064a with dissolve
        e "Good. ‘Cause I’m down to see that ass shake while we dance. Come on, let’s hit it."
        scene 69065a with dissolve
        m "[player_name]!..."
        scene black with Fade(2.0, 1.0, 1.0)
        jump nicdancingsecond
    else:
        scene 69063a with dissolve
        "{color=#A8E4A0}{i}{size=-3}You both take a sip, and she starts to look a bit more relaxed, as she huffs a bit of air after the shot."
        if mohito2:
                scene 69063b with dissolve
                "{color=#A8E4A0}{i}{size=-3} She took a big sip of her drink"
                scene 69061b with dissolve
                m "This drink is delicious."
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                pause 1
                $ lustep6 += 1
                show image "images/Stats/Dom[domep6].png" at statleft
                show image "images/Stats/Lust[lustep6].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domep6].png"
                hide image "images/Stats/Lust[lustep6].png"
                hide text with dissolve
        scene 69063b with dissolve
        e "Are you tipsy yet?"
        scene 69063c with dissolve
        m "Nooo...."
        scene 69063b with dissolve
        e "Good. ‘Cause I’m down to see that ass shake while we dance. Come on, let’s hit it."
        scene 69061b with dissolve
        m "[player_name]!..."
        scene black with Fade(2.0, 1.0, 1.0)
        jump nicdancingsecond

label nicdancingsecond:
    $ set_dance_menu_position()

    $ set_dance_menu_position()


    show nicdance1 with dissolve


    $ current_image = renpy.random.choice([
        "Ep6/lefthand.png",
        "Ep6/righthand.png",
        "Ep6/leftfoot.png",
        "Ep6/rightfoot.png"
    ])


    show image current_image at title with dissolve
    $ timeout_label = "faildance2"
    $ timeout = 2


    menu (screen="dance"):
        "Left Hand":
            if current_image == 'Ep6/lefthand.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints2 += 1
                jump check_points2
            else:
                jump faildance2
        "Right Hand":
            if current_image == 'Ep6/righthand.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints2 += 1
                jump check_points2
            else:
                jump faildance2
        "Left Foot":
            if current_image == 'Ep6/leftfoot.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints2 += 1
                jump check_points2
            else:
                jump faildance2
        "Right Foot":
            if current_image == 'Ep6/rightfoot.png':
                show text "Good!" with dissolve
                hide text with dissolve
                $ dancepoints2 += 1
                jump check_points2
            else:
                jump faildance2

label faildance2:
    hide image current_image
    $ fail_dance2 += 1
    if fail_dance2 >= 2:
        if speedguy >= 1 and speedsaver == False:
            show text "Ooops!...One more try cause you got SPEED perk!"
            $ speedsaver = True
            hide text
            jump nicdancingsecond
        else:
            jump faildancefin2
    $ dancepoints2 = 0
    show text "Ooops!...One more try!"
    pause
    hide text
    jump nicdancingsecond

label faildancefin2:
    hide image current_image
    m "Oh [player_name]... Haha"
    jump afterdance2

label check_points2:
    if dancepoints2 >= 6:
        jump dance2gamewin
    else:
        jump nicdancingsecond


label dance2gamewin:
            hide image current_image
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            pause 1
            $ niclovebonusfactor += 1
            $ lustep6 += 1
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[domep6].png"
            hide image "images/Stats/Lust[lustep6].png"
            hide text with dissolve

label afterdance2:
    if ep6alcohol == 6:
        scene 690761 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You dance together again, and [woman_name] is starting to loosen up more. Shortly after, trying not to run out of breath, you return to the couch with her."
        scene 690762 with dissolve
        scene 690763 with dissolve
        m "I drank a little too much... I want to go back."
        scene 690762 with dissolve
        scene 690761 with dissolve
        e "But we've only just arrived!"
        scene 69057b with dissolve
        m "Let's go..."
        jump carafterdancelovefail
    elif ep6alcohol >3 and ep6alcohol <6 and domep6 > 7 or ep6alcohol >3 and ep6alcohol <6 and lustep6 > 7 :
        scene 69066 with dissolve
        "{color=#A8E4A0}{i}{size=-3} You dance together again, and [woman_name] is starting to loosen up more. Shortly after, trying not to run out of breath, you return to the couch with her."
        e "Phew...I’m tired but... shit you can move..."
        scene 69054talk2 with dissolve
        m "*Hic* You can... m-move too... What a dancer."
        scene 69054talk3 with dissolve
        e "You’re looking pretty hot out there. Those hips don’t lie."
        scene 69054talk4 with dissolve
        m "Stop it... You’re making me blush."
        scene 69054talk5 with dissolve
        e "See, that’s the point. I made it."
        scene 69054talk74 with dissolve
        m "*Hic*... Hmpf... You know, your dad never danced like you. I don’t know where you’ve got that dancer gene from."
        scene 69054talk73 with dissolve
        e "You’re not the first chick I take to the club, [woman_name]. But you could be the last if you happened to date me..."
        scene 69054talk72 with dissolve
        m "I... *hic*... I don’t know... Uh... Can I have another drink?"
        scene 69054talk73 with dissolve
        e "Oh so you’re straight-up asking now... Good..."
        scene 69060bar with dissolve
        "{color=#A8E4A0}{i}{size=-3} Back for more, you returned to the bar, calling the bartender."
        f "Third time’s the charm, huh? What can I get you?"
        menu:

            "One tequila drink. Make it double and a beer.":
                scene 69060bar2 with dissolve
                f "You got it, boss man."

            "One mojito and a beer.":
                scene 69060bar2 with dissolve
                f "Coming right up."

        "{color=#A8E4A0}{i}{size=-3} Once again, you walked your way back to where she was at, with your drinks in your hands."
        scene 69066b with dissolve
        e "Here you go..."
        scene 69066a with dissolve
        e "Wanna down it and head for another spin? I’m ready..."
        scene 69065 with dissolve
        m "Give me a break..."
        scene 69066c with dissolve
        e "Ah, come on... The night’s young... And you like young things, right?!"
        scene 69066a with dissolve
        m "*Hic* You little devil..."
        "{color=#A8E4A0}{i}{size=-3} Sip after sip, she began to worsen, and becoming more and more tipsy."
        scene 69066b with dissolve
        e "Woah, are you okay?!"
        scene 69066a with dissolve
        m "*Hic*... Y-Yeah... Sort of."
        scene 69066b with dissolve
        e "Good. Good enough."
        scene 69066c with dissolve
        m "Mhm..."
        scene 69066d with dissolve
        e "Come on, let’s hit the dancefloor again...!"
        m "Well... *hic*... Okay... If you insist...*hic*"
        scene black with Fade(2.0, 1.0, 1.0)
        jump nicdancingthird

    else:
        scene 69060a with dissolve
        "{color=#A8E4A0}{i}{size=-3} You dance together again, and [woman_name] is starting to loosen up more. Shortly after, trying not to run out of breath, you return to the couch with her."
        e "Phew...I’m tired but... shit you can move..."
        scene 69060f with dissolve
        m "You can move too! What a dancer."
        scene 69060e with dissolve
        e "You’re looking pretty hot out there. Those hips don’t lie."
        scene 69060f with dissolve
        m "Mhm..."
        scene 69060h with dissolve
        e "Want another drink?"
        scene 69060g with dissolve
        m "No... i think i'll pass now."
        scene 69060f with dissolve
        m "We can go back home. It was really fun!"
        scene 69060e with dissolve
        e "Ohh... okay..."
        scene black with Fade(2.0, 1.0, 1.0)
        jump carafterdancelovefail

label nicdancingthird:
    $ set_dance_menu_position()
    show nicdance2 with dissolve
    $ renpy.random.seed()
    $ current_image = renpy.random.choice([
        "Ep6/lefthand.png",
        "Ep6/righthand.png",
    ])

    show image current_image at title with dissolve

    menu (screen="dance"):
                "Left Hand":
                    if current_image == 'Ep6/lefthand.png':
                        show text "Who cares, just grope her..." with dissolve
                        hide text with dissolve
                        $ dancepoints3 += 1
                        jump check_points3
                    else:
                        show text "Who cares, just grope her..." with dissolve
                        hide text with dissolve
                        $ dancepoints3 += 1
                        jump check_points3
                "Right Hand":
                    if current_image == 'Ep6/righthand.png':
                        show text "Who cares, just grope her..." with dissolve
                        hide text with dissolve
                        $ dancepoints3 += 1
                        jump check_points3
                    else:
                        show text "Who cares, just grope her..." with dissolve
                        hide text with dissolve
                        $ dancepoints3 += 1
                        jump check_points3

label check_points3:
    if dancepoints3 >= 6:
        jump dance3gamewin
    else:
        jump nicdancingthird

label dance3gamewin:
            hide image current_image
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            pause 1
            $ lustep6 += 1
            show image "images/Stats/Dom[domep6].png" at statleft
            show image "images/Stats/Lust[lustep6].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[domep6].png"
            hide image "images/Stats/Lust[lustep6].png"
            hide text with dissolve
            scene 69075 with dissolve
            "{color=#A8E4A0}{i}{size=-3} As you danced, you began to grope her. From her waist to her cheeks and down to her thighs, you felt her slightly sweaty skin grip on your fingers."
            scene 69075a with dissolve
            pause
            scene 69075b with dissolve
            pause
            scene 69075c with dissolve
            scene nictouch738 with dissolve
            m "[player_name], not here..."
            scene nictouch739 with dissolve
            e "Why not? Nobody's really watching."
            scene nictouch740 with dissolve
            "{color=#A8E4A0}{i}{size=-3} But as you said that, you slipped a hand under her dress, and with a devilish smile, you ripped her panties out with one single hefty pull."
            scene nictouch738 with dissolve
            m "[player_name]! What are you doing?!"
            scene nictouch741 with dissolve
            e "Shh, just go with it. You know you want to."
            scene black with Fade(2.0, 1.0, 1.0)
            "{color=#A8E4A0}{i}{size=-3} Flustered, she walked back to the couch, and you followed her footsteps."
            scene 690760 with dissolve
            e "You alright? Thought we were having ‘special’ fun."
            scene 690761 with dissolve
            scene 690762 with dissolve
            scene 690763 with dissolve
            m "Yeah, just... just need to sit for a bit... *Hic*..."
            scene 690762 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Suddenly, and struggling to stand, she stood up and tipsy-walked around you, making her way to the dancefloor."
            scene 69057a with dissolve
            m "I think I'm gonna dance alone for a bit."
            scene 69057b with dissolve
            e "Wha...? ...Just don’t go too far away."
            scene black with Fade(2.0, 1.0, 1.0)
            "{color=#A8E4A0}{i}{size=-3} You finished your bear and lost any sight of her into the club’s dancing crowd."
            scene 69057c with dissolve
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} W-What? Where is she?"
            scene 69057d with dissolve
            "{color=#A8E4A0}{i}{size=-3} You quickly stood up, and started pushing through the people, searching for her."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Where the hell did she go?"
            scene 69057e with dissolve
            "{color=#A8E4A0}{i}{size=-3} She's nowhere to be found. Frustration and anxiety began to actually hit you and course through your veins."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn it, [woman_name]. Where are you?"
            scene black with Fade(2.0, 1.0, 1.0)
            "{color=#A8E4A0}{i}{size=-3} After a frantic search, you decided to arm yourself and check on the bathrooms."
            jump nicintoiletwithguy

label carafterdancelovefail:
    stop music
    play music "music/Forest.mp3"
    scene 69200carb with dissolve
    "{color=#A8E4A0}{i}{size=-3} You help her into the passenger seat, placing her butt on the soft cushioned seat, and then get into the driver's seat."
    scene 69200car1 with dissolve
    e "Are you okay?"
    scene 69200car2 with dissolve
    m "I'm just... really tired"
    scene 69200car1 with dissolve
    scene 69200car2 with dissolve
    m "You know..."
    scene 69200car1 with dissolve
    e "What?"
    scene 69200car3 with dissolve
    m "I just wanted to thank you for... behaving and... Being a good man."
    scene 69200car1 with dissolve
    e "You don't need to thank me..."
    scene 69200cartalk1 with dissolve
    m "..."
    scene 69200cartalk2 with dissolve
    e "After all... You're already thanking me be letting be by your side after... well... everything..."
    scene 69200cartalk1 with dissolve
    e "And, well... There's not a place where I'd like to be other than beside you..."
    scene 69200cartalk2 with dissolve
    e "You're the only one that I want, and as long as I'm here for you, everything will be alright..."
    play sound "music/snoring.mp3"
    e "..."
    scene 69200cartalk4 with dissolve
    e "Mhm... ok..."
    scene black with Fade(2.0, 1.0, 1.0)
    $ endingnothing = True
    play sound "music/snoring.mp3"
    jump sleepdressep6

label carafterdancelove:
    stop music
    play music "music/Forest.mp3"
    scene 69200carb with dissolve
    e "Come on, let's get you to the car. You need to rest."
    m "Ohhh... Alright... Careful, my legs hurt! *Hic*"
    e "I figured... Let me help you getting inside the car."
    scene 69200car with dissolve
    "{color=#A8E4A0}{i}{size=-3} You help her into the passenger seat, placing her on it, and then get into the driver's seat."
    scene 69200car1 with dissolve
    e "Are you okay? You look way too busted."
    scene 69200car2 with dissolve
    m "I'm just... really tired and a bit d-dizzy *Hic*"
    scene 69200car1 with dissolve
    scene 69200car2 with dissolve
    m "You know..."
    scene 69200car1 with dissolve
    e "What?"
    scene 69200car3 with dissolve
    m "I just wanted to thank you for... behaving and... *Hic*... Being a good man."
    scene 69200car1 with dissolve
    e "You don't need to thank me... I just wanted to take care of you, anyway. It wouldn’t have been a great idea to leave you there."
    scene 69200car2 with dissolve
    m "You can be sweet when you want to be, [player_name]."
    scene 69200car1 with dissolve
    e "You know I can be more than just sweet when I want to."
    scene 69200b with dissolve
    "{color=#A8E4A0}{i}{size=-3} You reach over and gently lift her legs, placing them on your lap. You start to massage her calves, trying to ease her discomfort, as you run your hands up and down her silky legs."
    scene 69200c with dissolve
    m "Mmm... That feels g-good..."
    scene 69200b with dissolve
    e "You know I only want to make you feel good... Thought a little rub would do better than massages..."
    scene 69200c with dissolve
    m "I know... I can... *Hic*... see that you're try-trying..."
    scene 69200b with dissolve
    "{color=#A8E4A0}{i}{size=-3} As you continue to massage her legs, you remember that you had taken off her panties while you were dancing."
    scene 69200c with dissolve
    e "You know, I can make you feel even better if you want."
    scene 69200b with dissolve
    m "W-What do you mean? *Hic*"
    scene 69200c with dissolve
    e "Trust me..."
label replayloveep6:
    scene 69200d with dissolve
    "{color=#A8E4A0}{i}{size=-3} You gently lift her dress, revealing her bare pussy to the air."
    scene 690082 with dissolve
    m "Mngh... W-Wha..."
    scene 690081 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You lean down and start to kiss her inner thighs, moving slowly upwards."
    scene 69202 with dissolve
    m "Oh... [player_name]... What are you doing?"
    scene 690081 with dissolve
    e "Shh... Just relax and enjoy it. I promise I'll make you feel good, you know what this tongue can do..."
    scene 69202a with dissolve
    "{color=#A8E4A0}{i}{size=-3} You continue to kiss and lick her thighs, moving closer to her throbbing pussy lips. She lets out a soft moan, her body responding to your touch."
    scene 69202b with dissolve
    m "Mmm... *Hic*"
    scene 69202a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Your dick throbbed in your pants to the scent of your [woman_role]’s pussy being so close to you, her heat, and her throbbing that almost matched yours."
    show niccarcl1 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You finally reach her watering pussy, and begin to lick her gently, your tongue exploring every sensitive spot. She moans softly, her body arching in pleasure."
    "{color=#A8E4A0}{i}{size=-3} You ran your tongue up and down, panting as you ate her warm and bittersweet pussy, with each lick sending mind bending pulses of pleasure across her body all the way up to her brain."
    "{color=#A8E4A0}{i}{size=-3} After a few licks of your relentless tongue, her pussy throbbed, and began to drool all over your mouth, lips, and tongue: She was getting too pent up, and the only thing that could satisfy her hungry pussy wasn’t your tongue."
    "{color=#A8E4A0}{i}{size=-3} You ran your tongue up from her bulging clit that throbbed everytime you jerked it with your tongue all the way down to her crack, where a small pool of pussy fluids began to form, casually sticking onto her skin, pulled by your tongue movements."
    e "God, you’re drooling a lot... You’re about to flood the damn seat..."
    "{color=#A8E4A0}{i}{size=-3} She blushed, ashamed of being unable to control her fluids, and even more ashamed of you noticing it."
    m "Oh f-fuck... [player_name]... S-Stop..."
    scene 690081 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You did as she asked, you stopped, sat down comfortably and pulled her towards you by her hands."
    scene 690081b with dissolve
    scene 690081c with dissolve
    e "Blow me."
    scene niczip with dissolve
    "{color=#A8E4A0}{i}{size=-3} She leans over and instantly starts to unzip your pants, her hands shaking slightly from the alcohol and excitement."
    scene 69213 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You gazed at her curves as she unzipped your pants, and you couldn’t help it but reach her back, and quickly slip her dress out, pulling it upwards. She followed your movements by stretching her arms so you could slip it easily."
    scene 69214 with dissolve
    m "T-Thanks..{p}Now, where... *hic*... was I?"
    show niccarlick
    "{color=#A8E4A0}{i}{size=-3} Without thinking it twice, she turned her face towards that hard, hot, and sticky cock  of yours, and began licking on your big, virile, bloated balls, as she caressed your shaft with her left cheek, and your tip spurted pre on her hair. "
    e "Mhgnh... You're so dirty when you're drunk..."
    "{color=#A8E4A0}{i}{size=-3} Without responding, perhaps out of embarrassment, she blushed even more, realizing she had no control over her actions. Her judgment was completely clouded by her feminine hormones responding to the scent of your young, virile cock."
    scene carbjstart_frame with dissolve
    "{color=#A8E4A0}{i}{size=-3} Quickly, without much hesitation, she took your cock and, with her lips planted on the tip of your glans, swallowed your entire cock in one go. Her throat bulged, and she made choking sounds."
    show niccarbj2
    pause
    e "Oh god... You're so good at sucking..."
    pause
    "{color=#A8E4A0}{i}{size=-3} With her head bobbing up and down, the saliva accumulating at your tip started to drip down to your balls, spreading across her lips and chin each time her face touched your balls. She seemed insatiable, like she couldn't stop. The alcohol had turned her into a cock-hungry slut."
    "{color=#A8E4A0}{i}{size=-3} Up and down she went. The sounds were incredibly lewd, like something out of a porno. It seemed too good to be true, but it was happening: your [woman_role] had thrown away her dignity to give in to her hormonal and drunken desire to choke on her [player_role]'s cock."
label carbjcamera:
    hide text with dissolve
    pause
    menu (screen="rightchoice"):
        "Change Camera":
            hide niccarbj2
            show niccarbj1
            jump carbjcamera2

        "{color=#FFD1DF}{i}*Compliment her blowing*":
            $ random_textcar = [
                "Mngh! Fuck! How can your mouth be this... hot and... tight?!",
                "Mngh... That's a good sucker...",
                "Ngh... Bet you love how that cock-pulsing feels on your lips",
                "Mmm... You're using your mouth for the second best thing it can do: Suck a real man's dick.",
                "Fuck... Those sounds you can do are driving me crazy...",
                "ou can suck it like a pornstar... Or well... A porn-[woman_role]..."
            ]
            show text "[random_textcar[textcar_index]]" at title with dissolve
            play sound "music/Mon.mp3"
            $ textcar_index = (textcar_index + 1) % len(random_textcar)
            pause
            jump carbjcamera
        "Continue":
            jump carbjend

label carbjcamera2:
    hide text with dissolve
    pause
    menu (screen="rightchoice"):
        "Change Camera":
            hide niccarbj1
            show niccarbj2
            jump carbjcamera

        "{color=#FFD1DF}{i}*Compliment her blowing*":
            $ random_textcar = [
                "Mngh! Fuck! How can your mouth be this... hot and... tight?!",
                "Mngh... That's a good sucker...",
                "Ngh... Bet you love how that cock-pulsing feels on your lips",
                "Mmm... You're using your mouth for the second best thing it can do: Suck a real man's dick.",
                "Fuck... Those sounds you can do are driving me crazy...",
                "ou can suck it like a pornstar... Or well... A porn-[woman_role]...",
            ]
            show text "[random_textcar[textcar_index]]" at title with dissolve
            play sound "music/Mon.mp3"
            $ textcar_index = (textcar_index + 1) % len(random_textcar)
            pause
            jump carbjcamera2
        "Continue":
            jump carbjend




label carbjend:
    "{color=#A8E4A0}{i}{size=-3} But unfortunately, you were about to cum. Her mouth was too eager, the pressure she applied with her cheeks as she sucked created a vacuum force that could draw out every last drop of your cum."
    e "Shit, shit... No... stop... I want to do something more before I come."
    scene 69211 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Confused, she stopped sucking and looked at you with concern."
    scene 69212 with dissolve
    "{color=#A8E4A0}{i}{size=-3} With one easy grab of your hand on her asscheeks, you pushed her inwards, towards you, and placed her right on top of your pulsing dick."
    scene 69212a with vpunch
    m "Mmngh..."
    "{color=#A8E4A0}{i}{size=-3} Unable to form a full sentence in approval, she just lowered herself, as her plump pussy lips allowed you into her tight, warm and soft hole, as she gasped on your way inside."
    scene niccumfin2 with vpunch
    m "Oh guh... Mfffm..."
    scene 69230 with dissolve
    e "God damn... You’re TIGHT..."
    show nicfckinside with dissolve
    "{color=#A8E4A0}{i}{size=-3} She starts to ride you, her hips moving in a rhythm that matches your thrusts. The car rocks gently with your movements."
    m "Guh... Mmm..."
    e "I reckon it’s fat but... Good god, you sound like I’ve melt your brain with my dick."
    "{color=#A8E4A0}{i}{size=-3} You continue to move together, your bodies in sync as you chase your own pleasure, still having in mind to make her cum and drool on your titanium hard cock."
    "{color=#A8E4A0}{i}{size=-3} Each smack of her ass on your thighs and balls felt like heaven. Her movements were fast, and never stopped for a break. Same pace, and always moving back and forth, clearly knowing how to stroke a dick with her cunt."
    "{color=#A8E4A0}{i}{size=-3} Smack after smack, slide after slide, her ass bounced as you didn’t need to guide it, although you had your hand placed on her left cheek just in case she needed to stop, and you didn’t feel like letting her: After all, it was your dick, and ‘your’ pussy too."
    "{color=#A8E4A0}{i}{size=-3} It was after all this combination of relentless pussy-drilling cock riding where her legs began to shake, her crack began to sweat and her moans began more and more depraved and careless, she was close, and it was her way to show it to you."
    show nicfckinside2 with dissolve
    show text "Hey, look, it's that sexy chick from the club with that young man!" with dissolve
    $ renpy.pause(3, hard=True)
    hide text
    show text "What a champ! Fucking such a mommy!" with dissolve
    $ renpy.pause(3, hard=True)
    hide text
    hide nicfckinside2
    show nicfckinside with dissolve
    m "Mngh...{p}C-Cum...."
    e "Ngh... Are you gonna cum too?"
    m "Mmgh..."
    e "Whatever you say... Fuck... Let’s cum together..."
    "{color=#A8E4A0}{i}{size=-3} With a final thrust, you can feel your fat balls retract and lift themselves up as they stick against the base of your fat cock, and smack over and over again her pussy, as she responds to the imminent cum bath by smacking her hips harder against you, completely lost in herself."
    scene niccumfin2 with vpunch
    play sound "music/niccum1.mp3"
    $ renpy.pause(1, hard=True)
    scene niccumfin3 with vpunch
    $ renpy.pause(1, hard=True)
    scene niccumfin2 with vpunch
    $ renpy.pause(1, hard=True)
    "{color=#A8E4A0}{i}{size=-3} Your balls empty themselves deep inside of her, pulsing, and filling her womb with your sticky sperm that made her feel as if she’s getting bloated."
    scene 69212a with dissolve
    play sound "music/niccum2.mp3"
    $ maxmccumep7 += 1
    "{color=#A8E4A0}{i}{size=-3} She collapses against you, her breath coming in short gasps as she’s now full of your cum..."
    m "Oh god... I..."
    e "Sh... It’s okay, it’s okay..."
    "{color=#A8E4A0}{i}{size=-3} She leans against you, her body relaxing as she drifts off to sleep, quickly beginning to snore."
    e "Oh, shit, you’re asleep?! Damn... That was fast..."
    e "Alright... Let’s get you home..."
    scene 69500 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You carefully lift her off your lap and help her back into the passenger seat. You start the car and drive your way back home, trying not to take fast turns or bumps."
    $ renpy.end_replay()
    scene black with Fade(2.0, 1.0, 1.0)
    $ endinglove = True
    "{color=#A8E4A0}{i}{size=-3} You had finally arrived to your house, and parked next to your house."
    scene 69998 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You carefully lift her out of the car, cradling her in your arms. She stirs slightly but doesn't wake up."
    scene 69999 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You carried her into the house and up to her bedroom, laying her gently on the bed, placing her butt first, and then slowly lowering her head onto the pillow."
    scene 69999b with dissolve
    "{color=#A8E4A0}{i}{size=-3} You took off her shoes and then lay down next to her"
    scene 69999c with dissolve
    e "Sleep tight..."
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} With a soft sigh, you close your eyes and drift off to sleep, holding her close, feeling her warmth radiate through your body."
    "{color=#A8E4A0}{i}{size=-3} Another night was done for, and by far, it had been your best one yet."
    jump endchapter6

label nicintoiletwithguy:
    play music "music/club.mp3"
    scene 69110 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Where the fuck is she going?..."
    y "How old are you, hot stuff?"
    m "I... I want to leave..."
    scene 69110a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's [woman_name]!"
    y "Hm... You look like a real sexy mommy who's looking to forget about her hubby for a while"
    y "How old are you... 40?"
    m "I'm.... I'm 37..."
    scene 69110b with dissolve
    y "Man...{p}I could be your stepson if you want...{p}You know what i mean... stepmom?"
    m "Uhm..."
    y "Yeah yeah, now get on yo' knees and take your stepson's dick up your mouth..."
    scene 69100 with vpunch
    e "What the fuck?!"
    scene 69100a with dissolve
    y "BACK THE FUCK OFF!"
    show text "Prepare! You need to kick his ass now." with dissolve
    with Pause(2)
    hide text with dissolve
    jump fight1


label fight1:
    # Losuj pozycję menu
    python:
        set_fight_menu_position()

    scene 69100a with dissolve
    if easyfight == False:
        $ timeout = 1
    elif easyfight == True:
        $ timeout = 1 + easyfight
    $ timeout_label = "fightlost"

    # Wyświetl menu walki
    menu (screen="fight"):
        "Punch him":
            play sound "music/punch1.mp3"
            jump fight2

label fight2:
    python:
        set_fight_menu_position()
    scene 69100b with vpunch
    scene 69100c with dissolve
    scene 69100d with dissolve
    if easyfight == False:
        $ timeout = 1
    elif easyfight == True:
        $ timeout = 1 + easyfight
    $ timeout_label = "fightlost"
    menu (screen="fight"):
        "Punch him":
            play sound "music/punch2.mp3"
            jump fight3

label fight3:
    python:
        set_fight_menu_position()
    scene 69100e with vpunch
    scene 69100f with dissolve
    scene 69100g with dissolve
    scene 69100h with dissolve
    scene 69100i with dissolve
    if easyfight == False:
        $ timeout = 1
    elif easyfight == True:
        $ timeout = 1 + easyfight
    $ timeout_label = "fightlost"
    menu (screen="fight"):
        "Dodge":
            play sound "music/dodge.mp3"
            jump fight4

label fight4:
    python:
        set_fight_menu_position()
    scene 69100j with dissolve
    if easyfight == False:
        $ timeout = 1
    elif easyfight == True:
        $ timeout = 1 + easyfight
    $ timeout_label = "fightlost"
    menu (screen="fight"):
        "Kick him":
            play sound "music/kick.mp3"
            jump fight5

label fight5:
    scene 69100k with vpunch
    scene 69100l with dissolve
    scene 69100m with dissolve
    scene 69100n with dissolve
    scene 69100o with dissolve
    scene 69100p with dissolve
    scene 69100r with dissolve
    m "[player_name], STOP"
    play sound "music/punch3.mp3"
    scene 69100s with vpunch
    scene 69100t with dissolve
    scene 69100u with dissolve
    e "YOU SON OF A BITCH!"


label fightwon:
    scene 69101 with dissolve
    e "He just fainted."
    scene 69101a with dissolve
    e "I hope you didn't stain my shirt with your blood."
    m "[player_name]..."
    if easyfight == False:
        if not easymode:
                $ achValid6 += 1
                $ achievement.grant("Achiev27")
                $ achievement.sync()
                if not persistent.achievement27:
                                             show Achiev27 at achievment with easeintop:
                                                        zoom 0.5
                                                        rotate_animation

                                             "You have received the achievement!{p}{b}\"Damn... what a hit!\"{/b}"
                                             "Number of achievements earned in this chapter [achValid6]/4"
                                             hide Achiev27
                                             $ persistent.achievement27 = True
    scene 69102 with dissolve
    e "And now... You..."
    scene 69102a with dissolve
    e "What the fuck was that?!"
    e "I just looked away for a moment and you took a random bastard to the bathroom!"
    scene 69102h with dissolve
    m "It... wasn't my fault..."
    scene 69102i with dissolve
    m "I told him I wasn't feeling so well, so I asked him to take me to the table, and he brought me here..."
    scene 69102f with dissolve
    m "B-But luckily, you came in just in time."
    scene 69102g with dissolve
    show image "images/Stats/Dom[domep6].png" at statleft
    show image "images/Stats/Lust[lustep6].png" at statright

    menu:
        "I think that’s bullshit. {size=-8}(Req. 5 Domination Points){/size}" if domep6 > 8 :
            hide image "images/Stats/Dom[domep6].png"
            hide image "images/Stats/Lust[lustep6].png"
            jump toiletfckep6

        "Okay, if you say so... Let’s head back to the car, just before his friends come for revenge, or something. {size=-8}(Req. 5 Lust Points for ending){/size}":
            hide image "images/Stats/Dom[domep6].png"
            hide image "images/Stats/Lust[lustep6].png"
            if lustep6 > 8:
                jump carafterdancelove
            else:
                jump carafterdancelovefail

label toiletfckep6:
    scene nicleaves9 with dissolve
    "{color=#A8E4A0}{i}{size=-3}The toilet door was slammed. That stupid son of a bitch probably got out."
    scene nicleaves9a with dissolve
    e "But first, I need to take a breath... this guy really pissed me off."
    scene 69102d with dissolve
    m "[player_name], let's get out of here... I don’t feel like staying anymore."
    scene 69102j with dissolve
    scene nicleaves0 with dissolve
    e "Stop right there. Where the fuck you think you’re going?"
    scene nicleaves0a with dissolve
    e "I know you wanted to fuck, so now we’re going to fuck."
    scene nicleaves0b with dissolve
    m "Wha...."
    $ nicdomrouteep5 = True
    if nicdomrouteep5 == True:
        scene 69103a with dissolve
        m "[player_name]! You promised you wouldn't do anything. Ugh! You don’t have a word!"
        scene 69103b with dissolve
        e "That was before you went to the bathroom with the first guy you came across, you harlot."
        e "Now get down, on your knees.{p}You're going to blow me in this club’s shitter like the nasty skank you are."
        scene 69103c with dissolve
        m "I don’t wanna do it! Not with you..."
        jump sucktoiletep6
    else:
        scene 69103d with dissolve
        m "I won't fuck with you."
        scene 69103a with dissolve
        m "Are you nuts?!"
        scene 69103c with dissolve
        jump sucktoiletep6

label sucktoiletep6:
    scene 69103c with dissolve
    "{color=#A8E4A0}{i}{size=-3}You didn't let her finish. With a strong movement, you made her kneel in front of you and you jumped out of your shorts."
    scene 69103e with dissolve
    "{color=#A8E4A0}{i}{size=-3}You're not sure if it's because she's drunk..."
    show toiletblowcam1
    "{color=#A8E4A0}{i}{size=-3}or maybe it's your dominant tone that had finally melted down her brain..."
    "{color=#A8E4A0}{i}{size=-3}...but your obedient [woman_role] just started sucking on your warm, already pre-cum dripping cock like a cock-hungry whore."
    "{color=#A8E4A0}{i}{size=-3}...Perhaps she’d finally come to her senses, and realized you were the only dick she’s ever needed."

label toiletsckcam1:
    pause
    menu (screen="leftchoice"):
        "Change Camera 1/4":
            hide toiletblowcam1
            show toiletblowcam2
            "{color=#A8E4A0}{i}{size=-3}Her lips seemed glued to your cock, as if your sweat and pre-cum had acted like glue to her bitchmade lips."
            e "Man, it’s like you’re getting better at it even after all those years of sucking dick."
            m "Mphf!"
            jump toiletsckcam2

        "Continue":
            jump toiletfckstart

label toiletsckcam2:
    pause
    menu (screen="leftchoice"):
        "Change Camera 2/4":
            hide toiletblowcam2
            show toiletblowcam3
            "{color=#A8E4A0}{i}{size=-3}Her desperate, excited pants were ragged and intense as you talked to her. You could feel her breath on your thick cock, drying it slightly, while her tongue lapped at it, coating it with her thick, viscous spit that she kept hawking up and drooling all over your shaft."
            e "Hell yeah, spit all over that thing...{p}Drool like if you’re getting paid for it, like a good whore."
            pause
            e "You could probably make a living out of it. Sucking dicks for a living... Or rather, living to suck this dick."
            jump toiletsckcam3

        "Continue":
            jump toiletfckstart

label toiletsckcam3:
    pause
    menu (screen="leftchoice"):
        "Change Camera 3/4":
            hide toiletblowcam3
            show toiletblowcam4
            "{color=#A8E4A0}{i}{size=-3}Her lips slid effortlessly, leaving a trail of her slobber all over your veiny length, the friction wiping away any trace of lipstick."
            e "I bet you’re pretending my cock’s tip is one of your merlot bottles, you drunk slut."
            e "Keep on going, the only liquid getting out of it will be my spunk."
            jump toiletsckcam4

        "Continue":
            jump toiletfckstart


label toiletsckcam4:
    pause
    menu (screen="leftchoice"):
        "Change Camera 4/4":
            hide toiletblowcam4
            show toiletblowcam1
            "{color=#A8E4A0}{i}{size=-3}You gripped her head firmly, guiding her, but even when you eased up, she kept bobbing her head back and forth on her own, almost automatically. To you, it seemed like you've already almost fully fried her brain."
            e "Shit! You’re even doing it by yourself... You’re cute for a bitch who failed being a good [woman_role] and now is her [player_role] cumslut."
            pause
            e "Moan if you agree."
            "{color=#A8E4A0}{i}{size=-3}She moaned on your cock, blushing, and swallowing her own spit afterwards."
            e "I knew it..."
            jump toiletsckcam1

        "Continue":
            e "Now, look at me."
            jump toiletfckstart


label toiletfckstart:
    scene 69140 with dissolve
    e "Get up"
    scene 69140a with dissolve
    e "You don't need this no more."
    scene 69140b with dissolve
    m "But... you took my panties..."
    scene 69140c with dissolve
    m "N-No! No, no, n-no..."
    scene 69140d with dissolve
    e "Calm down, I just want to help taking your dress off."
    scene 69140e with dissolve
    e "It's too expensive for you to fuck it up! I-I don't want to get it dirty."
    scene 69140ee with dissolve
    m "Oh...{p}*hic* okay..."
    scene 69140f with dissolve
    e "Now get on your knees next to the toilet"
    scene 69152 with dissolve
    m "W-Wha? What are you doing?!..."
    scene 69152a with vpunch
    e "I’m gonna fuck your shit up from behind right here like a whore."
    scene 69151 with dissolve
    m "Don't!!"
    e "Shut your mouth."
    scene 69150start with vpunch
    "{color=#A8E4A0}{i}{size=-3}It seemed like blowing you off was just enough foreplay for her pussy, making her so wet that her entrance was already half open, aching for your dick, to which you responded by sliding it in."
    m "What...AH!"
    show toiletep6
    pause
    "{color=#A8E4A0}{i}{size=-3}You felt like everything you'd always wanted was finally happening right before your eyes. There was no turning back after this, and you believed that both of you knew it."
    pause
    "{color=#A8E4A0}{i}{size=-3}Her pussy felt wet and tight, as if the vacuum created by your rough movements and your enormous size made your cock suck into her insatiable womb."
    pause
    "{color=#A8E4A0}{i}{size=-3}With each thrust, you made her breath quicken as your cock swelled more and more."
label toiletfckstart2:
    if slapach == True:
        if not easymode:
                $ achValid6 += 1
                $ achievement.grant("Achiev28")
                $ achievement.sync()
                if not persistent.achievement28:
                                             show Achiev28 at achievment with easeintop:
                                                        zoom 0.5
                                                        rotate_animation

                                             "You have received the achievement!{p}{b}\"Someone here likes spanking.\"{/b}"
                                             "Number of achievements earned in this chapter [achValid6]/4"
                                             hide Achiev28
                                             $ persistent.achievement28 = True
    show toiletep6
    pause
    menu (screen="rightchoice"):
       "Spank her":
            hide toiletep6
            show slapep6 with dissolve
            $ slaptoilet += 1
            if slaptoilet == 1:
                show text "With one stiff slap on her round ass, you smacked it so loud it even over-thrown the music in the back in terms of loudness." with dissolve
            elif slaptoilet == 2:
                show text "Take this!" with dissolve
            elif slaptoilet == 3:
                show text "And this!" with dissolve
            elif slaptoilet == 4:
                show text "Fucking slut!" with dissolve
            elif slaptoilet == 5:
                $ slapach = True
                show text "Want sum’ more?" with dissolve
                $ slaptoilet = 0
            $ renpy.pause(2.5, hard=True)
            hide text with dissolve
            jump toiletfckstart2
       "Continue":
            "{color=#A8E4A0}{i}{size=-3}With your hips thrusting hard against your [woman_role]'s ass, you could feel your balls, full of sperm ready to impregnate her, slapping against her pussy lips over and over again."
            jump cummingep6toilet


label cummingep6toilet:
    menu (screen="rightchoice"):
        "Cum inside":
            hide toiletep6
            show cmintoil
            $ renpy.pause(3, hard=True)
            "{color=#A8E4A0}{i}{size=-3}You couldn’t hold back no more, so with one final hefty smack of your hips against her cheeks, you emptied your balls inside her warm cunt, blasting her uterus in the process with your sperm."
            e "FUUUUUCK..."
            scene 69153 with dissolve
            e "Mmm... Fuck... Just look at that pretty pussy of yours, all gaped and drooling out my nut."
            show cminsep6
            e "It was about time it drooled with something that isn’t your own fluids, slut."
            jump leaveclub


        "Cum on her back":
            show befcmtoil with dissolve
            m "{color=#ffa500}{i}*Breathing heavily*{/i}{/color}"
            e "I'm sure you'd rather have it inside... but I'd rather spray my nut all over your slutty body so everyone sees it."
            show cmtoiletback
            $ renpy.pause(3, hard=True)
            e "What a nice view..."
            jump leaveclub


label fightlost:
    scene toiletlost with vpunch
    "You Lost!"
    "You can make this fight easier or just skip it."
    if easyfight == 0:
        menu:
            "Let me punch this bro again!!":
                jump nicintoiletwithguy
            "Make it easier for me! (No achievement)":
                $ easyfight += 1
                jump nicintoiletwithguy
            "Skip it, i hate these minigames (No achievement)":
                jump fight5
    elif easyfight > 0:
        menu:
            "This speed is ok for me (No achievement)":
                jump nicintoiletwithguy
            "Make it even more easier for me! (No achievement)":
                $ easyfight += 1
                jump nicintoiletwithguy
            "Skip it, i hate these minigames (No achievement)":
                jump fight5

label leaveclub:
    $ maxmccumep7 += 1
    scene 69142 with dissolve
    e "Get it together. I'll wait outside. We're going home."
    $ renpy.end_replay()
    scene black with Fade(4.0, 1.0, 2.0)
    y "That lucky bastard scored a real hottie."
    y "Cougars weren't that bloodthirsty when I was about his age..."
    y "She could be his [woman_role]!"
    stop music
    play music "music/Forest.mp3"
    scene 69200carb with dissolve
    "{color=#A8E4A0}{i}{size=-3} You help her into the passenger seat, placing her butt on the soft cushioned seat, and then get into the driver's seat."
    scene 69200cartalk1 with dissolve
    m "..."
    scene 69200cartalk2 with dissolve
    e "..."
    scene 69200cartalk1 with dissolve
    e "..."
    scene 69200cartalk2 with dissolve
    e "....."
    play sound "music/snoring.mp3"
    e "..."
    scene 69200cartalk4 with dissolve
    e "Mhm..."
    scene black with Fade(2.0, 1.0, 1.0)
    $ endingdomino = True
    play sound "music/snoring.mp3"
    jump sleepdressep6

label sleepdressep6:
    scene 69998dress with dissolve
    "{color=#A8E4A0}{i}{size=-3} You carefully lift her out of the car, cradling her in your arms. She stirs slightly but doesn't wake up."
    scene 69999dress with dissolve
    "{color=#A8E4A0}{i}{size=-3} You carried her into the house and up to her bedroom, laying her gently on the bed, placing her butt first, and then slowly lowering her head onto the pillow."
    scene 69999b with dissolve
    "{color=#A8E4A0}{i}{size=-3} You took off her shoes and then lay down next to her"
    scene 69999c with dissolve
    e "Sleep tight..."
    scene black with Fade(2.0, 1.0, 1.0)
    "{color=#A8E4A0}{i}{size=-3} With a soft sigh, you close your eyes and drift off to sleep, holding her close, feeling her warmth radiate through your body."
    "{color=#A8E4A0}{i}{size=-3} Another night was done for, and by far, it had been your best one yet."

    jump endchapter6

label endchapter6:
    show text "{size=+5}End of Chapter 6{/size}" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)

    jump statsep6

label statsep6:

     $ achVall = achValid + achValid2 + achValid3 + achValid4 + achValid5 + achValid6
     if not easymode:
         "So far you have achieved {b}[achVall]{/b} out of 28 available achievements!"
         if tomscstat == 1:
            "...and 1/1 secret achievement...:-)"
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

     scene black with fade

     jump episode7
