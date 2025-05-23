﻿default persistent.player_name = "Tu"
default player_name = persistent.player_name
default persistent.player_role = "El hijo del marido"
default player_role = persistent.player_role
default persistent.woman_role = "Madrastra"
default woman_role = persistent.woman_role
default persistent.woman_name = "Nicole"
default woman_name = persistent.woman_name
default persistent.nicosister_role = "[woman_name]'s hermana"
default nicosister_role = persistent.nicosister_role
default persistent.tommywoman_role = "La madrastra de Tommy"
default tommywoman_role = persistent.tommywoman_role


default easymode = False

define e = Character("[player_name]", color="#FFA500")
define m = Character("[woman_role]", color="#FF0000")
define t = Character("Tommy", color="#FFFC33")
define y = Character("???", color="C733FF")
define z = Character("[tommywoman_role]", color="330066")
define p = Character("Gary", color="0CC3F8")
define c = Character("Crowd", color="065535")
define d = Character("Dad", color="27a344")
define a = Character("[nicosister_role]", color="fd60bc")
define r = Character("Marco", color="#808080")
define s = Character("Kevin", color="#8fa832")
define h = Character("Sheila", color="#fc6603")
define b = Character("Bouncer", color="#808080")
define f = Character("Bartender", color="#ffa500")
define r = Character("Old man", color="#0000FF")
define u = Character("Rent-a-car", color="#FF00FF")
define x = Character("Charming female voice", color="#FF0000")
define o = Character("Prostitute", color="#FFC0CB")
define oi = Character("???", color="#FFC0CB")
define i = Character("Space Warrior", color="#ffa500")
define j = Character("Super Space Warrior", color="#ff4d00")
define td = Character("Tommy's father", color="#8f714f")
define att = Character("Clerk", color="#8fa832")
define l = Character("Lopez", color="#FFA500")
define ym = Character("Young [woman_name]", color="#FF0000")
define jo = Character("Young John", color="#27a344")






define flash = Fade(.25, 0.0, .75, color="#fff")

define gui.dialogue_text_outlines = [ (1, "#00000080", 1, 2) ]
define gui.charaters_text_outlines = [ (1, "#00000080", 1, 2) ]
define gui.interface_text_outlines = [ (1, "#00000080", 1, 2) ]

style window:
    background None

image bedroom = Movie(fps=60, size=None, play="images/Intro/Mov000A.webm", loop= True)
image bedroomopen = Movie(channel="movie_dp", play="images/Intro/Mov0000.webm", loop= False)
image mc1 = "images/Intro/MC1.jpg"
image mc2 = "images/Intro/MC2.jpg"
image mc3 = "images/Intro/MC3.jpg"
image mc4 = "images/Intro/MC4.jpg"
image s2bj = Movie(channel="movie_dp", play = "images/Ep2/s2bj00_1.webm")
image s2h1 = Movie(channel="movie_dp", play = "images/Ep2/s2h1.webm")
image s2h2 = Movie(channel="movie_dp", play = "images/Ep2/H1v2.webm")
image bj70 = Movie(channel="movie_dp", play = "images/Ep2/0070bj.webm")
image bj68v1 = Movie(channel="movie_dp", play = "images/Ep2/0068Bjv1.webm")
image bj68v2 = Movie(channel="movie_dp", play = "images/Ep2/0068Bjv2.webm")
image bj68v3 = Movie(channel="movie_dp", play = "images/Ep2/0068Bjv3.webm")
image bj69v1 = Movie(channel="movie_dp", play = "images/Ep2/0069Bjv1.webm")
image bj69v2 = Movie(channel="movie_dp", play = "images/Ep2/0069Bjv2.webm")
image bj69v3 = Movie(channel="movie_dp", play = "images/Ep2/0069Bjv3.webm")
image bj69v4 = Movie(channel="movie_dp", play = "images/Ep2/0069Bj.webm")
image bj69v5 = Movie(channel="movie_dp", play = "images/Ep2/0069Bja.webm")
image hjfingerv1 = Movie(channel="movie_dp", play = "images/Ep2/HjFingerv1.webm")
image hjfingerv2 = Movie(channel="movie_dp", play = "images/Ep2/HjFingerv2.webm")
image tit001 = Movie(channel="movie_dp", play = "images/Ep1/tit001.webm")
image tit002 = Movie(channel="movie_dp", play = "images/Ep1/tit002.webm")
image drzwi = Movie(channel="movie_dp", play = "images/Ep1/drzwi.webm")
image hhjj0 = Movie(channel="movie_dp", play = "images/Ep1/hhjj0.webm")
image hhjj1 = Movie(channel="movie_dp", play = "images/Ep1/hhjj1.webm")
image finishmomtommy = Movie(channel="movie_dp", play = "images/Ep1/finishmomtommy.webm", loop=False, image="10052")
image chokeep1 = Movie(channel="movie_dp", play = "images/Ep1/choke.webm")
image carleft = Movie(channel="movie_dp", play = "images/Ep1/carleft.webm")
image fing = Movie(channel="movie_dp", play = "images/Ep1/fing.webm")
image fing2 = Movie(channel="movie_dp", play = "images/Ep1/fing2.webm")
image hjstart = Movie(channel="movie_dp", play = "images/Ep1/hjstart.webm")
image bjretro = Movie(channel="movie_dp", play = "images/Ep3/bj0301.webm")
image shower = Movie(channel="movie_dp", play = "images/Ep3/shower.webm")
image bedanim = Movie(channel="movie_dp", play = "images/Ep3/bedanim.webm")
image jealous = Movie(channel="movie_dp", play = "images/Ep3/jealous.webm")
image facefu = Movie(channel="movie_dp", play = "images/Ep3/facefu.webm")
image cameradown = Movie(channel="movie_dp", play = "images/Ep3/cameradown.webm", loop = 0)
image facemedium = Movie(channel="movie_dp", play = "images/Ep3/facemedium.webm")
image facetotal = Movie(channel="movie_dp", play = "images/Ep3/facetotal.webm")
image hjep3 = Movie(channel="movie_dp", play = "images/Ep3/hjep3.webm")
image caress = Movie(channel="movie_dp", play = "images/Ep3/caress.webm")
image tvmovie = Movie(channel="movie_dp", play = "images/Ep3/tv1.webm")
image alpacinotv = Movie(channel="movie_dp", play = "images/Ep3/alpacinotv.webm")
image nicolefinggood = Movie(channel="movie_dp", play = "images/Ep3/fingep3nic.webm")
image lasthjep3 = Movie(channel="movie_dp", play = "images/Ep3/lastjhep3.webm")
image logo = Movie(channel="movie_dp", play = "images/Intro/logo.webm", loop=False)
image tomrun = Movie(channel="movie_dp", play = "images/Ep1/tomrun.webm", loop=False, image="10023b")
image grabmtom = Movie(channel="movie_dp", play = "images/Ep1/grabmtom.webm", loop=False, image="grabblast")
image ep1kick = Movie(channel="movie_dp", play = "images/Ep1/ep1kick.webm", loop=False, image="10026a")
image chokefindres = Movie(channel="movie_dp", play = "images/Ep1/chokefindres.webm", loop=False, image="chokefin165")
image grabnictitsep1 = Movie(channel="movie_dp", play = "images/Ep1/grabnictitsep1.webm", loop=False, image="grabtts38")
image ep1shame = Movie(channel="movie_dp", play = "images/Ep1/ep1shame.webm", loop=False, image="shame40")
image ep1grabfinal = Movie(channel="movie_dp", play = "images/Ep1/ep1grabfinal.webm", loop=False, image="10505")
image dckep1grab = Movie(channel="movie_dp", play = "images/Ep1/dckep1grab.webm", loop=False, image="dckgrab118")
image headbutt = Movie(channel="movie_dp", play = "images/Ep1/headbutt.webm", loop=False, image="headbutt2")
image dckep1msg = Movie(channel="movie_dp", play = "images/Ep1/dckep1msg.webm")
image cameranico = Movie(channel="movie_dp", play = "images/Ep3/cameranico.webm")
image sidecm = Movie(channel="movie_dp", play = "images/Ep3/sidecm.webm")
image hidden = Movie(channel="movie_dp", play = "images/Ep3/hidden.webm")
image tvmovienontr = Movie(channel="movie_dp", play = "images/Ep3/tvmovienontr.webm")
image s2touchfirst = Movie(channel="movie_dp", play = "images/Ep2/s2touchfirst.webm")
image finalep1 = Movie(channel="movie_dp", play = "images/Ep1/finalep1.webm")
image beforehb = Movie(channel="movie_dp", play = "images/Ep1/beforehb.webm")
image sheillbj = Movie(channel="movie_dp", play = "images/Ep2/sheillbj.webm")
image sheillback = Movie(channel="movie_dp", play = "images/Ep2/sheillback.webm")


image Achiev1 = "images/Ep2/Achiev1.png"
image Achiev2 = "images/Ep2/Achiev2.png"
image Achiev3 = "images/Ep2/Achiev3.png"
image Achiev4 = "images/Ep2/Achiev4.png"
image Achiev5 = "images/Ep2/Achiev5.png"
image Achiev6 = "images/Ep2/Achiev6.png"
image Achiev7 = "images/Ep3/Achiev7.png"
image Achiev8 = "images/Ep3/Achiev8.png"
image Achiev9 = "images/Ep3/Achiev9.png"
image Achiev10 = "images/Ep3/Achiev10.png"
image Achiev11 = "images/Ep4/Achiev11.png"
image Achiev12 = "images/Ep4/Achiev12.png"
image Achiev13 = "images/Ep4/Achiev13.png"
image Achiev14 = "images/Ep4/Achiev14.png"
image Achiev15 = "images/Ep4/Achiev15.png"
image Achiev16 = "images/Ep5/Achiev16.png"
image Achiev17 = "images/Ep5/Achiev17.png"
image Achiev18 = "images/Ep5/Achiev18.png"
image Achiev19 = "images/Ep5/Achiev19.png"
image Achiev20 = "images/Ep5/Achiev20.png"
image Achiev21 = "images/Ep2/Achiev21.png"
image Achiev22 = "images/Ep5/Achiev22.png"
image Achiev23 = "images/Ep5/Achiev23.png"
image Achiev24 = "images/Ep5/Achiev24.png"
image Achiev28 = "images/Ep6/Achiev28.png"
image Achiev25 = "images/Ep6/Achiev25.png"
image Achiev26 = "images/Ep6/Achiev26.png"
image Achiev27 = "images/Ep6/Achiev27.png"
image Achiev29 = "images/Ep7/Achiev29.png"
image Achiev30 = "images/Ep7/Achiev30.png"
image Achiev31 = "images/Ep7/Achiev31.png"
image Achiev32 = "images/Ep7/Achiev32.png"
image s3cr3ta1 = "images/Ep5/mmmmtooo.png"
image gstwach = "images/Ep5/gstw.png"

image Achiev1_lock = "images/Ep2/Achiev1_lock.png"
image Achiev2_lock = "images/Ep2/Achiev2_lock.png"
image Achiev3_lock = "images/Ep2/Achiev3_lock.png"
image Achiev4_lock = "images/Ep2/Achiev4_lock.png"
image Achiev5_lock = "images/Ep2/Achiev5_lock.png"
image Achiev6_lock = "images/Ep2/Achiev6_lock.png"
image Achiev7_lock = "images/Ep3/Achiev7_lock.png"
image Achiev8_lock = "images/Ep3/Achiev8_lock.png"
image Achiev9_lock = "images/Ep3/Achiev9_lock.png"
image Achiev10_lock = "images/Ep3/Achiev10_lock.png"
image Achiev11_lock = "images/Ep4/Achiev11_lock.png"
image Achiev12_lock = "images/Ep4/Achiev12_lock.png"
image Achiev13_lock = "images/Ep4/Achiev13_lock.png"
image Achiev14_lock = "images/Ep4/Achiev14_lock.png"
image Achiev15_lock = "images/Ep4/Achiev15_lock.png"
image Achiev16_lock = "images/Ep5/Achiev16_lock.png"
image Achiev17_lock = "images/Ep5/Achiev17_lock.png"
image Achiev18_lock = "images/Ep5/Achiev18_lock.png"
image Achiev19_lock = "images/Ep5/Achiev19_lock.png"
image Achiev20_lock = "images/Ep5/Achiev20_lock.png"
image Achiev21_lock = "images/Ep2/Achiev21_lock.png"
image Achiev22_lock = "images/Ep5/Achiev22_lock.png"
image Achiev23_lock = "images/Ep5/Achiev23_lock.png"
image Achiev24_lock = "images/Ep5/Achiev24_lock.png"
image Achiev28_lock = "images/Ep6/Achiev28_lock.png"
image Achiev25_lock = "images/Ep6/Achiev25_lock.png"
image Achiev26_lock = "images/Ep6/Achiev26_lock.png"
image Achiev27_lock = "images/Ep6/Achiev27_lock.png"
image Achiev29_lock = "images/Ep7/Achiev29_lock.png"
image Achiev30_lock = "images/Ep7/Achiev30_lock.png"
image Achiev31_lock = "images/Ep7/Achiev31_lock.png"
image Achiev32_lock = "images/Ep7/Achiev32_lock.png"


image 20000aTo20000eAnimated:
    "images/Ep2/20000a.png"
    pause 0.5
    "images/Ep2/20000b.png"
    pause 0.5
    "images/Ep2/20000c.png"
    pause 0.5
    "images/Ep2/20000d.png"
    pause 0.5
    "images/Ep2/20000c.png"
    pause 0.5
    "images/Ep2/20000b.png"

transform rotate_animation:
    linear 2.0 rotate 360

init:
    $ achievment = Position(xpos=0.9, xanchor=0.9, ypos=0.05, yanchor=0.05)
    $ statleft = Position(xpos=0.9, xanchor=0.9, ypos=0.01, yanchor=0.05)
    $ statright = Position(xpos=0.9, xanchor=0.9, ypos=0.01, yanchor=0.05)
    $ title = Position(xpos=0.5, xanchor=0.5, ypos=0.55, yanchor=0.1)
    $ title2 = Position(xpos=0.5, xanchor=0.5, ypos=0.58, yanchor=0.1)
    $ moneystat = Position(xpos=0.05, xanchor=0, ypos=0.05, yanchor=0)
    $ mccumep7stat = Position(xpos=0.05, xanchor=0, ypos=0.05, yanchor=0)
    $ niccumep7stat = Position(xpos=0.05, xanchor=0, ypos=0.1, yanchor=0)
    $ narratortalk = Position(xpos=0.5, xanchor=0.5, ypos=0.8, yanchor=0.1)
    $ credits = Position(xpos=0.3, xanchor=0.5, ypos=0.4, yanchor=0.1)
    $ credits2 = Position(xpos=0.3, xanchor=0.5, ypos=0.3, yanchor=0.1)
    $ creditslv = Position(xpos=0.2, xanchor=0.5, ypos=0.45, yanchor=0.1)
    $ creditsright = Position(xpos=0.85, xanchor=0.5, ypos=0.45, yanchor=0.1)
    $ creditsuniv = Position(xpos=0.85, xanchor=0.5, ypos=0.45, yanchor=0.1)
    $ creditsdom = Position(xpos=0.8, xanchor=0.5, ypos=0.4, yanchor=0.1)




default lust = 4
default domination = 4
default everydayhjq = 0
default hjquestion = 0
default forcebj = 0
default achValid = 0
default achValid2 = 0
default achValid3 = 0
default hjoptions = 0
default beforeforce = 0
default secondAchievDone = 0
default tommyfriend = 0
default tommymomsubmission = 0
default dadfriend = 0
default itguy = 0
default nicoledominance = 4
default canyoublowmestat = 0
default tryfingeringep3stat = 0
default achVall = 0
default hiddendoor = 0
default massagesecondtest = 0
default massagefail = 0
default mcknowsrecord = 0
default massagebeforeafraid = 0
default getonherlapfail2 = 0
default getonherlapfail = 0
default optionpointsep3 = 0
default afraidcheck = 0
default pushherbedcheck = 0
default timeout = 8
default timeout_label = None
default playerHP = 3
default tommyHP = 5
default endingep2full = False
default endingep3full = False
default money = 0
default telltommy = False
default nicep1dom = 4
default chokeep1kick = False
default episode1checkfinal = False
default ep1bodyfan = False
default thinkep1 = 0
default ep1rude = 0
default mtommoney = 0
default tommypaylater = False
default tommytalkep1 = False
default tommybeingkicked = False
default mctellnamemtommy = False
default mcnotalkwithmtommy = False
default tommymomcarhj = False
default tommymomep1choke = False
default tommysawmomincar = False
default niclovebonusfactor = 0
default sheilacheated = False
default sheilahappy = False
default sheilahappysx = False
default sheiladominated = False
default tommymrolegive = False
default tommywomanshort_role = "Stepmom"

init:
    $ achievement.register("Achiev01")
    $ achievement.register("Achiev02")
    $ achievement.register("Achiev03")
    $ achievement.register("Achiev04")
    $ achievement.register("Achiev05")
    $ achievement.register("Achiev06")
    $ achievement.register("Achiev07")
    $ achievement.register("Achiev08")
    $ achievement.register("Achiev09")
    $ achievement.register("Achiev10")
    $ achievement.register("Achiev11")
    $ achievement.register("Achiev12")
    $ achievement.register("Achiev13")
    $ achievement.register("Achiev14")
    $ achievement.register("Achiev15")
    $ achievement.register("Achiev16")
    $ achievement.register("Achiev17")
    $ achievement.register("Achiev18")
    $ achievement.register("Achiev19")
    $ achievement.register("Achiev20")
    $ achievement.register("Achiev21")
    $ achievement.register("Achiev22")
    $ achievement.register("Achiev23")
    $ achievement.register("Achiev24")
    $ achievement.register("Achiev25")
    $ achievement.register("Achiev26")
    $ achievement.register("Achiev27")
    $ achievement.register("Achiev28")
    $ achievement.register("Achiev29")
    $ achievement.register("Achiev30")
    $ achievement.register("Achiev31")
    $ achievement.register("Achiev32")


label splashscreen:

    scene black with Pause(1)

    show text "ZERATGAMES PRESENTS" with dissolve
    $ renpy.pause(3, hard=True)

    hide text with dissolve

    show logo
    $ renpy.pause(5, hard=True)
    hide logo with dissolve
    $ renpy.pause(1, hard=True)

    show text "Este juego está destinado únicamente a usuarios mayores de 18 años. Al acceder o jugar a este juego, confirmas que tienes al menos 18 años." with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    return


label start:
    scene black
    show mc1 with fade
    "¡Hola!"
    show mc2 with dissolve
    "{color=#FFD1DF}{i}*opción*{/i}{/color}  <- Este color indica acciones en lugar de discurso."
    "{color=#ffa500}{i}*sonido*{/i}{/color}  <- Este color representa el sonido"
    show mc3 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Este es el narrador.{/size}{/i}{/color}"
    "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Este formato representa los pensamientos de un personaje."
    "Mientras juegas, a veces puedes obtener una ventaja que te ayudará en algunas conversaciones."
    "Obtendrás la primera como un regalo de mi parte.{p}Usar esta ventaja te dará un consejo para resolver ciertas conversaciones."
    "¡A través de esto, podrás ver y leer mis pensamientos!"
    "{color=#ffa500}*********************{/color}\nObtendrás la primera como un regalo de mi parte. \n{color=#ffa500}*********************{/color}"
    show mc4 with dissolve
    show screen hint("Este tipo es un poco extraño, pero no creo que pueda encontrar a nadie más para contar esta historia.")
    "Y se ve así."
    hide screen hint
    hide mc4 with dissolve
    show mc3 with dissolve
    "Puede decidir si desea jugar normalmente o comenzar el modo fácil."
    "En modo fácil, tendrá puntos de estadísticas adicionales desde el principio.Esto le permitirá superar la mayoría de las conversaciones, pero no podrá obtener logros."
    show mc3 with dissolve
    "Tienes que decidir ahora.¡No puedes cambiar esta opción sin comenzar un nuevo juego!"
    show screen hint("Siempre elijo el modo fácil cuando quiero una FAP rápida ... pero la versión normal tiene logros y 1 escena de bonificación ... la opción difícil ...")

    menu:
        "Modo fácil (recomendado)\n{color=#3d85c6} Puntos de bonificación + Sugerencias{/color}{size=-8}\n+2 puntos al comienzo de cada episodio \ n puedes omitir minijuegos al instante":
            $ easymode = True
            jump ep1start

        "Modo duro\n{color=#8fce00} Logros + escena de bonificación{/color}{size=-8}\n Puedes omitir minijuegos después de 3 falla":
            menu:
                    "¿Estás Seguro?"
                    "¡Sí!":
                        jump ep1start
                    "Hmm.. Tal vez intente el Modo Fácil...":
                        $ easymode = True
                        jump ep1start

            jump ep1start

label ep1start:
    hide screen hint
    scene black with fade
    if easymode:
        show text "Puntos de modo fáciles!"
        show image "images/Stats/Dom[nicep1dom].png" at statleft
        pause 1
        $ tommymomsubmission += 2
        $ nicep1dom += 2
        show image "images/Stats/Dom[nicep1dom].png" at statleft
        pause 1
        hide text

    $ player_name = renpy.input("¿Cual es mi nombre? \n {i}(Escribe ahora)", )
    $ player_name = player_name.strip()
    $ persistent.player_name = player_name
    $ player_role = renpy.input("¿Quién soy yo para la esposa de mi padre? \n {i}(Ingrese 'Hijo del esposo' o puede escribir 'Hijo' o algo más.){/i}", )
    $ player_role = player_role.strip() or "Husband's son"
    $ persistent.player_role = player_role
    $ woman_role = renpy.input("¿Qué papel juega la mujer en esta historia para ti? \n {i}(Ingrese para 'madrastra' o puede escribir 'mamá' o algo más){/i}", )
    $ woman_role = woman_role.strip() or "Stepmom"
    $ persistent.woman_role = woman_role
    $ woman_name = renpy.input("¿Y cómo se llama? \n {i}(Ingrese para 'Nicole' o escriba algo más){/i}", )
    $ woman_name = woman_name.strip() or "Nicole"
    $ persistent.woman_name = woman_name
    $ persistent.pName = player_name
    $ persistent.pRole = player_role
    $ persistent.wRole = woman_role
    $ persistent.wName = woman_name
    show mc1 with fade
    e "Entonces [woman_name] es mi [woman_role], y yo soy su [player_role]. ¡Genial!"
    hide screen hint
    scene 0001 with Fade(2.0, 1.0, 1.0)
    show screen hint("Solo para su información.No soy tan corto, ¡solo estoy escabullido!")
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Estoy viviendo con mi [woman_role] y papá, y esta noche me arrastré hasta la puerta de su habitación."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Veamoslo y verás por qué estamos aquí ..."
    hide screen hint
    show screen hint("Espero que sea un adulto ...")
    menu:
        "Solo debes abrir esta puerta si eres mayor de 18 años."
        "Sí, soy adulto y tengo más de 18 años.":
            hide screen hint
            "La siguiente escena contiene NTR, pero es importante para la historia."
            show bedroomopen
            pause 3
            show bedroom
            "{color=#ffa500}{i}*a slight creak*{/i}"
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oops, I hope nobody heard that"
        "Desafortunadamente no soy tan viejo. ¡Es hora de jugar Phortnight!":
            return
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Conocer a mi [woman_role], [woman_name]"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ella tiene 37 años, es profesora de historia en la universidad y es una mujer indudablemente hermosa."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Pero ahora mismo, parece un poco... ocupada."
    pause
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Verá, una mujer casada, tarde en la noche, complaciendo a un hombre con la boca ... no es exactamente una cosa inusual en la mayoría de los hogares."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Excepto por una pequeña cosa ... {p} ese hombre no es mi papá, ¡y estoy seguro de que sabe que no estará en casa hasta mañana!"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} ... y no tengo idea de quién es ese hijo de puta ..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} No soy estúpido, así que es hora de reunir un poco de evidencia.Sonríe por la cámara."
    play sound "music/camera.mp3"
    scene 0005
    with flash
    "{color=#ffa500}{i}*sonido de la cámara*{/i}"
    scene black with fade
    m "¿¡QUÉ DEMONIOS!?"
    m "[player_name] ¡Vuelve aquí!"
    show logo
    $ renpy.pause(3, hard=True)
    show text "Creado por ZeratGames" at title with dissolve
    $ renpy.pause(3, hard=True)
    show text "Episodio 1" at title2 with dissolve
    $ renpy.pause(2, hard=True)

    with Pause(1)


label episode1:
    scene black with fade
#      EPISODE 1
    scene 10001 with dissolve
    pause 2
    play sound "music/bip.mp3"
    "{color=#ffa500}{i}*alarm clock sound*{/color}"
    "..."
    play sound "music/bip.mp3"
    "{color=#ffa500}{i}*beep beep*"
    "..."
    play sound "music/bip.mp3"
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
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Qué noche..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} [player_name]..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Qué le había pasado?"
    scene 10008 with dissolve
    pause 1
    scene 10009 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Todavía es muy joven."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Esta es probablemente la edad en que comienza a tener picazón sobre la vida sexual ..."
    scene 10010 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But... ¿Por qué tomó una foto?"
    scene 10010a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Espero que no ... se mueva a ..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} NO. {p}Ciertamente no. {p}No [player_name]"
    scene 10011 with dissolve
    scene 10012 with dissolve
    scene 10013 with dissolve
    scene 10013a with dissolve
    scene 10013b with dissolve
    scene 10014 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Necesito hablar con él sobre esto HOY."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Normalmente enviaría a John ... pero esta vez no puedo ...."
    scene 10014b with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Tal vez estoy exagerando sin razón."
    scene 10014c with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Debería levantarse ahora para que no llegue tarde a la clase ..."
    scene 10015 with dissolve
    e "{color=#ffa500}{i}*Snoring*"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}Será mejor que no lo despierte."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Lo veré en la universidad de todos modos."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Aunque ni siquiera puedo pensar en la conversación que tendremos ...{p}Todavía...{p}No creo que pueda escapar de eso"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Él tiene que borrar esas fotos que tomó ayer."
    "{color=#A8E4A0}{i}{size=-3} [woman_name] dejó la habitación"
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
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Tengo que levantarme."
    scene 10016 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Hm, tengo la sensación de que este será un día interesante."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Qué debo hacer con las fotos ahora?{p}Ellas me dan un poder loco sobre mi [woman_role]"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Esta es una oportunidad para obtener lo que quiero.Con estas fotos, puedo hacerla hacer cualquier cosa, por favor"
    scene 10016a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Necesito dinero?"
    scene 10016b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Por supuesto que sí ..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Pero hay algo ...{p}Quiero más que dinero ..."
    e "..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ...¿Es posible?"
    scene 10016c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Al menos ya no tendré que escucharla gemir en la noche"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Aunque los de ella eran bastante agradables de escuchar, a veces ..."
    scene black with fade
    show text "One hour later" at title with dissolve
    $ renpy.pause(1, hard=True)
    show text "Mercino University" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10022a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Malditos clases.¿Por qué fui a la universidad? {p} podría ir a trabajar."
    scene 10022b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ya no siento que estoy aprendiendo nada, y las chicas están tan jodidas que no puedo manejar ninguno de ellos."
    scene 10022c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Creo que es hora de un cigarrillo ..."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ...O no."
    show tomrun with dissolve
    $ renpy.pause(5, hard=True)
    scene 10023b with dissolve
    t "Ah, ow, ouch"
    scene 10024 with dissolve
    e "Tommy!"
    e "Dame mi dinero para la hierba que tienes el viernes"
    scene 10024a with dissolve
    e "¿Quién crees que soy, eh?{p}Jodido Santa Claus?"
    scene 10024b with dissolve
    t "Suspiro..."
    scene 10024c with dissolve
    t "No lo tengo, amigo ... ya lo he gastado todo."
    scene 10024a with dissolve
    e "Bueno, no me dejas otra opción"
    scene 10024c with dissolve
    t "No ... espera"
    scene 10025 with dissolve
    t "Permítame verificar..."
    scene 10025a with dissolve
    t "Esto es todo lo que tengo."
    t "Lo devolveré la próxima semana"

    if tommymrolegive == False:
        $ tommywomanshort_role = renpy.input("Tommy vive con su ... \n {i}(Entrar para 'Stepmom o escribir 'Mom' o algo más - a 3-letter La palabra es la mejor opción.){/i}", )
        $ tommywoman_role = "Tommy's " + (tommywomanshort_role.strip() if tommywomanshort_role.strip() else "Stepmom")
        $ tommywomanshort_role = tommywomanshort_role.strip() if tommywomanshort_role.strip() else "Stepmom"
        $ tommymrolegive = True
        $ persistent.tommywoman_role = tommywoman_role
        $ persistent.tRole = tommywoman_role
    show screen hint("Está asustado como el infierno.¿Pero vale la pena tenerlo como enemigo?")
    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Tomar el dinero*{/i}{/color} {color=#00ff00}{i}+100${/i}":
                hide screen hint
                scene 10026sad with dissolve
                $ money += 100
                show text "{color=#00ff00}{size=+15}+1 0 0 ${/color}" with dissolve
                with Pause(2)
                "{i}Total: [money]$"
                hide text with dissolve
                jump wezpieniadze

            "¡Deja de mentir!¡Tu mamá es rica!¡Devuelve mi dinero, hijo de puta! {color=#FFD1DF}{i}*Kick him*{/i}{/color}\n{color=#3d85c6} Tommy -2, +125$":
                hide screen hint
                $ tommybeingkicked = True
                $ tommyfriend -= 2
                jump kopniak

            "Muy bien, enfriar.Hoy estoy teniendo un buen día.Puedes devolverme la próxima semana.\n{color=#3d85c6} +150$ later":
                hide screen hint
                $ tommypaylater = True
                $ tommyfriend += 1
                jump dobryhumor
    else:
        menu:
            "{color=#FFD1DF}{i}*Take the money*{/i}{/color} {color=#00ff00}{i}+100${/i}":
                hide screen hint
                scene 10026sad with dissolve
                $ money += 100
                show text "{color=#00ff00}{size=+15}+1 0 0 ${/color}" with dissolve
                with Pause(2)
                "{i}Total: [money]$"
                hide text with dissolve
                jump wezpieniadze

            "¡Deja de mentir!¡Tu mamá es rica!¡Devuelve mi dinero, hijo de puta! {color=#FFD1DF}{i}*Kick him*{/i}{/color}":
                hide screen hint
                $ tommybeingkicked = True
                $ tommyfriend -= 2
                jump kopniak

            "Muy bien, enfriar.Hoy estoy teniendo un buen día.Puedes devolverme la próxima semana.":
                hide screen hint
                $ tommypaylater = True
                $ tommyfriend += 1
                jump dobryhumor

label wezpieniadze:
    e "Bien, que así sea{p}Pero el viernes es mejor que me consigas el resto o estás jodido."
    e "Ahora sal de aquí."
    scene 10026sad2 with dissolve
    t "okayGraciasMan!"
    scene 10022a with dissolve
    e "Odio a estos chicos ricos. "
    jump dzwonek

label kopniak:
    scene 10026 with dissolve
    e "Dame todo el dinero"
    show ep1kick with dissolve
    t "Ouch"
    scene afterkop with dissolve
    t "¿Por qué estás haciendo esto?¡Esa mierda estaba loca!"
    scene afterkop2 with dissolve
    e "Sí, mierda que has estado fumando el mismo durante un año y sigue volviendo por más."
    scene afterkop3 with dissolve
    t "Toma esto ... es todo lo que tengo ..."
    t "yo...{p}Realmente no tengo ...{p}ya no"
    $ money += 125
    show text "{color=#00ff00}{size=+15}+1 2 5 ${/color}" with dissolve
    with Pause(2)
    "{i}Total: [money]$"
    scene 10024 with dissolve
    e "Sigh"
    scene 10024c with dissolve
    t "No es justo.No deberías estar haciendo esto ..."
    scene 10024 with dissolve
    e "¿Justo?La vida no es justa.Hacer frente a ello."
    e "Estamos en la universidad, así que es una buena lección para ti"
    e "Ahora sal de aquí."
    scene 10022a with dissolve
    e "Odio a estas niñas ricas"
    jump dzwonek

label dobryhumor:
    scene 10026happy with dissolve
    t "¡¿Hablas en serio?!"
    scene 10027a with dissolve
    e "Sí, levántate"
    scene 10027b with dissolve
    t "okayGraciasDude!{p}¡Te conseguiré un extra para sostenerme!{p}Gracias de nuevo, hombre!¡En realidad!"
    scene 10027a with dissolve
    e "Ahora vete{p}Antes de cambiar de opinión."
    scene 10027b with dissolve
    t "¡Claro!"
    scene 10022a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Es uno de mis clientes más frecuentes, no puedo asustarlo demasiado."
    jump dzwonek

label dzwonek:
    scene black with fade
    show text "Dining hall" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10031 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Estoy aburrida"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Por lo general, todas las clases son aburridas."
    scene 10031a with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Además, la mayoría de los maestros aquí son viejos y feos."
    scene 10031b with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Por qué es el único maestro guapo mi [woman_role]?!"
    scene 10031c with vpunch
    stop music fadeout 1.0
    play music "music/Mtom.wav"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Owww"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Y quién es ese?"
    scene 10031d with dissolve
    y "¡Eh, tú!"
    e "¿A mí?"
    scene 10032 with dissolve
    y "Si tu"
    y "Eres [player_name]?"
    scene 10032a with dissolve
    show screen hint("Hot Mommy pregunta por mí en la escuela.Probablemente no quiera salir.Pero me pregunto que esta pasando.")

    if easymode:
            menu:
                    "Sí, ese soy yo.":
                        $ mctellnamemtommy = True
                        jump taktoja

                    "No.":
                        jump nienieznam

                    "Para una chica tan bonita, puedo ser [player_name]\n{color=#3d85c6} +1 point":
                        $ tommymomsubmission += 1
                        jump charming

    else:
        menu:
                "Sí, ese soy yo.":
                    $ mctellnamemtommy = True
                    jump taktoja

                "No.":
                    jump nienieznam

                "Para una chica tan bonita, puedo ser [player_name]":
                    $ tommymomsubmission += 1
                    jump charming

label nienieznam:
    hide screen hint
    scene 10035 with dissolve
    y "Oh bueno ...{p}Pensé por la descripción que podría haber sido tú."
    scene 10035a with dissolve
    y "¿Lo conoces y sabes dónde puedo encontrarlo?"
    scene 10032a with dissolve
    show screen hint("Puedo cepillarla o averiguar qué está pasando.")
menu:
        "En realidad soy yo":
            $ mctellnamemtommy = True
            jump taktoja

        "Voy a clase con él, pero no sé dónde podría estar ahora.":
            jump kojarzego

label charming:
    hide screen hint
    scene 10034a with dissolve
    y "Es bueno ser llamado niña, pero soy padre"
    scene 10034 with dissolve
    y "Entonces..."

    scene 10034a with dissolve
    y "Es tu nombre [player_name]?"
    show screen hint("Puedo cepillarla o averiguar qué está pasando.")
menu:
        "Sí, ese soy yo.":
            $ mctellnamemtommy = True
            jump taktoja

        "No":
            jump nienieznam


label taktoja:
    hide screen hint
    scene 10035 with dissolve
    y "Entonces eres tú ..."
    scene 10036a with dissolve
    y "..."
    scene 10033 with dissolve
    y "Soy la mamá de Tommy ..."
    scene 10036 with dissolve
    e "¿La madre de Tommy?..."
    show screen hint("¿Perra vestida así especialmente para mí?")
menu:
        "¿Y por qué estás vestido tan bien?¿Para mí?":
            jump dressedep1

        "Ok ... ¿cómo puedo ayudarte?":
            jump okep1

label dressedep1:
    hide screen hint
    scene 10032t with dissolve
    z "No es asunto tuyo, maldito-tristante ....{p}Sé de tu negocio ... y mi hijo."
    scene 10036a with dissolve
    e "¿Qué quieres decir?"
    z "{color=#A8E4A0}{i}{size=-3}Ella respiró hondo, tratando de calmarse después del estallido cuando te llamó a una maleza"

label okep1:
    hide screen hint
    scene 10032 with dissolve
    z "Sé que lo estás vendiendo marihuana."
    scene 10033 with dissolve
    z "Me gustaría hablar de eso, pero preferiría no hacerlo aquí."
    scene 10036 with dissolve
    z "..."
    scene 10035a with dissolve
    z "¿Podemos hablar de eso en mi coche?Lo estacioné justo afuera, en el estacionamiento."
    z "No quiero que vea que estoy hablando contigo."
    z "¿Puedes omitir la clase ahora?"
    show screen hint("Esto podría ser interesante.")
    scene 10036 with dissolve
    if easymode:
        menu:
                "Seguro":
                    hide screen hint
                    jump mtwychodziwie

                "No, déjame en paz\n{color=#3d85c6} Camino final":
                    $ mcnotalkwithmtommy = True
                    hide screen hint
                    jump mtwychodzizla

    else:

        menu:
                "Seguro":
                    hide screen hint
                    jump mtwychodziwie

                "No, déjame en paz":
                    $ mcnotalkwithmtommy = True
                    hide screen hint
                    jump mtwychodzizla


label kojarzego:
    scene 10032 with dissolve
    y "Oh... ok."
    scene 10036 with dissolve
    pause
    scene 10033a with dissolve
    y "Puedes decir [player_name] ¿Esa madre de Tommy lo está buscando?"
    scene 10033 with dissolve
    y "¿Y que quiero hablar con él y estaré esperando afuera en un SUV plateado?"
    scene 10032z with dissolve
    e "¡Claro!"
    scene 10033 with dissolve
    z "Gracias"
    scene 10037x with dissolve
    scene 10037x1 with dissolve
    scene 10037x2 with dissolve
    scene 10037x3 with dissolve
    scene 10037z with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Hmm, eso podría ser interesante"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Debería ir a ella?"
    show screen hint("No sé si quiero que sepa que veré a su madre.¿Quién sabe qué podría venir de eso?")
    if easymode:
        menu:
                "{color=#FFD1DF}{i}*Ir a la clase*{/i}{/color}":
                    jump lekcjabezniej

                "Tal vez le pregunte a Tommy sobre esto ....\n{color=#3d85c6} Posible compartir, +1 Tommy":
                    $ tommytalkep1 = True
                    $ tommyfriend += 1
                    jump poinformujTommyego

                "{color=#FFD1DF}{i}*Ir a su coche*{/i}{/color}":
                    jump rozmowazmamatommyego
    else:
        menu:
                "{color=#FFD1DF}{i}*Ir a la clase*{/i}{/color}":
                    jump lekcjabezniej

                "Tal vez le pregunte a Tommy sobre esto ...":
                    $ tommytalkep1 = True
                    $ tommyfriend += 1
                    jump poinformujTommyego

                "{color=#FFD1DF}{i}*Ir a su coche*{/i}{/color}":
                    jump rozmowazmamatommyego

label mtwychodziwie:
    scene 10037x with dissolve
    z "Estaré esperando afuera"
    scene 10037x1 with dissolve

    scene 10037x2 with dissolve

    scene 10037x3 with dissolve

    scene 10037z with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Me pregunto qué quiere de mí."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Tal vez le pregunte a Tommy sobre esto ...."

    show screen hint("No sé si quiero que sepa que veré su [tommywomanshort_role].Aunque quién sabe qué saldrá de eso?")
    if easymode:
        menu:
                "{color=#FFD1DF}{i}*Habla con Tommy*{/i}{/color}\n{color=#3d85c6} Posible compartir, +1 Tommy":
                    $ tommytalkep1 = True
                    $ tommyfriend += 1
                    jump poinformujTommyego

                "{color=#FFD1DF}{i}*Salir de la universidad*{/i}{/color}":
                    jump rozmowazmamatommyego
    else:
        menu:
                "{color=#FFD1DF}{i}*Habla con Tommy*{/i}{/color}":
                    $ tommytalkep1 = True
                    $ tommyfriend += 1
                    jump poinformujTommyego

                "{color=#FFD1DF}{i}*Salir de la universidad*{/i}{/color}":
                    jump rozmowazmamatommyego

label mtwychodzizla:
    scene 10032s with dissolve
    z "¿Qué les pasa a todos estos estudiantes ahora?"
    scene 10032t with dissolve
    z "Como desées.Definitivamente hablaré con director al respecto"
    scene 10037y with dissolve
    scene 10037y1 with dissolve
    scene 10037y2 with dissolve
    scene 10037y3 with dissolve
    scene 10037z with dissolve
    $ renpy.pause(1, hard=True)
    jump lekcjabezniej

label poinformujTommyego:
    scene 10037 with dissolve
    e "hey Tommy{p}Esperar"
    scene 10037b with dissolve
    t "Sí?"
    t "¿Qué deseas?"
    scene 10037c with dissolve
    e "Tu mamá quiere hablar conmigo"
    e "¿Qué le dijiste?"
    scene 10037a with dissolve
    t "¡¿A mí?!¡Nada!"
    t "Lo juro"
    if tommyfriend > 0:
        jump tommyfriend
    else:
        jump tommynotfriend

label tommyfriend:
    scene 10037b with dissolve
    t "¿Puedo preguntarte algo?"
    t "¿Puedes decirme dónde vas a conocer a mi mamá?"

    if easymode:

        menu:
                "{color=#FFD1DF}{i}*Decirle*{/i}{/color}\n{color=#3d85c6} Posible compartir, +1 Tommy":
                    $ telltommy = True
                    jump powiedzmu

                "{color=#FFD1DF}{i}*No le digas*{/i}{/color}":
                    jump tommynotfriend
    else:
        menu:
                "{color=#FFD1DF}{i}*Decirle*{/i}{/color}":
                    $ telltommy = True
                    jump powiedzmu

                "{color=#FFD1DF}{i}*No le digas*{/i}{/color}":
                    jump tommynotfriend


label powiedzmu:
    hide screen hint
    scene 10037d with dissolve
    e "Se supone que debe estar esperándome en el estacionamiento."
    scene 10037e with dissolve
    e "Ella dijo que quería hablar conmigo en privado."
    scene 10037 with dissolve
    t "Lo tengo ... {p} gracias por ser honesta."
    t "Realmente no le dije nada{p}Pero tal vez ella supuso que estoy fumando Cush ..."
    e "Okay.{p}Puedes ir ahora"
    scene 10037f with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ella no se veía fuerte ... bueno, al menos sé que no me va a secuestrar o algo así."
    jump rozmowazmamatommyego

label tommynotfriend:
    hide screen hint
    scene 10037 with dissolve
    e "¡Si ella inventa algo estúpido, tú pagarás por ello!"
    e "Ahora sal de mi vista"
    scene 10037f with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ella no se veía fuerte ... bueno, al menos sé que no me va a secuestrar o algo así."
    jump rozmowazmamatommyego


label lekcjabezniej:
    scene lesson with dissolve
    "No pasó nada especial durante esta lección"
    "La próxima lección es con tu [woman_role]"
    scene black with fade
    jump lekcjahistoria

label rozmowazmamatommyego:
    scene black with fade
    show text "Calle cerca de la universidad" with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10039 with dissolve
    z "Hey!{p}Aquí!"
    scene 10039a with dissolve
    z "Buena..."
    z "Nosotras no hablaremos aqui"
    scene drzwi0 with dissolve
    z "Entra."
    show drzwi
    $ renpy.pause(0.65, hard=True)
    scene drzwi1 with dissolve
    z "Tomaremos un pequeño paseo desde la universidad."
    scene black with fade
    show text "El bosque circundante" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text with dissolve
    scene 10040mowi2 with dissolve
    z "Gracias por aceptar hablar"
    scene 10040mowi with dissolve
    z "Me preocupa lo que ha estado sucediendo entre tú y mi hijo"
    z "Quiero entender por qué está sucediendo esto y encontrar una solución"
    e "oh,ComeOn!{p}¿quéQuieresDeTommyYDeMí?"
    z "Tommy ha sido profundamente afectado por sus acciones, y no lo defenderé."
    scene 10040mowi2 with dissolve
    z "Tommy es un buen niño.Nunca habría recogido el hábito de marihuana si no fuera por ti."
    z "Pero sé que si lo reporto al rector, solo empeorará las cosas."
    z "Yo también fui a la escuela y sé cómo termina"
    z "Por eso prefiero llevarme bien"
    scene 10040slucha with dissolve
    e "¿Llevarse bien?¿Cómo?"
    scene 10040mowi with dissolve
    z "Aquí está $200{p}Eso es más de lo que probablemente ganes de él."
    z "Nunca volverás a venderle nada."
    show screen hint("Siempre me ha encantado el dinero.Pero las mamás calientes más.")

    if easymode:
        menu:
                "¿No podemos simplemente conocernos mejor?":
                    hide screen hint
                    jump lepiejpoznac

                "¿Qué pasa si no quiero el dinero?":
                    hide screen hint
                    jump niechcepieniedzy

                "{color=#FFD1DF}{i}*Toma el dinero.Pueden ser útiles más tarde.*{/i}{/color} \n{color=#3d85c6} +200$, Ends character path":
                    hide screen hint
                    $ money += 200
                    $ mtommoney += 1
                    show text "{color=#00ff00}{size=+15}+2 0 0 ${/color}" with dissolve
                    with Pause(2)
                    "{i}Total: [money]$"
                    hide text with dissolve
                    jump takefromtommymom
    else:
        menu:
                "¿No podemos simplemente conocernos mejor?":
                    hide screen hint
                    jump lepiejpoznac

                "¿Qué pasa si no quiero el dinero?":
                    hide screen hint
                    jump niechcepieniedzy

                "{color=#FFD1DF}{i}*Toma el dinero.Pueden ser útiles más tarde.*{/i}{/color}":
                    hide screen hint
                    $ money += 200
                    $ mtommoney += 1
                    show text "{color=#00ff00}{size=+15}+2 0 0 ${/color}" with dissolve
                    with Pause(2)
                    "{i}Total: [money]$"
                    hide text with dissolve
                    jump takefromtommymom

label takefromtommymom:
    scene 10040slucha with dissolve
    e "¿Qué ahora?"
    scene 10040mowi with dissolve
    z "Ahora saldrás del auto y te olvides de Tommy."
    z "recuerdaQueTenemosUnTrato,SiNo,LoReportaréAlRector"
    jump endwithmoney

label lepiejpoznac:
    scene 10040zlamowi with dissolve
    z "No entiendo"
    z "¿Qué quieres decir con decir algo así?"
    scene 10040zlaslucha with dissolve
    show screen hint("Ella está temblando de estrés.Puedo presionarla.")


    if easymode:

        menu:
            "Eso tal vez solo te chupes mi polla si quieres algo de mí.\n{color=#3d85c6} +1 Point":
                hide screen hint
                $ tommymomsubmission += 1
                jump mozepoprostusuck

            "Simplemente no quiero quitarte dinero.Tommy es un gran cliente, después de todo.":
                hide screen hint
                jump niechcepieniedzy

    else:
        menu:
            "Que tal vez solo te chupes mi polla si quieres algo de mí.":
                hide screen hint
                $ tommymomsubmission += 1
                jump mozepoprostusuck

            "Simplemente no quiero quitarte dinero.Tommy es un gran cliente, después de todo.":
                hide screen hint
                jump niechcepieniedzy

label mozepoprostusuck:
    scene 10040zdziwiona with dissolve
    z "..."
    scene 10040smd with dissolve
    z "Wh ... ¿Qué?"
    scene 10040smda with dissolve
    z "Fingiré que no escuché eso ..."
    z "Pero sal de mi auto ahora."
    e "Ok, está bien, lo siento por eso.Fue grosero.{p}Pero si quieres algo de mí ...{p}Muéstrame tus tetas."
    jump showmeinthecar

label niechcepieniedzy:
    scene 10040zlamowi with dissolve
    z "No entiendo"
    scene 10040zlaslucha with dissolve
    e "Simply{p}I don't want money from you. I will earn much more."
    scene 10040mowi with dissolve
    z "So you'll just leave him?"
    e "No"
    scene 10040zlamowi with dissolve
    z "Hmph...."
    z "Quería llevarme bien contigo de alguna manera, pero veo que será difícil."
    scene 10040zlaslucha2 with dissolve
    e "Pero quiero llevarse bien contigo"
    scene 10040zlaslucha with dissolve
    z "Hm?"
    z "No me interesa jugar.Solo quiero que dejes a Tommy solo"
    e "Oh, no es un juego, ya sabes."
    e "No quieres hacer un gran problema, ¿verdad? {p} ... Quiero que me muestres tus tetas"
label showmeinthecar:
    scene 10040zdziwiona with dissolve
    z "Espera ... ¿qué?"
    scene 10040zlamowi with dissolve
    z "¿Estás loco?"
    z "No haré nada como eso"
    z "Creo que iré a hablar con el rector al respecto"
    scene 10040zlaslucha with dissolve
    e "Muéstrame tus tetas y consideraré dejar solo a Tommy.Podría cambiar todo"
    z "¡De ninguna manera!"
    e "Solo escúchame"
    e "Si me muestras tus tetas, puede ser una señal de confianza, un gesto que me ayudará a pensar en el bienestar de tu hijo."
    e "Vale la pena disparar, ¿no?"
    scene 10040slucha with dissolve
    e "Además, tu cuerpo se ve increíble, eres una mujer hermosa ..."
    scene 10040smd with dissolve
    e "Estamos en el bosque ... y nadie lo sabrá de todos modos"
    scene 10040zlamowi with dissolve
    z "No es una opción en absoluto{p}tienes la edad de mi hijo{p}No cuentes con eso"
    scene 10040smda with dissolve
    z "No haré esto"
    scene 10040smutna with dissolve
    e "Vamos, no seas tan mojigata.{p}Es solo un pequeño favor.No tomaré no por una respuesta."
    scene 10040smd with dissolve
    z "No puedo creer que me estés pidiendo que haga algo como esto.{p}Está mal ..."
    scene 10040smutna with dissolve
    e "Sin embargo, piénselo.Si te niegas, ¿quién sabe lo que podría hacerle a Tommy?{p}¿Tal vez lo atraparán con marihuana y lo arrojarán de la universidad?"
    scene 10040zlamowi with dissolve
    z "No ... Definitivamente no harás eso."
    scene 10040zlaslucha with dissolve
    e "Solo hazlo y dejaré a Tommy solo.Prometo.{p}Es un pequeño sacrificio para garantizar su seguridad, ¿no?"
    z "..."
    z "..."
    z "..."
    scene 10040smutnasciaga with dissolve
    z "No puedo creer que esté haciendo esto ..."
    z "Pero si eso significa que ya no le venderá esta mierda ..."
    e "Eso es lo que me gusta escuchar.El futuro de Tommy ahora está en tus manos."
    scene 10040sciagamowi with dissolve
    z "Si le cuentas a alguien sobre esto, te mataré"
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
    z "Disfrutar"
    z "..."
    e "Son hermosos ... maldita sea."
    "{color=#A8E4A0}{i}{size=-3}Tu polla estaba cada vez más duro con cada segundo que pasó.Sus tetas eran algo más, fuera de lo ordinario"
    scene 10043 with dissolve
    e "Tan agradable ..."
    "{color=#A8E4A0}{i}{size=-3}Se veían suaves y cálidos.Como si pudieras aplastar tu mano sobre ella."
    scene 10043a with dissolve
    e "Este será nuestro pequeño secreto..."
    e "Tengo que tocarlas"
    scene 10044 with dissolve
    z "..."
    scene 10044a with dissolve
    z "No"
    show screen hint("Parece que hará lo que sea que le digan.Me pregunto qué tan lejos llegará.")

    if easymode:

        menu:
            "Callarse la boca\n{color=#3d85c6} +1 Point":
                hide screen hint
                scene 10044shock with dissolve
                $ tommymomsubmission += 1
                jump menuaftershut

            "Puedo ver que estás encendido.":
                hide screen hint
                jump widzezepodniecona

    else:
        menu:
            "Callarse la boca":
                hide screen hint
                scene 10044shock with dissolve
                $ tommymomsubmission += 1
                jump menuaftershut

            "Puedo ver que estás encendido.":
                hide screen hint
                jump widzezepodniecona

label widzezepodniecona:
    z "Eso no es cierto"

label menuaftershut:
    "{color=#A8E4A0}{i}{size=-3}La miraste con una expresión más mala, tratando de presionarla."
    if easymode:
        menu:

            "O me dejas o me voy":
                jump letmecycka

            "{color=#FFD1DF}{i}*Agarra sus tetas*{/i}{/color}\n{color=#3d85c6} +1 Point":
                $ tommymomsubmission += 1
                jump grabcycek
    else:
        menu:

            "O me dejas o me voy":
                jump letmecycka

            "{color=#FFD1DF}{i}*Agarra sus tetas*{/i}{/color}":
                $ tommymomsubmission += 1
                jump grabcycek

label grabcycek:
    scene 10044grab with dissolve
    z "HUH!?"
    scene 10044grab1 with dissolve
    e "hush...shhh"
    scene 10044grab2 with dissolve
    z "..."
    e "Recuerda que estás haciendo esto por Tommy"
    jump letmecycka2

label letmecycka:

    scene 10044 with dissolve
    z "..."
    scene 10044sad2 with dissolve
    z "..."
    scene 10044sad with dissolve
    z "...{p}...Ok..."
    jump letmecycka2

label shutupandcycek:
    e "Recuerda que estás haciendo esto por Tommy"
    scene 10044sad with dissolve
    z "..."
    scene 10044sad2 with dissolve
    z "..."
    scene 10044a with dissolve
    z "...{p}...Ok..."
label letmecycka2:

    show tit001 with dissolve
    z "..."
    "{i}*Su respiración se acelera*"
    z "..."
    scene 10045y with dissolve
    z "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} ¿Cómo me involucré en algo como esto?.."
    scene 10045z with dissolve
    z "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} El amigo de mi hijo buscaba mis pechos y lo dejé hacerlo..."
    show tit002 with dissolve
    $ renpy.pause(2.7, hard=True)
    scene 10045
    "{color=#A8E4A0}{i}{size=-3}Después de agarrarlos y apretar tu mano sobre sus suaves melones, no pudiste evitarlo: necesitabas sacar tu gran polla palpitante."
    z "...{p}¿Qué diablos estás haciendo ??!"
    e "No soy una niña"
    e "¿Crees que solo tocar tus tetas sería suficiente para mí?"

    if tommymomsubmission > 1:
        jump endingtommymom
    else:
        jump endingwithouttommy


label endingtommymom:
    $ tommymomcarhj = True
    scene 10047 with dissolve

    scene 10047a with dissolve

    scene 10048 with dissolve
    e "Ahora toma tu pequeña mano y toma mi polla"
    e "Y entonces tu Tommy será intocable durante todos sus estudios"
    z "..."
    show grabmtom
    e "Sabes qué hacer."

    if not easymode:
        $ achValid += 1
        $ achievement.grant("Achiev01")
        $ achievement.sync()
        if not persistent.achievement1:
            show Achiev1 at achievment with easeintop:
                    zoom 0.5
                    rotate_animation

            "¡Has recibido logros!{p}\"Convencer a la madre de Tommy para que haga sacrificios\"."
            "Número de logros obtenidos en este capítulo [achValid]/3"
            hide Achiev1
            $ persistent.achievement1 = True
    scene nochoke00 with dissolve
    show hhjj0
    $ renpy.pause(2, hard=True)
    e "Muy lindo..."
    $ renpy.pause(3, hard=True)

menu:

        "Ahogarla":
            $ tommymomep1choke = True
            jump choketommymom

        "No la ahogues":
            jump finishtommymom

label choketommymom:
    scene choke0 with dissolve
    e "No te detengas"
    show chokeep1
    "{color=#A8E4A0}{i}{size=-3}Apretaste tu agarre alrededor de su garganta, empujando tu mano hacia la barbilla."
    $ renpy.pause(3, hard=True)
    e "Ahora esto es lo que realmente me gusta"
    pause
    e "Será mejor que volvamos a hacer esto la próxima semana.{p}Quiero decir, harías un sacrificio por tu hijo, ¿no?"
    jump finishtommymom

label finishtommymom:
    $ renpy.pause(2, hard=True)
    e "Manténgalo más apretado"
    e "Tan buena{p}Estoy a punto de correrme."
    e "ooooooh"
    scene finish00 with dissolve:
        zoom 0.5
    e "Ah"
    $ maxmccumep7 += 1
    show finishmomtommy
    $ renpy.pause(4, hard=True)
    e "Oh.. Wowoowwwww..."
    scene 10052 with dissolve
    e "Lindo..."
    $ renpy.end_replay()

    if telltommy == True:
        $ tommysawmomincar = True
        t "Mamá??!"

        scene 10052tom with dissolve
        if not easymode:
            $ achValid += 1
            $ achievement.grant("Achiev02")
            $ achievement.sync()
            if not persistent.achievement2:
                show Achiev2 at achievment with easeintop:
                        zoom 0.5
                        rotate_animation

                "¡Has recibido logros!{p}\"Hazte amiga de Tommy\"."
                "Número de logros obtenidos en este capítulo [achValid]/3"
                hide Achiev2
            $ persistent.achievement2 = True
            z "Tommy?!"

            scene glass with dissolve
            e "¡Oh, hola Tommy!"
            scene glass2 with dissolve
            e "..."
            jump endingtommy
        else:
            z "Tommy?!"

            scene glass with dissolve
            e "Oh hola tommy!"
            scene glass2 with dissolve
            e "..."
            jump endingtommy
    else:
        scene 10052nottom with dissolve
        z "Ahora, sal de mi coche"
        z "Y recuerda lo que prometiste"
        e "Sí..."
        jump endwithmoney

label endingwithouttommy:

    scene glass2 with vpunch
    z "Saca la mierda de mi coche"
    z "No sé lo que estabas pensando, ¡pero no haré nada de eso!"
    z "¡Ya te he permitido demasiado y no olvides lo que prometiste!"

label endwithmoney:
    scene 10056 with dissolve
    e "..."

    show carleft
    $ renpy.pause(2, hard=True)

    scene 10056a
    e "..."

    scene 10057 with dissolve
    e "Chica loca"
    scene 10058 with dissolve
    e "Debo darme prisa.¡Las clases llegarán pronto!"
    scene 10058a with dissolve
    e "Tengo lecciones con mi [woman_role]"
    scene black with fade
    show text "Universidad" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    jump lekcjahistoria


label endingtommy:
    scene glass2 with dissolve
    z "¡Sal de mi coche!"
    z "AHORA!"

    scene 10056 with dissolve
    e "..."

    show carleft
    $ renpy.pause(2, hard=True)

    scene 10057
    e "Chica loca{p}Necesito volver a la universidad muy rápido."
    scene 10058 with dissolve
    e "Tengo lecciones con mi [woman_role] pronto"
    scene 10058a with dissolve
    e "Me pregunto a dónde fue Tommy."
    scene black with fade
    show text "Universidad" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    jump lekcjahistoria

label lekcjahistoria:
    stop music fadeout 1.0
    play music "music/Mnic.wav"
    scene 10100 with dissolve
    e "{color=#ffa500}{i}*panting*"
    scene 10100a with dissolve
    p "Ey [player_name]."
    scene 10100b with dissolve
    p "Te ves como una mierda."
    scene 10100c with dissolve
    e "A la mierda Gary"
    scene 10101 with dissolve
    e "Ustedes idiotas ni siquiera pueden encender las luces ..."
    scene 10101a with dissolve
    p "Si intentas convertirlo en ti mismo, verías que no funciona."
    scene 10101b with dissolve
    "{color=#ffa500}{i}*La puerta golpea*"
    show 10102 at Move((0, 0), (0, 0.99), 7.0, xanchor=0, yanchor=0.5)
    $ renpy.pause(7, hard=True)
    p "Daaamn"
    p "Amo estas clases"
    e "Muy divertido"
    scene 10103a with dissolve
    m "¡Buenas tardes!"
    scene 10104 with dissolve
    c "Buenas tardes{p}¡Hola!"
    scene 10104a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Uhh..."
    scene 10104b with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Parece roto ..."
    scene 10105 with dissolve
    m "La luz no parece estar funcionando ..."
    m "Pronto estará oscuro afuera, solo verificaré la asistencia y hoy no habrá clases."
    scene 10107 with dissolve
    c "Rudón!"
    scene 10107a with dissolve
    p "¿Por qué estás tan sudoroso?"
    scene 10107b with dissolve
    e "Cuida tu propio negocio Dickhead."
    scene 10107c with dissolve
    p "Está bien, está bien, solo estoy preguntando"


    scene 101060 with dissolve
    p "Sabes que [player_name]?"
    scene 101061 with dissolve
    p "Eres estúpida como la mierda{p}Pero tu [woman_role]? Maldita sea, ella es tan jodidamente caliente, amigo ..."
    scene 101064 with dissolve
    p "¿Crees que le gustan las pollas jóvenes?"
    scene 101068 with dissolve
    e "Vete a la mierda."
    scene 101067 with dissolve
    p "Frío hermano"
    scene 101066 with dissolve
    p "Solo digo que si tuviera un [woman_role] así, no la dejaría dormir"
    scene 101068 with dissolve
    e "Me pregunto si eras tan valiente cuando le pidiste a Paige en una cita."
    scene 101064 with dissolve
    p "Paige parece una mierda junto a tu[woman_role], dudar."
    scene 101066 with dissolve
    p "Realmente te envidio."
    scene 101065 with dissolve
    p "¿Vive tu vieja amiga contigo?"

    show screen hint("Recuerdo que la relación con mi padre era ...")

    if easymode:
            menu:
                "Si, esta bien.":
                    hide screen hint
                    scene 101068 with dissolve
                    e "Es un tipo genial"
                    scene 101066 with dissolve
                    p "Siempre puedo reemplazarlo si quieres"
                    scene 101067 with dissolve
                    e "Prefiero ser huérfana."
                    jump niclesson

                "Sí, pero nunca está en casa y simplemente me molesta. \n{color=#3d85c6} Papá -1":
                    hide screen hint
                    $ dadfriend -= 1
                    scene 101068 with dissolve
                    e "Y cuando está en casa, discutimos todo el tiempo"
                    scene 101066 with dissolve
                    p "Siempre puedo reemplazarlo si quieres"
                    scene 101067 with dissolve
                    e "Prefiero ser huérfana."
                    jump niclesson

    else:
            menu:
                "Sí, está bien.":
                    hide screen hint
                    scene 101068 with dissolve
                    e "Es un tipo genial"
                    scene 101066 with dissolve
                    p "Siempre puedo reemplazarlo si quieres"
                    scene 101067 with dissolve
                    e "Prefiero ser huérfana."
                    jump niclesson

                "Sí, pero nunca está en casa y simplemente me molesta.":
                    hide screen hint
                    $ dadfriend -= 1
                    scene 101068 with dissolve
                    e "Y cuando está en casa, discutimos todo el tiempo"
                    scene 101066 with dissolve
                    p "Siempre puedo reemplazarlo si quieres"
                    scene 101067 with dissolve
                    e "Prefiero ser huérfana."
                    jump niclesson

label niclesson:
    scene 101080a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} El esta aquí.{/i}"
    scene 101081 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Enfocar [woman_name]{/i}"
    scene 101082 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Sigue hablando con su amiga y ellas me miran.{/i}"
    scene 101081 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Espero que no sea lo suficientemente estúpido como para contarle a sus amigos lo que pasó{/i}"
    scene black with fade
    show text "Varios minutos de comprobación de asistencia más tarde" at title with dissolve
    $ renpy.pause(2, hard=True)
    scene 1010900 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Puedo ver cada vez menos, está empezando a oscurecer{/i}"
    scene 1010901 with dissolve
    m "...and...{p}Mr. Zerat?"
    c "¡Ausente hoy!"
    scene 1010902 with dissolve
    m "Eso es todo.Dígale a todos los que están ausentes que tendrán que compensar el día."
    m "Y les deseo a todas las demás un buen fin de semana."

    scene 10110 with dissolve
    p "¿Vienes?"
    scene 10110a with dissolve
    e "Necesito hablar con mi [woman_role]{p} Me uniré a ti más tarde"
    scene 10110b with dissolve
    p "Claro nos vemos luego amiga"

    scene 1011208 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Solo mirala."
    scene 1011209 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ella está extremadamente estresada."
    scene 1011210 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Fingiré que me voy, me pregunto si me detendrá"
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
    m "[player_name] esperar..."
    scene 1011309 with dissolve
    e "Sí?"
    scene 1011310 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} No sé por qué siempre hay llaves en la puerta aquí, pero gracias por eso ...."
    "{color=#ffa500}{i}*el sonido del bloqueo de la puerta.*"
    scene 1stage0 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Tengo que estar segura, es obvio que está estresada.{/i}"
    scene 1stage1 with dissolve
    m "¿Podemos hablar?"
    scene 1stage2 with dissolve
    e "Seguro..."
    scene 1stage3 with dissolve
    e "...[woman_role].{p}"
    scene 1stage4 with dissolve
    pause
    scene 1stage5 with dissolve
    m "Lo que hiciste ..."
    scene 1stage6 with dissolve
    m "...Estaba equivocada"
    scene 1stage7 with dissolve
    pause 0.5
    scene 1stage8 with dissolve
    pause 0.5
    scene 1stage9 with dissolve
    pause 0.5
    show screen hint("Creo que sería bueno hacerla sentir culpable por toda la situación.")

    if easymode:
        menu:
            "¿Entonces es mi culpa? \n{color=#3d85c6} +1 Point":
                hide screen hint
                jump historiarozmowa1
            "¿Qué diablos estás haciendo?\n{color=#3d85c6} +1 Point":
                hide screen hint
                jump historiarozmowa2
            "Realmente me gustan estas fotos.":
                hide screen hint
                scene 2stage00
                pause 0.5
                scene 2stage01
                pause 0.5
                scene 2stage02
                pause 0.5
                scene 2stage03
                pause 0.5
                jump historiarozmowa3

    else:
        menu:
            "¿Entonces es mi culpa?":
                hide screen hint
                jump historiarozmowa1
            "¿Qué diablos estás haciendo?":
                hide screen hint
                jump historiarozmowa2
            "Me gustan mucho estas fotos.":
                hide screen hint
                scene 2stage00
                pause 0.5
                scene 2stage01
                pause 0.5
                scene 2stage02
                pause 0.5
                scene 2stage03
                pause 0.5
                jump historiarozmowa3

label historiarozmowa1:
    scene 2stage00 with dissolve
    m "No."
    scene 2stage01 with dissolve
    m "Lo lamento."
    show image "images/Stats/Dom[nicep1dom].png" at statleft
    pause 1
    $ nicep1dom += 1
    show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicep1dom].png" with dissolve
    scene 2stage02 with dissolve
    m "No deberías haber visto esto.{p}Y lo siento por eso."
    scene 2stage03 with dissolve

    menu:
        "Pero estoy muy contenta de haberlo visto.":
            jump historiarozmowa3
        "Me rompiste el corazón ese día.":
            jump butisawit

label butisawit:
    scene stage12 with dissolve
    m "No sé qué decir."
    m "Lo siento mucho"
    scene stage13 with dissolve
    show screen hint("Ser demasiado vulgar en este momento probablemente no valga la pena.Pero definitivamente la sorprenderá.")
    menu:
        "Deberías estar chupando mi polla allí, no de un extraño":
            hide screen hint
            $ ep1rude +=1
            jump historiamiddle
        "Ni siquiera sabes lo que significa cuando ves tu [woman_role] de rodillas frente a un extraño":
            hide screen hint
            jump historiarozmowa2


    scene stage12 with dissolve



label historiarozmowa2:
    scene 2stage00 with dissolve
    m "Soy... {p}Lo lamento."
    show image "images/Stats/Dom[nicep1dom].png" at statleft
    pause 1
    $ nicep1dom += 1
    show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicep1dom].png" with dissolve
    scene 2stage01 with dissolve
    m "Esto nunca volverá a suceder."
    scene 2stage03 with dissolve
    m "¿Puedes eliminar las fotos que tomaste?"

    menu:
        "¿Por qué haría eso?De hecho, me gustan mucho, te ves genial.":
            jump historiarozmowa3
        "Depende":
            jump historiaapologize


label historiarozmowa3:
    scene 2stage04 with dissolve
    m "Entiendo que a tu edad te interesa .."
    scene stage06 with dissolve
    m "... el cuerpo femenino, y tal ..."
    scene stage07 with dissolve
    m "Pero soy tu [woman_role], Entonces ... imágenes como esa son muy, muy inapropiadas."
    scene stage08 with dissolve
    scene stage09 with dissolve
    scene stage10 with dissolve
    scene stage11 with dissolve
    scene stage12 with dissolve
    m "Te estoy pidiendo que las elimines."
    scene stage13 with dissolve
    show screen hint("Ella debería saber cómo me afecta su persona.")

    if easymode:
        menu:
                "¿Así?":
                    hide screen hint
                    e "No las voy a eliminar gratis."
                    jump historiaapologize
                "Solo pensar en estas fotos hace que mi cuerpo temble.\n{color=#3d85c6} +1 Point":
                    hide screen hint
                    jump historiarozmowa5

    else:
        menu:
                "¿Así?":
                    hide screen hint
                    e "No las voy a eliminar gratis."
                    jump historiaapologize
                "Solo pensar en estas fotos hace que mi cuerpo temble. ":
                    hide screen hint
                    jump historiarozmowa5


label historiaapologize:
    scene stage3view1 with dissolve
    m "¿Qué quieres decir?"
    scene stage3view2 with dissolve
    m "¿Quieres chantajearme por dinero?"
    show screen hint("Ella no se parece al tipo de persona que cortésmente se pondría en cuclillas y me chuparía ahora.")

    if easymode:
        menu:
            "¿Quién dijo algo sobre el dinero?\n{color=#3d85c6} Mejor opción":
                jump historiarozmowa4
            "Depende de si serás mi perra a partir de ahora.":
                $ ep1rude -=1
                jump historiabitch
    else:
        menu:
            "¿Quién dijo algo sobre el dinero?":
                jump historiarozmowa4
            "Depende de si serás mi perra a partir de ahora.":
                $ ep1rude -=1
                jump historiabitch

label historiarozmowa4:
    scene stage3view3 with dissolve
    m "¿Así que lo que?"

    if easymode:
        menu:
            "Soy fan de tu cuerpo.\n{color=#3d85c6} Mejor opción":
                  $ ep1bodyfan = True
                  jump historiashutup
            "La única forma en que elimino las fotos es si me chupas la polla.":
                  hide screen hint
                  $ ep1rude += 1
                  jump historiasuck
            "{color=#FFD1DF}*Ahogarla*\n{color=#3d85c6} Ahogar pero eso terminará la escena.":
                  hide screen hint
                  jump ep1chokeciuchyalt

    else:
        menu:
            "Soy fan de tu cuerpo.":
                  $ ep1bodyfan = True
                  jump historiashutup
            "La única forma en que elimino las fotos es si me chupas la polla.":
                  hide screen hint
                  $ ep1rude += 1
                  jump historiasuck
            "{color=#FFD1DF}*Ahogarla*":
                  hide screen hint
                  jump ep1chokeciuchyalt

label historiasuck:
    scene frontview01 with dissolve
    e "La única forma en que elimino las fotos es si me chupas la polla."
    jump historiamiddle

label historiarozmowa5:
    scene stage14 with dissolve
    m "..."
    show image "images/Stats/Dom[nicep1dom].png" at statleft
    pause 1
    $ nicep1dom += 1
    show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicep1dom].png" with dissolve
    e "No las voy a eliminar gratis."
    jump historiaapologize

label historiabitch:
    scene frontview01 with dissolve
    e "Depende de si serás mi perra a partir de ahora."
label historiamiddle:
    scene frontviewshock with dissolve
    m "..."
    scene frontviewshock2 with dissolve
    m "..."
    scene frontviewangry with dissolve
    m "¿Cómo te atreves a hablar conmigo así?"
    scene frontviewangry2 with dissolve
    m "..."

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Ahogarla*{/i}{/color}{size=-8}(Req. 2 Domination){/size}\n{color=#3d85c6} Ahogar pero eso terminará la escena." if nicep1dom > 5:
                hide screen hint
                jump ep1chokeciuchy

            "Shut up and listen":
                jump historiashutup
    else:
        menu:
            "{color=#FFD1DF}{i}*Ahogarla*{/i}{/color}{size=-8}(Req. 2 Domination){/size}" if nicep1dom > 5:
                hide screen hint
                jump ep1chokeciuchy

            "Cállate y escucha":
                jump historiashutup

label ep1chokeciuchyalt:
    scene chokefin000 with dissolve
    jump ep1chokemid

label ep1chokeciuchy:
    scene chokefin000 with dissolve
    e "¿Y cómo debo hablar contigo?"
label ep1chokemid:
    show chokefindres
    $ renpy.pause(3, hard=True)
    m "[player_name]!"
    scene chokedres01 with dissolve
    m "DETENER!"
    scene chokedres02 with dissolve
    e "Estás engañando a mi padre en su casa"
    scene chokedres03 with dissolve
    e "Así que de ahora en adelante te trataré como te mereces"
label kickep1bad:
    scene ep1kicknic with vpunch
    e "AAAAH"
    scene ep1kicknic2 with dissolve
    e "MIERDA"
    $ chokeep1kick = True
    scene black with fade
    show text "[woman_name] se quedó sin el auditorio" at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    jump episode2


label historiashutup:
    if ep1bodyfan == True:
        scene stage3view3 with dissolve
        m "..."
        m "Qué quieres decir...?"
        show image "images/Stats/Dom[nicep1dom].png" at statleft
        pause 1
        $ nicep1dom += 1
        show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicep1dom].png" with dissolve
        scene stage3view6 with dissolve
        e "Sabes que haré cualquier cosa por ti."
        jump historiadecision
    e "Sabes que haré cualquier cosa por ti."

label historiadecision:
    e "Si me dejas ser buena contigo."
    show screen hint("Debería ser consistente en lo que digo.")
    menu:
         "... y al mismo tiempo serás mi pequeño coño.":
               hide screen hint
               jump historiasuck3

         "... Te cuidaré bien y de tus necesidades.":
               hide screen hint
               $ needsep1 = True
               jump historiadecision2

label historiasuck3:
    scene frontview01 with dissolve
    e "... y al mismo tiempo serás mi pequeño coño."
    if ep1rude == 1:
        scene historiasck with dissolve
        m "¿¡Qué sucede contigo!?Primero me cuentas algo sobre ... sobre ... {p}chupando polla? {p}¿Y ahora que puedo ser tu pequeño coño?Te golpeaste la cabeza [player_name]??"
        scene historiasck2 with dissolve
        m "Por favor, terminemos esta conversación, está estresado por toda esta situación."
        show image "images/Stats/Dom[nicep1dom].png" at statleft
        pause 1
        $ nicep1dom += 1
        show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicep1dom].png" with dissolve
        jump historiadecision3
    elif ep1rude ==0:
        scene historiasck with dissolve
        m "Tu que?!{p}Te golpeaste la cabeza [player_name]??"
        scene historiasck2 with dissolve
        m "Por favor, terminemos esta conversación, está estresado por toda esta situación."
        jump historiadecision3
    elif ep1rude ==-1:
        scene historiasck with dissolve
        m "¿¡Qué sucede contigo!?Primero me cuentas algo sobre ... sobre ...{p}ser tu puta? {p}¿Y ahora que puedo ser tu pequeño coño?Te golpeaste la cabeza [player_name]??"
        scene historiasck2 with dissolve
        m "Por favor, terminemos esta conversación, está estresado por toda esta situación."
        show image "images/Stats/Dom[nicep1dom].png" at statleft
        pause 1
        $ nicep1dom += 1
        show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicep1dom].png" with dissolve
        jump historiadecision3

label historiadecision2:
    scene needs with dissolve
    m "Mi...{p}...necesidades?"
label historiadecision3:
    show screen hint("A veces es mejor pensar dos veces que hacerlo una vez.")

    if easymode:
        menu:

            "{color=#FFD1DF}{i}*Agarra las correas de su vestido*{/i}{/color} {size=-8}(Req. 3 Domination){/size}" if nicep1dom > 6:
                hide screen hint
                jump grabstrapsep1
            "{color=#FFD1DF}*Toca sus tetas* \n{color=#3d85c6} Renderizado adicional, pero eso terminará la escena.":
                hide screen hint
                jump grabtitsep1
            "*Piensa que hacer a continuación* \n{color=#3d85c6} Hazlo dos veces por +1 point " ('#FFD1DF'):
                $ thinkep1 += 1
                jump thinkwhattodo

    else:
        menu:

            "{color=#FFD1DF}{i}*Agarra las correas de su vestido*{/i}{/color} {size=-8}(Req. 3 Domination){/size}" if nicep1dom > 6:
                hide screen hint
                jump grabstrapsep1
            "{color=#FFD1DF}*Toca sus tetas*":
                hide screen hint
                jump grabtitsep1
            "*Piensa que hacer a continuación*" ('#FFD1DF'):
                $ thinkep1 += 1
                jump thinkwhattodo

label thinkwhattodo:
    if thinkep1 == 1:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Puedo agarrar sus tetas, pero estoy segura de que no le gustará.{/i}"
        jump historiadecision3
    if thinkep1 == 2:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} [woman_name] Parece estresado por mi falta de acción.{/i}"
        show image "images/Stats/Dom[nicep1dom].png" at statleft
        pause 1
        $ nicep1dom += 1
        show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicep1dom].png" with dissolve
        jump historiadecision3
    if thinkep1 > 2:
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Parece que has agotado todas las posibilidades ...{/i}"
        jump historiadecision3

label grabtitsep1:
    hide screen hint
    scene grabtts00 with dissolve
    e "Sé lo que quieres"
    show grabnictitsep1
    $ renpy.pause(2, hard=True)
    m "[player_name]!!"
    jump kickep1bad

label grabstrapsep1:
    hide screen hint
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
    e "No lo necesitas"
    scene shame00 with dissolve
    e "Si no quieres que alguien se entere, se mantendrás en silencio ahora."
    show image "images/Stats/Dom[nicep1dom].png" at statleft
    pause 1
    $ nicep1dom += 1
    show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicep1dom].png" with dissolve
    show ep1shame
    $ renpy.pause(2, hard=True)
    scene 10499 with vpunch
    pause
    scene 10499a with dissolve
    e "No soy tu enemigo"
    scene 10500 with dissolve
    e "Puedo eliminar todas las fotos y olvidarme de todo"
    scene 10502 with dissolve
    e "Pero debes ser castigado"
    scene 10503 with dissolve
    m "Soy tu [woman_role]...No es normal lo que estás haciendo"
    scene 10501 with dissolve
    m "¿Has visto lo suficiente?Yo quiero ir"
    scene 10503a with dissolve
    e "Quiero ser tu amigo [woman_role]."
    scene 10504 with dissolve
    e "Y las amigas se ayudan"
    show ep1grabfinal
    $ renpy.pause(14, hard=True)
    scene 10505 with dissolve
    e "And I'm your best friend"
    show dckep1msg
    m "[player_name]..."
    m "¿Por qué estás haciendo esto?."
    e "Shhh..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Es demasiado fuerte, no tengo la oportunidad de liberarme"
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Cálmate [woman_name], Definitivamente no hará nada mas"
    scene dckgrab059 with dissolve
    e "Solo mira el efecto que tienes en mí"
    show dckep1grab with dissolve
    $ renpy.pause(4, hard=True)
    e "Ahh"
    scene 10506 with vpunch
    m "Detener..."
    show image "images/Stats/Dom[nicep1dom].png" at statleft
    pause 1
    $ nicep1dom += 4
    show image "images/Stats/Dom[nicep1dom].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicep1dom].png" with dissolve
    show finalep1 with dissolve
    $ renpy.pause(1, hard=True)
    m "[player_name], Por favor deja ir mi mano"
    $ renpy.pause(2, hard=True)
    m "Lo siento mucho..."
    e "Tienes manos tan delicadas"
    "{color=#A8E4A0}{i}{size=-3}Tus piernas estaban temblando al toque de su mano alrededor de tu polla.Una parte de ti no podía creer lo que estaba pasando."
    "{color=#A8E4A0}{i}{size=-3}Guiste su mano hacia arriba y hacia abajo, tratando de hacerla masturbarte más rápido y más rápido."
    "{color=#A8E4A0}{i}{size=-3}Con cada golpe, podrías sentir que tu polla se preparaba para correrse, ya que comenzó a latir, y tus bolas se levantaron."
    scene 10507 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Necesito detenerlo..."
    show beforehb with dissolve
    $ renpy.pause(2, hard=True)
    scene 10508 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} AHORA"
    show headbutt with dissolve
    $ renpy.pause(3, hard=True)
    scene lastsce0 with dissolve
    e "OUCH"
    "{color=#A8E4A0}{i}{size=-3} [woman_name] se escapó."
    scene lastsce1 with dissolve
    scene lastsce2 with dissolve
    scene lastsce3 with dissolve
    scene lastsce4 with dissolve
    scene lastsce5 with dissolve
    scene lastsce6 with dissolve
    pause
    scene lastsce7 with dissolve
    pause
    jump chapter1final

label chapter1final:
    if not easymode:
        $ achValid += 1
        $ achievement.grant("Achiev03")
        $ achievement.sync()
        if not persistent.achievement3:
            show Achiev3 at achievment with easeintop:
                        zoom 0.5
                        rotate_animation

            "¡Has recibido logros!{p}\"Mano\"."
            "Número de logros obtenidos en este capítulo [achValid]/3"
            hide Achiev3
            $ persistent.achievement3 = True


    scene black with fade
    show text "[woman_name] se escapó del auditorio." at title with dissolve
    $ renpy.pause(2, hard=True)
    hide text

    $ renpy.end_replay()

    if not easymode:
        $ achVall = achValid

        "¡Hasta ahora has logrado [Achvall] de 3 logros disponibles!"
    else:
        "No recibió ningún logro porque está jugando en modo fácil."
    if itguy >= 1 and speedguy >= 1:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
    elif itguy >= 1 and speedguy == 0:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}"
    elif itguy == 0 and speedguy >= 1:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
    else:
        "Ventajas ganadas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}"

    jump episode2


label episode2:
    scene black with fade

    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 2" at title with dissolve
    $ renpy.pause(3, hard=True)
    stop music fadeout 1.0
    play music "music/Mshl.mp3"
    if easymode:
        show text "Puntos de modo fáciles!"
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        pause 1
        $lust += 2
        $domination += 2
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        pause 1
        hide text
    scene new200010 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Mientras caminaste a casa, a mitad de camino, viste a una chica en la distancia vestida con un atuendo bastante extraño."
    scene new200011 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Qué pasa con ella?{p}Parece un maldito jaguar o algo así..."
    scene new200012 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Es ella uno de esos promotores de seguros?Tal vez haya una nueva compañía con un nombre de animal o algo así."
    scene new200013 with dissolve
    "{color=#A8E4A0}{i}{size=-3}Siguiste caminando, actuando informal, pero tan pronto como te acercaste lo suficientemente cerca, ella prácticamente saltó hacia ti, ansiosa por hablar."
    h "¡Hi!Mi nombre es Sheila.{p}¿Te gustaría salvar un castor?"
    scene new20003 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Antes de responder, la escaneaste de la cabeza a los pies, notando su figura delgada pero curvilínea.Tenía pechos alegre pero pequeño, una cintura delgada y un culo redondeado y pequeño."
    e "Hm ... necesitaría más de un minuto con ese 'castor' entre tus piernas, cariño."
    scene new20004 with dissolve
    h "E-Excuse Me?"
    scene new20004a with dissolve
    e "Oh ... lo siento, ¿de qué se trata esto?"
    scene new20004 with dissolve
    h "Ejem ... bueno, eh, estoy con 'save the rivers', una pequeña organización recolectando donaciones y firmas para ayudar a salvar a los castores en la ciudad que están siendo desplazados debido a que las corporaciones arrojan contaminantes al río."
    scene new20004c with dissolve
    h "Es solo 50$ Eso puede salvar a la familia Beaver."
    scene new20004a with dissolve
    h "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Espero que esté de acuerdo ....{p}Esta es mi última oportunidad de salvar a estos pobres animales."
    e "Bien...{p}¿Pero no deberías estar vestido con algo relacionado con los castores?"
    scene new20004b with dissolve
    h "Uh... ¿Qué quieres decir?"
    e "Quiero decir, estás aquí tratando de salvar a los castores, pero estás vestido como uno de sus depredadores naturales."
    scene new20003b with dissolve
    h "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} No recuerdo lo que se suponía que debía responder a la pregunta sobre mi atuendo."
    scene new20003c with dissolve
    h "Oh ... uh ... bueno ..."
    e "Sigue adelante, estoy escuchando."
    scene new20003cc with dissolve
    h "Bien...{p}No sé, la compañía me hace usar esto. {p} Supongo que es atraer a más donantes."
    e "Ya veo ... deben estar desesperados por dinero, ¿eh?"
    scene new20003a with dissolve
    h "... Sí, podrías decir eso.{p}Parece que a nadie en esta ciudad se preocupa por los castores.No he recibido un solo dólar todo el día, y tengo que informar en una hora."
    scene new20004d with dissolve
    e "Entonces ... harías cualquier cosa para asegurarte de traer esos 50 dólares a tu pequeña compañía, ¿eh?"
    scene new20004 with dissolve
    h "...Yeah, la campaña casi ha terminado, y no estoy cumpliendo con las expectativas ... y tenemos un objetivo realmente ambicioso."
    scene new20004a with dissolve
    e "Vaya, estás realmente comprometido con Beavers, ¿eh?{p}¿Qué, es tu papá o algo así?"
    scene new20004e with dissolve
    h "Ja ja, muy divertida...{p}¿Sabías que cuando los castores construyen presas, ayudan a prevenir inundaciones y desbordamientos que amenazan a nuestra ciudad?"
    scene new20003aa with dissolve
    e "Uh ... pensé que era todo lo contrario."
    scene new20004f with dissolve
    h "No, y no solo eso, los castores son pequeñas criaturas lindas y adorables.No podría vivir en un mundo sin ellos."
    scene new20003aa with dissolve
    e "Pensé que podrías comerlos ..."
    scene new20004b with dissolve
    h "Bueno, sí...{p}Pero, ¿qué tipo de lunático haría eso?{p}¿Te comerías a tu perro?"
    e "No..."
    scene new20004g with dissolve
    h "¡Exactamente!Amo a Beavers, no solo porque son gorditos y lindos, sino por el papel que juegan en nuestro ecosistema.Pero sobre todo ....-"
    scene new20004c with dissolve
    h "..Los huelguistas son los ingenieros de la naturaleza, que crean presas y alojamientos complejos que remodelan los paisajes y crean hábitats vitales de humedales..."
    $ timeout_label = "beaver1"
    $ timeout = 1
    menu:
        "Ekhm...":
            jump beaver1
label beaver1:
    scene new20004h with dissolve
    h "Estos roedores laboriosos son especies clave, lo que significa que su presencia tiene un impacto desproporcionadamente grande en su entorno, beneficiando a innumerables otras plantas y animales. "
    $ timeout_label = "beaver2"
    $ timeout = 1
    menu:
        "Uhm...":
            jump beaver2
label beaver2:
    scene new20004 with dissolve
    h "Sus estanques y humedales actúan como filtros de agua naturales, mejorando la calidad del agua y ayudando a mitigar sequías e inundaciones."
    $ timeout_label = "beaver3"
    $ timeout = 1
    menu:
        "But...":
            jump beaver3
label beaver3:
    scene new20003a with dissolve
    h "Además, los hábitats de castores sirven como sumideros de carbono, jugando un papel crucial en la combinación del cambio climático al almacenar cantidades significativas de gases de efecto invernadero."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Oh Dios, ¿cuándo se va a callar? "
    scene new20004 with dissolve

    if easymode:
        menu:
            "Muy bien, cállate!Aquí está tu $50. Adiós. \n{color=#3d85c6} -50$ y sin escena" if money >= 50:
                $ money -= 50
                $ sheilahappy = True
                scene new20004e with dissolve
                h "Oh!...{p} Bueno, no esperaba esa reacción ...{p}Gracias!"
                e "Sí, sí ... lo que sea.De nada."
                scene new20003c with dissolve
                h "¿También le gustaría firmar aquí para elevar la petición de mi empresa al Honorable Ayuntamiento?"
                scene new20003aa with dissolve
                e "Supongo..."
                "{color=#A8E4A0}{i}{size=-3} Agarraste la pluma y firmaste la petición."
                e "Hecho."
                scene new20004f with dissolve
                h "T-gracias!{p}GoAdiós"
                "{color=#A8E4A0}{i}{size=-3} Sheila se apresuró desde que llegaba tarde para regresar a su compañía."
                jump eveningep2


            "No, estoy bien.A la mierda los Beavtles.Ni siquiera me gusta su música":

                scene new20004angry with dissolve
                h "Castores, no los beavtles"
                scene new20004listen with dissolve
                e "Oh ... sí, no.Tampoco me importan."
                scene new20004sad with dissolve
                h "B-pero!{p}Por favor!"
                scene new20004sad2 with dissolve
                e "No."
                scene new20004sad with dissolve
                h "¡Haré cualquier cosa!¡Por favor!¡No puedo volver con las manos vacías!"
                scene new20004sad2 with dissolve
                e "Espera ... ¿Acabas de decir algo?"
                scene new20003e with dissolve
                h "Sí..."
                scene new20004sad2 with dissolve
                e "Bueno ... sígueme.{p}Creo que podemos resolver algo..."
                scene new20004angry with dissolve
                h "¿Qué?Seguirte?¿¡A donde!?"
                scene new20004sad2 with dissolve
                e "Tal vez ... ese callejón allí mismo ...."
                scene new20004 with dissolve
                h "Uhm ...{p}¡Pero por qué!?{p}¿No puedes contarme sobre tu trato aquí?"
                scene new20004listen with dissolve
                e "Uh ... No. Es una especie de secreto.{p}No quiera que niñes no deseados se asoman."
                scene new20004c with dissolve
                h "... Está bien..."
                "{color=#A8E4A0}{i}{size=-3} SHeila te siguió al callejón a la mitad de la calle."
                jump alleysheila

            "Oye, ¿realmente quisiste decir algo ara ese dinero?":
                scene new20003e with dissolve
                h "Sí..."
                scene new20004sad2 with dissolve
                e "Estas segura"
                scene new20004b with dissolve
                h "¡Sí!Haría cualquier cosa por ellos ...."
                scene new20004sad2 with dissolve
                e "Bueno ... sígueme.{p}Creo que podemos resolver algo..."
                scene new20004angry with dissolve
                h "¿Qué?Seguirte?¿¡A donde!?"
                scene new20004sad2 with dissolve
                e "Quizás ... ese callejón allí mismo..."
                scene new20004 with dissolve
                h "Uhm...{p}¿¡Pero por qué!?{p}¿No puedes contarme sobre tu trato aquí?"
                scene new20004listen with dissolve
                e "Uh... No.Es una especie de secreto.{p}No quiero que las orejas no deseadas se asoman."
                scene new20004c with dissolve
                h "... Está bien..."
                "{color=#A8E4A0}{i}{size=-3} Sheila te siguió al callejón a la mitad de la calle."
                jump alleysheila

    else:
        menu:
            "Muy bien, cállate!Aquí está tu $50. Adiós." if money >= 50:
                $ money -= 50
                $ sheilahappy = True
                scene new20004e with dissolve
                h "Oh!...{p} Bueno, no esperaba esa reacción ...{p}Gracias!"
                e "Sí, sí ... lo que sea.De nada."
                scene new20003c with dissolve
                h "¿También le gustaría firmar aquí para elevar la petición de mi empresa al Honorable Ayuntamiento?"
                scene new20003aa with dissolve
                e "I guess..."
                "{color=#A8E4A0}{i}{size=-3} Agarraste la pluma y firmaste la petición."
                e "Hecho."
                scene new20004f with dissolve
                h "T-gracias!{p}Adiós!"
                "{color=#A8E4A0}{i}{size=-3} Sheila se apresuró desde que estaba llegando tarde para regresar a su compañía."
                jump eveningep2


            "No, estoy bien.A la mierda los Beavtles.Ni siquiera me gusta su música":

                scene new20004angry with dissolve
                h "Castores, no los beavtles"
                scene new20004listen with dissolve
                e "Oh ... sí, no.Tampoco me importan."
                scene new20004sad with dissolve
                h "B pero!{p}Por favor!"
                scene new20004sad2 with dissolve
                e "Nope."
                scene new20004sad with dissolve
                h "¡Haré cualquier cosa!¡Por favor!¡No puedo volver con las manos vacías!"
                scene new20004sad2 with dissolve
                e "Espera ... ¿Acabas de decir algo?"
                scene new20003e with dissolve
                h "Sí..."
                scene new20004sad2 with dissolve
                e "Bueno ... sígueme.{p}Creo que podemos resolver algo ..."
                scene new20004angry with dissolve
                h "¿Qué?Seguirte?¿¡A donde!?"
                scene new20004sad2 with dissolve
                e "Tal vez ... ese callejón allí mismo ...."
                scene new20004 with dissolve
                h "Uhm...{p}¿¡Pero por qué!?{p}¿No puedes contarme sobre tu trato aquí?"
                scene new20004listen with dissolve
                e "Uh... No. It's kind of secret.{p}Don't want any unwanted ears peeking."
                scene new20004c with dissolve
                h "... Alright..."
                "{color=#A8E4A0}{i}{size=-3} Sheila followed you into the alley halfway down the street."
                jump alleysheila

            "Oye, ¿realmente quisiste decir "algo" para ese dinero?":
                scene new20003e with dissolve
                h "Sí..."
                scene new20004sad2 with dissolve
                e "Estas segura"
                scene new20004b with dissolve
                h "¡Sí!Haría cualquier cosa por ellos..."
                scene new20004sad2 with dissolve
                e "Bueno ... sígueme.{p}Creo que podemos resolver algo ...."
                scene new20004angry with dissolve
                h "¿Qué?Seguirte?¿¡A donde!?"
                scene new20004sad2 with dissolve
                e "Quizás ... ese callejón allí mismo..."
                scene new20004 with dissolve
                h "Uhm...{p}Pero por qué!?{p}¿No puedes contarme sobre tu trato aquí?"
                scene new20004listen with dissolve
                e "Uh... No. Es una especie de secreto.{p}No quiero que las orejas no deseadas se asoman."
                scene new20004c with dissolve
                h "... Está bien..."
                "{color=#A8E4A0}{i}{size=-3} Sheila te siguió al callejón a la mitad de la calle."
                jump alleysheila

label alleysheila:
    scene black with fade
    pause
    scene new20005 with dissolve
    e "Mira, tengo una propuesta seria para ti..."
    scene alejka7 with dissolve
    h "Sí...{p}Dime..."
    scene alejka7a with dissolve
    e "Puedo ver que no quieres alejarte con las manos vacías..{p}Y no quiero ir a casa con mis bolas llenas ...."
    scene alejka6 with dissolve
    e "Si atrapas mi deriva..."
    scene alejka3 with dissolve
    h "Esperar...{p}Estas sugiriendo..."
    scene alejka2 with dissolve
    e "Vamos, me ayudas, te ayudo.{p}¿Qué dices?"
    scene alejka0 with dissolve
    h "¡Estás loco!"
    scene alejka1 with dissolve
    e "¡Oye, piensa en los pobres castores!Además, ninguno de estos idiotas en la ciudad te está dando dinero.Tal vez piensan que eres un estafador o algo así."
    scene alejka4 with dissolve
    h "...No soy un estafador ...."
    scene alejka0 with dissolve
    h "Beavers pobres en P, realmente necesitan nuestra ayuda ...{p}Mi ayuda..."
    scene alejka2 with dissolve
    e "Entonces ... ¿vas a desperdiciar esta oportunidad para ayudarlos?"
    scene alejka3 with dissolve
    h "... No..."
    scene alejka7a with dissolve
    e "¡Entonces vamos, anímate!Muéstrame esas tetas..."
    scene alejka6 with dissolve
    h "W-¿Quién?{p}N-¡De ninguna manera!"
    scene alejka7 with dissolve
    h "¡Pensé que te referías a otro tipo de trato!¿¡Qué demonios!?"
    scene alejka7 with dissolve
    e "¿Tienes otra opción?Está parpadeando tus tetas o dejando morir a los castores.{p}Tú decides"
    scene alejka4 with dissolve
    h "¡Eres un bastardo irreflexivo!"
    scene alejka5 with dissolve
    e "Y usted es una perra en quiebra que necesita 50 $ por una causa que a nadie fuera de su pequeña empresa le importa.Qué vergüenza.{p}Tetas o dejar.Ahora."
    scene alejka1 with dissolve
    h "Ugh..."
    scene new20006 with dissolve
    pause 0.5
    scene new20007 with dissolve
    pause 0.5
    scene new20008 with dissolve
    e "Mmm...{p}Tus pezones son difíciles ....{p}Parece que estás disfrutando de esto..."
    scene new20008a with dissolve
    h "Es todo para las castores ... Algo para ellas ... ¿De acuerdo?"
    scene new20008b with dissolve
    e "Entonces ... dale la vuelta y déjame ver ese culo primero ...."
    scene new20008c with dissolve
    h "¿H-huh!?Pensé que estábamos ... ¡HECHO!"
    scene new20008b with dissolve
    e "Nuestro trato era vaciar mis bolas.Todavía no están vacíos, y necesito una buena acumulación.Vamos."
    scene new20008d with dissolve
    h "...{p}A-Intra, pero hazlo rápido..."
    scene new20008e with dissolve
    h "Las vidas están en juego.."
    e "Sí, sí ... lo que digas..."
    scene new20009a with dissolve
    "{color=#A8E4A0}{i}{size=-3} Se dio la vuelta, y rápidamente aprovechaste la oportunidad para darle un buen aspecto a esas mejillas, mirándolas en toda su gloria."
    show sheillback with dissolve
    "{color=#A8E4A0}{i}{size=-3}Empacado redondo, delgado y apretado, eso es exactamente lo que eran."
    "{color=#A8E4A0}{i}{size=-3} Después de verlo completamente, sacaste tu polla palpitante, ya goteando al verla."
    e "Ahora date la vuelta.Me volarás."
    h "B-But..."
    e "Hazlo.Es parte del trato.O me chupas o me voy."
    h "... ¡Bueno!Guh ... joder."
    scene new20010 with dissolve
    pause
    scene new20011 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Sheila se dio la vuelta, arrodillándose frente a ti mientras apuntaba tu polla a sus labios."
    scene new20012 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Vacilante, pero renunció, abrió la boca, permitiendo tu polla adentro."
    scene new20013 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Presionaste tu polla contra sus labios y lo dejas entrar, mientras empezaste a pelarla como nada."
    show sheillbj with dissolve
    "{color=#A8E4A0}{i}{size=-3} Con ambas palmas sosteniendo la cabeza, comenzaste a empujar, sintiendo cómo se cerró los labios alrededor de tu polla, chupándola, sabiendo lo que estaba haciendo."
    e "Buena ... Sella tus labios alrededor de él, haz que valga la pena."
    h "Gu-uh!"
    "{color=#A8E4A0}{i}{size=-3} Ella asintió y comenzó a sellar los labios con fuerza sobre tu palpitante polla, aplicando presión, mientras te sacudiste la cabeza con las manos las manos."
    "{color=#A8E4A0}{i}{size=-3} Siguiste empujando las caderas rápidamente, ya que tus bolas golpean su barbilla repetidamente."
    e "Mmm...{p}Un buen tonto.¡Estoy a la nuez!"
    "{color=#A8E4A0}{i}{size=-3} La agarraste de las orejas de su traje, tal vez burlándose y afirmando tu dominio, empujando los últimos pulgadas más rápido."
    e "Ahora sabemos para qué fueron estos ... tengo que dar crédito a su jefe por este."
    h "Mpfh...Guh!"
    scene sheilcm1 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Mientras tus bolas seguían golpeando, y tu polla mantuvo empuje, finalmente, con un gemido bajo, te metiste en la boca, salpicaste la garganta y la boca entera con gruesas cuerdas de semen."
    scene sheilcm2 with vpunch
    pause
    scene sheilcm3 with vpunch
    pause
    scene sheilcm4 with dissolve
    $ maxmccumep7 += 1
    e "Mmm...{p}Tragarlo todo, estuche de canasta."
    scene sheilcm5 with dissolve
    pause
    scene sheilcm6 with dissolve
    "{color=#ffa500}{i}*gulp*"
    "{color=#A8E4A0}{i}{size=-3} Sheila amordazó pero logró tragarse la mayor parte."
    scene sheilcm7 with dissolve
    h "Gah... Uf ... lo hice ... por los castores ... cualquier cosa por ellas..."
    scene sheilcm9 with dissolve
    "{color=#A8E4A0}{i}{size=-3} Te enloqueciste, mirándola mientras luchaba por recuperar la compostura, todavía arrodillándose frente a ti, sus mejillas se sonrojaban."
    $ renpy.end_replay()
    if not easymode:
            $ achValid2 += 1
            $ achievement.grant("Achiev21")
            $ achievement.sync()
            if not persistent.achievement21:
                     show Achiev21 at achievment with easeintop:
                                zoom 0.5
                                rotate_animation

                     "¡Has recibido el logro!{p}{b}\"Todo es para los castores.\".{/b}"
                     "Número de logros obtenidos en este capítulo [achValid2]/4"
                     hide Achiev21
                     $ persistent.achievement21 = True

    show text "{font=LilitaOne.ttf}{color=#e0d71d}MONEY: [money]${/color}{/font}" at moneystat with dissolve
    menu:

        "Throw the money in her face {size=-6}{color=#e0d71d}50${/color}{/size}" if money >= 50:
            hide text
            $ sheiladominated = True
            scene sheilcm10 with dissolve
            e "Aquí está tu maldito dinero."
            scene sheilcm11 with dissolve
            pause
            scene sheilcm11a with dissolve
            scene sheilcm11b with dissolve
            scene sheilcm11c with dissolve
            scene sheilcm11d with dissolve
            scene sheilcm11e with dissolve
            scene sheilcm11f with dissolve
            scene sheilcm11g with dissolve
            pause
            scene sheilcm11h with dissolve
            pause
            scene sheilcm11i with dissolve
            $ money -= 50
            play sound "music/buyshop.mp3"
            show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
            pause 2
            hide text with dissolve
            "{color=#A8E4A0}{i}{size=-3} Agarraste los 50 $ y arrojaste las facturas arrugadas en la cara.Ella se estremeció, pero rápidamente se apresuró a recogerlos."
            scene sheilcm11j with dissolve
            pause
            scene sheilcm11k with dissolve
            pause
            scene sheilcm11l with dissolve
            h "Cuarenta...{p}Cincuenta..."
            scene sheilcm11m with dissolve
            h "R-Bien...{p}Gracias..."
            scene sheilcm11n with dissolve
            "{color=#A8E4A0}{i}{size=-3} Sin otra palabra, metió el efectivo en su bolso y se fue."
            scene sheilcm11o with dissolve
            pause
            scene black with Fade(2.0, 1.0, 2.0)
            pause
            jump eveningep2


        "Pagarla normalmente {size=-6}{color=#e0d71d}50${/color}{/size}" if money >= 50:
            hide text
            $ sheilahappysx = True
            scene sheilcm10 with dissolve
            e "Aquí están tus 50 $.Hiciste un trabajo bastante bien allí"
            $ money -= 50
            play sound "music/buyshop.mp3"
            show text "{font=LilitaOne.ttf}{color=#e0d71d}Total: [money]${/color}{/font}"
            pause 2
            hide text with dissolve
            scene sheilcm11 with dissolve
            "{color=#A8E4A0}{i}{size=-3} Le entregaste el dinero, y ella lo tomó con la mano temblorosa."
            scene sheilcm11l with dissolve
            pause
            scene sheilcm11m with dissolve
            h "T-gracias...{p}Realmente nos has ayudado hoy."
            e "Si, seguro."
            "{color=#A8E4A0}{i}{size=-3} Te giraste y te alejaste, dejándola para recogerse."
            scene black with Fade(2.0, 1.0, 2.0)
            pause
            jump eveningep2


        "Hacer trampa y vete":
            hide text
            $ sheilacheated = True
            scene sheilllast with dissolve
            e "Sí, sobre eso..."
            scene sheilllasta with dissolve
            e "No tengo dinero en efectivo."
            scene sheilllastb with dissolve
            h "¿Qué?!"
            e "Tengo que irme."
            scene sheilllastc with dissolve
            "{color=#A8E4A0}{i}{size=-3} Te encendiste el talón y te escapaste sin mirar hacia atrás, dejándola en el callejón, aturdido."
            scene sheilllastd with dissolve
            h "H-Hey! No puedes simplemente...{p}¡Regresar!"
            scene black with Fade(2.0, 1.0, 2.0)
            pause

            jump eveningep2

label eveningep2:
    stop music fadeout 1.0
    play music "music/Audio003.mp3"
    scene 00000prolog with fade
    pause
    scene 00000prologa with fade
    pause
    scene 00000prologb with fade
    pause
    scene 00000prologc with fade

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Cómo me metí en este desastre?..?"
    m "..."
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} No quiero enfrentar la respuesta a eso ahora.Pero necesito hablar con él..."

    scene 20000 with fade

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ugh, he estado sentado aquí durante horas, viendo esta basura..{p}¿Se va a quedarse escondida toda la noche?"

    scene 20000 with dissolve:
        xalign 0.8
        yalign 0.4
        zoom 2
        ease 2 zoom 4

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Tal vez ella está esperando que venga a visitarla ...."

    scene 20000aTo20000eAnimated with dissolve:
        xalign 0.8
        yalign 0.4
        zoom 4

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Pero supongo que probablemente no."

    scene 20000 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Ese es el sonido de la puerta de su habitación..."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Aquí ella viene."

    scene 20001 with dissolve

    m "*sigh*"

    m "[player_name]"

    m "Nosotras necesitamos hablar{p}Ahora."

    e "Claro que no estoy ocupada{p}¿De qué quieres hablar?"

    scene 20001a

    m "Apague el televisor."

    m "Necesitamos discutir ... lo que pasó."

    if easymode:
        menu:
            "{color=#FFD1DF}{i}*Apagar el televisor*{/i}{/color}":
                jump wylacztelewizor

            "{color=#FFD1DF}{i}*Deja el televisor encendido*{/i}{/color} \n{color=#3d85c6} +1 Point":
                if not easymode:
                    $ achValid2 += 1
                    $ achievement.grant("Achiev04")
                    $ achievement.sync()
                    if not persistent.achievement4:
                        show Achiev4 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                        "Has recibido un logro!{p}\"De ninguna manera!\"."
                        "Número de logros obtenidos en este capítulo [achValid2]/4"
                        hide Achiev4
                        $ persistent.achievement4 = True
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ domination += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                with dissolve
                jump wlaczony

    else:
        menu:
            "{color=#FFD1DF}{i}*Apagar el televisor*{/i}{/color}":
                jump wylacztelewizor

            "{color=#FFD1DF}{i}*Deja el televisor encendido*{/i}{/color}":
                if not easymode:
                    $ achValid2 += 1
                    $ achievement.grant("Achiev04")
                    $ achievement.sync()
                    if not persistent.achievement4:
                        show Achiev4 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                        "¡Has recibido un logro!{p}\"¡De ninguna manera!\"."
                        "Número de logros obtenidos en este capítulo [achValid2]/4"
                        hide Achiev4
                        $ persistent.achievement4 = True
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ domination += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                with dissolve
                jump wlaczony


label wlaczony:

    scene 20001

    e "Apagarlo?No me parece.{p}Estoy viendo mi programa y me estás interrumpiendo..."

    m "Esto es serio, [player_name].{p}Creo que lo que tenemos que discutir es más importante que algún programa estúpido.."

    scene 20001b

    m "¿Puedes apagarlo?{p}Por favor"

    scene 20001a
    e "{i}Suspiro{/i}...{p}Está bien."
    jump niechcibedzie

label wylacztelewizor:

    scene 20001b
    e "Seguro"

label niechcibedzie:

    scene 20001b

    pause

    scene 20001c

    e "Hecho"

    e "Entonces ... ¿Qué es tan importante que necesitaras hablar conmigo tan repentinamente?"

    scene 20002

    m "No finjas que no sabes de lo que estoy hablando, [player_name]."

    scene 20003

    m "Lo que me hiciste...{p}...fue horrible."

    m "Y ciertamente no voy a dejarlo pasar sin resolverlo."

    scene 20004 with dissolve

    e "¿Qué vas a hacer?"

    scene 20005 with dissolve

    m "Voy a decirle a tu padre todo.Una confesión completa."

    m "Y luego le diré lo que hiciste ... cómo te enteraste, y luego lo usaste para chantajearme, solo para cumplir tus fantasías enfermas."

    scene 20006 with dissolve

    e "Ja!{p}Ha-ha-ha!"

    e "[woman_name], En serio, no puedes esperar que creas que realmente te vas a decirle a papá todo sobre cómo lo engañas cada vez que está fuera."

    scene 20007a with dissolve

    e "No hay forma de que tire todo lo que tienes de él en este matrimonio ... ¿solo para que pueda castigarme?"

    scene 20007b with dissolve

    e "¿Ese era realmente tu plan?¿No sabes que me ama?¡Probablemente me recompensará por descubrir que eres una puta engaño y mentirosa!"

    e "¿Y por qué él creería tu historia sobre lo que supuestamente te hice?Tienes que admitir que suena loco ...."

    e "... ¿Por qué alguna mujer normal y respetuosa se permitiría ser tratada así?Para ir con una solicitud de favores sexuales de ella[player_role]? ¿Solo para ocultar su comportamiento de Slutty?"

    e "En serio, no hay forma de que te crea.De todos modos, no tienes pruebas ... {pPero yo sí...."

    e "Supongo que tendrás que probar un poco más."

    scene 20003

    m "Nosotras vivimos juntas."

    if chokeep1kick == True:
        m "Ni siquiera quiero saber qué habías planeado si no hubiera huido de la sala de conferencias"

    if episode1checkfinal == True:
        m "¿No puedes esperar que acepte así que será?¿Me chantajas para hacer esas cosas aborrecibles contigo?"

        m "Soy tu [woman_role], No está bien.Es ilegal, o al menos inmoral."

        m "Y no es solo que no esté permitido ....{p}También es asqueroso."


    scene 20007a

    e "¿Entonces crees que no puedo ser encantado por tu belleza?"

    scene 20003

    m "Simplemente está mal.No podemos tener ese tipo de interacción."

    m "Y estás actuando como si todo fuera algún tipo de broma."

    m "¡Que no es!Lo que hiciste es algo muy serio.Un crimen, incluso."

    scene 20005 with dissolve

    m "Lo que sea que hice mientras tu padre estaba fuera ... lo que me hiciste fue aún peor."

    scene 20007b with dissolve

    pause

    scene 20007a with dissolve

    e "Quizás tengas razón."

    e "Pero tal vez no."

    e "Creo que hacer trampa a la espalda de alguien es peor."

    e "Y sé que no es la primera vez."


    menu:
        "Hablemos de esto.Ven, siéntate a mi lado.":
            jump usiadz

        "Creo que solo eres una chica traviesa.":
            jump naughtygirl


label naughtygirl:

    scene 20005

    m "No me llames así."

    m "Sigo siendo tu [woman_role].{p}No tu compañera de clase."

    scene 20007a

    e "Cariño, está bien.{Cálmatewn."

    e "Solo siéntate, no tienes que pararte allí, avanzando sobre mí para toda la conversación."

    scene 20003

    m "Bueno.Pero no pienses que voy a dejar esto.Confiaré en ti por ahora.Solo mantén tus manos para ti mismo."

    e "Por supuesto que no ... solo siéntate.Por favor..."

    jump oksit


label usiadz:

    scene 20009a with dissolve

    scene 20010 with dissolve

    scene 20009a with dissolve

    scene 20010 with dissolve

    scene 20009a with dissolve

    e "Hablemos de ello."

    scene 20007a


    e "No te voy a morder."

    if domination > 4:
        jump oksit
    else:
        jump naughtygirl


label oksit:

    scene 20004 with dissolve

    m "Okay..."

    scene 20003 with dissolve

    m "Me sentaré.Voy a confiar en ti.Sin embargo, no te atrevas a hacer nada divertido."

    scene 20002 with dissolve

    pause

    scene 20002b with dissolve

    pause

    scene 20011a with dissolve

    e "{color=#ffa500}{i}sniff... sniff...{/i}"

    scene 20011 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Es eso...?{/i}"

    scene 20011b with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh sí{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Definitivamente huele a alcohol{/i}"

    scene 20011bb with dissolve

    m "Mirar.Lo que hiciste fue mal ... muy mal."
    m "Pero ... no quiero arruinar mi relación con tu padre..."
    m "Y ... si vamos a seguir viviendo juntos, no quiero tener que evitar siempre."

    if easymode:
        menu:

            "{color=#FFD1DF}{i}*Echa un vistazo a su cuerpo.*{/i} \n{color=#3d85c6} +1 Lust Point":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ lust += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump przyjrzyjsiecialu

            "{color=#FFD1DF}{i}*Mírala directamente a los ojos.*{/i} \n{color=#3d85c6} +1 Love point (Important in later episodes)":
                $ niclovebonusfactor += 1
                jump patrzjejwoczy

    else:
        menu:

            "{color=#FFD1DF}{i}*Echa un vistazo a su cuerpo.*{/i}":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ lust += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump przyjrzyjsiecialu

            "{color=#FFD1DF}{i}*Mírala directamente a los ojos.*{/i}":
                $ niclovebonusfactor += 1
                jump patrzjejwoczy


label przyjrzyjsiecialu:

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Maldición{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ella se ve tan bien{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Soy increíblemente afortunada de que mi [woman_role] es un bebé{/i}"

    scene 20011c

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i}Delgada como una adolescente{/i}"

    scene 20011d

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Y esas piernas...{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Siempre me ha encantado verla cuando usa pantalones cortos{/i}"

    "{color=#A8E4A0}{i}{size=-3}Ella notó que estabas mirando su cuerpo{/size}{/i}{/color}"

label patrzjejwoczy:

    scene 20011 with dissolve

    pause

    scene 20011a with dissolve

    e "Yo tampoco quiero."

    e "Realmente me gusta nuestra nueva relación."

    scene 20012b with dissolve

    m "Escucharme.{p}Nosotras no tenemos una "relación”."
    m "La mitad de mí todavía no puedo creerlo ... como si estuviera en estado de shock..."

    scene 20013 with dissolve

    m "Después de lo que pasó en la escuela."

    scene 20013a with dissolve

    pause

    scene 20013 with dissolve

    m "{color=#ffa500}{i}*respiración profunda*{/i}{/color}{p}Sé que te lastimaron con lo que viste."

    scene 20013a with dissolve

    m "Pero soy una mujer adulta."

    m "Y tengo derecho a ser feliz también."

    scene 20014atalk with dissolve

    m "Y como mujer..."

    scene 20014asilent with dissolve

    pause

    scene 20014atalk2 with dissolve

    m "Tengo mis necesidades."

    scene 20014atalk with dissolve

    m "Y tu padre prefiere el juego y beber más que pasar tiempo con su esposa.{p}Más que ... cuidarme."

    e "Quizás lo que estás diciendo es razonable.{p}Veo que podrías sentirte descuidada."

    e "¡Pero eso todavía no te da el derecho de engañarlo con algunos tipos al azar!"

    e "Si tienes “needs”..."

    if easymode:
        menu:
            "Todo lo que tenías que hacer era preguntarme.\n{color=#3d85c6} +1 Lust Point":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ lust += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump askme

            "Deberías haberlo tentado.\n{color=#3d85c6} +1 Dom Point":
                e "Tentarlo, de la misma manera que me tientas todos los días, usando esos pantalones cortos y blusas sueltas."
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ domination += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump everyday

    else:
        menu:
            "Todo lo que tenías que hacer era preguntarme.":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ lust += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump askme

            "Deberías haberlo tentado.":
                e "Lo tentó, de la misma manera que me tientas todos los días, vistiendo esos pantalones cortos apretados y blusas sueltas."
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ domination += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump everyday

label askme:

    scene 20014ashock with dissolve
    m "Qué?!{p}Tú?!"

    m "Tú eres mi [player_role]!{p}La persona más cercana a mí..."

    scene 20014atalk2 with dissolve

    m "¿Qué se suponía que debía pedirte??"

    scene 20014asilent with dissolve

    if easymode:
        menu:
            "Sé cómo lidiar con una mujer cachonda como tú. \n{color=#3d85c6} +1 Dom Point":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ domination +=1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump everyday

            "Imagina ... si no fueras mi [woman_role]... ¿Me follarías todos los días? \n{color=#3d85c6} +1 Lust Point":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ lust += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump everyday

            "Como alguien cercano a ti, puedes confiar en mí ... estoy seguro de que podría haber ayudado.\n{color=#3d85c6} +1 Love point (Important in later episodes)":
                $ niclovebonusfactor += 1
                jump closestperson
    else:
        menu:
            "Sé cómo lidiar con una mujer cachonda como tú.":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ domination +=1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump everyday

            "Imagina ... si no fueras mi [woman_role]... ¿Me follarías todos los días?":
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                pause 1
                $ lust += 1
                show image "images/Stats/Dom[domination].png" at statleft
                show image "images/Stats/Lust[lust].png" at statright
                with dissolve
                pause 3
                hide image "images/Stats/Dom[domination].png"
                hide image "images/Stats/Lust[lust].png"
                jump everyday

            "Como alguien cercano a ti, puedes confiar en mí ... Estoy seguro de que podría haber ayudado.":
                $ niclovebonusfactor += 1
                jump closestperson


label everyday:

    scene 20014ashock with dissolve

    m "whaaat....!!?!!"

    m "¿Qué demonios te pasa?!"

    scene 20014atalk2 with dissolve

    m "Sigues siendo una niña."

    m "Y toda esta conversación es incorrecta y debemos olvidarnos de lo que sucedió."
    jump closestperson

label closestperson:

    scene 20013a with dissolve

    m "Sé que es mi culpa."

    m "Sé que lo que viste te hizo estar enojado conmigo..{p}Y por eso me hiciste..."

    scene 20013 with dissolve

    m "...hacer esas cosas."

    scene 20013 with dissolve

    m "Pero...{p}te perdono."

    e "..."

    m "Podemos fingir que no pasó nada y volver a cómo estaban antes ....{p}viven normalmente juntos."
    m "Y prometo que haré lo correcto de tu padre de ahora en adelante ....{p}No te lastimaré de nuevo."

    scene 20014alisten with dissolve

    if easymode:
        menu:
            "Pero no quiero fingir que no pasó nada.\n{color=#3d85c6} +1 Love point (Importante en episodios posteriores)":
                $ niclovebonusfactor += 1
                jump beautiful

            "Me diste una paja.Quiero más. {size=-8}(Req. Episode 1 Final Scene){/size}" if nicep1dom > 7:
                jump evil

    else:
        menu:
            "Pero no quiero fingir que no pasó nada.":
                $ niclovebonusfactor += 1
                jump beautiful

            "Me diste una paja.Quiero más. {size=-8}(Req. Episode 1 Final Scene){/size}" if nicep1dom > 7:
                jump evil

label beautiful:

    scene 20014alook with dissolve

    e "Eres la mujer más bonita que conozco."

    e "Incluso solo sentado aquí ahora mismo, a tu lado ... si soy sincero, no puedo negar que me estás poniendo extremadamente cachondo."

    scene 20014atalk with dissolve

    m "No me digas cosas así, [player_name]."

    m "Eres mucho más joven que yo. Debes buscar una pareja sexual que esté más cerca de tu propia edad.."

    scene 20014ashock with dissolve

    e "Prefiero un socio con experiencia."

    jump talkbeforehj

label evil:

    scene 20014alook with dissolve

    e "De hecho, [woman_name], Me gusta que seas tan adicta al sexo."

    scene 20014atalk with dissolve

    e "Porque soy la misma...{p}Pienso todo el tiempo...{p}acerca de ti."
    e "Tal vez, juntos, podemos encontrar una manera de controlar nuestros deseos..{p}y evitar cometer más errores con los extraños."

    scene 20014alook with dissolve

    e "Podríamos ser buenos el uno para el otro."

    jump talkbeforehj

label talkbeforehj:

    scene 20014atalk2 with dissolve

    m "¿Puedes parar?"

    m "¿No entiendes que todo lo que dices es ... incorrecto?"

    scene 20014asilent with dissolve

    pause

    scene 20013 with dissolve

    m "¡Lo que sucedió en la universidad estaba mal!Nunca debería haber permitido que se intensifique así..{p}Pero estaba en estado de shock, creo."

    scene 20013a with dissolve

    m "Todo pasó tan rápido."

    scene 20014alook with dissolve

    e "¡No!No fue “wrong”...Fue maravilloso."

    e "No fue hasta ese momento que me di cuenta de cuánto me preocupo por ti."

    e "Y cuánto quiero sentirme cerca de ti así de nuevo."

    "{color=#ffa500}{i}*clothes rustling*"


label pantsdown:

    scene 20015shock with dissolve

    m "HEY!"

    scene 20015 with dissolve

    m "[player_name]! ¿Qué estás haciendo?!"

    m "¡Detente esto!¡Guarda esa cosa!"

    scene 20021a with dissolve

    e "Nah..."

    scene 20021a with dissolve

    e "Estoy cansada de solo hablar."

    scene 20022b with dissolve

    e "¿Sabes que?"

    scene 20022b with dissolve

    e "Quiero más."

    scene 20023 with dissolve
    if nicep1dom > 7:
        e "Lo hiciste por mí una vez, ahora puedes hacerlo de nuevo."
    else:
        jump nohandj2
label nohandj2:
    scene 20023a with dissolve

    m "No hagas esto.Por favor, vuelva a colocar los pantalones."

    scene 20015 with dissolve

    m "Yo ... No quiero hacer nada por el estilo ... contigo."

    scene 20015a with dissolve

    "{color=#A8E4A0}{i}{size=-3}Ella sigue mirando tu pene{/i}"

    scene 20015 with dissolve

    m "Solo quería hablar ...."

    scene 20015a with dissolve

    e "Nosotras podemos hablar un poco más ... {p}Cuando hayas terminado conmigo."

    e "¿Por qué no te acercas más?."

    scene 20023 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} El alcohol debe estar afectándola, de lo contrario ella ciertamente se habría escapado..."

    e "Vamos, no es nada."

    e "No hay nadie más aquí ... nadie lo sabrá ...."

    e "Esta será la última vez, y luego eliminaré las fotos."

    scene 20015a with dissolve

    e "Vamos.Prometo."

    scene 20015 with dissolve

    m "..."

    m "Elimine las imágenes primero."

    scene 20015a with dissolve

    e "¿Crees que soy estúpida?"

    e "Sé cómo funciona eso.Una vez que se hayan ido, me dejarás aquí, frustrado."

    e "Vamos, date prisa ... o podría comenzar a tener otras ideas sobre qué hacer con las fotos."

    scene 20023 with dissolve

    pause

    scene 20023a with dissolve

    m "*sigh* Solo tengo que confiar en ti.Para hacer lo correcto."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Creo que ella dijo eso hoy."

    scene 20023bb with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} En realidad lo hará ... definitivamente está borracha."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i}Soy super afortunada"

    scene 20023bbb with dissolve

    e "Vamos [woman_role]"

    scene 20023b with dissolve

    "{color=#A8E4A0}{i}{size=-3}Ella se detuvo, congelada, solo miraba fijamente tu polla.{/i}"

    scene 20023bbbb with dissolve

    m "No...{p}want...{p}para hacerlo."

    menu:
        "Por favor, solo ayúdame ...":
            scene 20023bbbbb with dissolve
            m "Bueno...{p}Pero por favor, cierra los ojos ... y no digas nada."
            jump s2h1on

        "Vamos, solo tómalo en tu mano.":
            scene 20023bbbbb with dissolve
            m "*gasp*!"
            jump s2h1on



label s2h1on:
    show s2h1 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ella realmente lo está haciendo ....{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Pensé que sería más difícil convencerla...{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i}Tengo que permanecer en control ... no puedo joderlo ahora.{/i}"

label menufirsthj:

    pause
    show screen hint("Debería seguir presionando...\nElla podría romper.")
    if easymode:
        menu:
            "Eres tan bueno en esto ... más rápido, por favor \n{color=#3d85c6} Hazlo 3x por puntos":
                hide screen hint
                $ everydayhjq += 1
                jump everydayhj

            "{color=#FFD1DF}{i}*Obligarla a chuparte*{/i}{/color} \n{color=#3d85c6} Camino final":
                hide screen hint
                jump beforeforceblow

            "Admítelo, te gustan las pollas jóvenes, [woman_role]\n{color=#3d85c6} Hazlo 3x por puntos":
                hide screen hint
                $ hjquestion +=1
                jump sheverygood

            "{color=#FFD1DF}{i}*Toca su coño*{/i}{/color} {size=-8}(Req. 2 Lust and 1 Domination)":
                hide screen hint
                if lust > 5 and domination > 4:
                    jump touchpussy
                else:
                    jump beforeforceblow
    else:
        menu:
            "Eres tan bueno en esto ... más rápido, por favor":
                hide screen hint
                $ everydayhjq += 1
                jump everydayhj

            "{color=#FFD1DF}{i}*Obligarla a chuparte*{/i}{/color}":
                hide screen hint
                jump beforeforceblow

            "Admítelo, te gustan las pollas jóvenes, [woman_role]":
                hide screen hint
                $ hjquestion +=1
                jump sheverygood

            "{color=#FFD1DF}{i}*Toca su coño*{/i}{/color} {size=-8}(Req. 2 Lust and 1 Domination)":
                hide screen hint
                if lust > 5 and domination > 4:
                    jump touchpussy
                else:
                    jump beforeforceblow

label beforeforceblow:

    $ beforeforce +=1
    if beforeforce == 1:
        "{color=#A8E4A0}{i}{size=-3} Ella hizo un extraño sonido de pánico.{/i}"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Hmm, debería tener cuidado...{/i}"
        jump menufirsthj

    elif beforeforce == 2:
        "{color=#A8E4A0}{i}{size=-3} Ella comienza a irritar.{/i}"
        e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Debería probar algo más o la asustaré.{/i}"
        jump menufirsthj

    elif beforeforce == 3:
        jump forceblow

label everydayhj:

    if everydayhjq == 1:
        "{color=#A8E4A0}{i}{size=-3} Ella no respondió, distraída por lo que estaba haciendo.{/i}"
        jump menufirsthj

    if everydayhjq == 2:
        scene 20024
        m "Tranquilizarse....{p}Te dije que no dijeras nada."
        show s2h1
        jump menufirsthj

    if everydayhjq == 3:
        show s2h2 with dissolve
        "{color=#A8E4A0}{i}{size=-3} Ella bajó la cabeza ligeramente y no respondió ...{p}... Pero comenzó a trabajar más rápido con su mano!{/i}"
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        pause 1
        $ domination += 1
        $ lust += 1
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[domination].png"
        hide image "images/Stats/Lust[lust].png"

        if secondAchievDone == 0 and hjquestion > 1:
            $ secondAchievDone += 1
            if not easymode:
                $ achValid2 += 1
                $ achievement.grant("Achiev05")
                $ achievement.sync()
                if not persistent.achievement5:
                    show Achiev5 at achievment with easeintop:
                        zoom 0.5
                        rotate_animation

                    "¡Has recibido un logro!{p}\"Puntaje de puntos máximos durante una paja.\""
                    "Número de logros obtenidos en este capítulo [achValid2]/4"
                    hide Achiev5
                    $ persistent.achievement5 = True
            jump menufirsthj
        else:
            jump menufirsthj

    if everydayhjq > 3:
        "{color=#A8E4A0}{i}{size=-3} Ella no respondió, pero siguió tratando de complacerte.{/i}"
        jump menufirsthj

label sheverygood:
    if hjquestion == 1:
        m "Justo... No.{p}No me hables así."
        jump menufirsthj

    if hjquestion == 2:
        m "{i}*susurrando suavemente*{/i} N... No...."
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        pause 1
        $ lust += 1
        $ domination += 1
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        with dissolve
        pause 3
        hide image "images/Stats/Dom[domination].png"
        hide image "images/Stats/Lust[lust].png"

        if secondAchievDone == 0 and everydayhjq > 2:
            $ secondAchievDone += 1
            if not easymode:
                $ achValid2 += 1
                $ achievement.grant("Achiev05")
                $ achievement.sync()
                if not persistent.achievement5:
                    show Achiev5 at achievment with easeintop:
                        zoom 0.5
                        rotate_animation

                    "¡Has recibido un logro!{p}\"Puntaje de puntos máximos durante una paja.\""
                    "Número de logros obtenidos en este capítulo [achValid2]/4"
                    hide Achiev5
                    $ persistent.achievement5 = True

            jump menufirsthj
        else:
            jump menufirsthj

    if hjquestion > 2:
        "{color=#A8E4A0}{i}{size=-3} Ella no respondió, pero siguió trabajando para complacerte con la mano.{/i}"
        jump menufirsthj

label touchpussy:
    hide screen hint

    scene 20030x

    pause

    scene 20031x

    m "Qué...?"

    scene 20032x with dissolve

    m "Oye ... pare..."

    show s2touchfirst with dissolve

    m "No... ahhh!"

    m "... no debes ...."

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Oh Dios ... ella ya está mojada...{/i}"

    pause

    show hjfingerv1 with dissolve

    "{color=#A8E4A0}{i}{size=-3}Ella gime suavemente{/i}"

    m "YNo puedes..."

    "{color=#A8E4A0}{i}{size=-3} Sus caderas se mueven involuntariamente, frotando su coño contra tus dedos."

    m "{color=#ffa500}{i}*Moans*"

    e "Oh sí ... eso es tan bueno ...."

    m "..."

    e "Hazlo más rápido [woman_role]..."

    show hjfingerv2 with dissolve

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ella está haciendo lo que digo ahora ....{/i}"

    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ver cómo está claramente borracha ... tal vez intentaré llevar las cosas más allá...{/i}"

    scene s20035 with dissolve

    pause

    scene s20036 with dissolve

    e "Chupar!"

    show s2bj
    $ renpy.pause(3, hard=True)

    scene s20035 with dissolve

    "{color=#A8E4A0}{i}{size=-3} Se detuvo de inmediato cuando se dio cuenta de lo que pasó"
    $ renpy.end_replay()

label forceblow:

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

    m "¿Qué diablos estás haciendo?!"

    scene 20051 with dissolve

    m "No soy una puta que puedas insultar y perder el tiempo ... ¡y no estoy haciendo esto!"

    scene 20052 with dissolve

    m "¡Lo que acabas de intentar hacer se llama violación!"

    scene 20053 with dissolve

    m "No me importa a dónde vayas ...{p}Pero mañana tienes que salir de esta casa."

    scene 20054 with dissolve

    if easymode:
        menu:
            "Déjala ir \n{color=#3d85c6} +1 Punto de amor pero sin escena (importante en episodios posteriores)":
                    $ niclovebonusfactor += 1
                    $ renpy.end_replay()
                    jump endingfail

            "{color=#FFD1DF}{i}*Obligarla a chuparte*{/i}{/color} {size=-8} \n(Req.3 lujuria y 3 dominación) or {color=#00ff00}20\%\ chance{/color}":
                    if lust > 6 and domination > 6:
                        jump bjFinal
                    else:
                        jump endinge1chance
    else:
        menu:
            "Let her go":
                    $ niclovebonusfactor += 1
                    $ renpy.end_replay()
                    jump endingfail

            "{color=#FFD1DF}{i}*Obligarla a chuparte*{/i}{/color} {size=-8} \n(Req.3 lujuria y 3 dominación) or {color=#00ff00}20\%\ chance{/color}":
                    if lust > 6 and domination > 6:
                        jump bjFinal
                    else:
                        jump endinge1chance

label endinge1chance:

    $ endinge1chanceint = renpy.random.randint(1, 100)
    if endinge1chanceint >= 80:
        show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        jump bjFinal
    else:
        show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        jump endingfail

label bjFinal:

    scene 20055
    stop music fadeout 1.0
    play music "music/Mnicdk.mp3"
    $ renpy.pause(2, hard=True)

    if not easymode:
        $ achValid2 += 1
        $ achievement.grant("Achiev06")
        $ achievement.sync()
        if not persistent.achievement6:
            show Achiev6 at achievment with easeintop:
                zoom 0.5
                rotate_animation
            "Has recibido un logro!{p}\"¿Quién es la jefa? Desbloqueaste la escena final..\""
            "Número de logros obtenidos en este capítulo [achValid2]/4"
            hide Achiev6
            $ persistent.achievement6 = True
    pause

    "{color=#A8E4A0}{i}{size=-3}Justo cuando ella comenzó a alejarse, te agarras de la muñeca."

    scene 20057 with dissolve

    e "Parece que no entiendes..."

    scene 20056a with dissolve

    e "... Esa eres mi puta ahora."

    scene 20058 with dissolve
    scene 20059 with dissolve
    scene 20060 with dissolve
    scene 20060a with dissolve
    scene 20060b with dissolve
    scene 20061 with dissolve
    scene 20062 with dissolve

    e "¿Y sabes lo que hacen las putas?"

    scene 20063 with dissolve

    e "Chupan la polla."

    show bj68v1 with dissolve

    e "Solo así."

    m "MMM!!!"

    show bj68v2 with dissolve
    e "Oh ... eso es asombroso ..."

    m "{color=#ffa500}{i}*Ella hace sonidos extraños como si quisiera decir algo*"

    e "Sí ... eso es muy bueno..."

    e "Pero quiero que vayas más rápido."

    "{color=#A8E4A0}{i}{size=-3}La obligas a moverse más rápido"

    show bj68v3 with dissolve

    e "Oohhhh.."

    pause

    e "{color=#ffa500}{i}*groans*{/i}{/color} Tan buena"

    "{color=#A8E4A0}{i}{size=-3}Empujaste sus manos lejos de ti y colocaste tu mano en la parte posterior de su cabeza"

    show bj69v4 with dissolve

    e "Tu boca es increíble."

    pause

    e "Eres la mejor [woman_role] alguna vez."

    e "Si hubiera sabido que sería tan bueno, lo habrías chupado por mí hace mucho tiempo."

    show bj69v5 with dissolve

    pause

    e "Me encanta la sensación de tus labios y lengua..."

    e "Sí ... así como eso..."

    e "Lo sabía ... realmente eres una verdadera puta."

    "{color=#A8E4A0}{i}{size=-3}Ella no puede decir nada, pero la escuchas tratando de gemir.{/i}"

    show bj70 with dissolve

    e "{color=#ffa500}{i}*gimazos*{/i}{/color} Me vas a hacer venir pronto..."

    e "¡Justo en tu boca!"

    "{color=#A8E4A0}{i}{size=-3}Ella comenzó a luchar en pánico."

    scene 20070 with vpunch

    e "AGHHH!!!"

    scene 20070a with vpunch

    scene 20070a with vpunch

    e "Oh GOD DAAAAAAAAMN!!!"

    scene 20070b with vpunch

    scene 20070b with vpunch

    scene 20070b with vpunch
    $ maxmccumep7 += 1
    e "*panting* ¡Tómalo!Tomar todo, [woman_role]!!"

    scene 20070c with vpunch

    scene 20070c with vpunch

    e "Ahhhhhh...."

    scene 20070d with dissolve

    e "..."

    scene 20070e with dissolve

    e "Eso fue tan bueno..."

    "{color=#A8E4A0}{i}{size=-3}Ella está en silencio ... pero puedes ver que está en shock total."

    scene 20071a with dissolve

    m "{color=#ffa500}{i}*Respira mucho{/i}"

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

    m "No puedo creer ....{p}Me hiciste esto..."
    $ endingep2full = True
    scene 20073g with dissolve

    if easymode:
        menu (screen="rightchoice"):
            "Gracias, Fue un verdadero placer correrse en tu boca":
                jump nicelips

            "{color=#FFD1DF}{i}*Permanecer silenciosa*{/i}{/color}":
                jump silent

            "Creo que acabo de hacer el amor en tu boca.":
                jump calledface

            "Lo siento mucho...No pude resistirme.st...\n{color=#3d85c6} +1 Love point (Importante en episodios posteriores)":
                $ niclovebonusfactor += 1
                jump couldntep2resist

    else:
        menu (screen="rightchoice"):
            "Gracias, Fue un verdadero placer correrse en tu boca":
                jump nicelips

            "{color=#FFD1DF}{i}*Permanecer silenciosa*{/i}{/color}":
                jump silent

            "Creo que acabo de hacer el amor en tu boca.":
                jump calledface

            "Lo siento mucho...{p}No pude resistir...":
                $ niclovebonusfactor += 1
                jump couldntep2resist

label couldntep2resist:

    scene 20073i with dissolve
    m "Lo siento?..."
    scene 20073h with dissolve
    m "..."

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

    "{color=#A8E4A0}{i}{size=-3}Ella se escapó a su habitación."
    jump endings2

label nicelips:

    scene 20073i with dissolve

    m "¿Cómo podrías hacer esto ... soy tu [woman_role]..."

    scene 20073h with dissolve

    e "No me importa eso.Tendrás que empezar a acostumbrarte."

    e "Es decir, si no quieres que mi papá conozca tu secreto."

    scene 20073i with dissolve

    m "Estas enferma, [player_name]...¡Estás mentalmente enfermo!"

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

    "{color=#A8E4A0}{i}{size=-3}Ella se escapó a su habitación."
    jump endings2

label silent:

    scene 20073h with dissolve

    m "..."

    e "..."

    scene 20073i with dissolve
    m "¿No vas a decir algo??"
    scene 20073h with dissolve
    e "..."
    scene 20073i with dissolve
    m "Cualquier cosa?"

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

    "{color=#A8E4A0}{i}{size=-3}Ella se escapó a su habitación."
    jump endings2


label calledface:

    scene 20073i with dissolve

    m "No, no estaba haciendo el amor.{p}Me obligaste..."

    scene 20073h with dissolve

    e "Naaah, diría que es más como ... un trato."

    e "Un trato ... donde me mantendré en silencio ...{p}Y podrás seguir fingiendo que no estás traicionando a mi padre."

    m "..."

    e "Y también te quedarás callado ...{p}Pero eso es principalmente porque tu boca estará llena, ¡jaja!"

    scene 20073i with dissolve

    m "Eres un niño enfermo, sucio y sucio."

    scene 20073h with dissolve

    e "Y eres una puta que es un increíble tonto de polla.{p}Creo que hacemos una gran pareja."

    e "Y si otros pueden usar la boca, yo también quiero usarla."

    e "Porque después de lo que hiciste hoy, sé lo bien que se siente...{p}y me encanta."

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

    "{color=#A8E4A0}{i}{size=-3}Ella se escapó a su habitación."
    jump endings2


label endings2:

    scene black with fade

    $ renpy.end_replay()

    $ achVall = achValid + achValid2
    if not easymode:
        "Hasta ahora has logrado [achVall] ¡De los 7 logros disponibles!"
    else:
        "No recibió ningún logro porque está jugando en modo fácil."
    if itguy >= 1 and speedguy >= 1:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
    elif itguy >= 1 and speedguy == 0:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#5ed42f}{b}ITGUY{/b}{/color}"
    elif itguy == 0 and speedguy >= 1:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}, {color=#cb2fd6}{b}SPEED{/b}{/color}"
    else:
        "Ventajas aprendidas: 1/1{p}{color=#2f63d4}{b}PERCEPTION{/b}{/color}"

    jump episode3

label endingfail:

    scene 20054a with dissolve

    e "Mierda"
    e "Ella se fue"
    e "Podría haberlo jugado de manera diferente..."
    e "Pero mañana también es un día"
    jump endings2


label episode3:
    if easymode:
        show text "Puntos de modo fáciles!"
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        pause 1
        $lust += 2
        $domination += 2
        show image "images/Stats/Dom[domination].png" at statleft
        show image "images/Stats/Lust[lust].png" at statright
        pause 1
        hide text

    show logo
    $ renpy.pause(3, hard=True)
    show text "Episode 3" at title with dissolve
    $ renpy.pause(2, hard=True)
    stop music fadeout 1.0
    play music "music/Mda.wav"
    scene 30001 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Bueno ... seguro que fue un buen día."
    scene 30002 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Por supuesto, tengo curiosidad por saber qué hay en mi [woman_role]'s mente ahora mismo ... {p}Probablemente sintiéndose terrible."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Pero es totalmente su culpa, no la mía."
    scene 30003 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} ¿Huh? {p} es eso ...?"
    scene 30003drzwi with dissolve
    "{color=#ffa500}{i}*Desbloqueos de la puerta delantera"
    scene 30003opendoor with dissolve
    d "Hey hey hey!"
    d "¡Adivina quién ha vuelto, amigas!"
    scene 30004 with dissolve
    e "¿Papá?¡Estás de vuelta!"
    scene 30004dad with dissolve
    d "¡Sí, chico!Estoy aquí ahora.{p}Sin embargo, solo volví por un día."

    d "Cancelaron una de mis reuniones y decidí pasar para ver cómo estabas."

    d "Es [woman_name] hogar?"
    scene 30004 with dissolve
    e "Sí, probablemente durmiendo en su habitación.Es sábado, después de todo."
    scene 30005 with dissolve
    d "Tengo que bañarme.Soy todo muy recién del viaje."

    d "Y también ....[player_name]...{p}Quiero hablar contigo más tarde, pero no aquí y no ahora."
    scene 30006 with dissolve
    d "¿Quizás deberíamos salir por algo para comer más tarde, tal vez?"
    scene 30007 with dissolve
    d "Ya sabes, un unión casual de padre-hijo juntos."
    scene 30004 with dissolve
    e "Claro, no tengo nada más que hacer de todos modos."
    scene 30005 with dissolve
    d "Genial, luego haz lo que quieras por un tiempo."
    scene 30001 with dissolve
    "{color=#ffa500}{i}*una voz del corredor{i}"
    scene 30003 with dissolve
    "{color=#ffa500}{i}*un llamado tranquilo en la puerta{i}"

    d "Uhm... [woman_name]?"

    d "Las puertas están cerradas.."
    scene 30002 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Por supuesto que están cerradas.. {p}Las revisé por la noche.{/i}"
    scene 30008 with dissolve
    d "[player_name] ¿Sabes por qué la puerta del dormitorio está cerrada?{p}Es tu [woman_role] ¿Cerrándote a ti?"
    scene 30003 with dissolve
    e "¿Está cerrado?No sé.Tendrás que preguntarle."
    scene 30005 with dissolve
    d "Extraña..."

    d "Tomaré un baño rápido y podemos ir de inmediato.¿Qué dices?"
    scene 30003 with dissolve
    e "Seguro"

    scene black with fade
    show text "Local Restaurant" at title with dissolve
    $ renpy.pause(2, hard=True)
    scene 30011b with dissolve
    d "Extrañaba venir a este lugar."

    d "Como en las barras de la carretera todo el tiempo, y todo lo que sirven saben a mierda."
    scene 30010 with dissolve
    e "Supuse eso: la comida apesta tanto que te estás perdiendo la basura que sirven aquí."
    scene 30011a with dissolve
    d "Muy bien, vamos al grano.¿Sabes por qué te traje aquí, lejos de [woman_role]?"


    if easymode:

        menu:
            "¿Porque te apeteciste?":
                jump dadrestaurant

            "Porque estás durmiendo con mi [woman_role]?\n{color=#3d85c6} Dad +1":
                $ dadfriend += 1
                jump dadjokes

            "¿Porque eres súper genial papá?":
                jump dadrestaurant
    else:

        menu:
            "Because you felt like it?":
                jump dadrestaurant

            "Because you're sleeping with my [woman_role]?":
                $ dadfriend += 1
                jump dadjokes

            "Because you are super cool dad?":
                jump dadrestaurant


label dadrestaurant:
    scene 30011b with dissolve
    d "Of course!"
    d "But actually it's for a different reason."
    jump dadtalk

label dadjokes:
    scene 30011c with dissolve
    d "Hehe"
    scene 30011d with dissolve
    d "This is my favorite dad joke."

    d "You learn very quickly."
    scene 30011b with dissolve
    d "But actually it's for a different reason."
    jump dadtalk

label dadtalk:

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
    d "Alright, but don’t get me twisted: I’m putting you against your [woman_role].{p}You are the only person I trust who can help me out in this."
    d "And I still hope that I am wrong in my doubts."
    scene 30010 with dissolve
    e "Sure thing, Dad. Buddies for life, right?"
    scene 30011d with dissolve
    d "Buddies for life."
    d "Oh, I think our food is on its way."

    scene black with fade
    stop music fadeout 1.0
    play music "music/Mnicdk.mp3"
    show text "Meantime" at title with dissolve
    $ renpy.pause(2, hard=True)
    show text "[player_name]'s house'" at title2 with dissolve
    $ renpy.pause(2, hard=True)
    hide text
    show shower
    m "..."

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What am I supposed to do?{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} [player_name] is acting up.{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Is it because of me?{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Was it because he saw me... cucking his dad...?{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} John is back and I’ve got to act like nothing happened?{i}"

    m "..."

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What should I do?{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I can't even talk to [player_name] because he's acting like he's off the leash.{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} But... Nothing will happen as long as John is at home{p}Maybe it's a good time to talk about it with [player_name].{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I can't imagine continuing to live with him under this roof.{i}"

    if endingep2full == True:
        scene black with fade
        pause
        show bjretro
        m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He was all dommy and… masculine...{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} All the things he said..."

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} He treated me like a....{p}whore?{i}"
    scene 30020 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You have to be strong, [woman_name].{p}You cannot allow your [player_role] to treat you like this...{i}"

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} You are still his [woman_role], for god’s sake!{i}"

    scene 30021 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What if...."

    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I will use his own weapon against him..."
    scene 30022 with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} This might work."

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

menu:
        "{color=#FFD1DF}{i}*Push the door*{/i}{/color}":
            jump pushthedoorep3

        "{color=#FFD1DF}{i}*Stay hidden*{/i}{/color}":
            $ hiddendoor += 1
            jump stayhiddenep3


label stayhiddenep3:

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

    jump movieevening

label pushthedoorep3:

    scene 30029a with dissolve
    m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Ah, here it is.{i}"
    scene 30029b with dissolve
    pause 1
    scene 30029c with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} What would a polite serial killer say at a moment like this??"

    $ serialkiller = renpy.input("What should I say to my [woman_role]? \n{i}(Press Enter if you don't want to say anything or write something else){/i}", )
    $ serialkiller = serialkiller.strip() or "..."

    scene 30029ca with dissolve
    pause 1
    scene 30029cb with dissolve
    pause 1
    scene 30029cc with dissolve
    pause 1
    scene 30029cd with dissolve
    e "[serialkiller]"

    if serialkiller.upper().find("HELLO") != -1 or serialkiller.upper().find("GOOD MORNING") != -1 or serialkiller.upper().find("GOOD AFTERNOON") != -1:
            scene 30029dbonus with dissolve
            $ nicoledominance += 1
            show image "images/Stats/Dom[nicoledominance].png" at statleft
            with dissolve
            pause 3
            hide image "images/Stats/Dom[nicoledominance].png"
            with dissolve
            m "[player_name]?!!?"

            if not easymode:
                $ achValid3 += 1
                $ achievement.grant("Achiev07")
                $ achievement.sync()
                if not persistent.achievement7:
                    show Achiev7 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                    "You have received the achievement!{p}\"You are well-mannered!\"."
                    "Number of achievements earned in this chapter [achValid3]/4"
                    hide Achiev7
                    $ persistent.achievement7 = True

    elif serialkiller.upper().find("SUCK") != -1 or serialkiller.upper().find("FUCK") != -1 or serialkiller.upper().find("LICK") != -1:
            $ nicoledominance += 1
            show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
            pause 3
            hide image "images/Stats/Dom[nicoledominance].png" with dissolve
            scene 30029d with dissolve
            m "[player_name]?!!?"

    else:

            scene 30029d with dissolve
            m "[player_name]?!!?"

    scene 30030a with dissolve

    m "What are you doing here?!"

    scene 30030b with dissolve

    m "Leave my room immediately!"

label crouchingtiger:
menu:
        "{color=#FFD1DF}{i}*Grab a towel":
            $ nicoledominance += 1
            show image "images/Stats/Dom[nicoledominance].png" at statleft
            with dissolve
            pause 3
            hide image "images/Stats/Dom[nicoledominance].png"
            with dissolve
            jump grabatowel
        "{color=#FFD1DF}{i}*Push her onto the bed":
            $ nicoledominance += 1
            show image "images/Stats/Dom[nicoledominance].png" at statleft
            with dissolve
            pause 3
            hide image "images/Stats/Dom[nicoledominance].png"
            with dissolve
            jump pushherbed

label pushherbed:


    $ pushherbedcheck += 1
    scene 30031aa with dissolve
    pause 0.5
    scene 30031ab with dissolve
    pause 0.5
    scene 30031ac with dissolve
    pause 0.5
    scene 30031ad with dissolve
    pause 0.5
    scene 30031ae with dissolve
    pause 0.5
    scene 30031af with dissolve
    pause 0.5
    m "OUCH"
    show 30031ba2 at Move((0.5, -1), (0.5, 0.0), 10.0, xanchor=0.5, yanchor=0):
        zoom 2
    pause 10
    scene 30031ba2 with dissolve
    m "[player_name] stop..."
    e "You jumped into bed as soon as I showed up?"
    scene 30031ba3 with dissolve
    e "I have to admit..."
    show bedanim
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She is completely scared and frozen in place"
    e "You are a very attractive woman [woman_role]"
    e "If all 37-year-old women had legs like you{p}the world would be a beautiful place."

    scene 30031kick with dissolve
    m "Leave..."
    m "Me..."
    scene 30031kicka with dissolve
    pause 1
    scene 30031kickb with vpunch:
        zoom 0.5
    show text "{size=50}ALONE!" with dissolve
    hide text
    pause 0.5
    jump dadcomingforhelp


label grabatowel:

    scene 30031 with dissolve
    e "I think you don't need this, [woman_role]."
    scene 30032 with dissolve
    pause 1
    scene 30033 with dissolve
    pause 1
    e "I'll just take a quick look."
    show 30037 at Move((0.5, 0.0), (0.5, -2.0), 10.0, xanchor=0.5, yanchor=0)
    pause 10
    scene 30037a with vpunch
    m "STOP"
    jump dadcomingforhelp

label dadcomingforhelp:
    scene 30031kickd with vpunch
    e "HEY!"
    e "That's not fair."
    e "I was nice."

    scene 30031kicke with dissolve
    d "[woman_name]?!"
    scene 30031kickf with dissolve
    d "What happened?"
    scene 30031kicke with dissolve
    d "Is everything okay, honey?"
    scene 30031kickg with dissolve
    d "[player_name], what happened?"

    if easymode:
        menu:
                "I accidentally walked in on my [woman_role]":
                    jump accident
                "Nothing happened, Dad. {color=#FFD1DF}{i}*Wink at your father*{/i}{/color}\n{color=#3d85c6} Dad +1 (may affect the ending)":
                    $ dadfriend += 1
                    jump winkdad
                "I was waiting for [woman_name] in the room, and she came in and got scared":
                    jump accident
                "Nothing happened, right [woman_role]?":
                    jump nothingright
    else:
        menu:
                "I accidentally walked in on my [woman_role]":
                    jump accident
                "Nothing happened, Dad. {color=#FFD1DF}{i}*Wink at your father*{/i}{/color}":
                    $ dadfriend += 1
                    jump winkdad
                "I was waiting for [woman_name] in the room, and she came in and got scared":
                    jump accident
                "Nothing happened, right [woman_role]?":
                    jump nothingright

label nothingright:
    scene 30031kickg with dissolve
    m "...Ye..."
    m "..Yeah...{p}He creeped me out! I didn’t expect him to be there!..."
    $ nicoledominance += 1
    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
    scene 30031kickg with dissolve
    d "Honey, did you hurt yourself?"
    scene 30031kicki with dissolve
    d "Oh wow, that looks like quite a welcome for your husband."
    if pushherbedcheck > 0:
        scene 30042 with dissolve:
            zoom 0.5
    else:
        scene 30042c with dissolve:
                          zoom 0.5
    m "..."
    m "Can you both leave, please?"
    m "I want to get dressed..."
    d "Heh… I’d love to stay...{p}well, let's go buddy."
    scene 30031kickh with dissolve
    d "Let's give [woman_name] some privacy"
    $ renpy.end_replay()
    jump movieevening

label accident:
    scene 30031kickg with dissolve
    d "Honey, did you hurt yourself?"
    scene 30031kicki with dissolve
    d "Oh wow, that looks like quite a welcome for your husband."
    if pushherbedcheck > 0:
        scene 30042 with dissolve:
            zoom 0.5
    else:
        scene 30042c with dissolve:
                          zoom 0.5
    m "..."
    m "Can you both leave, please?"
    m "I want to get dressed..."
    d "Heh… I’d love to stay...{p}well, let's go buddy."
    scene 30031kickh with dissolve
    d "Let's give her some space"
    $ renpy.end_replay()
    jump movieevening

label winkdad:

    d "I ran as fast as I could"
    scene 30031kickg with dissolve
    d "Honey, did you hurt yourself?"
    scene 30031kicki with dissolve
    d "Oh wow, that looks like quite a welcome for your husband."
    if pushherbedcheck > 0:
        scene 30042 with dissolve:
            zoom 0.5
    else:
        scene 30042c with dissolve:
                          zoom 0.5
    m "..."
    m "Can you both leave, please?"
    m "I want to get dressed..."
    d "Heh… I’d love to stay...{p}well, let's go buddy."
    scene 30031kickh with dissolve
    d "Let's give her some space"
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} Damn,{p}I think my son is… on the slow bus."
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I wanted him to follow [woman_name] when I left, not right away."
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I just hope he doesn't fuck the entire operation up."
    $ renpy.end_replay()
    jump movieevening

label movieevening:
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
    d "{color=#ffa500}{i}*whispers*{/i}{/color} Are you having fun? Think you can answer the next question?"
    scene telewizja with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} Jordan, focus now. This question is worth $15,000!"
    scene tvshow08 with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} Which of the following best describes a CPU (Central Processing Unit)?"
    scene tvshow09 with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} A. A storage device that holds your files permanently."
    scene tvshow10 with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} B. The computer's 'brain' that performs calculations and executes instructions."
    scene tvshow11 with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} C. A device that displays images on your screen."
    scene tvshow12 with dissolve
    "{color=#ffa500}{i}*(Television)*{/i}{/color} D. A cooling system that prevents computer overheating."
    d "Oh, that's easy - everyone knows that a CPU is computer memory."
    "{color=#fff000}{i}*(Television - Jordan)*{/i}{/color} It's either B or D, or maybe C... Actually, A could work too."

    menu (screen="tvchoice"):
        "C":
            e "C"
            jump wrongtvshow
        "A":
            e "A"
            jump wrongtvshow
        "D":
            e "D"
            jump wrongtvshow
        "B":
            e "B"
            jump goodtvshow


label goodtvshow:
    "{color=#fff000}{i}*(Television - Jordan)*{/i}{/color} I think the correct answer will be B."
    "{color=#ffa500}{i}*(Television)*{/i}{/color} And this is the correct answer!"
    scene 31001b with dissolve
    d "Damn, I got it mixed up with RAM."
    d "You're really good!"
    "{color=#ffa500}*********************{/color}\nYou received the ITguy perk.\n{color=#ffa500}*********************{/color}"
    $ itguy += 1
    $ dadfriend += 1
    if not easymode:
                    $ achValid3 += 1
                    $ achievement.grant("Achiev08")
                    $ achievement.sync()
                    if not persistent.achievement8:
                        show Achiev8 at achievment with easeintop:
                                zoom 0.5
                                rotate_animation

                        "You have received the achievement!{p}\"ITguy.\"."
                        "Number of achievements earned in this chapter [achValid3]/4"
                        ""
                        hide Achiev8
                        $ persistent.achievement8 = True

    jump aftertvshow

label wrongtvshow:
     scene 31001a with dissolve
     d "I'm telling you its A"
     "{color=#fff000}{i}*(Television - Jordan)*{/i}{/color} I think the correct answer will be A."
     d "YOU SEE!?"
     "{color=#ffa500}{i}*(Television)*{/i}{/color} And unfortunately this is the wrong answer!"
     jump aftertvshow

label aftertvshow:
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

# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START# FINAL START

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

    if hiddendoor == 0:

        m "Then you sneaked into my room waiting for an opportunity..."

    else:
        scene 31028angryhq with dissolve
        m "I also saw you covering yourself with a pillow."

    scene 31028hq with dissolve
    m "It doesn't even bother you that your father is next to you."
    scene 31028listenhq with dissolve
    e "This is what true love looks like."
    e "If you were as devoted to Father as I am to you, this situation would not exist."
    scene 31028lipbitehq with dissolve
    pause
    scene 31028talk with dissolve
    m "It seems to me that no matter what I say, you still don't care."

    if easymode:
        menu:
            "I really care about you.":
                jump butireallycareep3

            "{color=#FFD1DF}{i}*Start massaging her thighs*{/i}{/color} {size=-8}(Req. 2 domination points){/size}" if nicoledominance >= 6:
                $ massagebeforeafraid += 1
                jump massagethigsep3

            "{color=#FFD1DF}{i}*Show her the video of her cheating*{/i}{/color} {size=-8}(Req. ITguy perk ){/size}\n{color=#3d85c6} +1 Point" if itguy >= 1:
                jump showtvep3

    else:
        menu:
            "I really care about you.":
                jump butireallycareep3

            "{color=#FFD1DF}{i}*Start massaging her thighs*{/i}{/color} {size=-8}(Req. 2 domination points){/size}" if nicoledominance >= 6:
                $ massagebeforeafraid += 1
                jump massagethigsep3

            "{color=#FFD1DF}{i}*Show her the video of her cheating*{/i}{/color} {size=-8}(Req. ITguy perk ){/size}" if itguy >= 1:
                jump showtvep3


label butireallycareep3:
    scene 31028hq with dissolve
    m "I don’t think we have the same concept for what caring about someone is. The point is: You don’t seem to understand how WRONG this is…"

    if easymode:
        menu:
            "I don’t give a shit about what’s wrong, I just want to claim you and make you mine. \n{color=#3d85c6} This may give you a point later":
                $ optionpointsep3 += 1
                scene 31028lipbitehq with dissolve
                pause
                scene 31028eyewhathq with dissolve
                m "… Y-You’re just horny…."
                scene 31028lipbitehq with dissolve
                e "Alright, yeah. Perhaps I’m horny too… But that’s not the point."
                scene 31028eyewhathq with dissolve
                m "Then what’s the point?"
                jump whatsthepoint


            "I don’t want to hear what’s wrong or what’s right… I just want to do what my heart tells me to…":
                scene 31028hq with dissolve
                m "Something tells me it’s not your heart the only one speaking…"
                m "Then what’s the point?"
                jump whatsthepoint

    else:
        menu:
            "I don’t give a shit about what’s wrong, I just want to claim you and make you mine.":
                $ optionpointsep3 += 1
                scene 31028lipbitehq with dissolve
                pause
                scene 31028eyewhathq with dissolve
                m "… Y-You’re just horny…."
                scene 31028lipbitehq with dissolve
                e "Alright, yeah. Perhaps I’m horny too… But that’s not the point."
                scene 31028eyewhathq with dissolve
                m "Then what’s the point?"
                jump whatsthepoint


            "I don’t want to hear what’s wrong or what’s right… I just want to do what my heart tells me to…":
                scene 31028hq with dissolve
                m "Something tells me it’s not your heart the only one speaking…"
                m "Then what’s the point?"
                jump whatsthepoint


label whatsthepoint:

    if easymode:
        menu:
            "The point is… that I love you. I love you more than I’ve ever loved any woman in my life":
                scene 31028lipbitehq with dissolve
                m " … But… This is way far across the line."
                e "You just have to say that you love me more than you love my dad."
                scene 31028angryhq with dissolve
                m "I can’t love you anymore… Not in the line you want to cross…"
                scene 31028eyewhathq with dissolve
                e "There are no lines in our love… I don’t love you as a [woman_role]… I love you as MY woman. "
                m "..."
                jump tremblingep3

            "The point is that I want your sweet pussy always available for my cock. \n{color=#3d85c6} This may give you a point later":
                $ optionpointsep3 += 1
                scene 31028whathq with dissolve
                pause
                scene 31028angryhq with dissolve
                m "...I don’t know what to say anymore..."
                scene 31028silent with dissolve
                e "Just say you want my cock a few inches up your womb."
                scene 31028angryhq with dissolve
                m "You’re crossing the line!"
                e "Has that ever mattered to you? You’ve cheated on him already, it’s not a big deal for you."
                e "You’ve grown desensitized from the first moment you’ve got yourself a dick inside who’s not my father’s."
                m "L-Lower your tone, young boy! I’m still your [woman_role]."
                jump tremblingep3

    else:
        menu:
            "The point is… that I love you. I love you more than I’ve ever loved any woman in my life":
                scene 31028lipbitehq with dissolve
                m " … But… This is way far across the line."
                e "You just have to say that you love me more than you love my dad."
                scene 31028angryhq with dissolve
                m "I can’t love you anymore… Not in the line you want to cross…"
                scene 31028eyewhathq with dissolve
                e "There are no lines in our love… I don’t love you as a [woman_role]… I love you as MY woman. "
                m "..."
                jump tremblingep3

            "The point is that I want your sweet pussy always available for my cock.":
                $ optionpointsep3 += 1
                scene 31028whathq with dissolve
                pause
                scene 31028angryhq with dissolve
                m "...I don’t know what to say anymore..."
                scene 31028silent with dissolve
                e "Just say you want my cock a few inches up your womb."
                scene 31028angryhq with dissolve
                m "You’re crossing the line!"
                e "Has that ever mattered to you? You’ve cheated on him already, it’s not a big deal for you."
                e "You’ve grown desensitized from the first moment you’ve got yourself a dick inside who’s not my father’s."
                m "L-Lower your tone, young boy! I’m still your [woman_role]."
                jump tremblingep3




label massagethigsep3:

    scene 31030 with dissolve
    e "I only care about you..."
    show cameradown
    pause 1.4
    scene 31030a
    e "...and your beautiful legs."
    show caress with dissolve
    $ nicoledominance += 1
    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
    e "I promised you that I would take care of you..."
    "{color=#A8E4A0}{i}{size=-3}She's trembling with fear."
    if massagesecondtest == 1:
          jump wehadadeal
    elif afraidcheck  >= 1:
          jump wehadadeal
    else:
          jump tremblingep3



label showtvep3:

    e "Look at the TV"
    menu:
        "Show NTR Scene from prologue?"

        "Yeah":
                show tvmovie
        "No":
                show tvmovienontr


    e "Remember that?"
    m "Why did you..."
    m "Yes, I remember"
    m "Please turn it off."

    $ nicoledominance += 1
    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
    e "Sure, I just thought you forgot."
    e "I won't show this to anyone, don't be afraid."
    show cameradown
    pause 1.4
    scene 31030a
    e "But everything comes with a price."
    show caress with dissolve
    e "And I promised you that I would take care of you..."
    "{color=#A8E4A0}{i}{size=-3}She's trembling with fear."
    jump tremblingep3


label tremblingep3:

    if massagebeforeafraid == 0:

        menu:

            "{color=#FFD1DF}{i}*Get on her lap*{/i}{/color} {size=-8}(Req. 3 domination points){/size}" if nicoledominance >= 7:
                jump getonherlapep3

            "I want to wake up every day and...":
                jump dontbeafraidep3

            "I saw your beautiful body today {size=-8}(Req. Remain hidden behind the door){/size}" if hiddendoor == 1:
                jump sawbodyhiddenep3

    else:

        menu:

            "{color=#FFD1DF}{i}*Get on her lap*{/i}{/color} {size=-8}(Req. 3 domination points){/size}" if nicoledominance >= 7:
                jump getonherlapep3

            "I saw your beautiful body today {size=-8}(Req. Remain hidden behind the door){/size}" if hiddendoor == 1:
                jump sawbodyhiddenep3

            "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I see there's no chance... {/i}":
                    "{i} Your [woman_role] got up and went to the bedroom{i}"
                    jump episode3endingsolobad


label sawbodyhiddenep3:

        scene 31028hq with dissolve
        m "You...{p}...what did you do?"
        scene 31028sluchahq with dissolve
        e "I saw you changing clothes in your room, soaking wet from the shower..."
        e "I was in the room with you."
        scene 31028hq with dissolve
        m "Are you serious!?"
        m "Did you peek and stare at me you little creep!?"
        scene 31028whathq with dissolve
        "{color=#A8E4A0}{i}{size=-3} Her lips quivered."
        $ nicoledominance += 1
        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicoledominance].png" with dissolve
        scene 31028nottalk with dissolve
        m "It's not normal what you're doing..."
        jump dontbeafraidep3


label dontbeafraidep3:

    if easymode:
        menu:
            "I want to wake up every day and make out to your slutty lips.\n{color=#3d85c6} This may give you a point later":
                $ optionpointsep3 += 1
                scene 31028hq with dissolve
                m "O-Oh...{p}Okay but...{p}But that’s a lot..."
                scene 31028whathq with dissolve
                e "It started thinking about you this way the day I saw you getting banged. I got jealous."
                scene 31028not with dissolve
                m "I already apologized to you for that..."
                jump dontbeafraidep3choose

            "I want to wake up every day next to you.":
                scene 31028angryhq with dissolve
                m "I know what you tried to do there… You little sly…"
                scene 31028hqa with dissolve
                e "I can’t express it, because I’m just not that good with words, I’m more of an action type of guy…"
                scene 31028eyewhathq with dissolve
                m "Yeah… I can tell…"
                jump dontbeafraidep3choose
    else:
        menu:
            "I want to wake up every day and make out to your slutty lips. ":
                $ optionpointsep3 += 1
                scene 31028hq with dissolve
                m "O-Oh...{p}Okay but...{p}But that’s a lot..."
                scene 31028whathq with dissolve
                e "It started thinking about you this way the day I saw you getting banged. I got jealous."
                scene 31028not with dissolve
                m "I already apologized to you for that..."
                jump dontbeafraidep3choose

            "I want to wake up every day next to you.":
                scene 31028angryhq with dissolve
                m "I know what you tried to do there… You little sly…"
                scene 31028hqa with dissolve
                e "I can’t express it, because I’m just not that good with words, I’m more of an action type of guy…"
                scene 31028eyewhathq with dissolve
                m "Yeah… I can tell…"
                jump dontbeafraidep3choose

label dontbeafraidep3choose:
    scene 31028lipbitehq with dissolve
    menu:

        "{color=#FFD1DF}{i}*Start massaging her thighs*{/i}{/color} {size=-8}(Req. 2 domination points){/size} or {color=#00ff00}50\%\ chance{/color}" if massagefail == 0:
            if nicoledominance >= 6:
                $ afraidcheck += 1
                jump massagethigsep3
            else:
                jump massagethigsep3chance

        "{color=#FFD1DF}{i}*Get on her lap*{/i}{/color} {size=-8}(Req. 3 domination points){/size} or {color=#00ff00}33\%\ chance{/color}" if getonherlapfail == 0:
            if nicoledominance >= 7:
                jump getonherlapep3
            else:
                jump getonherlapep3chance

        "Remember we had a deal?":
             jump wehadadeal

label wehadadeal:
    if easymode:
        menu:
            "And it seems that You don’t understand: I OWN YOU.\n{color=#3d85c6} You will receive more additional points based on your previous choices":
                $ optionpointsep3 += 1
                scene 31028hq with dissolve
                if optionpointsep3 > 2:
                        $ nicoledominance += 2
                        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicoledominance].png" with dissolve

                elif optionpointsep3 > 1:
                        $ nicoledominance += 1
                        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicoledominance].png" with dissolve

                m "...You...{p}You don’t...{p}Own me... Ngh..."

            "Just… Please, allow yourself to look at me as someone else… You need to understand \n{color=#3d85c6} You will receive additional points based on your previous choices":
                scene 31028angryhq with dissolve
                if optionpointsep3 > 2:
                    $ nicoledominance += 1
                    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
                    pause 3
                    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
                m "You’ve always been a creep… I can’t look you with other eyes… You’re ruining everything!"

    else:
        menu:
            "And it seems that You don’t understand: I OWN YOU.":
                $ optionpointsep3 += 1
                scene 31028hq with dissolve
                if optionpointsep3 > 2:
                        $ nicoledominance += 2
                        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicoledominance].png" with dissolve

                elif optionpointsep3 > 1:
                        $ nicoledominance += 1
                        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
                        pause 3
                        hide image "images/Stats/Dom[nicoledominance].png" with dissolve

                m "...You...{p}You don’t...{p}Own me... Ngh..."

            "Just… Please, allow yourself to look at me as someone else… You need to understand":
                scene 31028angryhq with dissolve
                if optionpointsep3 > 2:
                    $ nicoledominance += 1
                    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
                    pause 3
                    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
                m "You’ve always been a creep… I can’t look you with other eyes… You’re ruining everything!"



    menu:

          "{color=#FFD1DF}{i}*Get on her lap*{/i}{/color} {size=-8}(Req. 3 domination points){/size} or {color=#00ff00}50\%\ chance{/color}" if getonherlapfail2 == 0:
                if nicoledominance >= 7:
                    jump getonherlapep3
                else:
                    jump getonherlapep3chance2

          "{size=-8}{color=#89CFF0}(thinking...){/color}{/size}{i} I see there's no chance... {/i}":
                    "{i} Your [woman_role] got up and went to the bedroom{i}"
                    jump episode3endingsolobad


label massagethigsep3chance:

    $ massagethigsep3chanceint = renpy.random.randint(1, 100)
    if massagethigsep3chanceint >= 50:
        show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        $ massagesecondtest = 1
        $ afraidcheck += 1
        jump massagethigsep3
    else:
        show cameradown
        pause 1.4
        scene 31030a
        m "Dont touch me."
        show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        $ massagefail = 1
        jump dontbeafraidep3choose


label getonherlapep3chance:

    $ getonherlapep3chanceint = renpy.random.randint(1, 100)
    if getonherlapep3chanceint > 67:
        show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        $ nicoledominance += 1
        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicoledominance].png" with dissolve
        jump getonherlapep3
    else:
        show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        $ getonherlapfail = 1
        jump dontbeafraidep3choose

label getonherlapep3chance2:

    $ getonherlapep3chanceint2 = renpy.random.randint(1, 100)
    if getonherlapep3chanceint2 >= 50:
        show text "{color=#00ff00}{size=+10}S U C C E S S!{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        $ nicoledominance += 1
        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicoledominance].png" with dissolve
        jump getonherlapep3
    else:
        show text "{color=#f00}{size=+10}F A I L{/color}" with dissolve
        with Pause(2)
        hide text with dissolve
        $ getonherlapfail2 = 1
        "{i} Your [woman_role] got up and went to the bedroom{i}"
        jump episode3endingsolobad

label getonherlapep3:

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

    if easymode:
        menu:

            "{color=#FFD1DF}{i}*Grab her hands*{/i}{/color}":
                jump grabherhandsep3

            "So stroke my dick with your hand":
                jump strokedickep3

            "So what can you offer me? \n{color=#3d85c6} +1 Point":
                jump whatcanyouoffer
    else:
        menu:

            "{color=#FFD1DF}{i}*Grab her hands*{/i}{/color}":
                jump grabherhandsep3

            "So stroke my dick with your hand":
                jump strokedickep3

            "So what can you offer me?":
                jump whatcanyouoffer

label whatcanyouoffer:

    m "What?{p}I'm not offering anything"
    e "Your negotiating position is not very good."
    e "Offer me something [woman_role], or I'll take it myself."
    m "{color=#ffa500}{i}*She squealed slightly*{/i}{/color}"
    m "I can..."
    m "{color=#ffa500}{i}*She sighed*{/i}{/color}"
    m "I can do it...{p}with my hand..."
    $ nicoledominance += 1
    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
    "{color=#A8E4A0}{i}{size=-3}Her voice trembled as she said these words."
    e "So do it."
    jump strokedickep3


label strokedickep3:

    "{color=#A8E4A0}{i}{size=-3}She's totally confused."
    if mcknowsrecord == 0:
        m "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Everything is being recorded, if stroke his dick, I’ll have great proof that he’s forcing me to do it..."
    else:
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

    if nicoledominance >= 8:
        jump bjep3

    else:
        e "From tomorrow we will be alone here [woman_role]."
        e "Get ready for a little more work."
        e "Oh shit, don't stop, ugh."
        e "I think I'll cum soon."
        scene 31032d with dissolve
        $ maxmccumep7 += 1
        e "Don't cover it with your hand!"
        scene 31032d with vpunch
        pause 0.5
        scene 31032d with vpunch
        pause 1.5
        scene 31032d with vpunch
        pause 0.5
        scene 31032cm with dissolve
        e "Fuuuuck"
        e "Why did you do that?{p}I wanted to cum on your face."
        "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom.{i}"
        jump episode3endingsolo

label bjep3:
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
        $ maxmccumep7 += 1
        "{color=#A8E4A0}{i}{size=-3}She squeals and tries to break free, but unfortunately it is too late.{/i}"
        scene 31096 with dissolve
        e "Marked as mine."
        if mcknowsrecord == 1:
            e "Our video you recorded will be beautiful."
        else:
            m "..."

        m "Lesth me gho...."
        if nicoledominance >= 9:
                jump ffep3

        else:
                e "You are so beautiful."
                scene 31097 with dissolve
                e "Thank you [woman_role]."
                e "You can go."
                "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom.{i}"
                jump episode3endingsolo

label ffep3:
        e "Honestly, I don't want to finish yet."

        menu:
            "{i}Let her go":
                e "But you can go..."
                "{i} Your [woman_role] got up and went to the bathroom.{i}"
                $ renpy.end_replay()
                jump episode3endingsolo

            "{i}Facefuck her":
                jump facefuckep3

label facefuckep3:

        scene 31096 with dissolve
        e "And now I'm going to fuck your mouth [woman_role]."
        show facemedium with dissolve
        $ nicoledominance += 1
        show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
        pause 3
        hide image "images/Stats/Dom[nicoledominance].png" with dissolve
        e "My cum in your mouth feels so nice."
        e "How does it feel to swallow your [player_role]'s cum?"
        "{i}She moans.{/i}"
        e "Your lips feel very nice."
        e "They are made for sucking cocks."
        e "Mine especially."
        e "You know what? I don't think that's fast enough for a cock sucker like you."
        "{i}She starts moaning louder and louder, she probably can't take it anymore.{/i}"

        menu:
            "{i}Give her a break.":
                "{i} Your [woman_role] got up and went to the bathroom.{i}"
                $ renpy.end_replay()
                jump episode3finalbonus

            "{i}She definitely needs to suck it more.":
                jump facefucktotalep3

label facefucktotalep3:
        show facetotal with dissolve
        e "Now good?"
        m "{color=#ffa500}{i}*She moans loudly*{/i}{/color}"
        e "How does it feel when your own [player_role] fucks you in the mouth?"
        e "I don't think you'll be able to say much when we're done."
        e "{color=#ffa500}{i}*Breathing heavily*{/i}{/color}"
        e "You sucked my soul out of my body, damn."
        e "I need to rest."
        $ renpy.end_replay()
label replayff:
        if _in_replay:
            $nicoledominance = 9
            jump strokedickep3

        jump episode3finalbonus


label grabherhandsep3:


    scene 31040aa with dissolve
    $ nicoledominance += 1
    show image "images/Stats/Dom[nicoledominance].png" at statleft with dissolve
    pause 3
    hide image "images/Stats/Dom[nicoledominance].png" with dissolve
    m "Wait"
    m "I'm recording everything now."
    $ mcknowsrecord = 1
    scene 31040 with dissolve
    e "Great, we'll watch it together later."
    e "Now suck."
    scene 31040b with dissolve
    m "I will not do it...."
    m "Stop demanding such things from me! You pervert!"
    m "I am your [woman_role]!"
    scene 31032c with dissolve
    e "Take my cock in your hand! Now!"
    scene 31032d with dissolve
    e "You're turning me on too much... you need to release some of my blood pressure."
    e "Now jerk it off…"

    if not easymode:
        $ achValid3 += 1
        $ achievement.grant("Achiev09")
        $ achievement.sync()
        if not persistent.achievement9:
            show Achiev9 at achievment with easeintop:
                     zoom 0.5
                     rotate_animation

            "You have received the achievement!{p}\"You have total control.\"."
            "Number of achievements earned in this chapter [achValid3]/4"
            ""
            hide Achiev9
            $ persistent.achievement9 = True
    jump strokedickep3

label episode3finalbonus:
    scene 31051full with dissolve
    m "..."
    m "{color=#ffa500}{i}*She breathe heavily*{/i}{/color}"
    scene 31097 with dissolve
    e "I love it."
    e "But..."
    e "I didn't cum second time..."
    m "..."
    scene 31098 with dissolve
    m "My mouth...{p}hurts...."
    e "I'm not surprised, my dick is huge."
    e "Hey...{p}Let me sit next to you"

    stop music fadeout 1.0
    play music "music/Mn.wav"
    scene 31099 with dissolve
    e "You look fine."
    scene 31099a with dissolve
    e "Ready for round two?"
    m "..."

label episode3finalbonuschoice:
    scene 31099 with dissolve

    if tryfingeringep3stat <= 1:

        if easymode:
            menu:

                "Maybe you can blow me again?":
                    jump canyoublowme

                "{color=#FFD1DF}{i}*Try fingering her*{/i}{/color}\n{color=#3d85c6} Do it 3 times" :
                    jump tryfingeringep3

                "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I guess it's time to go to the bathroom and finish and then go to sleep.{i}":
                    "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom before you.{i}"
                    jump episode3endingsolo
        else:
            menu:

                "Maybe you can blow me again?":
                    jump canyoublowme

                "{color=#FFD1DF}{i}*Try fingering her*{/i}{/color}":
                    jump tryfingeringep3

                "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I guess it's time to go to the bathroom and finish and then go to sleep.{i}":
                    "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom before you.{i}"
                    jump episode3endingsolo


    elif tryfingeringep3stat > 1:
        menu:
            "Maybe you can blow me again?":
                jump canyoublowme

            "{color=#FFD1DF}{i}*Try fingering her*{/i}{/color} {size=-8}(Req. 6 domination points){/size}":
                jump tryfingeringep3

            "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I guess it's time to go to the bathroom and finish and then go to sleep.{i}":
                "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom before you.{i}"
                jump episode3endingsolo


label canyoublowme:
    $ canyoublowmestat += 1

    if canyoublowmestat == 1:
            m "..."
            m "No."
            jump episode3finalbonuschoice

    elif canyoublowmestat == 2:
            m "I already told you...I can't feel my mouth..."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} She didn't say no, just that her mouth hurts."
            jump episode3finalbonuschoice

    elif canyoublowmestat == 3:
            "{color=#A8E4A0}{i}{size=-3}She doesn't answer."
            jump episode3finalbonuschoice

    elif canyoublowmestat == 4:
            "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom."
            jump episode3endingsolo



label tryfingeringep3:
    $ tryfingeringep3stat += 1

    if tryfingeringep3stat == 1:
            scene 31101 with dissolve
            pause
            scene 31101a with dissolve
            m "..."
            m "Please don't."
            jump episode3finalbonuschoice

    elif tryfingeringep3stat == 2:
            scene 31101 with dissolve
            pause
            scene 31101a with dissolve
            pause
            scene 31101b with dissolve
            m "You've already done what you wanted. Let me rest."
            "{color=#A8E4A0}{i}{size=-3}She took your hand."
            jump episode3finalbonuschoice

    elif tryfingeringep3stat == 3 and nicoledominance >= 10:
            label lasthjep3:
            scene 31101 with dissolve
            pause
            scene 31101a with dissolve
            pause
            scene 31101b with dissolve
            pause
            scene black with fade
            "{color=#A8E4A0}{i}{size=-3}You started fingering her"
            $ niclovebonusfactor += 1
            if not easymode:
                $ achValid3 += 1
                $ achievement.grant("Achiev10")
                $ achievement.sync()
                if not persistent.achievement10:
                    show Achiev10 at achievment with easeintop:
                            zoom 0.5
                            rotate_animation

                    "You have received the achievement!{p}\"To the last drop!\"."
                    "Number of achievements earned in this chapter [achValid3]/4"
                    hide Achiev10
                    $ persistent.achievement10 = True
            show nicolefinggood
            m "{color=#ffa500}{i}*She moans softly*{/i}{/color}"
            m "{color=#ffa500}{i}*whispers*{/i}{/color} [player_name]..."
            "{color=#A8E4A0}{i}{size=-3}She said your name quietly.{/i}"
            "{color=#A8E4A0}{i}{size=-3}Her hips move involuntarily, rubbing her pussy against your fingers."
            scene 31103b with dissolve
            e "You know what to do with your hand."
            scene 31103a with dissolve
            pause 1
            scene 31103 with dissolve
            "{color=#A8E4A0}{i}{size=-3}Your [woman_role] grabbed your dick."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I didn't expect it to be this easy..."
            show lasthjep3
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} But i fucking love it."
            "{color=#ffa500}{i}*You both moan quietly*{/i}{/color}"
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I think she has already fully given herself to me."
            e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} And that’s what turns me on the most."
            scene 31103 with dissolve
            e "Awww...."
            scene 31103cm with vpunch
            $ maxmccumep7 += 1
            "{color=#A8E4A0}{i}{size=-3}You feel pleasant chills{i}"
            scene 31102a
            m "{color=#ffa500}{i}*She let out a loud, single moan*{/i}{/color}"
            $ endingep3full = True
            scene 31102b with dissolve
            pause 0.5
            scene 31102c with dissolve
            pause 0.5
            scene 31102d with dissolve
            pause 0.5
            scene 31102e with dissolve
            pause 0.5
            scene 31102f with dissolve
            pause 0.5
            $ renpy.end_replay()
            jump episode3ending

    elif tryfingeringep3stat == 3:
            scene 31101 with dissolve
            pause
            scene 31101a with dissolve
            pause
            scene 31101b with dissolve
            "{color=#A8E4A0}{i}{size=-3}She took your hand.{/i}"
            "{color=#A8E4A0}{i}{size=-3}Your [woman_role] got up and went to the bathroom.{i}"
            "I guess you didn't dominate her enough..."
            jump episode3endingsolo

label episode3endingsolo:
    scene 31109 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} What a great day."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I'm tired as hell. I don't even want to finish.{i}"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I guess it'll be better if I just go to sleep...{i}"

    scene black with fade

    jump stats

label episode3endingsolobad:
    scene 31109 with dissolve
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Fuck."
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I fucked up.{i}"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I guess it'll be better if I just go to sleep...{i}"

    scene black with fade

    jump stats

label episode3ending:
    e "{color=#A8E4A0}{i}{size=-3}She fell asleep on your shoulder"
    e "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I think I tired her out..."
    e "{color=#ffa500}{i}*whispers*{/i}{/color} Goodnight [woman_name]."
    "{color=#A8E4A0}{i}{size=-3}She doesn't answer."

    scene black with fade
    show text "{size=+5} A few hours later{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    show text "{size=+5} Very early morning{/size}" with dissolve
    with Pause(2)
    hide text with dissolve
    with Pause(1)

    scene 31120 with dissolve
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} Oh, she must have been very tired.{p}She fell asleep with her clothes on.{i}"
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} How sweet… They sleep together!{i}"
    scene 31121 with dissolve
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} I definitely need to spend more time with them...{i}"
    "{color=#ffa500}{i}*He sighed*{/i}{/color}"
    d "{size=-8}{color=#89CFF0}(thinking...){/color}{/size} It's time to get ready for work.{i}"
    scene black with fade

    jump stats

label stats:

    $ achVall = achValid + achValid2 + achValid3

    if not easymode:
        "So far you have achieved [achVall] out of 11 available achievements!"
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

    jump episode4
