## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.
init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (3 + 1)

    replay_page = 0

    class ReplayItem:
        def __init__(self, thumbs, replay, name):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name

        def num_replay(self):
            return len(self.thumbs)

    #add replay items here format below

    #Replay_items.append(ReplayItem(["the thumbnail"], "the_label_from_code", "brief description"))
    Replay_items = []
    Replay_items.append(ReplayItem(["Rthumb3"], "endingtommymom", "Episode 1 Sacrifice"))
    Replay_items.append(ReplayItem(["Rthumb4"], "grabstrapsep1", "Episode 1 Final Scene"))
    Replay_items.append(ReplayItem(["Rthumb19"], "alleysheila", "Episode 2 All for the beavers"))
    Replay_items.append(ReplayItem(["Rthumb1"], "touchpussy", "Episode 2 Bad Speaker"))
    Replay_items.append(ReplayItem(["Rthumb2"], "bjFinal", "Episode 2 Final Scene"))
    Replay_items.append(ReplayItem(["Rthumb5"], "crouchingtiger", "Episode 3 Crouching tiger"))
    Replay_items.append(ReplayItem(["Rthumb6"], "replayff", "Episode 3 Final Scene"))
    Replay_items.append(ReplayItem(["Rthumb7"], "lasthjep3", "Episode 3 Bonus Scene"))
    Replay_items.append(ReplayItem(["Rthumb8"], "lickpussyep4", "Episode 4 This is her moment"))
    Replay_items.append(ReplayItem(["Rthumb9"], "fuckthroatep4", "Episode 4 This is your moment"))
    Replay_items.append(ReplayItem(["Rthumb10"], "grabep4", "Episode 4 Somefeet"))
    Replay_items.append(ReplayItem(["Rthumb11"], "cleancock", "Episode 4 Ending Dom"))
    Replay_items.append(ReplayItem(["Rthumb12"], "kissep4", "Episode 4 Ending Lust"))
    Replay_items.append(ReplayItem(["Rthumb13"], "balconysuck", "Episode 5 Hidden Scene"))
    Replay_items.append(ReplayItem(["Rthumb14"], "bedep5scene", "Episode 5 Eve's wet dreams "))
    Replay_items.append(ReplayItem(["Rthumb15"], "willdeletephoto", "Episode 5 Morning (Love)"))
    Replay_items.append(ReplayItem(["Rthumb16"], "obedientep5", "Episode 5 Morning (Domination)"))
    Replay_items.append(ReplayItem(["Rthumb17"], "grabhairep5sofa", "Episode 5 Morning Full Domination"))
    Replay_items.append(ReplayItem(["Rthumb18"], "mtomshare", "Episode 5 Sharing scene"))
    Replay_items.append(ReplayItem(["Rthumb20"], "mtomtomep5without", "Episode 5 Solo scene"))
    Replay_items.append(ReplayItem(["Rthumb21"], "auntwinedrink", "Episode 5 Too much wine!"))
    Replay_items.append(ReplayItem(["Rthumb22"], "forceeveep5", "Episode 5 Now!"))
    Replay_items.append(ReplayItem(["Rthumb23"], "eveningwitheve", "Episode 5 Memflix&Chill"))
    Replay_items.append(ReplayItem(["Rthumb24"], "nighteve", "Episode 5 Good Dreams"))
    Replay_items.append(ReplayItem(["Rthumb25"], "ep5showernic", "Episode 5 Pose for me"))
    Replay_items.append(ReplayItem(["Rthumb26"], "sxfavor", "Episode 5 Strong Wine"))
    Replay_items.append(ReplayItem(["Rthumb27"], "opendoorfinal", "Episode 5 No regrets"))
    Replay_items.append(ReplayItem(["Rthumb28"], "evereplayep6", "Episode 6 Eve is Horny"))
    Replay_items.append(ReplayItem(["Rthumb29"], "replaytommyep6", "Episode 6 Tommy just want to have fun "))
    Replay_items.append(ReplayItem(["Rthumb30"], "sucktoiletep6", "Episode 6 Nicole Domination Ending"))
    Replay_items.append(ReplayItem(["Rthumb31"], "replayloveep6", "Episode 6 Nicole Love Ending"))
    Replay_items.append(ReplayItem(["Rthumb32"], "mtomreplaynight", "Episode 6 Night Stalker"))
    Replay_items.append(ReplayItem(["Rthumb33"], "bathnickep7dom", "Episode 7 Good Morning! (Domination)"))
    Replay_items.append(ReplayItem(["Rthumb34"], "bathnickep7love", "Episode 7 Good Morning! (Love)"))
    Replay_items.append(ReplayItem(["Rthumb35"], "replaymtomchangingscene", "Episode 7 Another Sacrifice"))
    Replay_items.append(ReplayItem(["Rthumb36"], "replayspascene", "Episode 7 Hot Date"))
    Replay_items.append(ReplayItem(["Rthumb37"], "evespasxanimcmlabelreplay", "Episode 7 Wait for me!"))
    Replay_items.append(ReplayItem(["Rthumb38"], "endingdominostage1", "Episode 7 Final Domination (I)"))
    Replay_items.append(ReplayItem(["Rthumb41"], "endinglovestage1", "Episode 7 Final Love (I)"))
    Replay_items.append(ReplayItem(["Rthumb39"], "stage2nicole", "Episode 7 Final Domination (II)"))
    Replay_items.append(ReplayItem(["Rthumb42"], "stage2nicolelv", "Episode 7 Final Love (II)"))
    Replay_items.append(ReplayItem(["Rthumb40"], "hconep7", "Episode 7 Final Domination (III)"))
    Replay_items.append(ReplayItem(["Rthumb43"], "lvphase3camrepeat", "Episode 7 Final Love (III)"))







# a black background screen for the selection
image black = "#000"

#the locked image for the replay gallery if you're using the gallery you can use the same (if you want to)
image replay_locked = "images/replay/replay_lock.jpg"

#384x216 (16x9) set 1280x720p for the lock and thumbnails
#600x338 (16x9) set 1920x1080 for the lock and thumbnails
#replay thumbnails images setup defined here
image Rthumb1 = ("images/replay/thumbe21.jpg")
image Rthumb2 = ("images/replay/thumbe22.jpg")
image Rthumb3 = ("images/replay/thumbe11.jpg")
image Rthumb4 = ("images/replay/thumbe12.png")
image Rthumb5 = ("images/replay/thumbe31.png")
image Rthumb6 = ("images/replay/thumbe32.png")
image Rthumb7 = ("images/replay/thumbe33.png")
image Rthumb8 = ("images/replay/thumbe41.png")
image Rthumb9 = ("images/replay/thumbe42.png")
image Rthumb10 = ("images/replay/thumbe43.png")
image Rthumb11 = ("images/replay/thumbe44.png")
image Rthumb12 = ("images/replay/thumbe45.png")
image Rthumb13 = ("images/replay/thumbe51.jpg")
image Rthumb14 = ("images/replay/thumbe52.png")
image Rthumb15 = ("images/replay/thumbe53.jpg")
image Rthumb16 = ("images/replay/thumbe54.jpg")
image Rthumb17 = ("images/replay/thumbe55.jpg")
image Rthumb18 = ("images/replay/thumbe56.png")
image Rthumb19 = ("images/replay/thumbe20.png")
image Rthumb20 = ("images/replay/thumbe57.jpg")
image Rthumb21 = ("images/replay/thumbe58.png")
image Rthumb22 = ("images/replay/thumbe59.png")
image Rthumb23 = ("images/replay/thumbe510.png")
image Rthumb24 = ("images/replay/thumbe511.jpg")
image Rthumb25 = ("images/replay/thumbe512.jpg")
image Rthumb26 = ("images/replay/thumbe514.jpg")
image Rthumb27 = ("images/replay/thumbe513.jpg")
image Rthumb28 = ("images/replay/thumbe61.png")
image Rthumb29 = ("images/replay/thumbe62.png")
image Rthumb30 = ("images/replay/thumbe64.png")
image Rthumb31 = ("images/replay/thumbe63.png")
image Rthumb32 = ("images/replay/thumbe65.png")
image Rthumb33 = ("images/replay/thumbe71.png")
image Rthumb34 = ("images/replay/thumbe72.png")
image Rthumb35 = ("images/replay/thumbe73.png")
image Rthumb36 = ("images/replay/thumbe74.png")
image Rthumb37 = ("images/replay/thumbe75.png")
image Rthumb38 = ("images/replay/thumbe76.png")
image Rthumb41 = ("images/replay/thumbe76.png")
image Rthumb39 = ("images/replay/thumbe77.jpg")
image Rthumb42 = ("images/replay/thumbe77.jpg")
image Rthumb40 = ("images/replay/thumbe78.jpg")
image Rthumb43 = ("images/replay/thumbe79.png")

