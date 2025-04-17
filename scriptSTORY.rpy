
label ep1startnoob:
    hide screen hint
    scene black with fade

    $ player_name = renpy.input("What is my name? \n {i}(Type Now)", )
    $ player_name = player_name.strip()
    $ persistent.player_name = player_name
    $ player_role = renpy.input("Who am I to my dad's wife? \n {i}(Enter for 'Husband's son' or write something else){/i}", )
    $ player_role = player_role.strip() or "Husband's son"
    $ persistent.player_role = player_role
    $ woman_role = renpy.input("What role does the woman in this story play for you? \n {i}(Enter for 'Stepmom' or write something else){/i}", )
    $ woman_role = woman_role.strip() or "Stepmom"
    $ persistent.woman_role = woman_role
    $ woman_name = renpy.input("And what's her name? \n {i}(Enter for 'Nicole' or write something else){/i}", )
    $ woman_name = woman_name.strip() or "Nicole"
    $ persistent.woman_name = woman_name
    $ persistent.pName = player_name
    $ persistent.pRole = player_role
    $ persistent.wRole = woman_role
    $ persistent.wName = woman_name
    show mc1 with fade
    e "So [woman_name] is my [woman_role], and i'm her [player_role]. Nice!"
    hide screen hint
    scene 0001 with Fade(2.0, 1.0, 1.0)
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I'm living with my [woman_role] and Dad, and this evening I crept up to their bedroom door."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Let's open it up and you'll see why we're here...."
    show screen hint("I hope he's an adult...")
    menu:
        "You should only open this door if you are an adult over 18 years of age."
        "Yes I am an adult and I am more than 18 years old.":
            hide screen hint
            "The next scene contains NTR but is important to the story."
            show bedroomopen
            pause 3
            show bedroom
            "{color=#ffa500}{i}*a slight creak*{/i}"
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oops, I hope nobody heard that"
        "Unfortunately I'm not that old. Time to go play Phortnight!":
            return
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Meet my [woman_role], [woman_name]"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She’s 37 years old, a history professor at the university, and an undeniably beautiful woman."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} But right now, she seems a bit... occupied."
    pause
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You see, a married woman, late at night, pleasing a man with her mouth... Is not exactly an unusual thing in most homes."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Except for one little thing... {p}That man is NOT my dad, and I’m sure as hell he knows he won’t be home until tomorrow!"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} ...And I have no idea who that motherfucker is.."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I'm not stupid, so it's time to gather a little evidence. Smile for the camera."
    scene 0005
    with flash
    play sound "music/camera.mp3"
    "{color=#ffa500}{i}*camera sound*{/i}"
    scene black with fade
    m "WHAT THE HELL!?"
    m "[player_name] get back here!"
    show logo
    $ renpy.pause(3, hard=True)
    show text "CREATED BY ZERATGAMES" at title with dissolve
    $ renpy.pause(3, hard=True)
    show text "Episode 1" at title2 with dissolve
    $ renpy.pause(2, hard=True)

    with Pause(1)


label episode1noob:
    scene black with fade
    scene 10001 with dissolve
    pause 2
    "{color=#ffa500}{i}*alarm clock sound*{/color}"
    "..."
    "{color=#ffa500}{i}*beep beep*"
    "..."
    "{color=#ffa500}{i}*beep beep*"
    scene 10002 with dissolve
    $ renpy.pause(1, hard=True)
    scene 10003a with dissolve
    $ renpy.pause(1, hard=True)
    scene 10003b with dissolve
    $ renpy.pause(1, hard=True)
    m "Mmm..."
    scene 10004 with dissolve
    $ renpy.pause(1, hard=True)
    scene 10005 with dissolve
    $ renpy.pause(1, hard=True)
    scene 10006 with dissolve
    $ renpy.pause(1, hard=True)
    scene 10007 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What a night..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} [player_name]..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What had gotten into him?"
    scene 10008 with dissolve
    pause 1
    scene 10009 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} He’s still very young."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} This is probably the age when he starts to have an itch about sex life..."
    scene 10010 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But... Why did he take a picture?"
    scene 10010a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I hope he doesn’t... Jerk off to..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} NO. {p}Certainly not. {p}Not [player_name]"
    scene 10011 with dissolve
    scene 10012 with dissolve
    scene 10013 with dissolve
    scene 10013a with dissolve
    scene 10013b with dissolve
    scene 10014 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I need to talk to him about this TODAY."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Normally I would send John... But this time I can’t..."
    scene 10014b with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Maybe I'm just freaking out for no reason."
    scene 10014c with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} He should get up now so he won't be late for class..."
    scene 10015 with dissolve
    e "{color=#ffa500}{i}*Snoring*"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I better not wake him up."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I will see him at the university anyways."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Although I can't even think of the conversation we’ll have...{p}Yet...{p}I don't think I can escape from it"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} He’s got to delete those pictures he took yesterday."
    "{i}[woman_name] left the room"
    scene 10015 with dissolve
    e "{color=#ffa500}{i}*Snoring*"
    scene black with fade
    show text "One hour later" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve

    scene 10015 with dissolve
    $ renpy.pause(1, hard=True)
    scene 10015aa with dissolve
    $ renpy.pause(2, hard=True)
    scene 10015a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I gotta get up."
    scene 10016 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Hm, I’ve got a feeling this is going to be an interesting day."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What should I do with the pictures now?{p}They give me an insane power over my [woman_role]"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} This is an opportunity to get what I want. With these pictures, I can make her do anything I please"
    scene 10016a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Do I need money?"
    scene 10016b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Of course I do..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But there's something...{p}I want more than money..."
    e "..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ...Is it even possible?"
    scene 10016c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} At least I won't have to hear her moaning in the night anymore"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Although those of hers were quite nice to hear, sometimes..."
    scene black with fade
    show text "One hour later" at title with dissolve
    $ renpy.pause(1, hard=True)
    show text "Mercino University" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10022a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Fucking classes. Why did I go to university at all?{p}I could go to work."
    scene 10022b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I don’t feel like I’m learning anything anymore, and the chicks are so fucked up that I can't handle any of them."
    scene 10022c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I think it's time for a ciggie..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ...or not."
    show tomrun with dissolve
    $ renpy.pause(5, hard=True)
    scene 10023b with dissolve
    t "Ah, ow, ouch"
    scene 10024 with dissolve
    e "Tommy!"
    e "Give me my money for the weed you got on Friday"
    scene 10024a with dissolve
    e "Who do you think I am, huh?{p}Fucking Santa Claus?"
    scene 10024b with dissolve
    t "Sigh..."
    scene 10024c with dissolve
    t "I don't have it, dude... I’ve already spent it all."
    scene 10024a with dissolve
    e "Well, you leave me no choice"
    scene 10024c with dissolve
    t "No... wait"
    scene 10025 with dissolve
    t "Let me check..."
    scene 10025a with dissolve
    t "This is all I have."
    t "I'll give it back next week"
    scene 10026sad with dissolve
    e "Fine, so be it{p}But on Friday you better get me the rest or you’re fucked."
    e "Now get outta here."
    scene 10026sad2 with dissolve
    t "Okay.. Thanks man!"
    scene 10022a with dissolve
    e "I hate these rich kids. "
    scene black with fade
    show text "Dining hall" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10031 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I’m bored."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Usually, all classes are boring."
    scene 10031a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} In addition, most of the teachers here are old and ugly."
    scene 10031b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Why is the only good looking teacher my [woman_role]?!"
    scene 10031c with vpunch
    stop music fadeout 1.0
    play music "music/Mtom.wav"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Owww"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} And who is that?"
    scene 10031d with dissolve
    y "Hey, You!"
    e "Me?"
    scene 10032 with dissolve
    y "Yes You"
    y "Are you [player_name]?"
    scene 10032a with dissolve
    e "Yeah, that’s me."
    scene 10035 with dissolve
    y "So it's you..."
    scene 10036a with dissolve
    y "..."
    scene 10033 with dissolve
    y "I'm Tommy's mom..."
    scene 10036 with dissolve
    e "Tommy’s mom?..."
    e "Ok... How can I help you?"
    scene 10032 with dissolve
    z "I know you're selling him weed."
    scene 10033 with dissolve
    z "I'd like to talk about it, but I'd prefer not to do it here."
    scene 10036 with dissolve
    z "..."
    scene 10035a with dissolve
    z "Can we talk about it in my car? I parked it right outside, at the parking lot."
    z "I don't want him to see that I'm talking to you."
    z "Can you skip the class now?"
    e "Sure"
    scene 10037x with dissolve
    z "I'll be waiting outside"
    scene 10037x1 with dissolve

    scene 10037x2 with dissolve

    scene 10037x3 with dissolve

    scene 10037z with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I wonder what she wants from me."

    scene black with fade
    show text "Street near the university" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10039 with dissolve
    z "Hey!{p}Here!"
    scene 10039a with dissolve
    z "Good..."
    z "We won't talk here"
    scene drzwi0 with dissolve
    z "Get in."
    show drzwi
    $ renpy.pause(0.65, hard=True)
    scene drzwi1 with dissolve
    z "We'll take a short drive from the university."
    scene black with fade
    show text "The surrounding forest" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10040mowi2 with dissolve
    z "Thank you for agreeing to talk"
    scene 10040mowi with dissolve
    z "I'm concerned about what's been happening between you and my son"
    z "I want to understand why this is happening and find a solution"
    e "Oh, come on!{p}What do you want from poor Tommy and me?"
    z "Tommy has been deeply affected by your actions, and I won't stand for it."
    scene 10040mowi2 with dissolve
    z "Tommy's a good kid. He'd never have picked up the weed habit if it wasn’t for you."
    z "But I know that if I report this to the chancellor, it will only make things worse"
    z "I went to school too and I know how it ends"
    z "That's why I prefer to get along with you"
    scene 10040slucha with dissolve
    e "Get along? How?"
    scene 10040mowi with dissolve
    z "Here's $200{p}That's more than you'll probably ever earn from him."
    z "You'll never sell him anything again."
    e "What if I don't want the money?"
    scene 10040zlamowi with dissolve
    z "What do you mean by saying something like that?"
    scene 10040zlaslucha with dissolve
    e "I just don't want to take money from you. Tommy is a great customer, after all."
    scene 10040zlamowi with dissolve
    z "I don't understand"
    scene 10040zlaslucha with dissolve
    e "Simply{p}I don't want money from you. I will earn much more."
    scene 10040mowi with dissolve
    z "So you'll just leave him?"
    e "No"
    scene 10040zlamowi with dissolve
    z "Hmph...."
    z "I wanted to get along with you somehow, but I can see that it will be difficult"
    scene 10040zlaslucha2 with dissolve
    e "But I want to get along with you"
    scene 10040zlaslucha with dissolve
    z "Hm?"
    z "I'm not interested in playing games. I just want you to leave Tommy alone"
    e "Oh, it's not a game, you know."
    e "You don't want to make a big deal out of it, do you?{p}...I want you to show me your tits"
    scene 10040zdziwiona with dissolve
    z "Wait... WHAT?!"
    scene 10040zlamowi with dissolve
    z "Are you crazy?"
    z "I won't do anything like that"
    z "I think I'll go talk to the rector about it"
    scene 10040zlaslucha with dissolve
    e "Show me your tits and I'll consider leaving Tommy alone. It could change everything"
    z "No way!"
    e "Just hear me out"
    e "If you show me your tits, it may be a sign of trust, a gesture that will help me think about your son's well-being."
    e "It's worth a shot, isn't it?"
    scene 10040slucha with dissolve
    e "Also, your body look amazing, you are a beautiful woman..."
    scene 10040smd with dissolve
    e "We're in the woods... and no one will know anyway"
    scene 10040zlamowi with dissolve
    z "Not an option at all{p}you're my son's age{p}don't count on that"
    scene 10040smda with dissolve
    z "I won't do this"
    scene 10040smutna with dissolve
    e "Come on, don't be such a prude.{p}It's just a small favor. I won't take no for an answer."
    scene 10040smd with dissolve
    z "I can't believe you're asking me to do something like this.{p}It's wrong..."
    scene 10040smutna with dissolve
    e "Think about it, though. If you refuse, who knows what I might do to Tommy?{p}Maybe they'll catch him with weed and throw him out of the university?"
    scene 10040zlamowi with dissolve
    z "No... you definitely won't do that."
    scene 10040zlaslucha with dissolve
    e "Just do it, and I'll leave Tommy alone. I promise.{p}It's a small sacrifice to ensure his safety, isn't it?"
    z "..."
    z "..."
    z "..."
    scene 10040smutnasciaga with dissolve
    z "I can't believe I'm doing this..."
    z "But if it means you won't sell him this shit anymore..."
    e "That's what I like to hear. Tommy's future is now in your hands."
    scene 10040sciagamowi with dissolve
    z "If you tell anyone about this, I will kill you"
    scene 10040sciagaslucha with dissolve
    pause 1
    scene 10041 with dissolve
    pause 1
    scene 10041a with dissolve
    pause 1
    scene 10041b with dissolve
    pause 1
    scene 10041c with dissolve
    pause 1
    z "..."
    scene 10042 with dissolve
    pause 1
    scene 10042a with dissolve
    pause 0.5
    scene 10042b with dissolve
    pause 0.5
    scene 10042c with dissolve
    pause 0.5
    scene 10042d with dissolve
    z "Enjoy"
    z "..."
    e "They are beautiful...Damn."
    "{color=#A8E4A0}{i}{size=-3}Your dick was growing harder and harder with every second it passed. Her tits were something else, out of the ordinary"
    scene 10043 with dissolve
    e "So nice..."
    "{color=#A8E4A0}{i}{size=-3}They looked soft, and warm. As if you could squish your hand onto it."
    scene 10043a with dissolve
    e "This will be our little secret..."
    e "I have to touch them"
    scene 10044 with dissolve
    z "..."
    scene 10044a with dissolve
    z "No"
    "{color=#A8E4A0}{i}{size=-3}You looked at her with a meaner expression, trying to put pressure on her."
    e "Either you let me or I'm leaving"
    scene 10044 with dissolve
    z "..."
    scene 10044sad2 with dissolve
    z "..."
    scene 10044sad with dissolve
    z "...{p}...Ok..."
    show tit001 with dissolve
    z "..."
    "{i}*Her breathing quickens*"
    z "..."
    scene 10045y with dissolve
    z "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} How did I get involved in something like this..."
    scene 10045z with dissolve
    z "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} My son's friend gropes my breasts and I let him do it..."
    show tit002 with dissolve
    $ renpy.pause(2.7, hard=True)
    scene 10045
    "{color=#A8E4A0}{i}{size=-3}After grabbing them, and squishing your hand onto her soft melons, you couldn’t help it - You needed to whip your big throbbing cock out."
    z "...{p}What the fuck are you doing??!"
    e "I'm not a kid"
    e "You think that just touching your tits would be enough for me?"
    scene 10047 with dissolve

    scene 10047a with dissolve

    scene 10048 with dissolve
    e "Now take your little hand and grab my cock"
    e "And then your Tommy will be untouchable throughout his entire studies"
    z "..."
    show grabmtom
    e "You know what to do."
    scene nochoke00 with dissolve
    show hhjj0
    $ renpy.pause(2, hard=True)
    e "Very nice..."
    $ renpy.pause(3, hard=True)

    e "Hold it tighter"
    e "So good{p}I'm about to cum."
    e "ooooooh"
    scene finish00 with dissolve:
        zoom 0.5
    e "Ah"
    show finishmomtommy
    $ renpy.pause(4, hard=True)
    e "Oh.. Wowoowwwww..."
    scene 10052 with dissolve
    e "Nice..."
    scene 10052nottom with dissolve
    z "Now, get out of my car"
    z "And remember what you promised"
    e "Yeah..."

    scene 10056 with dissolve
    e "..."

    show carleft
    $ renpy.pause(2, hard=True)

    scene 10056a
    e "..."

    scene 10057 with dissolve
    e "Crazy chick"
    scene 10058 with dissolve
    e "I must hurry. Classes are coming soon!"
    scene 10058a with dissolve
    e "I have lessons with my [woman_role]"
    scene black with fade
    show text "University" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text

    stop music fadeout 1.0
    play music "music/Mnic.wav"
    scene 10100 with dissolve
    e "{color=#ffa500}{i}*panting*"
    scene 10100a with dissolve
    p "Hey [player_name]."
    scene 10100b with dissolve
    p "You look like shit."
    scene 10100c with dissolve
    e "Fuck off Gary"
    scene 10101 with dissolve
    e "You idiots can't even turn on the lights..."
    scene 10101a with dissolve
    p "If you tried to turn it on yourself, you would see that it doesn't work."
    scene 10101b with dissolve
    "{color=#ffa500}{i}*The door slams*"
    show 10102 at Move((0, 0), (0, 0.99), 7.0, xanchor=0, yanchor=0.5)
    $ renpy.pause(7, hard=True)
    p "Daaamn"
    p "I love these classes"
    e "Very funny"
    scene 10103a with dissolve
    m "Good afternoon!"
    scene 10104 with dissolve
    c "Good afternoon{p}Hello!"
    scene 10104a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Uhh..."
    scene 10104b with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It seems broken..."
    scene 10105 with dissolve
    m "The light doesn't seem to be working..."
    m "It will soon be dark outside, I'll just check attendance and there will be no classes today."
    scene 10107 with dissolve
    c "Hooray!"
    scene 10107a with dissolve
    p "Why are you so sweaty?"
    scene 10107b with dissolve
    e "Mind your own business dickhead."
    scene 10107c with dissolve
    p "Okay, okay, I'm just asking"

    scene 101060 with dissolve
    p "You know what [player_name]?"
    scene 101061 with dissolve
    p "You are stupid as fuck{p}But your [woman_role]? Damn, she’s so fucking hot, dude..."
    scene 101064 with dissolve
    p "Do you think she’s into young cocks?"
    scene 101068 with dissolve
    e "Fuck you."
    scene 101067 with dissolve
    p "Chill Bro"
    scene 101066 with dissolve
    p "I'm just saying that if I had a [woman_role] like that, I wouldn't let her sleep"
    scene 101068 with dissolve
    e "I wonder if you were as brave when you asked Paige out on a date."
    scene 101064 with dissolve
    p "Paige looks like shit next to your [woman_role], dude."
    scene 101066 with dissolve
    p "I really envy you."
    scene 101065 with dissolve
    p "Does your old pal live with you?"

    e "Yeah, but he's never home and he just pisses me off."
    scene 101068 with dissolve
    e "And when he's home, we argue all the time"
    scene 101066 with dissolve
    p "I can always replace him if you want"
    scene 101067 with dissolve
    e "I'd rather be an orphan."
    scene 101080a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He is here.{/i}"
    scene 101081 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Focus [woman_name]{/i}"
    scene 101082 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He keeps talking to his friend and they stare at me{/i}"
    scene 101081 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I hope he's not stupid enough to tell his friends about what happened{/i}"
    scene black with fade
    show text "Several minutes of checking attendance later" at title with dissolve
    $ renpy.pause(2, hard=True)
    scene 1010900 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I can see less and less, it's starting to get dark{/i}"
    scene 1010901 with dissolve
    m "...and...{p}Mr. Zerat?"
    c "Absent today!"
    scene 1010902 with dissolve
    m "That's all. Tell everyone who's absent that they will have to make up for the day."
    m "And I wish everyone else a nice weekend"
    scene 10110 with dissolve
    p "You coming?"
    scene 10110a with dissolve
    e "I need to talk to my [woman_role]{p}I'll join you later"
    scene 10110b with dissolve
    p "Sure, see you later, buddy."
    scene 1011208 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Just look at her."
    scene 1011209 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She is extremely stressed."
    scene 1011210 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I'll pretend I'm leaving, I wonder if she'll stop me"
    scene 1011211 with dissolve
    pause
    scene 10112a0 with dissolve
    pause 0.5
    scene 10112a1 with dissolve
    pause 0.5
    scene 10112a2 with dissolve
    pause 0.5
    scene 10112a3 with dissolve
    pause 0.5
    scene 10112a4 with dissolve
    pause 0.5
    scene 10112a5 with dissolve
    pause 0.5
    scene 10112a6 with dissolve
    pause 0.5
    scene 10112a7 with dissolve
    pause 0.5
    scene 10112a8 with dissolve
    pause 0.5
    scene 10112a9 with dissolve
    m "[player_name] wait..."
    scene 1011309 with dissolve
    e "Yeah?"
    scene 1011310 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I don't know why there are always keys in the door here, but thanks for that..."
    "{color=#ffa500}{i}*the sound of the door locking.*"
    scene 1stage0 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I have to be confident, it's obvious that she's stressed.{/i}"
    scene 1stage1 with dissolve
    m "Can we talk?"
    scene 1stage2 with dissolve
    e "Sure..."
    scene 1stage3 with dissolve
    e "...[woman_role].{p}"
    scene 1stage4 with dissolve
    pause
    scene 1stage5 with dissolve
    m "What you did..."
    scene 1stage6 with dissolve
    m "...was wrong."
    scene 1stage7 with dissolve
    pause 0.5
    scene 1stage8 with dissolve
    pause 0.5
    scene 1stage9 with dissolve
    pause 0.5
    e "I really like these photos."

    scene 2stage00
    pause 0.5
    scene 2stage01
    pause 0.5
    scene 2stage02
    pause 0.5
    scene 2stage03
    pause 0.5
    scene 2stage04 with dissolve
    m "I understand that at your age you are interested in.."
    scene stage06 with dissolve
    m "...the female body, and such...."
    scene stage07 with dissolve
    m "But I'm your [woman_role], so... Pictures like that are very, very inappropriate."
    scene stage08 with dissolve
    scene stage09 with dissolve
    scene stage10 with dissolve
    scene stage11 with dissolve
    scene stage12 with dissolve
    m "I am asking you to remove them."
    scene stage13 with dissolve
    "Just thinking about these photos makes my body shiver."

    scene stage3view3 with dissolve
    m "So what?"
    e "I'm a fan of your body."

    e "If you let me be good to you..."
    e "...I will take good care of you and your needs."
    scene needs with dissolve
    m "My...{p}...needs?"
    scene stage3viewdress1 with dissolve
    pause 0.25
    scene stage3viewdress2 with dissolve
    pause 0.25
    scene stage3viewdress3 with dissolve
    pause 0.25
    scene stage3viewdress4 with dissolve
    pause 0.25
    scene stage3viewdress5 with dissolve
    pause 0.25
    scene stage3viewdress6 with dissolve
    pause 0.25
    scene stage3viewdress7 with dissolve
    e "You don't need it"
    scene shame00 with dissolve
    e "If you don't want anyone to find out, you'll keep quiet now."
    show ep1shame
    $ renpy.pause(2, hard=True)
    scene 10499 with vpunch
    pause
    scene 10499a with dissolve
    e "I am not your enemy"
    scene 10500 with dissolve
    e "I can delete all the photos, and forget about everything"
    scene 10502 with dissolve
    e "But you must be punished"
    scene 10503 with dissolve
    m "I'm your [woman_role]... it's not normal what you're doing"
    scene 10501 with dissolve
    m "Have you seen enough? I want to go"
    scene 10503a with dissolve
    e "I want to be your friend, [woman_role]."
    scene 10504 with dissolve
    e "And friends help each other"
    show ep1grabfinal
    $ renpy.pause(14, hard=True)
    scene 10505 with dissolve
    e "And I'm your best friend"
    show dckep1msg
    m "[player_name]..."
    m "Why are You doing this..."
    e "Shhh..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He is too strong, I have no chance to break free"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Calm down [woman_name], he definitely won't do anything more"
    scene dckgrab059 with dissolve
    e "Just look at the effect you have on me"
    show dckep1grab with dissolve
    $ renpy.pause(4, hard=True)
    e "Ahh"
    scene 10506 with vpunch
    m "Stop..."
    show finalep1 with dissolve
    $ renpy.pause(1, hard=True)
    m "[player_name], please let go of my hand"
    $ renpy.pause(2, hard=True)
    m "I am really sorry..."
    e "You’ve got such delicate hands"
    "{color=#A8E4A0}{i}{size=-3}Your legs were shaking to the touch of her hand around your cock. A part of you couldn’t believe what was going on."
    "{color=#A8E4A0}{i}{size=-3}You guided her hand up and down, trying to make her jerk you off faster, and faster."
    "{color=#A8E4A0}{i}{size=-3}With every stroke, you could feel your cock getting ready to cum, as it began to throb, and your balls lifted themselves up."
    scene 10507 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I need to stop it..."
    show beforehb with dissolve
    $ renpy.pause(2, hard=True)
    scene 10508 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} NOW"
    show headbutt with dissolve
    $ renpy.pause(3, hard=True)
    scene lastsce0 with dissolve
    e "OUCH"
    "{color=#A8E4A0}{i}{size=-3} [woman_name] ran away."
    scene lastsce1 with dissolve
    scene lastsce2 with dissolve
    scene lastsce3 with dissolve
    scene lastsce4 with dissolve
    scene lastsce5 with dissolve
    scene lastsce6 with dissolve
    pause
    scene lastsce7 with dissolve
    pause
    scene black with fade
    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 2" at title with dissolve
    $ renpy.pause(3, hard=True)
    stop music fadeout 1.0
    play music "music/Mshl.mp3"
    scene new200010 with dissolve
    "{color=#A8E4A0}{i}{size=-3} As you walked home, midway through, you spotted a girl in the distance dressed in a rather weird outfit."
    scene new200011 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What’s up with her?{p}She looks like a damn jaguar or something..."
    scene new200012 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Is she one of those insurance promoters? Maybe there’s a new company with some animal name or something."
    scene new200013 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You kept walking, acting casual, but as soon as you got close enough, she practically jumped at you, eager to talk."
    h "H-Hi! My name’s Sheila.{p}Would you like to save a beaver?"
    scene new20003 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Before responding, you scanned her from head to toe, noticing her slim but curvy figure. She had perky but small breasts, a slim waist, and a rounded, petite ass."
    e "Hm... I’d need more than a minute with that 'beaver' between your legs, sweetheart."
    scene new20004 with dissolve
    h "E-Excuse me?"
    scene new20004a with dissolve
    e "Oh... Sorry, what’s this about?"
    scene new20004 with dissolve
    h "Ahem... Well, uh, I’m with 'Save the Rivers' a small organization collecting donations and signatures to help save the beavers in town that are being displaced because of corporations dumping pollutants into the river."
    scene new20004c with dissolve
    h "It's only 50$ that can save the beaver family."
    scene new20004a with dissolve
    h "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I hope he agrees...{p}This is my last chance to save these poor animals."
    e "Right...{p}But shouldn’t you be dressed in something related to beavers?"
    scene new20004b with dissolve
    h "Uh... What do you mean?"
    e "I mean, you're out here trying to save beavers, but you're dressed like one of their natural predators."
    scene new20003b with dissolve
    h "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I don't remember what I was supposed to answer to the question about my outfit."
    scene new20003c with dissolve
    h "Oh... Uh... Well..."
    e "Go ahead, I’m listening."
    scene new20003cc with dissolve
    h "Well...{p}I don’t know, the company makes me wear this.{p}I guess it’s to attract more donors."
    e "I see... They must be desperate for money, huh?"
    scene new20003a with dissolve
    h "...Yeah, you could say that.{p}Seems like no one in this city cares about beavers. I haven’t gotten a single dollar all day, and I’ve got to report back in an hour."
    scene new20004d with dissolve
    e "So... you’d do anything to make sure you bring those 50 dollars back to your little company, huh?"
    scene new20004 with dissolve
    h "...Yeah, the campaign’s almost over, and I’m not meeting expectations... And we’ve got a really ambitious goal."
    scene new20004a with dissolve
    e "Wow, you’re really committed to beavers, huh?{p}What, is your dad one or something?"
    scene new20004e with dissolve
    h "Ha ha, very funny...{p}Did you know that when beavers build dams, they help prevent flooding and overflows that threaten our city?"
    scene new20003aa with dissolve
    e "Uh... I thought it was the opposite."
    scene new20004f with dissolve
    h "Nope, and not just that, beavers are cute, adorable little creatures. I couldn’t live in a world without them."
    scene new20003aa with dissolve
    e "I thought you could eat them..."
    scene new20004b with dissolve
    h "Well, yeah...{p}But what kind of lunatic would do that?{p}Would you eat your dog?"
    e "No..."
    scene new20004g with dissolve
    h "Exactly! I love beavers, not just because they’re chubby and cute, but because of the role they play in our ecosystem. But above all...-"
    scene new20004c with dissolve
    h "...beavers are nature's engineers, creating complex dams and lodges that reshape landscapes and create vital wetland habitats...."
    scene new20004h with dissolve
    h "These industrious rodents are keystone species, meaning their presence has a disproportionately large impact on their environment, benefiting countless other plants and animals. "
    scene new20004 with dissolve
    h "Their ponds and wetlands act as natural water filters, improving water quality and helping to mitigate droughts and floods."
    scene new20003a with dissolve
    h "Moreover, beaver habitats serve as carbon sinks, playing a crucial role in combating climate change by storing significant amounts of greenhouse gases."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Oh god, when is she going to shut up? "
    scene new20004 with dissolve
    e "Hey, did you really mean ‘anything’ for that money?"
    scene new20003e with dissolve
    h "Yes..."
    scene new20004sad2 with dissolve
    e "Are you sure?"
    scene new20004b with dissolve
    h "Yeah! I’d do anything for them..."
    scene new20004sad2 with dissolve
    e "Well... Follow me.{p}I think we can work something out..."
    scene new20004angry with dissolve
    h "W-What? Follow you? To where!?"
    scene new20004sad2 with dissolve
    e "Perhaps... that alley right there..."
    scene new20004 with dissolve
    h "Uhm...{p}But why!?{p}Can't you just tell me about your deal here!?"
    scene new20004listen with dissolve
    e "Uh... No. It's kind of secret.{p}Don't want any unwanted ears peeking."
    scene new20004c with dissolve
    h "... Alright..."
    "{color=#A8E4A0}{i}{size=-3} Sheila followed you into the alley halfway down the street."
    scene black with fade
    pause
    scene new20005 with dissolve
    e "Look, I’ve got a serious proposal for you..."
    scene alejka7 with dissolve
    h "Yeah...{p}Tell me..."
    scene alejka7a with dissolve
    e "I can see you don’t want to walk away empty-handed...{p}And I don’t want to go home with my balls full..."
    scene alejka6 with dissolve
    e "If you catch my drift..."
    scene alejka3 with dissolve
    h "Wait...{p}Are you suggesting..."
    scene alejka2 with dissolve
    e "Come on, you help me, I help you.{p}What do you say?"
    scene alejka0 with dissolve
    h "You’re crazy!"
    scene alejka1 with dissolve
    e "Hey, think of the poor beavers! Besides, none of these jerks in the city are giving you money. Maybe they think you're a scammer or something."
    scene alejka4 with dissolve
    h "...I’m not a scammer..."
    scene alejka0 with dissolve
    h "P-Poor beavers, they really need our help...{p}My help..."
    scene alejka2 with dissolve
    e "So... Are you going to waste this opportunity to help them?"
    scene alejka3 with dissolve
    h "... No..."
    scene alejka7a with dissolve
    e "Then come on, cheer up! Show me those tits..."
    scene alejka6 with dissolve
    h "W-Wha!?{p}N-No way!"
    scene alejka7 with dissolve
    h "I thought you meant another type of deal! What the hell!?"
    scene alejka7 with dissolve
    e "Do you have another choice? It's either flashing your tits or letting beavers die.{p}Up to you"
    scene alejka4 with dissolve
    h "Y-You're one thoughtless bastard!"
    scene alejka5 with dissolve
    e "And you're one broke bitch that needs 50$ for a cause that no one outside your little company care about. What a shame.{p}Tits or leave. Now."
    scene alejka1 with dissolve
    h "Ugh..."
    scene new20006 with dissolve
    pause 0.5
    scene new20007 with dissolve
    pause 0.5
    scene new20008 with dissolve
    e "Mmm...{p}Your nipples are hard...{p}Seems like you’re enjoying this..."
    scene new20008a with dissolve
    h "It’s all for the beavers... Anything for them... Okay?"
    e "You'll blow me off."
    h "B-But..."
    e "Do it. It's part of the deal. You either suck me or I'm gone."
    h "... Okay! Guh... Fuck."
    scene new20010 with dissolve
    pause
    scene new20011 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Sheila turned around, kneeling in front of you as you aimed your cock at her lips."
    scene new20012 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Hesitant, but resigned, she opened her mouth, allowing your cock inside."
    scene new20013 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You pressed your cock against her lips, and let it all in, as you began to face-fuck her like nothing."
    show sheillbj with dissolve
    "{color=#A8E4A0}{i}{size=-3} With both palms holding her head, you began thrusting, feeling how she locked her lips around your cock, sucking it in, knowing what she was doing."
    e "Good... Seal your lips around it, make it worthwhile."
    h "Gu-uh!"
    "{color=#A8E4A0}{i}{size=-3} She nodded, and began to seal her lips tight on your throbbing cock, applying pressure to it, while you bobbed her head with your hands."
    "{color=#A8E4A0}{i}{size=-3} You kept thrusting your hips fast, as your balls hit her chin repeatedly."
    e "Mmm...{p}Such a good sucker. I'm 'bout to nut!"
    "{color=#A8E4A0}{i}{size=-3} You grabbed her from her suit's ears, perhaps taunting and asserting your dominance, thrusting the last few inches faster."
    e "Now we know what these were for... Gotta give credit to your boss for this one."
    h "Mpfh...Guh!"
    scene sheilcm1 with dissolve
    "{color=#A8E4A0}{i}{size=-3} As your balls kept hitting, and your dick kept thrust, finally, with a low groan, you came deep in her mouth, splashing her throat, and entire mouth with thick ropes of cum."
    scene sheilcm2 with vpunch
    pause
    scene sheilcm3 with vpunch
    pause
    scene sheilcm4 with dissolve
    e "Mmm...{p}Swallow it all, you basket case."
    scene sheilcm5 with dissolve
    pause
    scene sheilcm6 with dissolve
    "*gulp*"
    "{color=#A8E4A0}{i}{size=-3} Sheila gagged but managed to swallow most of it."
    scene sheilcm7 with dissolve
    h "Gah... Ugh... I-I did it... for the beavers... Anything for them..."
    scene sheilcm9 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You zipped up, watching her as she struggled to regain her composure, still kneeling in front of you, her cheeks blushed."

    scene sheilcm10 with dissolve
    e "Here’s your 50$. You did a pretty well job there"

    scene sheilcm11 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You handed her the money, and she took it with shaking hands."
    h "T-Thank you...{p}You’ve really helped us today."
    "{color=#A8E4A0}{i}{size=-3} You turned and walked away, leaving her to collect herself."
    scene black with Fade(2.0, 1.0, 2.0)
    stop music fadeout 1.0
    play music "music/Audio003.mp3"
    scene 00000prolog with fade
    pause
    scene 00000prologa with fade
    pause
    scene 00000prologb with fade
    pause
    scene 00000prologc with fade

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} How did I get myself into this mess....?"
    m "..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I don't wanna face the answer to that now. But I do need to talk with him..."

    scene 20000 with fade

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ugh, I've been sitting here for hours, watching this rubbish...{p}Is she going to stay hidden away all night?"

    scene 20000 with dissolve:
        xalign 0.8
        yalign 0.4
        zoom 2
        ease 2 zoom 4

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Maybe she's waiting for me to come visit her..."

    scene 20000aTo20000eAnimated with dissolve:
        xalign 0.8
        yalign 0.4
        zoom 4

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But I guess probably not."

    scene 20000 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} That's the sound of her bedroom door..."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Here she comes."

    scene 20001 with dissolve

    m "*sigh*"

    m "[player_name]"

    m "We need to talk. {p}Now."

    e "Sure, I'm not busy.{p}What do you want to talk about?"

    scene 20001a

    m "Turn off the TV."

    m "We need to discuss... what happened."

    scene 20001b
    e "Sure"

    scene 20001b

    pause

    scene 20001c

    e "Done"

    e "So... what's so important that you needed to talk to me so suddenly?"

    scene 20002

    m "Don't pretend you don't know what I'm talking about, [player_name]."

    scene 20003

    m "What you did to me...{p}...was horrific."

    m "And I'm certainly not going to let it just go by without resolving it."

    scene 20004 with dissolve

    e "What are you going to do?"

    scene 20005 with dissolve

    m "I'm going to tell your father everything. A full confession."

    m "And then I'll tell him what you did... how you found out, and then used it to blackmail me, just to fulfil your sick fantasies."

    scene 20006 with dissolve

    e "Ha!{p}Ha-ha-ha!"

    e "[woman_name], you can't seriously expect me to believe that you're actually going to tell Dad all about how you cheat on him every time he's away."

    scene 20007a with dissolve

    e "There's no way you'd throw away everything you've got from him in this marriage... just so he can punish me?"

    scene 20007b with dissolve

    e "Was that really your plan? Don't you know he loves me? He'll probably reward me for discovering that you're a cheating, lying whore!"

    e "And why would he even believe your story about what I supposedly did to you? You have to admit, it sounds crazy..."

    e "... Why would any normal, self-respecting woman would allow herself to be treated like that? To go along with a request for sexual favors from her [player_role]? Just to conceal her slutty behavior?"

    e "Seriously, there's no way he'd believe you. Anyway, you've got no proof... {p}But I do..."

    e "I guess you'll have to try a little harder."

    scene 20003

    m "We live together."

    scene 20007a

    e "So you think I can't be charmed by your beauty?"

    scene 20003

    m "It's simply wrong. We can't have that kind of interaction."

    m "And you're acting like it's all some kind of joke."

    m "It's not! What you did is a very serious thing. A crime, even."

    scene 20005 with dissolve

    m "Whatever I did while your father was away... what you did to me was even worse."

    scene 20007b with dissolve

    pause

    scene 20007a with dissolve

    e "Maybe you're right."

    e "But maybe not."

    e "I think cheating behind someone's back is worse."

    e "And I know it's not the first time."

    e "Let's talk about this. Come, sit next to me."

    scene 20009a with dissolve

    scene 20010 with dissolve

    scene 20009a with dissolve

    scene 20010 with dissolve

    scene 20009a with dissolve

    scene 20007a

    e "I'm not gonna bite you."

    scene 20004 with dissolve

    m "Okay..."

    scene 20003 with dissolve

    m "I'll sit. I'm going to trust you. Don't you dare do anything funny, though."

    scene 20002 with dissolve

    pause

    scene 20002b with dissolve

    pause

    scene 20011a with dissolve

    e "{color=#ffa500}{i}sniff... sniff...{/i}"

    scene 20011 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Is that...?{/i}"

    scene 20011b with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh yeah{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It definitely smells like alcohol{/i}"

    scene 20011bb with dissolve

    m "Look. What you did was wrong... very wrong."
    m "But... I don't want to ruin my relationship with your father..."
    m "And... if we're going to keep living together, I don't want to have to always be avoiding you."

    scene 20011 with dissolve

    pause

    scene 20011a with dissolve

    e "I don't want that either."

    e "I really like our new relationship."

    scene 20012b with dissolve

    m "Listen to me.{p}We don't have a “relationship”."
    m "Half of me still can't believe it... like I'm in shock..."

    scene 20013 with dissolve

    m "After what happened at school."

    scene 20013a with dissolve

    pause

    scene 20013 with dissolve

    m "{color=#ffa500}{i}*deep breath*{/i}{/color}{p}I know you were hurt by with what you saw."

    scene 20013a with dissolve

    m "But I'm a grown woman."

    m "And I have the right to be happy too."

    scene 20014atalk with dissolve

    m "And as a woman..."

    scene 20014asilent with dissolve

    pause

    scene 20014atalk2 with dissolve

    m "I have my needs."

    scene 20014atalk with dissolve

    m "And your father prefers gambling and drinking more than spending time with his wife.{p}More than... taking care of me."

    e "Maybe what you're saying is reasonable.{p}I can see you might feel neglected."

    e "But that still doesn't give you the right to cheat on him with some random guys!"

    e "If you have “needs”..."

    e "All you had to do was ask me."

    scene 20014ashock with dissolve
    m "What?!{p}You?!"

    m "You are my [player_role]!{p}The closest person to me..."

    scene 20014atalk2 with dissolve

    m "What was I supposed to ask you for?"

    scene 20014asilent with dissolve

    pause

    scene 20013a with dissolve

    m "I know it is my fault."

    m "I know that what you saw made you were angry with me...{p}and that's why you made me..."

    scene 20013 with dissolve

    m "...do those things."

    scene 20013 with dissolve

    m "But...{p}I forgive you."

    e "..."

    m "We can pretend nothing happened, and go back to how things were before...{p}live normally together."
    m "And I promise I'll do the right thing by your father from now on...{p}I won't hurt you again."

    scene 20014alisten with dissolve

    e "But I don't want to pretend nothing happened."

    scene 20014alook with dissolve

    e "You're the prettiest woman I know."

    e "Even just sitting here right now, next to you... if I am honest, I can't deny that you are making me extremely horny."

    scene 20014atalk with dissolve

    m "Don't say things like that to me, [player_name]."

    m "You're so much younger than me. You should look for a sexual partner who is closer to your own age."

    scene 20014ashock with dissolve

    e "I prefer a partner with experience."

    scene 20014atalk2 with dissolve

    m "Can you stop?"

    m "Don't you understand that everything you saying is... wrong?"

    scene 20014asilent with dissolve

    pause

    scene 20013 with dissolve

    m "What happened at the university was wrong! I should never have allowed it to escalate like that...{p}but I was in shock, I think."

    scene 20013a with dissolve

    m "Everything happened so fast."

    scene 20014alook with dissolve

    e "No! It wasn't “wrong”... it was wonderful."

    e "It wasn't until that moment that I realized how much I care about you."

    e "And how much I want to feel close to you like that again."

    "{color=#ffa500}{i}*clothes rustling*"

    scene 20015shock with dissolve

    m "HEY!"

    scene 20015 with dissolve

    m "[player_name]! What are you doing?!"

    m "Stop this! Put that thing away!"

    scene 20021a with dissolve

    e "Nah..."

    scene 20021a with dissolve

    e "I'm tired of just talking."

    scene 20022b with dissolve

    e "You know what?"

    scene 20022b with dissolve

    e "I want more."

    scene 20023a with dissolve

    m "Don't do this. Please, put your pants back on again."

    scene 20015 with dissolve

    m "I... I don't want to do anything like that... with you."

    scene 20015a with dissolve

    "{color=#A8E4A0}{i}{size=-3}She keeps staring at your penis{/i}"

    scene 20015 with dissolve

    m "I only wanted to talk..."

    scene 20015a with dissolve

    e "We can talk some more... {p}When you're done with me."

    e "Why don't you come closer."

    scene 20023 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} The alcohol must be affecting her, otherwise she certainly would have run away by now..."

    e "Come on, it's nothing."

    e "There's no one else here... no one will know about it..."

    e "This will be the last time, and then I'll delete the photos."

    scene 20015a with dissolve

    e "Come on. I promise."

    scene 20015 with dissolve

    m "..."

    m "Delete the pictures first."

    scene 20015a with dissolve

    e "You think I'm stupid?"

    e "I know how that works. Once they're gone, you'll just leave me here, frustrated."

    e "Come on, hurry up... or I might start to have other ideas on what to do with the pics."

    scene 20023 with dissolve

    pause

    scene 20023a with dissolve

    m "*sigh* I just have to trust you. To do the right thing."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I think she said that earlier today."

    scene 20023bb with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's actually gonna do it... she is definitely drunk."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I'm super lucky."

    scene 20023bbb with dissolve

    e "Come on [woman_role]"

    scene 20023b with dissolve

    "{color=#A8E4A0}{i}{size=-3}She stopped, frozen, just staring blankly at your dick.{/i}"

    scene 20023bbbb with dissolve

    m "I don't...{p}want...{p}to do it."

    e "Please, just help me out..."

    scene 20023bbbbb with dissolve
    m "Okay...{p}But please, close your eyes... and don't say anything."

    show s2h1 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's actually doing it...{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I thought it would be harder to convince her...{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Gotta stay in control... can't fuck it up now.{/i}"

    scene 20030x

    pause

    scene 20031x

    m "What...?"

    scene 20032x with dissolve

    m "Hey... stop..."

    show s2touchfirst with dissolve

    m "No... ahhh!"

    m "...You mustn't..."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh god... she's already wet...{/i}"

    pause

    show hjfingerv1 with dissolve

    "{color=#A8E4A0}{i}{size=-3} She moans softly{/i}"

    m "You can't..."

    "{color=#A8E4A0}{i}{size=-3} Her hips move involuntarily, rubbing her pussy against your fingers."

    m "{color=#ffa500}{i}*Moans*"

    e "Oh yeah... that's so good..."

    m "..."

    e "Do it faster, [woman_role]..."

    show hjfingerv2 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's doing what I say now...{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Seeing how she's clearly drunk...maybe I'll try taking things further...{/i}"

    scene s20035 with dissolve

    pause

    scene s20036 with dissolve

    e "Suck it!"

    show s2bj
    $ renpy.pause(3, hard=True)

    scene s20035 with dissolve

    "{color=#A8E4A0}{i}{size=-3} She stopped immediately when she realized what happened"

    scene 20040 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20041 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20042 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20043 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20044 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20045 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20046 with vpunch
    $ renpy.pause(0.2, hard=True)
    scene 20047 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20048 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20049 with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20050 with dissolve

    m "What the fuck are you doing?!"

    scene 20051 with dissolve

    m "I'm not some slut that you can insult and mess around... and I'm not doing this!"

    scene 20052 with dissolve

    m "What you just tried to do is called rape!"

    scene 20053 with dissolve

    m "I don't care where you go...{p}But tomorrow you have to get out of this house."

    scene 20055
    stop music fadeout 1.0
    play music "music/Mnicdk.mp3"
    $ renpy.pause(2, hard=True)
    pause

    "{color=#A8E4A0}{i}{size=-3}Just as she started walking away, you grabbed her wrist."

    scene 20057 with dissolve

    e "You don't seem to understand..."

    scene 20056a with dissolve

    e "...that you're my slut now."

    scene 20058 with dissolve
    scene 20059 with dissolve
    scene 20060 with dissolve
    scene 20060a with dissolve
    scene 20060b with dissolve
    scene 20061 with dissolve
    scene 20062 with dissolve

    e "And do you know what sluts do?"

    scene 20063 with dissolve

    e "They suck cock."

    show bj68v1 with dissolve

    e "Just like this."

    m "MMM!!!"

    show bj68v2 with dissolve
    e "Oh... that's amazing..."

    m "{color=#ffa500}{i}*She makes strange sounds as if she wanted to say something*"

    e "Yeah... that's real good..."

    e "But I want you to go faster."

    "{color=#A8E4A0}{i}{size=-3}You force her to move faster"

    show bj68v3 with dissolve

    e "Oohhhh.."

    pause

    e "{color=#ffa500}{i}*groans*{/i}{/color} So good."

    "{color=#A8E4A0}{i}{size=-3}You pushed her hands away from you and placed your hand on the back of her head"

    show bj69v4 with dissolve

    e "Your mouth is incredible."

    pause

    e "You are the best [woman_role] ever."

    e "If I had known it would be so nice, you would have sucked it for me a long time ago."

    show bj69v5 with dissolve

    pause

    e "I love the feel of your lips and tongue..."

    e "Yeah... just like that..."

    e "I knew it... you really are a real slut."

    "{color=#A8E4A0}{i}{size=-3}She can't say anything but you hear her trying to moan.{/i}"

    show bj70 with dissolve

    e "{color=#ffa500}{i}*groans*{/i}{/color} You're gonna make me come soon..."

    e "Right into your mouth!"

    "{color=#A8E4A0}{i}{size=-3}She started struggling in panic."

    scene 20070 with vpunch

    e "AGHHH!!!"

    scene 20070a with vpunch

    scene 20070a with vpunch

    e "Oh GOD DAAAAAAAAMN!!!"

    scene 20070b with vpunch

    scene 20070b with vpunch

    scene 20070b with vpunch

    e "*panting* Take it! Take it all, [woman_role]!!"

    scene 20070c with vpunch

    scene 20070c with vpunch

    e "Ahhhhhh...."

    scene 20070d with dissolve

    e "..."

    scene 20070e with dissolve

    e "That was so good..."

    "{color=#A8E4A0}{i}{size=-3}She's silent... but you can see she's in total shock."

    scene 20071a with dissolve

    m "{color=#ffa500}{i}*Breaths heavily{/i}"

    scene 20071b with dissolve

    $ renpy.pause(1, hard=True)

    scene 20071c with dissolve

    $ renpy.pause(1, hard=True)

    scene 20072 with dissolve

    $ renpy.pause(0.5, hard=True)

    scene 20072a with dissolve

    $ renpy.pause(0.5, hard=True)

    scene 20072b with dissolve

    $ renpy.pause(0.5, hard=True)
    scene 20072c with dissolve

    $ renpy.pause(0.5, hard=True)

    scene 20073 with dissolve
    $ renpy.pause(1, hard=True)

    scene 20073a with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20073b with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20073c with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20073d with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20073e with dissolve
    $ renpy.pause(0.2, hard=True)
    scene 20073g with dissolve
    $ renpy.pause(0.5, hard=True)
    scene 20073f with dissolve

    m "I...{p}I..."

    scene 20073g with dissolve

    pause

    scene 20073f with dissolve

    m "I can't believe...{p}You did this to me..."

    scene 20073h with dissolve

    m "..."

    e "..."

    scene 20073i with dissolve
    m "Aren't you going to say something?"
    scene 20073h with dissolve
    e "..."
    scene 20073i with dissolve
    m "Anything?"

    scene 20073h with dissolve

    pause

    scene 20086 with dissolve
    pause 0.2
    scene 20086a with dissolve
    pause 0.2
    scene 20087a with dissolve
    pause 0.2
    scene 20087b with dissolve
    pause 0.2
    scene 20088 with dissolve
    pause 0.2
    scene 20088a with dissolve

    "{color=#A8E4A0}{i}{size=-3}She ran away to her bedroom."
    scene black with fade
    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 3" at title with dissolve
    $ renpy.pause(2, hard=True)
    stop music fadeout 1.0
    play music "music/Mda.wav"
    scene 30001 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Well... It sure was a good day."
    scene 30002 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Of course, I'm curious what's on my [woman_role]'s mind right now... {p}Probably feeling terrible."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But it's totally her fault, not mine."
    scene 30003 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Huh?{p}Is that...?"
    scene 30003drzwi with dissolve
    "{color=#ffa500}{i}*Front door unlocks"
    scene 30003opendoor with dissolve
    d "Hey hey hey!"
    d "Guess who's back, amigos!"
    scene 30004 with dissolve
    e "Dad? You're back!"
    scene 30004dad with dissolve
    d "Yeah, kid! I’m here now.{p}However, I only came back for a day."

    d "They canceled one of my meetings and I decided to drop by to see how you were doing."

    d "Is [woman_name] home?"
    scene 30004 with dissolve
    e "Yeah, probably sleeping in her room. It's Saturday, after all."
    scene 30005 with dissolve
    d "I’ve got to take a bath. I'm all reeky from the trip."

    d "And also...[player_name]...{p}I want to talk with you later, but not here and not now."
    scene 30006 with dissolve
    d "Maybe we should go out for something to eat later, perhaps?"
    scene 30007 with dissolve
    d "You know, a casual father-son bonding together."
    scene 30004 with dissolve
    e "Sure, I’ve got nothing else to do anyway."
    scene 30005 with dissolve
    d "Great, then do whatever you want for a while."
    scene 30001 with dissolve
    "{color=#ffa500}{i}*a voice from the corridor{i}"
    scene 30003 with dissolve
    "{color=#ffa500}{i}*a quiet knock on the door{i}"

    d "Uhm... [woman_name]?"

    d "The doors are closed..."
    scene 30002 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Of course they are closed... {p}I checked them at night.{/i}"
    scene 30008 with dissolve
    d "[player_name] do you know why the bedroom door is closed?{p}Is your [woman_role] closing herself off to you?"
    scene 30003 with dissolve
    e "It's closed? I don't know. You'll have to ask her."
    scene 30005 with dissolve
    d "Strange..."

    d "I'll take a quick bath, and we can go straight away. What do you say?"
    scene 30003 with dissolve
    e "Sure"

    scene black with fade
    show text "Local Restaurant" at title with dissolve
    $ renpy.pause(2, hard=True)
    scene 30011b with dissolve
    d "I missed coming to this place."

    d "I eat at roadside bars the whole time, and everything they serve tastes like crap."
    scene 30010 with dissolve
    e "Figured that out - Food suck that much you’re missing the crap they serve here."
    scene 30011a with dissolve
    d "Alright, let’s get to the point. Do you know why I brought you out here, away from [woman_role]?"
    e "Because we are… besties?"
    scene 30011b with dissolve
    d "Of course!"
    d "But actually it's for a different reason."
    scene 30011a with dissolve
    d "First of all,{p}because if I don't take you anywhere within a year{p}they will take away my parental rights."
    scene 30012 with dissolve
    e "That’s stupid."
    scene 30011b with dissolve
    d "Secondly, I eat alone all the time, so it's nice to share a meal with you."
    scene 30012b with dissolve
    e "Alright"
    scene 30011b with dissolve
    d "Thirdly, I have a coupon that gives me two dinners for the price of one."
    scene 30012b with dissolve
    e "D’awww…"
    scene 30011a with dissolve
    d "And fourthly, because [woman_name] is probably cheating on me."
    scene 30012b with dissolve
    e "Ok"
    scene 30012a with dissolve
    e "Wait what?!"
    scene 30011a with dissolve
    d "I'm very sorry for including you into ‘marriage matters’, but you're old enough now, and I needed to talk to you."
    scene 30010 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He’s ruining my entire plan if he already knows.{i}"
    e "Why do you think so?...{p}I’m with her every day and I haven't noticed anything like that… No that I know."
    scene 30011a with dissolve
    d "It would be weird if you knew that."
    d "But I have a feeling something is going on..."
    scene 30011 with dissolve
    pause
    scene 30011a with dissolve
    d "I would like to ask you for help."

    d "I may be wrong...{p}I hope I'm wrong."

    d "I'll do something soon...{p}and I'd like you to watch her for me from now on and let me know if anything happens..."
    scene 30010 with dissolve
    e "What’s on your head?"
    scene 30011b with dissolve
    d "My bank account will be ‘accidentally’ blocked.{p}I'll tell her that the tax office is looking for something."
    scene 30012 with dissolve
    e "And what is she supposed to do with that?"
    scene 30010 with dissolve
    d "She will seek for help. And you’ve got to find out who she goes to for help."
    e "Eh… Sure, sounds like a plan."
    scene 30012 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This lunatic watches too many detective movies.{i}"
    e "What if she's actually innocent? Is she just going to starve to death because you’re suspicious of something?"
    e "Have you seen how slim she is? I give her 2 days."
    scene 30011b with dissolve
    d "Of course you have to eat something, so tell [woman_name] that you have savings and you will do groceries."
    d "I'll leave you some money plus a rather big bonus for you helping me out... alright?"
    scene 30010 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} So my [woman_role] will have to rely on me?{p}Hell yeah, that sounds… great.{i}"
    scene 30011c with dissolve
    d "I can see you’re quite happy with the bonus."
    scene 30010 with dissolve
    e "Yeah, really happy... and of course I’ll help you out!"
    scene 30011a with dissolve
    d "Alright, but don’t get me twisted - I’m putting you against your [woman_role].{p}You are the only person I trust who can help me out in this."
    d "And I still hope that I am wrong in my doubts."
    scene 30010 with dissolve
    e "Sure thing, Dad. Buddies for life, right?"
    scene 30011d with dissolve
    d "Buddies for life."
    d "Oh, I think our food is on its way."

    scene black with fade
    "{size=+20}20 minutes later{/size} {p}[player_name] home."
    scene 30023 with dissolve
    d "Honey{p}we're back!"
    scene 30024 with dissolve
    m "Hey, give me a minute. I'm almost done."

    scene 30025 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hmm, I left my clothes in the room."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I hope no one notices."

    scene 30026 with dissolve
    $ renpy.pause(1, hard=True)
    scene 30026a with dissolve
    $ renpy.pause(1, hard=True)
    scene 30026 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I don't think anyone's here."
    scene 30027 with dissolve
    $ renpy.pause(1, hard=True)
    scene 30028 with dissolve
    $ renpy.pause(1, hard=True)
    scene 30029 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I remember leaving the remote for the curtains somewhere around..."

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ah, here it is.{i}"

    scene 30029ca with dissolve
    pause 1
    scene 30029cb with dissolve
    pause 1
    scene 30029cc with dissolve
    pause 1
    show hidden with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Huhuhu{i}"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Now take off this towel and show me your sexy body"
    scene hidden9 with dissolve
    pause 1
    scene hidden18 with dissolve
    pause 1
    scene hidden24 with dissolve
    pause 1
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Come back here!"
    scene 30030hidden8 with dissolve
    e "..."
    "{color=#ffa500}{i}*The sound of a drawer opening*{/i}{/color}"
    e "..."
    e "...."
    scene 30030hidden3 with dissolve
    pause 1
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Bingo!"
    scene 30030hidden4 with dissolve
    pause 1
    scene 30030hidden5 with dissolve
    pause 1
    scene 30030hidden6 with dissolve
    pause 1
    scene 30030hidden7 with dissolve
    pause 1
    scene 30030hidden8 with dissolve
    pause 1
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Not again..."
    "{color=#ffa500}{i}*The sounds of clothes being put on*{/i}{/color}"
    "{color=#A8E4A0}{i}{size=-3}[woman_name] left the room{/i}"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn she left. Time to go."

    stop music fadeout 1.0
    play music "music/Mn.wav"
    scene black with fade
    show text "Evening" with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    show 31000start at Move((-0.5, -0.7), (0.5, -0.7), 10.0, xanchor=0.3, yanchor=-0.1):
        zoom 1.2
    pause 10
    scene 31000start with dissolve:
        zoom 0.5
    "{color=#ffa500}{i}*(Television)*{/i}{/color} That is... Incorrect! Sorry! The dark horse Mark is definitely not white."
    "{color=#ffa500}{i}*(Television)*{/i}{/color} But you still got the $10 as a consolation prize!"
    c "*Audience cheers with excitement*"
    show jealous
    e "hrmpf"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I won't lie,{p}I'm fucking jealous.{i}"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She should be sitting with me now"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} It would be so fucking great if I could just walk up to her...{p}...and stick my dick in her mouth.{i}"
    scene 31020 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} And have dad just watching me as I'm facefucking his wife.{i}"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} -Good job son, show her who's boss.{i}"
    scene 31020 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I wonder what he's thinking about now..."
    scene 31020a with dissolve
    pause
    scene 31001di with dissolve
    pause
    scene 31001di2 with dissolve
    pause
    scene 31020a with dissolve
    pause 1
    scene 31020b with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He's already imagining something {i}"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He doesn't care at all that his father is sitting next to him{i}"
    scene 31020 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He doesn't know that I can record him too.{i}"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} If he tries something stupid and finds out that he is being recorded, he’ll probably piss himself.{i}"
    scene telewizja with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} We'll take a quick commercial break, and when we return, Jordan will be our next contestant!"
    d "This guy Jerry, the host, is totally hilarious. I love his show!"
    scene 31020c with dissolve
    d "I don't know why but people who go to the show are complete idiots."
    d "If I went, I'd probably win the grand prize."
    scene 31001c with dissolve
    e "..."
    scene 31020 with dissolve
    m "..."
    scene 31020c with dissolve
    d "How are you doing at the university Blaini?{p}Have you picked up any girl yet?"
    scene 31001b with dissolve
    e "Loads."
    scene 31020c with dissolve
    d "Haha, look at yourself. I remember when you were younger{p}you said you were going to marry your [woman_role]."
    scene 31020d with dissolve
    m "..."
    scene 31001a with dissolve
    e "Can I? That would be amazing."
    scene 31020d with dissolve
    d "Heh, you’d bet."
    d "What do you think, [woman_name]? Do you want to marry [player_name]?"
    scene 31020b with dissolve
    m "..."
    m "I don't think so"
    scene 31020d with dissolve
    d "Haha, See? She's mine!"
    d "I won't give her up to you that easily"
    m "..."
    scene 31001c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} We'll see...{i}"
    scene black with fade
    show text "Some time later" with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    scene 31022 with dissolve
    pause
    scene 31023 with dissolve
    d "{color=#ffa500}{i}*yawns*{/i}{/color}"
    scene 31024 with dissolve
    d "{color=#ffa500}{i}*whispers*{/i}{/color} Psst...{p}[player_name]"
    scene 31001b with dissolve
    e "Yeah?"
    scene 31001c with dissolve
    d "{color=#ffa500}{i}*whispers*{/i}{/color} I see that you are a tough guy{p}Because your [woman_role] and I fall asleep immediately{i}"

    scene 31025 with dissolve
    d "Uhm..."
    d "I’ll need to take some sleep pills, otherwise I won’t get myself to sleep. {p}I’ve got to get up early because I have a long journey tomorrow."
    scene 31001a with dissolve
    e "You know better, good night dad."
    scene 31025 with dissolve
    d "There's a blanket next to you, cover your [woman_role] so she doesn't get cold at night."
    scene 31001c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She won't...{i}"
    e ".."
    e "..."
    scene 31001a with dissolve
    e "...."
    e "....."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I'll wait a while until he falls asleep..."
    scene black with fade
    show text "One minute and 13 seconds later" with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    "{color=#ffa500}{i}*snoring sounds*{/i}{/color}"
    stop music fadeout 1.0
    play music "music/Mnicdk.mp3"

    scene 31001b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Time to have some fun...{i}"


    scene black with fade
    scene cameranico1 with dissolve
    pause
    show cameranico
    pause 4.6
    scene cameranico2
    e "Hey [woman_role]"
    scene 31026standingup with dissolve
    pause 1
    scene 31026standingup1 with dissolve
    pause 1
    scene 31026standingup2 with dissolve
    pause 1
    scene 31028hq with dissolve
    m "Where's John?"
    scene 31028hqa with dissolve
    e "He went to sleep."
    e "He asked me to take care of you..."
    scene 31028lipbitehq with dissolve
    e "So you don't get cold at night."
    scene 31028eyewhathq with dissolve
    m "Why are you acting like this?"
    scene 31028angryhq with dissolve
    m "You've already punished me enough. How do you imagine this going forward?"
    scene 31028listenhq with dissolve
    e "That we will live happily ever after."
    scene 31028sluchahq with dissolve
    m "..."
    scene 31028angryhq with dissolve
    m "Your dad is in the next room."
    scene 31028hqa with dissolve
    e "Are you telling me this so we don't get caught?"
    scene 31028hq with dissolve
    m "No…"
    scene 31028angryhq with dissolve
    m "I'm telling you not to get stupid ideas."
    scene 31028listenhq with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I hope everything is being recorded."
    scene 31028hq with dissolve
    m "You've done a lot of bad things, [player_name]. You forced me to... please you with...{p}...my mouth."
    scene 31028hq with dissolve
    m "It doesn't even bother you that your father is next to you."
    scene 31028listenhq with dissolve
    e "This is what true love looks like."
    e "If you were as devoted to Father as I am to you, this situation would not exist."
    scene 31028lipbitehq with dissolve
    pause
    scene 31028talk with dissolve
    m "It seems to me that no matter what I say, you still don't care."

    scene 31028hq with dissolve
    m "I don’t think we have the same concept for what caring about someone is. The point is - You don’t seem to understand how WRONG this is…"

    e "I don’t want to hear what’s wrong or what’s right… I just want to do what my heart tells me to…"
    scene 31028hq with dissolve
    m "Something tells me it’s not your heart the only one speaking…"
    m "Then what’s the point?"
    e "The point is… that I love you. I love you more than I’ve ever loved any woman in my life"
    scene 31028lipbitehq with dissolve
    m " … But… This is way far across the line."
    e "You just have to say that you love me more than you love my dad."
    scene 31028angryhq with dissolve
    m "I can’t love you anymore… Not in the line you want to cross…"
    scene 31028eyewhathq with dissolve
    e "There are no lines in our love… I don’t love you as a [woman_role]… I love you as MY woman. "
    m "..."
    scene 31032 with dissolve
    m "Hey stop!"
    scene 31032a with dissolve
    m "What are you doing?!"
    "{color=#A8E4A0}{i}{size=-3} You took off your underwear."
    scene 31032b with dissolve
    m "I won't do anything."
    m "Stop… doing that."
    scene 31032c with dissolve
    e "It's time for you to use your mouth for something better than talking!"
    scene 31032d with dissolve
    m "I will not do it."
    m "Not with my mouth."
    "{color=#A8E4A0}{i}{size=-3}She's totally confused."
    scene 31032e with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} You've already done this once, [woman_name], you'll survive."

    scene black with fade
    show text "{color=#A8E4A0}{i}{size=-3}She closed her eyes and wrapped her hand around your cock." with dissolve
    with Pause(3)
    hide text with dissolve
    with Pause(1)
    e "[woman_role]..."
    e "look at me while you're massaging my cock..."
    show hjep3
    e "Ahhhh"
    e "Your sweet face is enough to turn me on."
    e "But when I see your delicate hand holding my cock..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Just ignore it [woman_name]"

    e "You know what? I prefer your sweet lips over your hands."
    "{color=#A8E4A0}{i}{size=-3}You grabbed her hands. "
    scene 31040b with dissolve
    e "Open your mouth, honey."
    show facefu
    "{color=#A8E4A0}{i}{size=-3}She squeals and moans but no one will hear it because she has your dick in her mouth{/i}"
    e "Fuck yeah..."
    e "Being in your mouth… [woman_role]… is far better than getting a handjob…"
    e "Oh, fuck."
    e "From tomorrow and on, we’ll be all by ourselves.{p}Get ready for such sucking my fuckstick every day, [woman_role]."
    m "{color=#ffa500}{i}*She squeals loudly*{/i}{/color}"
    e "I need to cum…"
    e "You're too good for me."
    show sidecm
    "{color=#A8E4A0}{i}{size=-3}She squeals and tries to break free, but unfortunately it is too late.{/i}"
    scene 31096 with dissolve
    e "Marked as mine."
    m "..."
    m "{color=#ffa500}{i}*She breathe heavily*{/i}{/color}"
    scene 31097 with dissolve
    e "I love it."
    m "..."
    scene 31098 with dissolve
    m "My mouth...{p}hurts...."
    e "I'm not surprised, my dick is huge."
    scene 31101 with dissolve
    pause
    scene 31101a with dissolve
    pause
    scene 31101b with dissolve
    "{color=#A8E4A0}{i}{size=-3}She took your hand.{/i}"
    "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom.{i}"
    scene 31109 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What a great day."
    scene black with fade

    stop music fadeout 1.0
    play music "music/Mn.wav"

    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 4" at title with dissolve
    $ renpy.pause(2, hard=True)

    scene 40001 with dissolve
    pause
    scene 40001a with dissolve
    pause
    scene 40001b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She got up early"
    scene 40002 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I really hope she didn't run away from home after what happened yesterday..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} It was probably the best day of my life"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Just like in those computer games"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Only this time it's for real"
    scene 40003 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I need to check if my dad left any money"
    scene black with fade
    scene 40080 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Great"
    scene 40081 with dissolve
    e "500 bucks"
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
    scene 40085a with dissolve
    e "Hey what's up?"
    scene 40085b with dissolve
    d "Hello, can you talk?... or just answer casually so Nicole doesn't know it's me."
    scene 40085 with dissolve
    e "Mhm"
    scene 40085b with dissolve
    d "I completely forgot about the electricity bill, and I have already blocked it and now I have no way to pay"
    d "Give Nicole the money, when I come back, I'll pay you again"
    scene 40085 with dissolve
    e "Sure no problem"
    scene 40085b with dissolve
    d "Thanks a lot, man. I’m glad I left you some more!"
    d "Take care, bye!!"
    scene 40084b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Fuck, i need this money..."

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
    e "From the day you stopped caring about the rest of your family."
    scene 40010listen2 with dissolve
    e "Because you chose to suck another guy's dick instead of saving your relationship with my dad."
    e "So I figured out: You might as well suck mine."
    scene 40010listen2 with dissolve
    e "You could invite a friend into your bedroom, and thought I wouldn’t notice, or suspect about you cheating?{p}How old do you think I am? Or rather: Do you think I’m retarded?"
    e "These walls aren't thick at all, I heard every moan you made… And it turned me on every time."
    scene 40010listen with dissolve
    e "Every time you did… All I wanted to do is just… Come in and join, and fuck you up."
    scene 40010talk with dissolve
    m "It's terrible what you’re saying..."
    m "I didn't expect you to be capable of... something like this."
    e "I didn't expect many things from you either..."

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
    e "We guys love to dominate, you love to be dominated, admit you’re turned on by it. Don’t lie to yourself."
    scene 40010talk3 with dissolve
    m "Where are you getting all of this from, the internet?"
    m "You have no idea about women and how to treat them, you sexist pig."
    scene 40010listen2 with dissolve
    e "I think I'm doing quite well"
    e "Every time I touch you there, you get all wet"
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

    scene 40025 with dissolve
    e "{color=#ffa500}{i}*Breaths heavily*{/i}{/color}"

    show handep4 with dissolve
    e "Thanks, it was very pleasant"
    "{color=#A8E4A0}{i}{size=-3}She didn't answer"

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
    $ nicosister_role = renpy.input("Who is that woman to you? \n {i}(Enter for '[woman_name]'s sister' or write something else){/i}", )
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
    e "Mmmm... not yet..."
    a "Really?!"
    a "You're such a pretty boy and you haven't kissed yet"

    e "I prefer older... women"
    a "Oh yeah... at that age you all hunt for those... whatever they call them"
    e "Milfs"
    e "An experienced woman can teach me more"
    a "Uhm.... Uhm....{p}And what about university?"
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
    scene 40038 with dissolve
    pause
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

    scene computer4 with dissolve
    e "Come on, [nicosister_role] watches porn about..."
    e "Domination..."
    e "Nephews..."
    e "Blackmail"
    e "JESUS I AM THE PERFECT MATCH FOR MY [nicosister_role]! I KNEW IT!"
    e "Who would have thought"
    e "A lot of this..."
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
    e "I'd like to see you naked..."
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
    a "You want to pay me $100 to take my clothes off?"
    a "Don't even joke like that..."
    e "I'll give you $200 to take your clothes off."
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
    stop music fadeout 1.0
    play music "music/Audio004.mp3"
    e "??!!?!"
    scene 40105 with vpunch
    e "What the hell?!"
    e "Hmm, is this [woman_role]?"
    e "It's a private gallery, I guess someone doesn't know that the photos are indexed in Booble"
    e "Whose account is this?! Strange name {b}xxx_Z3p0lz3p0l_xxx{/b}"
    stop music fadeout 1.0
    play music "music/Audio005.mp3"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She'll definitely know more"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But... not today"
    show transitionep4
    $ renpy.pause(25, hard=True)
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
    e "You know that I will always help you"
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
    e "I think it’s because I would actually die for you."
    m "Yeah, no wonder"
    m "You can’t live on false promises, you know"
    e "You’re beautiful from head to toe, really. Even the smallest bit of your body was made to be treated like this."
    m "You’re just trying to cloy my ear"
    e "I’m not, I’m just saying what I feel, as I always do. And this is it. You’re beautiful from head to toe, really. Even the smallest bit of your body was made to be treated like this."
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
    e "You can go..."
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

    scene black with fade
    stop music fadeout 1.0
    play music "music/Forest.mp3"
    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 5" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Evening" at title2 with dissolve
    $ renpy.pause(2, hard=True)

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
    show cigep5 with dissolve
    $ renpy.pause(2, hard=True)

    e "Hey..."
    scene 5b005a with dissolve
    e "Want a smoke?"
    scene 5b005 with dissolve
    m "No..."
    scene 5b006 with dissolve
    e "Okay."

    scene 5b0020 with dissolve
    "{color=#ffa500}{i}*the sound of taking a drag from a cigarette*{/i}"
    scene 5b0021 with dissolve
    m "Could you go and smoke somewhere else?"
    scene 5b0021a with dissolve
    pause
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
    scene 5b0025 with dissolve
    e "How are you?"
    scene 5b0030 with dissolve
    m "What do you think?"
    e "Are you drinking again?"
    scene 5b0033 with dissolve
    e "What kind of wine is it?"
    scene 5b0033a with dissolve
    pause
    scene 5b0033b with dissolve
    m "Merlot..."
    scene 5b0024b with dissolve
    m "Eve always brings me red wine when she gets it as a gift because she doesn’t like it."
    scene 5b0024 with dissolve
    m "I have to go to sleep.{p}I have to get up early in the morning."
    scene 5b0031
    e "[woman_role]..."
    scene 5b0040 with dissolve
    e "Good night"
    scene 5b0032 with dissolve
    pause
    scene 5b0032b with dissolve
    m "Good night..."
    scene 5b0032 with dissolve
    pause
    scene 5b0031 with dissolve
    pause
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
    scene phone1a with dissolve
    pause
    play sound "music/sms.mp3"
    scene phone2a with dissolve
    pause
    scene phone2aa with dissolve
    pause
    scene bed3 with dissolve
    play sound "music/sms.mp3"
    "{size=-8}{color=#89CFF0}(reading...){/color}{/size} {i}Thank you!{p}See you tomorrow!"
    pause
    scene bed2 with dissolve
    pause
    scene bed0
    pause
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

    stop music fadeout 1.0
    play music "music/Mn2.mp3"
    show text "Next day" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Morning" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    show morningmov
    $ renpy.pause(4, hard=True)
    scene 5000000 with dissolve
    scene 5000001 with dissolve
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
    pause
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
    scene 50008c with dissolve
    pause
    scene 50011button with dissolve
    m "WHAT THE..."
    scene 50011button2 with vpunch
    m "Don't..."
    scene 50011a with dissolve
    m "I really have to go to work."
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
    e "I'll consider it if you become my obedient bitch."
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
    pause
    hide ep5nick14a
    show ep5nick14
    pause

    scene 50110z
    hide ep5nick14a
    hide ep5nick14
    scene 500109 with dissolve
    m "Uhm..."
    show ep5nick15 with dissolve
    pause
    hide ep5nick14
    show ep5nick14a
    pause
    scene 500110 with dissolve
    m "I really need to go..."
    scene 500110a with dissolve
    m "I can't be late for work..."
    scene 500110b with dissolve
    e "You'll go... only when I cum"
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
    hide nicfing1
    show nicfing2 with dissolve
    pause
    hide nicfing2
    show nicfing1 with dissolve
    pause
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
    pause
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
    scene black with fade
    show text "General store in the city" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "Afternoon" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    scene 52000 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I like this store. The owner probably has every possible thing someone would want to buy."
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
    e "Both"
    s "Ok!"
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
    scene black with fade
    scene 52104 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This is his apartment"
    scene 52105 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Electric door lock?!"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Let me think..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} 3 keys look very worn...{p}{b}0{/b}... {b}1{/b}... and {b}4{/b}..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} and 1 and 0 are much more worn than number 4..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Neither Tommy nor his mother seem smart, so it can't be anything difficult..."
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
    scene 50311 with dissolve
    e "You probably don't want him to see us together again, or he might think he’ll have a new daddy, hehe."
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
    scene 50325wg with dissolve
    e "Now get on the bed"
    scene 50325wga with dissolve
    pause
    scene 50325wgb with dissolve
    pause
    scene 50358bj_withglasses with dissolve
    e "You see... there's nothing to be afraid of."
    scene 50358bj_withglasses2 with dissolve
    e "Tommy's future is in your mouth hehe."
    scene 50358bj_withglasses3 with vpunch
    "{color=#A8E4A0}{i}{size=-3} If it weren't for you stuffing her mouth with your dick, she would probably scream."
    hide mtomep5cam2
    show mtomsolobjwithg with dissolve
    pause
    hide mtomsolobjwithg
    show mtomep5cam2 with dissolve
    pause
    scene 503530 with dissolve
    e "Hmm?"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Interesting..."
    scene 503532a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} She's mine, dude."
    "{color=#A8E4A0}{i}{size=-3}Tommy left the apartment, obviously angry that you didn't let him at least watch.{/i}"
    show mtomsolobjwithg with dissolve
    pause
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
    "{color=#A8E4A0}{i}{size=-3}You grabbed her hands and impaled her on your dick.{/i}"
    show mtomsolo with dissolve
    $ renpy.pause(3, hard=True)
    "{color=#A8E4A0}{i}{size=-3}Her wet pussy invites you deeper with each thrust.{/i}"
    pause
    "{color=#A8E4A0}{i}{size=-3}She doesn't even try to resist while you fuck her and treat her like a common whore.{/i}"
    pause
    "{color=#A8E4A0}{i}{size=-3}With each slap, she moans louder and louder.{/i}"
    pause
    "{color=#A8E4A0}{i}{size=-3}You've managed to completely dominate this bitch, but you feel like you won't last much longer.{/i}"
    e "I want to cum on your face."
    z "....{p}no...."
    hide mtomsolo
    scene mtomgetup with vpunch
    e "Come to me"
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
    show text "You left the apartment, leaving Tommy's mom exhausted on the bed." at title with dissolve
    $ renpy.pause(2, hard=True)
    scene 51000 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} That was good..."
    scene 51000a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What should I do now?"


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
    e "Speaking of which!... I almost forgot! I brought you this..."
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
    scene 50107 with dissolve
    a "Well, I should get dressed, as you can see, I’m wrapped in towels like a MILF burrito... You know what I mean?"
    scene 50106 with dissolve
    e "Heh... Just the kind of burrito I like..."
    scene 50107 with dissolve
    e "Tsk... You’re such a dummy... Anyway, let me get dressed, I won’t be long."
    scene 50106 with dissolve
    e "Nah, you don't have to.{p}I actually wanted to ask you something quick and then head out."
    scene 50106a with dissolve
    a "Oh, well..."
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
    "You started unzipping your pants' fly, as you position yourself in front of her ready to fuck her throat."
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
    scene 53108 with dissolve
    "{color=#A8E4A0}{i}{size=-3} You sigh and pull your pants back up, zipping them as you sit back down on the couch."
    e "Fine... I guess you’ve earned a break. Can't be milking the cow dry."
    scene 53109 with dissolve
    "{color=#A8E4A0}{i}{size=-3} She giggles softly, leaning back against the couch"
    a "Mhm... Oh, look at the time..."
    scene 53110 with dissolve
    a "It’s getting late... why don’t you stay the night? We can watch a movie or something... just relax."
    e "Okay..."
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
    e "Nah, I really should get going."
    scene 53240a with dissolve
    a "*Sighs*..."
    scene 53240e with dissolve
    a "Okay, I guess I can't stop you... You know the way out."
    scene 53240d with dissolve
    e "Was a real pleasure to use your mouth and tits."
    scene 53240b with dissolve
    a "You may have a good dick but you're weird. Ugh."
    scene black with fade
    show text "After walking for a while, you finally arrive home." at title with dissolve
    $ renpy.pause(2, hard=True)

    "{color=#A8E4A0}{i}{size=-3} After opening the front door, you finally stepped into your home, feeling the peace that your -broken- home offered."
    e "Hello... I’m back..."
    "{color=#A8E4A0}{i}{size=-3} To your surprise, [woman_role] wasn’t in the living room, though this didn’t worry you — she could easily be in her room."
    "{color=#A8E4A0}{i}{size=-3} Just as you set foot on the stairs, you heard the sound of the shower running like a waterfall."

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
    e "Oh, come on. I’m not asking for much. You’re already here... you look great. What’s the harm?"
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
    e "Look, I can't be more straight with you. I just can't get enough of you."
    scene nicaftshow0 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Her blush deepens, and she looks away, clearly uncomfortable but not angry."
    scene nicaftshow4 with dissolve
    m "...Thanks, I guess."
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
    scene nicaftshow9a with dissolve
    e "Oh, I've got something for you."
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
    scene 55200red with dissolve
    "{color=#A8E4A0}{i}{size=-3} You hand her the red wine bottle."
    scene 55200redgood with dissolve
    e "I brought something to make tonight even better... Merlot. I know you love this thing."
    "{color=#A8E4A0}{i}{size=-3} Your [woman_role] seems less enthusiastic, though the gift is appreciated."
    scene 55200redgood2 with dissolve
    m "Oh... Merlot... It’s good."
    scene 55200redgood with dissolve
    e "It sure makes any bad movie more bearable."
    stop music fadeout 1.0
    play music "Music/Mnicdat.mp3"
    scene 55300 with dissolve
    e "I'll wait for you in the living room."
    scene black with Fade(2.0, 1.0, 2.0)
    "{color=#A8E4A0}{i}{size=-3} Without having a long wait, you still got eager to see her there, growing weary of waiting, until footsteps approached from the hall."
label nicfinalnoob:
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
            scene 56000sxdrinkpass with dissolve
            e "That's why I've poured a glass of Merlot for you"
            "{color=#A8E4A0}{i}{size=-3} She hesitates, her eyes flicking from the glass to you, and then back again."
            scene 56000sxdrink0 with dissolve
            "{color=#A8E4A0}{i}{size=-3} After a moment, she reaches out and takes it from you."
            scene 56000sxdrink1 with dissolve
            "{color=#A8E4A0}{i}{size=-3} She brings it to her lips, taking a slow sip."
            scene 56000sxdrink0 with dissolve
            m "At least it’s Merlot... Cheers."
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
            scene 56000sxdrink0 with dissolve
            "{color=#A8E4A0}{i}{size=-3} After what it seemed at eternity later, the movie finally winds down, as the credits roll across the screen."
            scene 56000sxdrink1 with dissolve
            m "I guess that's it... *Hip*"
            e "Shit, you're drunk. Are you sure you can walk upstairs on your own?"
            m "I'm not a granny. I'll go to sleep... You do whatever you want... *Hip*"
            e "Oh, mind your words."
            "{color=#A8E4A0}{i}{size=-3} Tipsy, she stands up, picks up the bottle of Merlot, and left you on your own at the living room."


            "{color=#A8E4A0}{i}{size=-3} After a while of watching TV, you didn't hear any more activity from [woman_name]'s room."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Sounds like she fell asleep."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Alcohol can do miracles on women, that's facts."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Perhaps I should go and check up on her... Hehe."
            scene 0001 with dissolve

label opendoorfinalnoob:
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
    hide nicep5last3cam2
    show nicep5last3
    pause
    hide nicep5last3
    show nicep5last3cam2
    pause
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
    show logo
    $ renpy.pause(2, hard=True)
    "{size=+15}Created by Zeratgames"
    scene black with fade
    ".."
    return
























