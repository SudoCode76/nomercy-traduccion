default nicolecmep4lick = 0
default auntbjtalkep4 = 0
default auntbjtalk2ep4 = 0
default auntpussytalkep4 = 0
default auntpussytalk2ep4 = 0
default auntsextalkep4 = 0
default auntsextalk2ep4 = 0
default dadphoneno = 0
default kissherep4stat = 0
default nicoledomep4 = 4
default nicolelustep4 = 4
default achValid4 = 0
default givemoneyep4 = False
default aunttalk1 = 0
default aunttalk2 = 0
default aunttalk3 = 0
default blockeasy = False
default easyphoto = 0
default easycomputer = 0
default dobrzeep3nicfactor = False
default zleep3nicfactor = False
default dobrze2ep3nicfactor = False
default zle2ep3nicfactor = False

default endingep4 = 0
default nicoledomending = False
default nicolelustending = False

default riddlebirthday = 0
default riddlebottle = 0
default riddlebra = 0
default riddledateagain = 0
default riddledress = 0
default riddlehair = 0
default riddlelocker = 0
default riddlemobile = 0
default riddlenick = 0
default riddlenight = 0
default riddlenotebook = 0
default riddlespring = 0
default riddlewatch = 0

default clickcomputer = 0
default kickcomputer = 0
default ctrlaltdelclick = 0
default browseropen = 0
default perktip = False

image talkep4 = Movie(play="images/Ep4/talkep4.webm", loop=False, image="40107")
image grabep4 = Movie(play="images/Ep4/grabep4.webm", loop=False, image="40108")
image grabep42 = Movie(play="images/Ep4/grabep42.webm", loop=False, image="40108a")
image grabep43 = Movie(play="images/Ep4/grabep43.webm", loop=False, image="40110a")
image feetmsgep4 = Movie(channel="movie_dp", play = "images/Ep4/feetmsgep4.webm")
image lickloopep4 = Movie(channel="movie_dp", play = "images/Ep4/lickloopep4.webm")
image cameradownep4 = Movie(play="images/Ep4/cameradownep4.webm", loop=False, image="40020")
image pantsdownep4 = Movie(play="images/Ep4/pantsdownep4.webm", loop=False, image="40020b")
image orgnicoep4 = Movie(play="images/Ep4/orgnicoep4.webm", loop=False, image="40021")
image afterbjep4 = Movie(play="images/Ep4/afterbjep4.webm", loop=False, image="aftercmep4")
image ep4cm = Movie(play="images/Ep4/ep4cm.webm", loop=False, image="bjep4cm")
image slapep4 = Movie(play="images/Ep4/slapep4.webm", loop=False, image="afterslapep4")
image homean = Movie(play="images/Ep4/homean.webm", loop=False, image="40036")
image nicocmep4 = Movie(play="images/Ep4/nicocmep4.webm", loop=False, image="40019b")
image stoplck = Movie(play="images/Ep4/stoplck.webm", loop=False, image="40023")
image walking = Movie(play="images/Ep4/walking.webm", loop=False, image="walkingend")
image cmep4 = Movie(play="images/Ep4/cmep4.webm", loop=False, image="cmep4sc")
image cleanbefore = Movie(play="images/Ep4/cleanbefore.webm", loop=False, image="cleanlastframe")
image beforekissep4 = Movie(play="images/Ep4/beforekissep4.webm", loop=False, image="endbeforekiss")
image ep4afterkiss = Movie(play="images/Ep4/ep4afterkiss.webm", loop=False, image="40301")
image shirtep4 = Movie(play="images/Ep4/shirtep4.webm", loop=False, image="shirtdown")
image bjfinalep4 = Movie(channel="movie_dp", play = "images/Ep4/bjfinalep4.webm")
image ancar = Movie(channel="movie_dp", play = "images/Ep4/ancar.webm")
image transitionep4 = Movie(channel="movie_dp", play = "images/Ep4/transitionep4.webm")
image garden = Movie(channel="movie_dp", play = "images/Ep4/garden.webm")
image gardentalk = Movie(channel="movie_dp", play = "images/Ep4/gardentalk.webm")
image ep4ff = Movie(channel="movie_dp", play = "images/Ep4/ep4ff.webm")
image handep4 = Movie(channel="movie_dp", play = "images/Ep4/handep4.webm")
image mcsee = Movie(channel="movie_dp", play = "images/Ep4/mcsee.webm")
image headan = Movie(channel="movie_dp", play = "images/Ep4/headan.webm")
image lake = Movie(channel="movie_dp", play = "images/Ep4/lake.webm")
image hjep4solo = Movie(channel="movie_dp", play = "images/Ep4/hjep4solo.webm")
image ep4lickmc = Movie(channel="movie_dp", play = "images/Ep4/ep4lickmc.webm")
image kissep4 = Movie(channel="movie_dp", play = "images/Ep4/kissep4.webm")
image fjep4 = Movie(channel="movie_dp", play = "images/Ep4/fjep4.webm")
image fjep4v2 = Movie(channel="movie_dp", play = "images/Ep4/fjep4v2.webm")
image sidefjep4 = Movie(channel="movie_dp", play = "images/Ep4/sidefjep4.webm")


label episode4:
    stop music fadeout 1.0
    play music "music/Mn.wav"

    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 4" at title with dissolve
    $ renpy.pause(2, hard=True)

    scene 40001 with dissolve
    if easymode:
        show text "Easy Mode points!"
        show image "images/Stats/Dom[nicoledomep4].png" at statleft
        show image "images/Stats/Lust[nicolelustep4].png" at statright
        pause 1
        $nicolelustep4 += 2
        $nicoledomep4 += 2
        show image "images/Stats/Dom[nicoledomep4].png" at statleft
        show image "images/Stats/Lust[nicolelustep4].png" at statright
        pause 1
        hide text
    if endingep2full == True:
        show text "You gain a dominance point for your actions in Episode 2." with dissolve
        with Pause(3)
        show image "images/Stats/Dom[nicoledomep4].png" at statleft
        show image "images/Stats/Lust[nicolelustep4].png" at statright
        pause 1
        $ nicoledomep4 += 1
        show image "images/Stats/Dom[nicoledomep4].png" at statleft
        show image "images/Stats/Lust[nicolelustep4].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[nicoledomep4].png"
        hide image "images/Stats/Lust[nicolelustep4].png"
        hide text with dissolve
        with Pause(1)

    if endingep3full == True:
        show text "You gain a Lust point for your actions in Episode 3." with dissolve
        with Pause(3)
        show image "images/Stats/Dom[nicoledomep4].png" at statleft
        show image "images/Stats/Lust[nicolelustep4].png" at statright
        pause 1
        $ nicolelustep4 += 1
        show image "images/Stats/Dom[nicoledomep4].png" at statleft
        show image "images/Stats/Lust[nicolelustep4].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[nicoledomep4].png"
        hide image "images/Stats/Lust[nicolelustep4].png"
        hide text with dissolve
        with Pause(1)

    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    pause 1
    scene 40001a with dissolve
    pause
    scene 40001b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She got up early"
    scene 40002 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I really hope she didn't run away from home after what happened yesterday..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} It was probably the best day of my life"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Just like in those computer games"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Only this time it's for real"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Should I cut her some slack?"

    if easymode:
        menu:

                "Maybe I should be a little better to her\n{color=#3d85c6} +1 Lust Point" :
                          jump ep4better

                "No mercy\n{color=#3d85c6} +1 Dom Point":
                          jump ep4nomercy

    else:
        menu:

                "Maybe I should be a little better to her":
                          jump ep4better

                "No mercy":
                          jump ep4nomercy



label ep4better:
    scene 40002b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Maybe a little..."
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump getupep4

label ep4nomercy:
    scene 40002a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Nah... she needs proper treatment "
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump getupep4


label getupep4:
    scene 40003 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I need to check if my dad left any money"
    scene black with fade
    scene 40080 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Great"
    scene 40081 with dissolve
    e "500 bucks"
    $ money += 500
    show text "{color=#00ff00}{size=+15}+5 0 0 ${/color}" with dissolve
    with Pause(2)
    "{i}Total: [money]$"
    hide text with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} It's not enough, but it's still something..."
    scene 40084 with dissolve
    pause
    scene 40084a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} No new messages..."
    scene 40082 with dissolve
    "{i}You hear screams from the next room"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I wonder what this is about..."
    scene 40083 with dissolve
    m "BUT HOW IS IT BLOCKED?!"
    scene 40083a with dissolve
    m "You went away for a week and your account is blocked?!"
    m "You know that I get paid only in 2 weeks?!"
    m "How do you think!??!?"
    m "Today is the last day to pay your electricity bill."
    scene 40083 with dissolve
    m "THIS MUST BE PAID TODAY"
    scene 40083b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Yay, they can't turn off the electricity, they have to pay it today."
    m "..."
    m "...."
    scene 40083a with dissolve
    m "And who is supposed to lend me money?! You know how difficult it is for everyone right now, no one has money"
    m "NO"
    m "I WILL NOT TAKE ANYTHING FROM HIM"
    m "..."
    m "What will you do?!"
    m "I had all my money in a joint account with you, and somehow you didn't say that it was a hopeless idea"
    scene 40083 with dissolve
    m "I’VE HAD ENOUGH OF YOU"
    scene 40083a with dissolve
    m "F u c k!"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} oh, someone is extremely pissed off..."
    m "Hey, can you come over here? Something happened and I need your help quick."
    scene 40083c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Hmm, I wonder who she called..."
    scene 40084 with dissolve
    "{color=#ffa500}{i}*Phone ringing*{/i}{/color}"
    scene 40084dad with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Father calls"
    show screen hint ("I have a feeling this is a very important phone call.")
    if easymode:
        menu:

            "{color=#FFD1DF}{i}*Pick up the phone*{/i}{/color}":
                hide screen hint
                jump phone1ep4

            "{color=#FFD1DF}{i}*Don't answer*{/i}{/color} \n{color=#3d85c6} No final scene in next episode ":
                hide screen hint
                jump nophone1ep4

    else:
        menu:

            "{color=#FFD1DF}{i}*Pick up the phone*{/i}{/color}":
                hide screen hint
                jump phone1ep4

            "{color=#FFD1DF}{i}*Don't answer*{/i}{/color}":
                hide screen hint
                jump nophone1ep4

label nophone1ep4:
    scene 40084b with dissolve
    $ dadphoneno += 1
    $ dadfriend -= 1
    e "I don't have time now, let him call me later."
    jump checkwomanep4

label phone1ep4:
    scene 40085a with dissolve
    e "Hey what's up?"
    scene 40085b with dissolve
    d "Hello, can you talk?... or just answer casually so Nicole doesn't know it's me."
    scene 40085 with dissolve
    e "Mhm"
    scene 40085b with dissolve
    d "I completely forgot about the electricity bill, and I have already blocked it and now I have no way to pay"
    d "Give Nicole the money, when I come back, I'll pay you again"

    if easymode:
        show screen hint ("I think this decision will have a huge impact.")
        menu:
                "It's MY money and it was meant for me, I won't give it to her.\n{color=#3d85c6} Dad -2":
                    hide screen hint
                    $ dadfriend -= 2
                    jump nophone2ep4

                "Sure, dad, no problem \n{color=#3d85c6} Dad +1, -500$":
                    hide screen hint
                    $ dadfriend += 1
                    $ givemoneyep4 = True
                    jump phone2ep4

    else:
        show screen hint ("I think this decision will have a huge impact.")
        menu:
                "It's MY money and it was meant for me, I won't give it to her.":
                    hide screen hint
                    $ dadfriend -= 2
                    jump nophone2ep4

                "Sure, dad, no problem":
                    hide screen hint
                    $ dadfriend += 1
                    $ givemoneyep4 = True
                    jump phone2ep4
label nophone2ep4:
    scene 40085b with dissolve
    d "Erm... well..."
    d "Not nice of you, think about it again"
    scene 40085a with dissolve
    e "I thought about it, I need this money"
    scene 40085b with dissolve
    d "Ok... Bye"
    scene 40084b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I can't give back all the money, I need it"
    jump checkwomanep4

label phone2ep4:
    scene 40085 with dissolve
    e "Sure no problem"
    scene 40085b with dissolve
    d "Thanks a lot, man. I’m glad I left you some more!"
    d "Take care, bye!!"
    scene 40084b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Fuck, i need this money..."
    jump checkwomanep4

label checkwomanep4:
    scene 40084b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Let's see what my [woman_role] is doing..."
    scene black with fade
    scene 40008 with dissolve
    e "Hey, can I come in?"
    m "..."
    m "Now you ask?"
    scene 40009 with dissolve
    e "I'm not a psycho, I just want to talk to you, that’s all."
    m "..."
    scene 40010 with dissolve
    e "About yesterday..."
    scene 40010talk with dissolve
    m "You turned my life into a living nightmare in just 2 days."
    scene 40010talk2 with dissolve
    m "I can't live like this..."
    m "I didn't expect you to be capable of... such things."
    scene 40010talk3 with dissolve
    m "When did you change this suddenly, [player_name]?"
    m "When did you stop treating me as a [woman_role] and start treating me like... fucktoy?"

    if easymode:
        menu:
                "I haven't changed at all, it's all because of you.\n{color=#3d85c6} +1 Lust Point, -1 Dom Point":
                            jump alwaysbecauseofyouep4

                "From the day you stopped caring about the rest of your family.\n{color=#3d85c6} +1 Dom Point, -1 Lust Point":
                            jump notcarefamilyep4

    else:
        menu:
                "I haven't changed at all, it's all because of you.":
                            jump alwaysbecauseofyouep4

                "From the day you stopped caring about the rest of your family.":
                            jump notcarefamilyep4


label alwaysbecauseofyouep4:
    scene 40010listen with dissolve
    e "Every time I looked at you, I saw you as a beautiful woman, not just a [woman_role]"
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 1
    $ nicoledomep4 -= 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump bedroomtalk1ep4

label notcarefamilyep4:
    scene 40010listen2 with dissolve
    e "Because you chose to suck another guy's dick instead of saving your relationship with my dad."
    e "So I figured out: You might as well suck mine."
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 1
    $ nicolelustep4 -= 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump bedroomtalk1ep4


label bedroomtalk1ep4:
    scene 40010listen2 with dissolve
    e "You could invite a friend into your bedroom, and thought I wouldn’t notice, or suspect about you cheating?{p}How old do you think I am? Or rather: Do you think I’m retarded?"
    e "These walls aren't thick at all, I heard every moan you made… And it turned me on every time."
    scene 40010listen with dissolve
    e "Every time you did… All I wanted to do is just… Come in and join, and fuck you up."
    scene 40010talk with dissolve
    m "It's terrible what you’re saying..."
    m "I didn't expect you to be capable of... something like this."


    if easymode:
        menu:
                 "Pfft... I’m sure you didn’t expect me to fuck your mouth that well.\n{color=#3d85c6} +1 Dom Point":
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             pause 1
                             $ nicoledomep4 += 1
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             with dissolve
                             pause 3
                             hide image "images/Stats/Dom[nicoledomep4].png"
                             hide image "images/Stats/Lust[nicolelustep4].png"
                             jump bedroomtalk2ep4

                 "That you and your [player_role] will cum while sitting in front of the TV with your mouth full of his cum? {size=-8}(Req. Episode 3 Full Ending){/size}\n{color=#3d85c6} +1 Dom Point, +1 Lust Point" if endingep3full == True:
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             pause 1
                             $ nicolelustep4 += 1
                             $ nicoledomep4 += 1
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             with dissolve
                             pause 3
                             hide image "images/Stats/Dom[nicoledomep4].png"
                             hide image "images/Stats/Lust[nicolelustep4].png"
                             jump bedroomtalk2ep4

                 "I didn't expect many things from you either... \n{color=#3d85c6} +1 Love point (Important in later episodes)":
                             $ niclovebonusfactor += 1
                             jump didntexpecteither

    else:
        menu:
                 "Pfft... I’m sure you didn’t expect me to fuck your mouth that well.":
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             pause 1
                             $ nicoledomep4 += 1
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             with dissolve
                             pause 3
                             hide image "images/Stats/Dom[nicoledomep4].png"
                             hide image "images/Stats/Lust[nicolelustep4].png"
                             jump bedroomtalk2ep4

                 "That you and your [player_role] will cum while sitting in front of the TV with your mouth full of his cum? {size=-8}(Req. Episode 3 Full Ending){/size}" if endingep3full == True:
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             pause 1
                             $ nicolelustep4 += 1
                             $ nicoledomep4 += 1
                             show image "images/Stats/Dom[nicoledomep4].png" at statleft
                             show image "images/Stats/Lust[nicolelustep4].png" at statright
                             with dissolve
                             pause 3
                             hide image "images/Stats/Dom[nicoledomep4].png"
                             hide image "images/Stats/Lust[nicolelustep4].png"
                             jump bedroomtalk2ep4

                 "I didn't expect many things from you either...":
                             $ niclovebonusfactor += 1
                             jump didntexpecteither



label bedroomtalk2ep4:
    scene 40010talk3 with dissolve
    m "Can you even still talk normally?"
    m "You just keep insulting me and saying all these perverted things…"
label didntexpecteither:
    scene 40010talk3 with dissolve
    m "You're just forcing me to do all this, I didn't want it at all"
    scene 40010listen2 with dissolve
    e "But what difference does it make, a dick is a dick, if you want them that much, it's right in front of you."
    e "Literally in front of you."
    scene 40010talk3 with dissolve
    m "Again, you’re the one forcing me to do all these things and you think you're doing something good? Of course not. You know what you’re doing."
    m "And you tell yourself that you're doing the right thing because I did something wrong..."
    m "The best [player_role] in the world."
    scene 40010listen2 with dissolve
    e "You're hurting my dad, he loves you, but I think it's about something else."

    if easymode:
        menu:

                 "What’s the problem? Didn’t I satisfy you every time we fucked?\n{color=#3d85c6} +1 Lust Point":
                             jump bedroomtalk3choice1ep4

                 "We guys love to dominate, you love to be dominated, admit you’re turned on by it. Don’t lie to yourself.\n{color=#3d85c6} +1 Dom Point":
                             jump bedroomtalk3choice2ep4

    else:
        menu:

                 "What’s the problem? Didn’t I satisfy you every time we fucked?":
                             jump bedroomtalk3choice1ep4

                 "We guys love to dominate, you love to be dominated, admit you’re turned on by it. Don’t lie to yourself.":
                             jump bedroomtalk3choice2ep4


label bedroomtalk3choice1ep4:
    scene 40010talk with dissolve
    m "NO, I didn't say anything like that"
    scene 40010listen with dissolve
    e "But you definitely thought about it"
    scene 40010talk with dissolve
    m "Not true..."
    e "Every time I touch you there, you get all wet. You can’t fight your natural sex urges back."
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump bedroomtalk3ep4


label bedroomtalk3choice2ep4:
    scene 40010talk3 with dissolve
    m "Where are you getting all of this from, the internet?"
    m "You have no idea about women and how to treat them, you sexist pig."
    scene 40010listen2 with dissolve
    e "I think I'm doing quite well"
    e "Every time I touch you there, you get all wet"
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump bedroomtalk3ep4


label bedroomtalk3ep4:
    scene 40010listen with dissolve
    e "Besides, don't you like me?"
    e "You always said I was handsome"
    scene 40010talk with dissolve
    m "Not handsome like that, jerk!"
    scene 40011 with dissolve
    e "So, how?"
    scene 40012 with dissolve
    m "What are you doing...?"
    scene 40013 with dissolve
    pause 0.5
    scene 40014 with dissolve
    pause 0.5
    scene 40015 with dissolve
    pause 0.5
    scene 40016 with dissolve
    pause 0.5
    m "Get off me"

label menunicoletalk:
    scene 40017 with dissolve

    if easymode:
        menu:

                 "{color=#FFD1DF}{i}*Cunnilingus her*{/i}{/color} \n{color=#3d85c6} Lust points but don't say anything!":
                             jump lickpussyep4

                 "{color=#FFD1DF}{i}*Fuck her mouth*{/i}{/color} \n{color=#3d85c6} Dom Points":
                             jump fuckthroatep4

                 "{color=#FFD1DF}{i}*Kiss her*{/i}{/color} \n{color=#3d85c6} It gives you achievement in normal mode" if kissherep4stat == 0:
                             jump kissherep4
    else:
        menu:

                 "{color=#FFD1DF}{i}*Cunnilingus her*{/i}{/color}":
                             jump lickpussyep4

                 "{color=#FFD1DF}{i}*Fuck her mouth*{/i}{/color}":
                             jump fuckthroatep4

                 "{color=#FFD1DF}{i}*Kiss her*{/i}{/color}" if kissherep4stat == 0:
                             jump kissherep4


label kissherep4:

    $ kissherep4stat = 1
    scene black with fade
    e "..."
    scene mcstop2 with dissolve
    e "Sir, I would like to kindly remind you that the title of this game is No Mercy."
    e "..."
    e "...."
    e "....."
    e "IF YOU WANT TO KISS SOMEONE JUST GO AND ROLEPLAY IT SOMEWHERE ELSE."
    e "..."
    e "...."
    scene mcstop3 with dissolve
    e "Rollback"
    e "......"
    e "......."
    e "[woman_name] is waiting for you."
    scene mcstop4 with dissolve
    e "......."
    e "I can sit here for hours, you'll be the one paying the electricity bill."
    e "........"
    scene mcstop5 with dissolve
    e "Ok, bro. I can give you the achievement for this{p}BUT NO KISSING SCENE...{p}yet."
    if not easymode:
        $ achValid4 += 1
        $ achievement.grant("Achiev11")
        $ achievement.sync()
        if not persistent.achievement11:
                 show Achiev11 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                 "You have received the achievement!{p}{b}\"Romantic psycho\".{/b}"
                 "Number of achievements earned in this chapter [achValid4]/5"
                 hide Achiev11
                 $ persistent.achievement11 = True
    e "If you don't want to go back on your own, let me help you"
    jump menunicoletalk

label lickpussyep4:

    scene 40016 with dissolve
    e "[woman_role]..."
    scene 40018 with dissolve
    e "..."
    show cameradownep4
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3}You reach down to her panties, as you slide your hands down her soft, warm thighs, feeling the soft touch of her skin against your desperate hands."
    e "What do we have here..."
    show pantsdownep4
    $ renpy.pause(6, hard=True)
    m "[player_name] please stop"
    show lickloopep4
    "{color=#A8E4A0}{i}{size=-3}Huffing, and sniffing, you take your meal to your mouth. With your tongue, you begin to lick on her pussy lips, as her fluids travel to your tastebuds, bending your mind drunk."
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 1
    $ nicoledomep4 -= 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    m "Ah..."
    show screen hint("It's hard to focus on something and still say anything...")
    $ timeout_label = "lickpussyep4_1good"
    menu:
        "You smell... beautiful":
            "..."
            jump lickpussyep4_1
        "Is it good for you?":
            "..."
            jump lickpussyep4_1

label lickpussyep4_1good:
    $ nicolecmep4lick += 1
    show text "{i}She moans..." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    jump lickpussyep4_1

label lickpussyep4_1:

    $ timeout_label = "lickpussyep4_2good"
    menu:
        "Do you like what I’m doing?":
            "..."
            jump lickpussyep4_2
        "I don't think anyone has licked you like this in a looong time":
            "..."
            jump lickpussyep4_2

label lickpussyep4_2good:
    $ nicolecmep4lick += 1
    show text "{i}Ahhh...." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    jump lickpussyep4_2

label lickpussyep4_2:

     if nicolecmep4lick == 2:
        $ timeout_label = "juzpogood"
     else:
        $ timeout_label = "juzpo"

     menu:
         "I'm good, right?":
             jump juzpo
         "Am I talking too much?":
             jump juzpo

label juzpogood:
    hide screen hint
    $ niclovebonusfactor += 4
    $ dobrzeep3nicfactor = True
    show nicocmep4
    $ renpy.pause(5, hard=True)
    show text "{i}She moaned, gripping your head tighter" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)
    show text "{i}She certainly enjoyed it. Every bit of it." with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    with Pause(1)
    $ renpy.end_replay()
    scene 40019 with dissolve
    if not easymode:
        $ achValid4 += 1
        $ achievement.grant("Achiev12")
        $ achievement.sync()
        if not persistent.achievement12:
                 show Achiev12 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                 "You have received the achievement!{p}{b}\"Silence is golden\".{/b}"
                 "Number of achievements earned in this chapter [achValid4]/5"
                 hide Achiev12
                 $ persistent.achievement12 = True
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 2
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"

    menu:

        "{color=#FFD1DF}{i}*Fuck her mouth*{/i}{/color}{size=-8} (Req. 2 Lust and 1 Domination Point) " if nicolelustep4 > 5 and nicoledomep4 > 4:
            jump fuckthroatep4cm
        "Leave her":
            jump endlickep4

label juzpo:
    hide screen hint
    show stoplck with vpunch
    $ renpy.pause(2, hard=True)
    m "STOP"
    scene 40024 with dissolve
    m "Leave my room{p}NOW!"
    e "I don't think I can make her cumming..."
    $ renpy.end_replay()


    menu:
             "{color=#FFD1DF}{i}*Jump on her*{/i}{/color} {size=-8}(Req. 3 Domination Points){/size} or {color=#00ff00}25\%\ chance{/color}":
                  jump fuckthroatep4chance
             "{color=#FFD1DF}{i}*Leave room*{/i}{/color}":
                  e "Let it be, I just wanted you to feel nice..."
                  jump ancoming


label fuckthroatep4chance:
    if nicoledomep4 > 6:
        jump fuckthroatep4

    $ fuckthroatep4chanceint = renpy.random.randint(1, 100)
    if fuckthroatep4chanceint >= 75:
        show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        jump fuckthroatep4
    else:
        show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        e "Let it be, I just wanted you to feel nice..."
        jump ancoming

label endlickep4:
     scene black with fade
     show text "{size=+5}You left her in the room clearly relaxed...{/size}" with dissolve
     with Pause(2)
     hide text with dissolve
     with Pause(1)
     pause
     jump ancoming

label fuckthroatep4:
    $ zleep3nicfactor = True
    scene black with fade
    stop music fadeout 1.0
    play music "music/Mnicdk.mp3"
    show text "{size=+5}You quickly got rid of your underwear{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    scene 40021 with fade
    m "What are you doing?!"
    scene 40021a with dissolve
    m "So that's what you came here for?!"
    scene 40021b with dissolve
    e "You suck and I'll be quiet"
    scene 40021c with dissolve
    e "That's the deal we have, right?"
    scene 40021d with dissolve
    "{color=#A8E4A0}{i}{size=-3}You launch yourself onto her, as you take your dick right into her mouth with no anticipation."
    show bjfinalep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}Grabbing a hold of her blonde hair, you begin to move your hips back and forth to the rythm of your heartbeat, as you force her to suck and gag on your overvirile and sex-drunken cock."
    m "MMMMM"
    e "I do not understand what you're saying"
    m "{color=#ffa500}{i}*GHLUK GHLUK GHLUK*{/i}{/color}"
    e "Probably something about my dick..."
    show ep4ff with dissolve
    e "So nice.."
    e "I love the feel of your lips..."
    e "I think I'm about to cum in your mouth soon"
    hide ep4ff
    show bjfinalep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She started struggling in panic"
    e "You don't want it in your mouth?{p}Okay{p}I'll cum on your face"
    show ep4cm with vpunch
    pause 3
    scene bjep4cm with dissolve
    e "Fuuuuck..."
    $ renpy.end_replay()
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 2
    $ nicolelustep4 -= 2
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    scene 40025 with dissolve
    e "{color=#ffa500}{i}*Breaths heavily*{/i}{/color}"
    jump endsucep4

label fuckthroatep4cm:
    show orgnicoep4
    $ renpy.pause(4, hard=True)
    m "Stop..."
    scene 40021a with dissolve
    pause
    scene 40021b with dissolve
    pause
    scene 40021c with dissolve
    pause
    scene 40021d with dissolve
    "{color=#A8E4A0}{i}{size=-3}You launch yourself onto her, as you take your dick right into her mouth with no anticipation."
    show bjfinalep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}Grabbing a hold of her blonde hair, you begin to move your hips back and forth to the rythm of your heartbeat, as you force her to suck and gag on your overvirile and sex-drunken cock."
    e "You moaned so sweetly."
    m "MMMMM"
    e "I do not understand what you're saying"
    m "{color=#ffa500}{i}*GHLUK GHLUK GHLUK*{/i}{/color}"
    e "Probably something about my dick..."
    show ep4ff with dissolve
    e "So nice.."
    e "I love the feel of your lips..."
    e "I think I'm about to cum in your mouth soon"
    hide ep4ff
    show bjfinalep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She started struggling in panic"
    e "You don't want it in your mouth?{p}Okay{p}I'll cum on your face"
    show ep4cm with vpunch
    $ maxmccumep7 += 1
    pause 3
    scene bjep4cm with dissolve
    e "Fuuuuck..."
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 2
    $ nicolelustep4 -= 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    scene 40025 with dissolve
    e "{color=#ffa500}{i}*Breaths heavily*{/i}{/color}"
    jump endsucep4

label endsucep4:
    stop music fadeout 5.0
    pause
    play music "music/Mn.wav"
    "{color=#A8E4A0}{i}{size=-3}You rolled over on her side"
    show afterbjep4 with dissolve
    pause 0.2
    scene aftercmep4 with dissolve

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Slap her ass*{/i}{/color}\n{color=#3d85c6} +1 Dom Point":
                jump slapassep4

            "{color=#FFD1DF}{i}*Put your hand on her leg*{/i}{/color}\n{color=#3d85c6} +1 Lust Point":
                jump handonlegep4
    else:
        menu:
            "{color=#FFD1DF}{i}*Slap her ass*{/i}{/color}":
                jump slapassep4

            "{color=#FFD1DF}{i}*Put your hand on her leg*{/i}{/color}":
                jump handonlegep4

label slapassep4:
    show slapep4 with dissolve
    pause 4
    scene afterslapep4 with dissolve
    e "Thanks"
    e "You're good."
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    "{color=#A8E4A0}{i}{size=-3}She didn't answer"
    jump ancoming

label handonlegep4:
    show handep4 with dissolve
    e "Thanks, it was very pleasant"
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    "{color=#A8E4A0}{i}{size=-3}She didn't answer"
    jump ancoming

label ancoming:

    scene black with fade
    stop music fadeout 1.0
    play music "music/Mat.wav"
    show text "{size=+5}Some time later{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    scene 40028 with dissolve
    y "Hey hey!"
    scene 40028a with dissolve
    e "Hmm?"
    e "Is that...Eve?"
    $ nicosister_role = renpy.input("Who is that woman to you? \n {i}(Enter for '[woman_name]'s sister' or write 'Aunt' or write something else){/i}", )
    $ nicosister_role = nicosister_role.strip()
    $ persistent.nicosister_role = nicosister_role
    show mcsee with dissolve
    e "[nicosister_role] came!"
    e "Hah, 1:0 dad, you forgot that she has a sister"
    scene 40030a with dissolve
    a "Hey, honey, oh my goodness, what happened?"
    m "Hello, let's sit down, would you like something to drink?"
    show mcsee with dissolve
    a "Wine... but if you don't have it, you can also give me some coffee."
    m "You came by car, I won't pour you any wine, and besides, I'm out of it."
    "{color=#A8E4A0}{i}{size=-3}You hear footsteps in the kitchen{/i}"
    "{color=#ffa500}{i}*The sound of a coffee machine*{/i}{/color}"
    scene 40031 with dissolve
    m "Here you go, your coffee"
    a "Thanks"
    a "Tell me what happened..."
    scene black with fade
    show text "{size=+5}Some female bullshit that doesn't matter at all{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)
    show gardentalk with fade
    m "As for why I called you..."
    m "John's bank account was blocked today..."
    m "And we have a joint account, so they blocked mine too"
    m "I need to borrow some money..."
    show garden with dissolve
    hide gardentalk
    a "[woman_name] If I had it, I would help you, but I have a problem myself"
    m "Even $100?"
    a "Girl. I’m desperate for cash too. I’d blow totally give head for 100 bucks if there was someone willing"
    a "Haha"
    a "The bank is chasing me for overdue payments. So, as soon as I get some money, they immediately take it from me"
    a "I went a bit overboard with the credit card..."
    a "But you know, when you're at my age, you've got to be more careful with your looks and take care of yourself..."
    a "Unless you're a chick like you. You'd look great even in a bag"
    show gardentalk with dissolve
    hide garden
    m "I do not know what to do"
    m "He says that they will unblock his account in a few days and that he will think of something"
    m "But I know very well that he won't come up with anything, he's a sucker for such things"
    m "I still don't know what this tax office is talking about, why they picked on it..."
    m "I'm afraid that something worse will soon come out of this and we will be left without money for longer"
    m "All our savings... they said that the bank is safer than cash, and here it is."
    show garden with dissolve
    hide gardentalk
    a "Cash only, honey. Don't believe in any banks."
    a "Oh, I almost forgot! My computer broke, is your little rascal at home maybe?"
    a "I would gladly borrow him for a while to check what's going on"
    m "He's at home..."
    m "He's at home, I'm sure he'll be happy to help you."
    a "Thank God, I can't even read the emails."
    a "Listen, I'll try to think about something and help you out somehow, but I can't promise you that I'll solve anything."
    a "I understand... Oh, also, if your young man comes with me now, I'll give him some food to bring you home, it should be enough for a day or two."
    m "Thank you so, so much. And I'm sorry for making you come over and such."
    a "Oh come on, honey, that's what a sister is for, so you don't have to deal with your problems alone"
    a "But... I can feel that something else is bothering you. I know you really well."
    m "No....it's nothing...really"
    a "You know you can't cheat on your sister... but if you want to confess, then..."
    show mcsee with dissolve
    a "You know where I live"
    a "Come to me, let me hug you. Don't worry anymore."

    scene black with fade
    show text "{size=+5}[player_name] come down to the garden!{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    scene 40033 with dissolve
    a "Hello, young one"
    e "Hi [nicosister_role]"
    a "Come with me, my computer is broken, you young people already know how to fix something like that"

    scene black with fade
    show text "{size=+5}You quickly got dressed and ran to your [nicosister_role]'s car" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    show ancar
    a "My little boy is growing up so fast"
    a "It must be hard for you when your dad is away all the time"
    e "Why?"
    a "You know... you're at an age where it's easy to have problems"
    a "Studying, friends, drugs, girls..."
    a "Has my little boy ever kissed a girl?"

    menu:

        "Yes, of course":
            jump jasnezetak

        "Mmmm... not yet...":
            $ aunttalk1 += 1
            jump jeszczenie

label jasnezetak:
    a "Oho, little heartbreaker"
    a "I'm very happy about this"
    jump olderprefer

label jeszczenie:
    a "Really?!"
    a "You're such a pretty boy and you haven't kissed yet"
    jump olderprefer

label olderprefer:
    e "I prefer older... women"
    a "Oh yeah... at that age you all hunt for those... whatever they call them"
    e "Milfs"

    menu:

        "Like you":
            $ aunttalk2 += 1
            a "I guess I'm not a milf, I don't have any children! Haha"
            jump caraunttalk1

        "An experienced woman can teach me more":
            $ aunttalk3 += 1
            a "Uhm.... Uhm....{p}And what about university?"
            jump caraunttalk1

label caraunttalk1:
    a "Does my sissy help you with your studies?"
    a "She always believed that learning was the most important thing in life, but because of this, she never had fun back in her youthful days."
    e "She helps me a lot, actually."
    e "We've been spending a lot of time lately... together"
    e "She’s been trying really hard."
    a "It’s nice to hear that. I always wanted to be like her, all smart and shit… But damn, I love partying"
    a "Well, in our family someone had to be the worse one so that the other one could be the better one"

    scene black with fade
    show text "{size=+5}You arrived at your [nicosister_role]'s apartment." with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    scene 40035 with dissolve
    a "Welcome to my little apartment"
    e "Doesn't look that small..."
    show homean
    $ renpy.pause(2, hard=True)
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But this is already looking quite big"
    scene 40038 with dissolve
    pause
    scene 40039a with dissolve
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Was he staring at my ass?"
    scene 40039a with dissolve
    a "Mmm, feel free to come inside"
    scene 40039b with dissolve
    a "Sit down, I'll prepare something to drink"
    scene 40040 with dissolve
    a "Do you want water, coffee?"
    scene 40041 with dissolve
    e "No thanks"
    a "If I pour myself some wine, will you be able to go back alone? I'm dying of thirst"
    e "Sure, there's a bus stop nearby"
    scene 40042 with dissolve
    a "Thanks [player_name]"
    scene 40043 with dissolve
    pause
    show headan with dissolve
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} God, I'm dying of thirst"
    scene 40044 with dissolve
    pause 1
    scene 40045 with dissolve
    pause 1
    scene 40045a with dissolve
    pause 1
    scene 40047 with dissolve
    a "I don't know what's wrong with this thing… But if you could take a look, I'd be very grateful"
    scene 40047a with dissolve
    a "The computer is in the bedroom"
    e "Sure"
    a "Thanks [player_name]"
    scene 40048 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} A PC in her bedroom... maybe I'll hack the camera and see what my [nicosister_role] is up to in the evenings. That’d be fun. Wouldn’t be much of a hassle either."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} You're a damn genius, [player_name]"
    scene 40050 with dissolve
    e "Huh?"
    scene 40051 with dissolve
    e "This picture..."
    e "Uhmm... Eve?"
    scene 40053 with dissolve
    e "Is this [woman_role]?"
    a "Aww..."
    scene 40052c with dissolve
    a "Yeah, this picture was taken before her prom! She was 18 years old then."
    a "She had a beautiful dress, she only wore it once, still, I never really know why, after all, it’s one of those fancy dresses that you could use anywhere, like..."
    e "Taking it to a fancy date?"
    a "Exactly"
    scene 40052b with dissolve
    e "And what about this guy...? Is that John?"
    scene 40051 with dissolve
    a "No, John wasn't in the country at that time, he worked on a ship for half a year and couldn't come."
    e "So who is it?"
    a "This is Lopez, your [woman_role]'s only friend from school"
    a "He was just weird."
    e "What do you mean?"
    a "Such a shady business guy..."
    a "Well, your [woman_role] somehow got along with him"
    a "And probably only with him... I don't remember that she had any other friends, although the whole school had a crush on her"
    "{color=#A8E4A0}{i}{size=-3}She became lost in thought{/i}"
    e "Woah, did she have long hair?"
    a "Yeah... then she cut it short and never went back to them"
    a "But even bald she would be pretty"
    e "But you haven't changed much, you're still hot"
    scene 40052c with dissolve
    a "Thanks... Hah I had a hard time squeezing into this dress."
    a "Those were great times, no stress, no problems, no loans and no banks"
    scene 40052b with dissolve
    a "{color=#ffa500}{i}*She sighed*{/i}{/color}"
    scene 40052c with dissolve
    a "Just wait, I have to do one thing in the kitchen, if you could look at the computer in the meantime"
    scene 40052b with dissolve
    e "Sure"
    scene 40054 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} And the whole plan went to shit. My [nicosister_role] doesn't have a camera"
    e "Maybe I'll buy her..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Hey, Eve, I bought you a camera, just don't move the computer from the bedroom"
    e "Hehe"
    e "Okay, what's going on here..."

label computerrepair:
    scene computer1 with dissolve
    if easymode:
        "You can skip this minigame."
        menu:
                "Skip":
                    jump ezcomputerjump

                "Let me try!":
                    jump ezcomputer

    if not easymode:
        if easycomputer > 2 and blockeasy == False:
            "It looks like you have a problem with this minigame.{p}If you want, i can remove it for you - but you won't get the achievement."
            $ easycomputer = 0
            menu:
                    "Help Me!":
                        jump ezcomputerjump

                    "I want to try again":
                        jump ezcomputer

                    "Don't ask me again - I want to get the achievements!":
                        $ blockeasy = True

label ezcomputer:
    if clickcomputer == False and browseropen == False and ctrlaltdelclick == False:
        show screen hint ("There must be a way... When I click something the computer thinks for a long time.. I can't click too much...")
    elif clickcomputer == True and browseropen == False and ctrlaltdelclick == False:
        hide screen hint
        show screen hint ("The computer is trying to start 'My Computer'...")
    elif clickcomputer == False and browseropen == True and ctrlaltdelclick == False:
        hide screen hint
        show screen hint ("The computer is trying to launch the browser...")
    elif clickcomputer == False and browseropen == False and ctrlaltdelclick == True:
        hide screen hint
        show screen hint ("The computer is trying to start the settings...")
    elif clickcomputer == True and browseropen == True and ctrlaltdelclick == False:
        hide screen hint
        show screen hint ("The computer is trying to start 'My Computer'...\nThe computer is trying to launch the browser...")
    elif clickcomputer == False and browseropen == True and ctrlaltdelclick == True:
        hide screen hint
        show screen hint ("The computer is trying to launch the browser...\nThe computer is trying to start the settings...")
    elif clickcomputer == True and browseropen == False and ctrlaltdelclick == True:
        hide screen hint
        show screen hint ("The computer is trying to start 'My Computer'...\nThe computer is trying to start the settings...")
    elif clickcomputer == True and browseropen == True and ctrlaltdelclick == True:
        hide screen hint
        show screen hint ("The computer is trying to start 'My Computer'...\nThe computer is trying to launch the browser...\nThe computer is trying to start the settings...")

    menu:

            "Click on My Computer":
                jump clickcomputer
            "Open browser":
                jump browseropen
            "Kick the computer":
                jump kickcomputer
            "Click on settings":
                jump ctrlaltdel


label clickcomputer:
    $ clickcomputer = True
    "{color=#ffa500}{i}*The computer is buzzing...*{/i}{/color}"
    "...and then nothing happened!"
    jump computerrepair

label browseropen:
    $ browseropen = True
    "{color=#ffa500}{i}*The computer is buzzing...*{/i}{/color}"
    "...and then nothing happened"
    jump computerrepair

label kickcomputer:
    $ easycomputer += 1
    if clickcomputer == True:
        scene computer3 with dissolve
        "What the hell?!"
        "Many windows started opening at once"
        "I guess I need to reset and start again"
        $ clickcomputer = False
        $ browseropen = False
        $ ctrlaltdelclick = False
        if itguy == 1 and perktip == False:
            $ perktip = True
            "{b}PERK ITGUY {/b}{p}Hmm... so the kick activates what I clicked earlier..."
            jump computerrepair
        else:
            jump computerrepair


    elif ctrlaltdelclick == True:
        scene computer2 with dissolve
        "Fuck, thousands of ads! Its a virus!!"
        "I can't click anything"
        "I guess I need to reset and start again"
        $ clickcomputer = False
        $ browseropen = False
        $ ctrlaltdelclick = False
        if itguy == 1 and perktip == False:
            $ perktip = True
            "{b}PERK ITGUY {/b}{p}Hmm... so the kick probably activates what I clicked earlier..."
            jump computerrepair
        else:
            jump computerrepair

    elif browseropen == True:
        hide screen hint
        scene computer5 with dissolve
        "Now the browser has started!"
        jump perkitrepair

    else:
        "Wow, you didn't miss!"
        "...but nothing happened."
        jump computerrepair

label ctrlaltdel:
    $ ctrlaltdelclick = True
    "{color=#ffa500}{i}*The computer is buzzing...*{/i}{/color}"
    "...and then nothing happened"
    jump computerrepair


label perkitrepair:
    if itguy == 1:
        "{b}PERK ITGUY {/b}{p}I know this virus... it launches through the browser history"
        e "If I delete the entire history, the virus will disappear too!"
        jump browsermenu
    else:
        jump browsermenu


label browsermenu:
    hide screen hint

    menu:

        "Open browser settings":
            jump computernothinghappen
        "Type Antivirus in Doodle":
            jump computernothinghappen
        "Open History":
            jump history


label computernothinghappen:
    "{color=#ffa500}{i}*The computer is buzzing...*{/i}{/color}"
    "Hey, everything has reset!"
    $ clickcomputer = False
    $ browseropen = False
    $ ctrlaltdelclick = False
    jump computerrepair

label history:

    e "Well, let's click on history..."
    scene computer4 with dissolve
    e "Come on, [nicosister_role] watches porn about..."
    e "Domination..."
    e "Nephews..."
    e "Blackmail"
    e "JESUS I AM THE PERFECT MATCH FOR MY [nicosister_role]! I KNEW IT!"
    e "Who would have thought"
    e "A lot of this..."

    menu:

        "Try to visit any link":
              jump computernothinghappen
        "Delete History":
              jump deletehist

label deletehist:
    e "Okay... time to delete it all"
    if not easymode:
        $ achValid4 += 1
        $ achievement.grant("Achiev13")
        $ achievement.sync()
        if not persistent.achievement13:
                 show Achiev13 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                 "You have received the achievement!{p}{b}\"Sextrix\".{/b}"
                 "Number of achievements earned in this chapter [achValid4]/5"
                 hide Achiev13
                 $ persistent.achievement13 = True

label ezcomputerjump:
    hide screen hint
    scene 40055 with dissolve
    a "Do you know how to fix it?"
    e "I've already done that"
    scene 40062 with dissolve
    a "Great, will it work?"
    scene 40060 with dissolve
    e "Yes, you got the virus because you were visiting porn sites"
    scene 40064 with dissolve
    a "YHPHG?@!#"
    a "IMPOSSIBLE, something must have clicked"
    scene 40061 with dissolve
    e "Exactly 261 times were clicked, including 130 times on porn about nephews, 90 times on blackmail and 41 times on domination"
    scene 40066 with dissolve
    a "Hmm... interesting statistics..."
    scene 40063 with dissolve
    a "But let's keep this between us...{p}...ok?"
    e "Sure, dont worry"
    scene 40067smile with dissolve
    e "Eve... I accidentally heard that you were short of money"
    scene 40067talksmile with dissolve
    a "Ooooh, I'm talking too loud, don't worry, it's not something you should worry about."
    scene 40067smile with dissolve
    e "I'm not worried, it's just that... I can help You because I’ve got my little stash, you know."
    scene 40062 with dissolve
    a "Hey, I asked you for help with the computer and I should pay you, not you lend it to me. But thank you for being so concerned about yours [nicosister_role]"
    a "Besides, I'll tell you that your [woman_role] needs it very much right now... I wasn't supposed to tell you, but they blocked their bank account..."
    scene 40067still with dissolve
    e "No problem, I have enough for everything"
    e "Besides, you doesn't have to give me anything back... but that's what I thought, because I can't talk to [woman_role] about certain topics, and my father is away..."
    e "Maybe you could... tell me a little about women?"
    scene 40067talksmile with dissolve
    a "Sure, feel free to ask, there are no taboo topics for me."
    scene 40067smile with dissolve
    e "I want to have someone to talk to about... sex, and you are an experienced woman"
    scene 40067shy with dissolve
    a "Ehm... experienced in sex... well, who else to talk to about such matters if not with your [nicosister_role]"
    a "{color=#ffa500}{i}*She sighed*{/i}{/color}"
    scene 40067talksmile with dissolve
    a "What do you want to know?"

    menu:

        "I want you to do to me what a woman does to a man...":
            $ auntbjtalkep4 += 1
            jump crazyep4

        "I want to make love with you":
            $ auntsextalkep4 += 1
            jump crazyep4

        "I'd like to see you naked...":
            $ auntpussytalkep4 += 1
            jump crazyep4

label crazyep4:
    scene 40064 with vpunch
    a "[player_name] are you crazy?"
    a "You're a grown man now, don't ask me to do things like that, even jokingly."
    a "You wanted to talk, and you want me... I won't comment..."
    e "I'll pay $100"
    e "I heard you say... {p}that you'd blow someone if they gave you $100.."
    scene 40065 with dissolve
    a "It was a joke"
    a "J O K E"
    scene 40066 with dissolve
    a "[player_name] honey, do you think I'm some kind of prostitute?"
    if auntbjtalkep4 == 1:
        a "Do you want to pay me $100 to give you a blowjob?"
        a "Don't even joke like that..."
    elif auntpussytalkep4 == 1:
        a "You want to pay me $100 to take my clothes off?"
        a "Don't even joke like that..."
    elif auntsextalkep4 == 1:
        a "Do you want to pay me $100 to have sex with you?"
        a "Don't even joke like that..."

    menu:

        "I'll give you $200 to give me a good sucking":
            $ auntbjtalk2ep4 += 1
            jump crazy2ep4

        "I'll give you $200 to make love to me":
            $ auntsextalk2ep4 += 1
            jump crazy2ep4

        "I'll give you $200 to take your clothes off.":
            $ auntpussytalk2ep4 += 1
            jump crazy2ep4

label crazy2ep4:
    scene 40061 with dissolve
    a "Ahh... so you don't think of me as a whore anymore... but as an exclusive prostitute because maybe I'll be tempted for more."
    scene 40065 with dissolve
    a "[player_name] I think you should go..."
    scene 40067talk with dissolve
    a "Thank you very much for your help... but please, fuck off."
    a "I am your [woman_role]’s sister"
    a "I can't even think about it..."
    scene 40067still with dissolve
    e "Uhm... looking at your history in the browser, you probably think quite often..."
    scene 40067angry with dissolve
    e "I'm an adult now, I can keep a secret"
    scene 40066 with dissolve
    a "Please leave now..."
    a "The bus runs here often..."
    a "Thank you for your help..."
    scene 40061 with dissolve
    e "Eve... Before I leave and you turn on your sites again..."
    e "Remember that it could be us..."
    scene 40067angry with dissolve
    pause
    scene ep4door with vpunch
    pause
    scene 40068 with dissolve
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What is it with these young people now..."
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Horny... probably because they watch porn on the Internet all the time... Gooners..."
    scene 40068a with dissolve
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But would [player_name] do something like that...?"
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} It's probably because of what he saw on the computer"
    scene 40068b with dissolve
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I couldn't have asked him for help..."
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But..."
    scene 40068c with dissolve
    a "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} It was quite exciting..."
    "{color=#ffa500}{i}*The sound of moaning from the computer*{/i}{/color}"
    scene black with fade
    "{size=+20}Some time later{p}Lake Mercino"

    scene walkingstart with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} The bus won't be there for another hour, good thing there's a lake nearby"
    show walking
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I can watch some porn on my cell phone and no one will notice me in the forest"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Or not, because maybe someone will notice and they will think I'm some kind of pervert"
    scene 40070 with dissolve
    pause
    show lake with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I used to come here often with my [woman_role]."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I should come back here with her, sex by the lake must be great"
    scene 40071 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Maybe I'll find some photos of my [woman_role] from school"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Apparently everything is on the internet"
    scene 40072 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She looked amazing then"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Hmm... I can't find anything."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} How to find it...?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Or maybe if I enter a date range I will find something..."
    e "Let's try typing: 2005, college, party, [woman_name]"

label transitionsceneep4:
    stop music fadeout 1.0
    play music "music/Audio004.mp3"
    e "??!!?!"
    scene 40105 with vpunch
    e "What the hell?!"
    e "Hmm, is this [woman_role]?"
    e "It's a private gallery, I guess someone doesn't know that the photos are indexed in Booble"
    e "Whose account is this?! Strange name {b}xxx_Z3p0lz3p0l_xxx{/b}"

label ep4riddleone:
    scene 40105 with dissolve
    $ easyphoto += 1
    if easymode:
        "You can skip this minigame."
        menu:
                "Skip":
                    jump ezphotojump

                "Let me try!":
                    jump ezphoto

    if not easymode:
        if easyphoto > 3 and blockeasy == False:
            $ easyphoto = 0
            "If you want, i can remove this minigame for you - but you won't get the achievement."
            menu:
                    "Help Me!":
                        jump ezphotojump

                    "I want to try again":
                        jump ezphoto

                    "Don't ask me again - I want to get the achievements!":
                        $ blockeasy = True

label ezphoto:
    show screen hint ("I've seen things from this picture somewhere before... I just can't quite remember where.")
    e "Reminds me of this photo..."
    menu:

            "The color of her hair...":
                $ riddlehair += 1
                jump ep4riddletwo

            "This dress...":
                $ riddledress += 1
                jump ep4riddletwo

            "This underwear...":
                $ riddlebra += 1
                jump ep4riddletwo

            "This bottle...":
                $ riddlebottle += 1
                jump ep4riddletwo

label ep4riddletwo:

    e "This date..."
    menu:

            "It's probably her birthday...":
                $ riddlebirthday += 1
                jump ep4riddlethree

            "It's spring...!":
                $ riddlespring += 1
                jump ep4riddlethree

            "It's 3 a.m...":
                $ riddlenight += 1
                jump ep4riddlethree

            "I've seen this date somewhere before...":
                $ riddledateagain += 1
                jump ep4riddlethree


label ep4riddlethree:

    e "And what's in the background...?"

    menu:
            "It's probably some kind of diary...":
                $ riddlenotebook += 1
                jump ep4riddlefour

            "This cabinet... I've never seen it before":
                $ riddlelocker += 1
                jump ep4riddlefour

            "Very nice watch... probably worth a lot now":
                $ riddlewatch += 1
                jump ep4riddlefour
            "Mobile phone? Did they exist in those times?":
                $ riddlemobile += 1
                jump ep4riddlefour

label ep4riddlefour:
    hide screen hint
    show screen hint ("It looks like there's a name hidden in that username, one that I've heard somewhere before...")
    $ photonick = renpy.input("And this xxx_Z3p0lz3p0l_xxx? Who could it be...? \n {i}(write your answer){/i}", )
    $ photonick = photonick.strip() or "..."

    if photonick.upper().find("LOPEZ") != -1 or photonick.upper().find("LOPEZLOPEZ") != -1:
                hide screen hint
                $riddlenick += 1
                jump ep4conclusion

    else:
                hide screen hint
                jump ep4conclusion


label ep4conclusion:

    if riddlehair == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} The color of her hair...{p}It's her natural color..."
    if riddledress == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This dress..."
        play sound "music/correct.mp3"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} {color=#00ff00}Beautiful red dress... Hey i think that I've seen it somewhere before."
    if riddlebra == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This underwear...{p}She was wearing underwear, rather ordinary..."
    if riddlebottle == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This bottle...{p}A bottle like any other... Probably whiskey"
    if riddlebirthday == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's probably her birthday...{p}Actually, I don't remebemer if it's really her birthday..."
    if riddlespring == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's spring...!{p}It was spring... it was warm."
    if riddlenight == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's 3 a.m...{p}Middle of the night, someone was probably worried..."
    if riddledateagain == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I've seen this date somewhere before..."
        play sound "music/correct.mp3"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} {color=#00ff00}...prom party?"
    if riddlenotebook == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It's probably some kind of diary...{p}I don't see any writing on this notebook."
    if riddlelocker == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This cabinet... I've never seen it before{p}A filing cabinet like a filing cabinet, there are plenty of them everywhere."
    if riddlewatch == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Very nice watch... probably worth a lot now..."
        play sound "music/correct.mp3"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} {color=#00ff00}And very characteristic, all yellow..."
    if riddlemobile == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Mobile phone? Did they exist in those times?{p}This was probably the first Eyphone"

        "[riddlenick]"

    if riddledress == 1 and riddledateagain == 1 and riddlewatch == 1 and riddlenick == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Wait a minute... my [nicosister_role] said that my [woman_role] only wore this dress once."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} This photo was taken the night after the prom party."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} And the guy in the photo was wearing this watch."
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Lopez..."
        if not easymode:
            $ achValid4 += 1
            $ achievement.grant("Achiev14")
            $ achievement.sync()
            if not persistent.achievement14:
                 show Achiev14 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                 "You have received the achievement!{p}{b}\"True Sextective\".{/b}"
                 "Number of achievements earned in this chapter [achValid4]/5"
                 hide Achiev14
                 $ persistent.achievement14 = True

        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I need to talk to my [nicosister_role] about this"
        label ezphotojump:
        stop music fadeout 1.0
        play music "music/Audio005.mp3"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She'll definitely know more"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But... not today"
        show transitionep4
        $ renpy.pause(25, hard=True)
        jump finaltalkep4

    if riddledress != 1 or riddledateagain != 1 or riddlewatch != 1 or riddlenick != 1:
            "But something doesn't feel right here... I have to remember that photo from her apartment."
            e "Focus [player_name]"
            scene 40051 with dissolve
            e "My [woman_role], my [nicosister_role] and Lopez..."
            e "I think i will remember now..."
            $ riddlehair = 0
            $ riddledress = 0
            $ riddlebra = 0
            $ riddlebottle = 0
            $ riddlebirthday = 0
            $ riddlespring = 0
            $ riddlenight = 0
            $ riddledateagain = 0
            $ riddlenotebook = 0
            $ riddlelocker = 0
            $ riddlewatch = 0
            $ riddlemobile = 0
            $ riddlenick = 0
            jump ep4riddleone


label finaltalkep4:
    scene transition2 with dissolve

    "{i}After walking back home, with your hands in your pockets, you take them out in order to grip on the doorknob, and opening the door."
    "{i}The moment you put a foot on the house’s floor, you hear a female sobbing: [woman_name] was crying, and chances are you are the reason why."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} God, I could recognize the sound of her tears a mile away. I need to go check up on her."
    scene 40200 with dissolve
    e "H-Hey!?"
    scene 40201 with dissolve
    m "Oh...{p}It’s you.{p}Kill me already you fucking creep"
    scene 40106 with dissolve
    e "Hey, that’s offensive for no reason."
    scene 40106b with dissolve
    m "Oh, you’re offended?{p}I-I couldn’t care less"
    scene 40106a with dissolve
    e "Well...{p}After all, you’re the one who brought it to herself."
    scene 40106c with dissolve
    m "This is exactly what I needed, getting put the blame on me for normal bored-out wife behavior.{p}How many times are you going to say it?"
    scene 40106 with dissolve
    e "I’m just going to say it, and REMIND it to you, as many times as it’s needed, but, not right now at all."
    e "Anyways..."


    if givemoneyep4 == True:
            scene 40106beforemoney with dissolve
            "{color=#A8E4A0}{i}{size=-3}You stood up, reach your pockets, and hand her over the money your dad gave you."
            scene 40106beforemmoney with dissolve
            e "Here, I think this will be enough for the rest of the month."
            $ money -= 500
            show text "{color=#f00}{size=+15}-5 0 0 ${/color}" with dissolve
            with Pause(2)
            "{i}Total: [money]$"
            hide text with dissolve
            scene 40106money with dissolve
            m "R-Really? Oh... this is..{p}Thank you.{p}That’s what I needed from you, really..."
            show image "images/Stats/Dom[nicoledomep4].png" at statleft
            show image "images/Stats/Lust[nicolelustep4].png" at statright
            pause 1
            $ nicolelustep4 += 1
            $ nicoledomep4 -= 1
            show image "images/Stats/Dom[nicoledomep4].png" at statleft
            show image "images/Stats/Lust[nicolelustep4].png" at statright
            with dissolve
            pause 3
            hide image "images/Stats/Dom[nicoledomep4].png"
            hide image "images/Stats/Lust[nicolelustep4].png"
            scene 40106 with dissolve
            e "You know that I will always help you"
            jump feetmassageep4

    else:
            jump feetmassageep4




label feetmassageep4:
    show talkep4
    $ renpy.pause(5, hard=True)
    "{color=#A8E4A0}{i}{size=-3}You smile, and get a hold of her left foot, swiftly and gently starting to massage it up and down, as you rub your thumbs on her sole, all the way down to her ankle."
    scene 40107 with dissolve
    m "Ah"
    scene 40107c with dissolve
    pause
    show feetmsgep4
    e "You know, this little monster likes taking good care of you in any way I can. That’s what a man does after all.{p}You don’t even need my dad at all while having me around. I am the real deal here."
    m "Do you really think so? Why?"
    e "Well..."

    if easymode:
        menu:
            "Because I’m the only thing you deserve, after all.\n{color=#3d85c6} +1 Dom Point, -1 Lust Point":
                jump deserveep4

            "I think it’s because I would actually die for you.\n{color=#3d85c6} +1 Lust Point":
                $ niclovebonusfactor += 1
                jump dieforep4
    else:
        menu:
            "Because I’m the only thing you deserve, after all.":
                jump deserveep4

            "I think it’s because I would actually die for you.":
                $ niclovebonusfactor += 1
                jump dieforep4

label deserveep4:

    m "Y-Yeah... for sure."
    m "After all, I’m the one who’s brought this to herself"
    e "You are a fast learner"
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicoledomep4 += 1
    $ nicolelustep4 -= 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump talk2ep4

label dieforep4:

    m "Yeah, no wonder"
    m "You can’t live on false promises, you know"
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    pause 1
    $ nicolelustep4 += 1
    show image "images/Stats/Dom[nicoledomep4].png" at statleft
    show image "images/Stats/Lust[nicolelustep4].png" at statright
    with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledomep4].png"
    hide image "images/Stats/Lust[nicolelustep4].png"
    jump talk2ep4

label talk2ep4:

    if easymode:
        menu:
            "Really, my dad is a loser for losing such a precious goddess brought down to earth, for real.\n{color=#3d85c6} -1 Dad, +1 Dom Point":
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                pause 1
                $ dadfriend -= 1
                $ nicoledomep4 += 1
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[nicoledomep4].png"
                hide image "images/Stats/Lust[nicolelustep4].png"
                jump dadloser

            "You’re beautiful from head to toe, really. Even the smallest bit of your body was made to be treated like this.\n{color=#3d85c6} +1 Lust Point":
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                pause 1
                $ nicolelustep4 += 1
                $ niclovebonusfactor += 1
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[nicoledomep4].png"
                hide image "images/Stats/Lust[nicolelustep4].png"
                jump cloymyear

    else:
        menu:
            "Really, my dad is a loser for losing such a precious goddess brought down to earth, for real.":
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                pause 1
                $ dadfriend -= 1
                $ nicoledomep4 += 1
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[nicoledomep4].png"
                hide image "images/Stats/Lust[nicolelustep4].png"
                jump dadloser

            "You’re beautiful from head to toe, really. Even the smallest bit of your body was made to be treated like this.":
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                pause 1
                $ nicolelustep4 += 1
                $ niclovebonusfactor += 1
                show image "images/Stats/Dom[nicoledomep4].png" at statleft
                show image "images/Stats/Lust[nicolelustep4].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[nicoledomep4].png"
                hide image "images/Stats/Lust[nicolelustep4].png"
                jump cloymyear


label cloymyear:
    m "You’re just trying to cloy my ear"
    e "I’m not, I’m just saying what I feel, as I always do. And this is it. You’re beautiful from head to toe, really. Even the smallest bit of your body was made to be treated like this."
    jump grabep4

label dadloser:
    m "And he lost me?"
    e "You know, I’m the closest one to him, so yeah...First and foremost, I could work him in such a way we can 'defuse the bomb', if you know what I mean."
    jump grabep4

label grabep4:
    "{color=#A8E4A0}{i}{size=-3}While rubbing her foot, as your eyes melted together, slightly drunk on the thought of being the most powerful being in the house right now: You felt like you could do whatever."

    show grabep4 with dissolve
    $ renpy.pause(5, hard=True)
    hide feetmsgep4
    "{color=#A8E4A0}{i}{size=-3}[woman_name] frowned, as you unzipped your pants, helping your cock get a breath of fresh air."
    show grabep42 with dissolve
    $ renpy.pause(2, hard=True)
    m "I really hate you for doing this"
    scene 40109 with dissolve
    m "I can’t believe I raised a creep..."
    show grabep43 with dissolve
    $ renpy.pause(3, hard=True)
    "{color=#A8E4A0}{i}{size=-3}The feeling of power was so strong, that intoxicated by your own thoughts, you took her foot and shoved it against your hard bulge."

    e "But at the same time, you love me. Perhaps you love me for making you feel pleasure you’ve never felt before."
    e "You know, you’ve said before that I’ve ruined your life, but really all I did was opening your eyes."
    e "You're going to jerk me off with both of your precious little feet. Show me just how skilled you are with those pretty little toes."
    show fjep4 with dissolve
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3}[woman_name] eyes widened in surprise, but she didn't resist. She knew that defying you would only lead to further consequences. Reluctantly, she obeyed, positioning her feet on either side of your pulsating cock."
    m "Ugh!..."
    "{color=#A8E4A0}{i}{size=-3}As her feet began to glide up and down your shaft, the sensation was unlike anything you had ever experienced. The dual stimulation sent waves of pleasure coursing through your body, making your breath hitch and your heart race."
    e "That's it, ugh... Stroke me harder. I want to feel your feet working me over, bringing me to the edge."
    e "Show me your titties, come on!"
    m "F-Fine… Whatever will make you finish quicker..."
    e "Just do it."
    show shirtep4 with dissolve
    $ renpy.pause(3, hard=True)
    "{color=#A8E4A0}{i}{size=-3}[woman_name] pulled her shirt revealing her tits to you, as they flashed on your eyes like two pearls."
    show fjep4v2 with dissolve
    "{color=#A8E4A0}{i}{size=-3}Your [woman_role] movements became more urgent, she was on fire, despite her negative first, her toes flexing and curling as she increased the speed and pressure."
    e "Just look at you, a grown woman giving her [player_role] a footjob..."
    show sidefjep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}Her toes rubbed against your sensitive skin, letting out moans of ecstasy from deep within your throat"
    e "...and obediently following all orders."
    e "You deserved a reward."
    show hjep4solo with dissolve
    "{color=#A8E4A0}{i}{size=-3}The power dynamic between you and [woman_name] became even more apparent as you stood over her, your cock throbbing with anticipation."
    e "I can’t tell whether you’re aching for my cum, or aching for this to stop. I don’t care.	"
    show cmep4 with dissolve
    $ maxmccumep7 += 1
    $ renpy.pause(2, hard=True)
    "{color=#A8E4A0}{i}{size=-3}Without warning, you felt surge of ecstasy building within you. Your pleasure levels peaked, and with a deep toned manly moan, you came like a geyser all over Nicole's face. Thick ropes of cum splattered across her delicate features."
    e "Ah..."

    scene 40220 with dissolve
    pause 0.5
    scene 40221 with dissolve
    pause 0.5
    scene 40222 with dissolve
    pause 0.5
    scene 40223 with dissolve
    pause 0.5
    scene 40224 with dissolve
    pause 0.5
    scene 40225 with dissolve
    pause 0.5
    scene 40226 with dissolve
    "{color=#A8E4A0}{i}{size=-3}After cleaning herself up, she looked up at you, her voice trembling. "
    scene 40227 with dissolve
    m "Can I go now? Please, just let me leave."
    $ renpy.end_replay()

    if nicoledomep4 >= 7 or nicolelustep4 >= 7:
        "{color=#A8E4A0}{i}{size=-3}You smirked, reveling in the power you held over her. This was just the beginning of your twisted game, and you had no intention of letting her off the hook so easily."
    else:
        "Go..."
        jump leavingep4

    menu:

        "{color=#FFD1DF}{i}*Order her to clean your dick*{/i}{/color} {size=-8}(Req. 5 Domination Points){/size}" if nicoledomep4 > 8:
            $ zle2ep3nicfactor = True
            jump cleancock

        "{color=#FFD1DF}{i}*Kiss her*{/i}{/color}{size=-8} (Req. 5 Lust Points){/size}" if nicolelustep4 > 8:
            $ niclovebonusfactor += 3
            $ dobrze2ep3nicfactor = True
            jump kissep4

        "You can go...":
            jump leavingep4

label cleancock:

    scene 40240 with dissolve
    e "Not so fast"
    scene 40241 with dissolve
    pause 0.5
    scene 40242 with dissolve
    e "Clean my dick with your tongue"
    scene clean01 with dissolve
    pause
    show cleanbefore with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} So easy... "
    show ep4lickmc with dissolve
    e "My little{p}...obedient...{p}slut."
    e "Your tongue is so nice..."
    e "My dick is so sensitive now, keep licking it"
    e "It turns me on that when I order you to do something, you do it"
    e "You probably like it"
    e "Good slut"

    scene 40301 with dissolve
    e "I can't do it anymore today, you've exhausted me."
    m "I..."
    scene 40301talk  with dissolve
    m "Can i go?"
    $ renpy.end_replay()
    $ nicoledomending = True

    if nicolelustep4 >= 9 and nicoledomep4 >= 9 and endingep4 == 0:
        menu:
            "{color=#FFD1DF}{i}*Kiss her*{/i}{/color}":
                    $ endingep4 += 1
                    $ niclovebonusfactor += 3
                    $ dobrze2ep3nicfactor = True
                    jump kissep4

            "You can go...":
                    jump leavingep4

    else:
            "You can go..."
            jump leavingep4

label kissep4:

    scene 40300 with dissolve
    pause
    scene 40300a with dissolve
    pause
    scene 40300b with dissolve
    "{color=#A8E4A0}{i}{size=-3}[woman_name]'s eyes widened in shock. She had expected a harsh punishment, but she hadn't anticipated having to kiss you. As you leaned in, she trembled, her lips quivering."
    scene 40300cc with dissolve
    m "I... I didn't mean... Please, I can't do this."
    show beforekissep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}But it was too late. You pressed your lips against hers forcefully, claiming her mouth in a possessive and dominating kiss. Her body stiffened, her eyes wide open in shock as you held her in place, not allowing her to escape."
    show kissep4 with dissolve
    "{color=#A8E4A0}{i}{size=-3}The utter shock kept her eyes open, as she slightly clenched them from time to time. She was horrorized by the monster you’ve become."
    "{color=#A8E4A0}{i}{size=-3}But she submitted completely to your lips"
    "{color=#A8E4A0}{i}{size=-3}And your tongue kept caressing hers"
    show ep4afterkiss with dissolve
    "{color=#A8E4A0}{i}{size=-3}Finally, you broke the kiss, leaving Nicole breathless and disoriented. She stared at you, her eyes filled with a mix of confusion and regret."
    scene 40301 with dissolve
    m "I..."
    scene 40301talk  with dissolve
    m "I can't do this. I can't go any further. Please, just let me go."
    $ renpy.end_replay()
    $ nicolelustending = True

    if nicolelustep4 >= 9 and nicoledomep4 >= 9 and endingep4 == 0:
        menu:
            "{color=#FFD1DF}{i}*Order her to clean your dick*{/i}{/color}":
                $ zle2ep3nicfactor = True
                e "Not so fast"
                $ endingep4 += 1
                jump cleancock

            "You can go...":
                jump leavingep4

    else:
            "You can go..."
            jump leavingep4

label leavingep4:

    if endingep4 > 0:
            if not easymode:
                $ achValid4 += 1
                $ achievement.grant("Achiev15")
                $ achievement.sync()
                if not persistent.achievement15:
                     show Achiev15 at achievment with easeintop:
                                zoom 0.5
                                rotate_animation

                     "You have received the achievement!{p}{b}\"I take both\".{/b}"
                     "Number of achievements earned in this chapter [achValid4]/5"
                     hide Achiev15
                     $ persistent.achievement15 = True

    scene 40228 with dissolve
    pause 0.5
    scene 40229 with dissolve
    pause 0.5
    scene 40230 with dissolve
    pause 0.5
    scene 40231 with dissolve
    pause 0.5
    scene 40232 with dissolve
    "{color=#A8E4A0}{i}{size=-3}She left the room, confused, disgusted of herself, and slammed the door shut, right after slamming shut the bathroom’s, as she took a shower, just as a way to feel clean."
    show text "{size=+5}End of Chapter 4{/size}" with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)

    jump statsep4

label statsep4:

    $ achVall = achValid + achValid2 + achValid3 + achValid4
    if not easymode:
        "So far you have achieved {b}[achVall]{/b} out of 16 available achievements!"
    else:
        "You did not receive any achievements because you are playing in easy mode."
    if itguy >= 1 and speedguy >= 1:
        "Learned Perks: 2/2{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
    elif itguy >= 1 and speedguy == 0:
        "Learned Perks: 2/2{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}"
    elif itguy == 0 and speedguy >= 1:
        "Learned Perks: 1/2{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
    else:
        "Learned Perks: 1/2{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}"


    jump episode5

    show logo

    "{size=+15}Created by Zeratgames"
    scene black with fade

    ".."

    return











