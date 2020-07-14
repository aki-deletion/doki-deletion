# Definitions.rpy

# This section defines stuff for DDLC and your mod!

# Use this as a starting point if you would like to override with your own.
define persistent.self = True
define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
# Change this to True to enable Developer Mode
define config.developer = True

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)

    # Get's position of Music
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # Delete's All Saves
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # Delete's Characters
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass

    # Restores Character's CHR
    def restore_all_characters():
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    # Restores Characters if their playthough matches current run.
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")

    # Controls time.
    def pause(time=None):
        #global _windows_hidden
        if not time:
            #_windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            #_windows_hidden = False
            return
        if time <= 0: return
        #_windows_hidden = True
        renpy.pause(time)
        #_windows_hidden = False

# Music

# This section is where you can reference DDLC audio and add your own!
# audio. - tells Ren'Py this is sound
# t1 - tells Ren'Py the label of the music/sound file
# <loop 22.073> - tells Ren'Py to loop the song at that time interval
# "bgm/1.ogg" - location of your music
define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

# Doki Poem Theme
define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.scream = "mod_assets/bgm/scream.mp3"
define audio.knock = "mod_assets/bgm/knock1.mp3"

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

image bedroom1 = "mod_assets/custom_bg/bedroom_1.png"
image s_hug = "mod_assets/custom_bg/s_hug.png"

# Character Definitions

# This is where the characters bodies and faces are defined.
# They are defined by left half, right half and their head.

# Sayori's Definitions
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

# Casual Sayori (Seen during her confession)
image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki's Definitions
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")

# Casual Natsuki (Seen if Natsuki is Selected to work with)
image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# Beta Natsuki
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri's Definitions
# Sprites with 1y1 are Yuri's Yandere Sprites
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

# Casual Yuri (Seen if Yuri is selected to help out)
image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika's Definitions
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat
image monika nud1 = "mod_assets/custom_sprites/monika_nude1.png"
image monika nud2 = "mod_assets/custom_sprites/monika_nude2.png"
image sayori nud1 = "mod_assets/custom_sprites/sayori_nude1.png"
image sayori nud2 = "mod_assets/custom_sprites/sayori_nude2.png"
image sayori nud3 = "mod_assets/custom_sprites/sayori_nude3.png"
image yuri nud1 = "mod_assets/custom_sprites/yuri_nude1.png"
image yuri nud2 = "mod_assets/custom_sprites/yuri_nude2.png"
image natsuki nud1 = "mod_assets/custom_sprites/natsuki_nude1.png"
image natsuki nud2 = "mod_assets/custom_sprites/natsuki_nude2.png"
image m_kill = "mod_assets/custom_sprites/m_kill.png"
# Character Variables

# This configure the character variables for writing dialog for each character
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer

# Persistent Variables

# These variables are load at game startup and exist on all saves.
default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

# Other Persistent Variables
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

# Poem Variables
# This is how much each character likes your poem day by day
# -1 - Bad, 0 - Neutral, 1 - Good
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem game
default poemwinner = ['sayori', 'sayori', 'sayori']

# This keeps track on who already read your poem
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This stores how many poems you read so far.
default poemsread = 0

# This stores who likes your poem the most.
# This controls which exclusive scene you will get each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# Tracks whether we watched Natsuki's and Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# Tracks whether Yuri runs away after the first exclusive scene of Act 2
default y_gave = False
default y_ranaway = False

# Tracks if we get to Natsuki's and Yuri's third poem
default n_read3 = False
default y_read3 = False

# Tracks who we chose to side with in Chapter 1
default ch1_choice = "sayori"

default n_poemearly = False

# Tracks whether we wanted to help Sayori and/or Monika
default help_sayori = None
default help_monika = None

# Tracks who we chose to spend time with in Chapter 4
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# Tracks if we accepted Sayori's Confession
default sayori_confess = True

# We read Natsuki's third poem in Chapter 23
default natsuki_23 = None
####Custom Characters####
image nico 1 = "mod_assets/custom_sprites/nico_01_02_s.jpg"
image nico 2 = "mod_assets/custom_sprites/nico_01_03_s.jpg"
image nico 3 = "mod_assets/custom_sprites/nico_01_04_s.jpg"
image nico 4 = "mod_assets/custom_sprites/nico_01_05_s.jpg"
image nico_b1 = "mod_assets/custom_sprites/nico_06_02_s.jpg"
image nico_b2 = "mod_assets/custom_sprites/nico_06_03_s.jpg"
image nico_b3 = "mod_assets/custom_sprites/nico_06_04_s.jpg"
image nico b4 = "mod_assets/custom_sprites/nico_06_05_s.jpg"
image nico c1 = "mod_assets/custom_sprites/nico_08_02_s.jpg"
image nico c2 = "mod_assets/custom_sprites/nico_08_03_s.jpg"
image nico c3 = "mod_assets/custom_sprites/nico_08_04_s.jpg"
image nico c4 = "mod_assets/custom_sprites/nico_08_05_s.jpg"

image ruby 1 = "mod_assets/custom_sprites/ruby_01_01_s.jpg"
image ruby 2 = "mod_assets/custom_sprites/ruby_01_02_s.jpg"
image ruby 3 = "mod_assets/custom_sprites/ruby_01_03_s.jpg"
image ruby 4 = "mod_assets/custom_sprites/ruby_01_04_s.jpg"
image ruby b1 = "mod_assets/custom_sprites/ruby_06_01_s.jpg"
image ruby b2 = "mod_assets/custom_sprites/ruby_06_02_s.jpg"
image ruby b3 = "mod_assets/custom_sprites/ruby_06_03_s.jpg"
image ruby b4 = "mod_assets/custom_sprites/ruby_06_04_s.jpg"

image eli 1 = "mod_assets/custom_sprites/eli_01_02_s.jpg"
image eli 2 = "mod_assets/custom_sprites/eli_01_03_s.jpg"
image eli 3 = "mod_assets/custom_sprites/eli_01_04_s.jpg"
image eli 4 = "mod_assets/custom_sprites/eli_01_05_s.jpg"
image eli b1 = "mod_assets/custom_sprites/eli_17_01_s.jpg"
image eli b2 = "mod_assets/custom_sprites/eli_17_02_s.jpg"

image kotori 1 = "mod_assets/custom_sprites/kotori_01_02_s.jpg"
image kotori 2 = "mod_assets/custom_sprites/kotori_01_03_s.jpg"
image kotori 3 = "mod_assets/custom_sprites/kotori_01_04_s.jpg"
image kotori b1 = "mod_assets/custom_sprites/kotori_08_02_s.jpg"
image kotori b2 = "mod_assets/custom_sprites/kotori_08_03_s.jpg"
image kotori b3 = "mod_assets/custom_sprites/kotori_08_04_s.jpg"
image kotori c1 = "mod_assets/custom_sprites/kotori_17_01_s.jpg"
image kotori c2 = "mod_assets/custom_sprites/kotori_17_02_s.jpg"

image leah 1 = "mod_assets/custom_sprites/leah_12_01_s.jpg"
image leah 2 = "mod_assets/custom_sprites/leah_12_03_s.jpg"
image leah 3 = "mod_assets/custom_sprites/leah_12_04_s.jpg"
image leah 4 = "mod_assets/custom_sprites/leah_12_06_s.jpg"

image lola 1 = "mod_assets/custom_sprites/lola1.png"
image lola 2 = "mod_assets/custom_sprites/lola2.png"
image lola 3 = "mod_assets/custom_sprites/lola3.png"
image lola 4 = "mod_assets/custom_sprites/lola4.png"
image lola 5 = "mod_assets/custom_sprites/lola5.png"
image lola 6 = "mod_assets/custom_sprites/lola6.png"
image lola 7 = "mod_assets/custom_sprites/lola7.png"
image lola 8 = "mod_assets/custom_sprites/lola8.png"
image lola sl = "mod_assets/custom_sprites/lola_sl.png"

image sara 1 = "mod_assets/custom_sprites/sara1.jpg"
image sara 2 = "mod_assets/custom_sprites/sara2.jpg"
image sara 3 = "mod_assets/custom_sprites/sara3.jpg"

############### Natsuki's dad ########################

### Base poses ###

image natsukidad 1a = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a.png")
image natsukidad 1b = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/b.png")
image natsukidad 1c = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/c.png")
image natsukidad 1d = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/d.png")
image natsukidad 1e = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/e.png")
image natsukidad 1f = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/f.png")
image natsukidad 1g = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/g.png")
image natsukidad 1h = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/h.png")
image natsukidad 1i = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/i.png")
image natsukidad 1j = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/j.png")
image natsukidad 1k = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/k.png")
image natsukidad 1l = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/l.png")
image natsukidad 1m = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/m.png")
image natsukidad 1n = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/n.png")
image natsukidad 1o = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/o.png")
image natsukidad 1p = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/p.png")
image natsukidad 1q = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/q.png")
image natsukidad 1r = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/r.png")
image natsukidad 1s = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/s.png")
image natsukidad 1t = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/t.png")
image natsukidad 1u = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/u.png")
image natsukidad 1v = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/v.png")
image natsukidad 1w = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a2.png")
image natsukidad 1x = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/aB.png")

image natsukidad 2a = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a.png")
image natsukidad 2b = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/b.png")
image natsukidad 2c = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/c.png")
image natsukidad 2d = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/d.png")
image natsukidad 2e = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/e.png")
image natsukidad 2f = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/f.png")
image natsukidad 2g = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/g.png")
image natsukidad 2h = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/h.png")
image natsukidad 2i = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/i.png")
image natsukidad 2j = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/j.png")
image natsukidad 2k = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/k.png")
image natsukidad 2l = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/l.png")
image natsukidad 2m = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/m.png")
image natsukidad 2n = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/n.png")
image natsukidad 2o = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/o.png")
image natsukidad 2p = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/p.png")
image natsukidad 2q = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/q.png")
image natsukidad 2r = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/r.png")
image natsukidad 2s = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/s.png")
image natsukidad 2t = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/t.png")
image natsukidad 2u = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/u.png")
image natsukidad 2v = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/v.png")
image natsukidad 2w = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a2.png")
image natsukidad 2x = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/aB.png")

image natsukidad 3a = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a.png")
image natsukidad 3b = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/b.png")
image natsukidad 3c = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/c.png")
image natsukidad 3d = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/d.png")
image natsukidad 3e = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/e.png")
image natsukidad 3f = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/f.png")
image natsukidad 3g = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/g.png")
image natsukidad 3h = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/h.png")
image natsukidad 3i = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/i.png")
image natsukidad 3j = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/j.png")
image natsukidad 3k = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/k.png")
image natsukidad 3l = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/l.png")
image natsukidad 3m = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/m.png")
image natsukidad 3n = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/n.png")
image natsukidad 3o = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/o.png")
image natsukidad 3p = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/p.png")
image natsukidad 3q = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/q.png")
image natsukidad 3r = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/r.png")
image natsukidad 3s = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/s.png")
image natsukidad 3t = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/t.png")
image natsukidad 3u = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/u.png")
image natsukidad 3v = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/v.png")
image natsukidad 3w = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a2.png")
image natsukidad 3x = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/aB.png")

image natsukidad 4a = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a.png")
image natsukidad 4b = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/b.png")
image natsukidad 4c = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/c.png")
image natsukidad 4d = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/d.png")
image natsukidad 4e = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/e.png")
image natsukidad 4f = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/f.png")
image natsukidad 4g = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/g.png")
image natsukidad 4h = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/h.png")
image natsukidad 4i = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/i.png")
image natsukidad 4j = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/j.png")
image natsukidad 4k = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/k.png")
image natsukidad 4l = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/l.png")
image natsukidad 4m = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/m.png")
image natsukidad 4n = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/n.png")
image natsukidad 4o = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/o.png")
image natsukidad 4p = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/p.png")
image natsukidad 4q = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/q.png")
image natsukidad 4r = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/r.png")
image natsukidad 4s = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/s.png")
image natsukidad 4t = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/t.png")
image natsukidad 4u = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/u.png")
image natsukidad 4v = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/v.png")
image natsukidad 4w = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a2.png")
image natsukidad 4x = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/aB.png")

image natsukidad 5a = im.Composite((960, 960), (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5b = im.Composite((960, 960), (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5c = im.Composite((960, 960), (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5d = im.Composite((960, 960), (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5e = im.Composite((960, 960), (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5f = im.Composite((960, 960), (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5g = im.Composite((960, 960), (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5h = im.Composite((960, 960), (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5i = im.Composite((960, 960), (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5j = im.Composite((960, 960), (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5k = im.Composite((960, 960), (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5l = im.Composite((960, 960), (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5m = im.Composite((960, 960), (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5n = im.Composite((960, 960), (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5o = im.Composite((960, 960), (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5p = im.Composite((960, 960), (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5q = im.Composite((960, 960), (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5r = im.Composite((960, 960), (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5s = im.Composite((960, 960), (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5t = im.Composite((960, 960), (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5u = im.Composite((960, 960), (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5v = im.Composite((960, 960), (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5w = im.Composite((960, 960), (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/3a.png")
image natsukidad 5x = im.Composite((960, 960), (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/3a.png")

### Base poses (With drunk blush) ###

image natsukidad 1ad = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/db.png")
image natsukidad 1bd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/db.png")
image natsukidad 1cd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/db.png")
image natsukidad 1dd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/db.png")
image natsukidad 1ed = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/db.png")
image natsukidad 1fd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/db.png")
image natsukidad 1gd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/db.png")
image natsukidad 1hd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/db.png")
image natsukidad 1id = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/db.png")
image natsukidad 1jd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/db.png")
image natsukidad 1kd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/db.png")
image natsukidad 1ld = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/db.png")
image natsukidad 1md = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/db.png")
image natsukidad 1nd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/db.png")
image natsukidad 1od = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/db.png")
image natsukidad 1pd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/db.png")
image natsukidad 1qd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/db.png")
image natsukidad 1rd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/db.png")
image natsukidad 1sd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/db.png")
image natsukidad 1td = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/db.png")
image natsukidad 1ud = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/db.png")
image natsukidad 1vd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/db.png")
image natsukidad 1wd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/db.png")
image natsukidad 1xd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/db.png")

image natsukidad 2ad = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/db.png")
image natsukidad 2bd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/db.png")
image natsukidad 2cd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/db.png")
image natsukidad 2dd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/db.png")
image natsukidad 2ed = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/db.png")
image natsukidad 2fd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/db.png")
image natsukidad 2gd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/db.png")
image natsukidad 2hd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/db.png")
image natsukidad 2id = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/db.png")
image natsukidad 2jd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/db.png")
image natsukidad 2kd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/db.png")
image natsukidad 2ld = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/db.png")
image natsukidad 2md = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/db.png")
image natsukidad 2nd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/db.png")
image natsukidad 2od = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/db.png")
image natsukidad 2pd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/db.png")
image natsukidad 2qd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/db.png")
image natsukidad 2rd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/db.png")
image natsukidad 2sd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/db.png")
image natsukidad 2td = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/db.png")
image natsukidad 2ud = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/db.png")
image natsukidad 2vd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/db.png")
image natsukidad 2wd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/db.png")
image natsukidad 2xd = im.Composite((960, 960), (0, 0), "natsukidad/1l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/db.png")

image natsukidad 3ad = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/db.png")
image natsukidad 3bd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/db.png")
image natsukidad 3cd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/db.png")
image natsukidad 3dd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/db.png")
image natsukidad 3ed = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/db.png")
image natsukidad 3fd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/db.png")
image natsukidad 3gd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/db.png")
image natsukidad 3hd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/db.png")
image natsukidad 3id = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/db.png")
image natsukidad 3jd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/db.png")
image natsukidad 3kd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/db.png")
image natsukidad 3ld = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/db.png")
image natsukidad 3md = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/db.png")
image natsukidad 3nd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/db.png")
image natsukidad 3od = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/db.png")
image natsukidad 3pd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/db.png")
image natsukidad 3qd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/db.png")
image natsukidad 3rd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/db.png")
image natsukidad 3sd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/db.png")
image natsukidad 3td = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/db.png")
image natsukidad 3ud = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/db.png")
image natsukidad 3vd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/db.png")
image natsukidad 3wd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/db.png")
image natsukidad 3xd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/db.png")

image natsukidad 4ad = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/db.png")
image natsukidad 4bd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/db.png")
image natsukidad 4cd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/db.png")
image natsukidad 4dd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/db.png")
image natsukidad 4ed = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/db.png")
image natsukidad 4fd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/db.png")
image natsukidad 4gd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/db.png")
image natsukidad 4hd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/db.png")
image natsukidad 4id = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/db.png")
image natsukidad 4jd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/db.png")
image natsukidad 4kd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/db.png")
image natsukidad 4ld = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/db.png")
image natsukidad 4md = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/db.png")
image natsukidad 4nd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/db.png")
image natsukidad 4od = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/db.png")
image natsukidad 4pd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/db.png")
image natsukidad 4qd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/db.png")
image natsukidad 4rd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/db.png")
image natsukidad 4sd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/db.png")
image natsukidad 4td = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/db.png")
image natsukidad 4ud = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/db.png")
image natsukidad 4vd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/db.png")
image natsukidad 4wd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/db.png")
image natsukidad 4xd = im.Composite((960, 960), (0, 0), "natsukidad/2l.png", (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/db.png")

image natsukidad 5ad = im.Composite((960, 960), (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5bd = im.Composite((960, 960), (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5cd = im.Composite((960, 960), (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5dd = im.Composite((960, 960), (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5ed = im.Composite((960, 960), (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5fd = im.Composite((960, 960), (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5gd = im.Composite((960, 960), (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5hd = im.Composite((960, 960), (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5id = im.Composite((960, 960), (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5jd = im.Composite((960, 960), (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5kd = im.Composite((960, 960), (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5ld = im.Composite((960, 960), (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5md = im.Composite((960, 960), (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5nd = im.Composite((960, 960), (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5od = im.Composite((960, 960), (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5pd = im.Composite((960, 960), (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5qd = im.Composite((960, 960), (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5rd = im.Composite((960, 960), (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5sd = im.Composite((960, 960), (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5td = im.Composite((960, 960), (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5ud = im.Composite((960, 960), (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5vd = im.Composite((960, 960), (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5wd = im.Composite((960, 960), (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")
image natsukidad 5xd = im.Composite((960, 960), (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/3a.png", (0, 0), "natsukidad/db.png")

### Bottle Poses ###

image natsukidad 6a = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a.png")
image natsukidad 6b = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/b.png")
image natsukidad 6c = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/c.png")
image natsukidad 6d = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/d.png")
image natsukidad 6e = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/e.png")
image natsukidad 6f = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/f.png")
image natsukidad 6g = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/g.png")
image natsukidad 6h = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/h.png")
image natsukidad 6i = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/i.png")
image natsukidad 6j = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/j.png")
image natsukidad 6k = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/k.png")
image natsukidad 6l = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/l.png")
image natsukidad 6m = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/m.png")
image natsukidad 6n = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/n.png")
image natsukidad 6o = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/o.png")
image natsukidad 6p = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/p.png")
image natsukidad 6q = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/q.png")
image natsukidad 6r = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/r.png")
image natsukidad 6s = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/s.png")
image natsukidad 6t = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/t.png")
image natsukidad 6u = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/u.png")
image natsukidad 6v = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/v.png")
image natsukidad 6w = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a2.png")
image natsukidad 6x = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/aB.png")

image natsukidad 7a = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a.png")
image natsukidad 7b = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/b.png")
image natsukidad 7c = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/c.png")
image natsukidad 7d = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/d.png")
image natsukidad 7e = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/e.png")
image natsukidad 7f = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/f.png")
image natsukidad 7g = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/g.png")
image natsukidad 7h = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/h.png")
image natsukidad 7i = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/i.png")
image natsukidad 7j = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/j.png")
image natsukidad 7k = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/k.png")
image natsukidad 7l = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/l.png")
image natsukidad 7m = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/m.png")
image natsukidad 7n = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/n.png")
image natsukidad 7o = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/o.png")
image natsukidad 7p = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/p.png")
image natsukidad 7q = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/q.png")
image natsukidad 7r = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/r.png")
image natsukidad 7s = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/s.png")
image natsukidad 7t = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/t.png")
image natsukidad 7u = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/u.png")
image natsukidad 7v = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/v.png")
image natsukidad 7w = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a2.png")
image natsukidad 7x = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/aB.png")

### Bottle Poses (With drunk blush) ###

image natsukidad 6ad = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/db.png")
image natsukidad 6bd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/db.png")
image natsukidad 6cd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/db.png")
image natsukidad 6dd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/db.png")
image natsukidad 6ed = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/db.png")
image natsukidad 6fd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/db.png")
image natsukidad 6gd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/db.png")
image natsukidad 6hd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/db.png")
image natsukidad 6id = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/db.png")
image natsukidad 6jd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/db.png")
image natsukidad 6kd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/db.png")
image natsukidad 6ld = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/db.png")
image natsukidad 6md = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/db.png")
image natsukidad 6nd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/db.png")
image natsukidad 6od = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/db.png")
image natsukidad 6pd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/db.png")
image natsukidad 6qd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/db.png")
image natsukidad 6rd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/db.png")
image natsukidad 6sd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/db.png")
image natsukidad 6td = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/db.png")
image natsukidad 6ud = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/db.png")
image natsukidad 6vd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/db.png")
image natsukidad 6wd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/db.png")
image natsukidad 6xd = im.Composite((960, 960), (0, 0), "natsukidad/1r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/db.png")

image natsukidad 7ad = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a.png", (0, 0), "natsukidad/db.png")
image natsukidad 7bd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/b.png", (0, 0), "natsukidad/db.png")
image natsukidad 7cd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/c.png", (0, 0), "natsukidad/db.png")
image natsukidad 7dd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/d.png", (0, 0), "natsukidad/db.png")
image natsukidad 7ed = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/e.png", (0, 0), "natsukidad/db.png")
image natsukidad 7fd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/f.png", (0, 0), "natsukidad/db.png")
image natsukidad 7gd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/g.png", (0, 0), "natsukidad/db.png")
image natsukidad 7hd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/h.png", (0, 0), "natsukidad/db.png")
image natsukidad 7id = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/i.png", (0, 0), "natsukidad/db.png")
image natsukidad 7jd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/j.png", (0, 0), "natsukidad/db.png")
image natsukidad 7kd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/k.png", (0, 0), "natsukidad/db.png")
image natsukidad 7ld = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/l.png", (0, 0), "natsukidad/db.png")
image natsukidad 7md = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/m.png", (0, 0), "natsukidad/db.png")
image natsukidad 7nd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/n.png", (0, 0), "natsukidad/db.png")
image natsukidad 7od = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/o.png", (0, 0), "natsukidad/db.png")
image natsukidad 7pd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/p.png", (0, 0), "natsukidad/db.png")
image natsukidad 7qd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/q.png", (0, 0), "natsukidad/db.png")
image natsukidad 7rd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/r.png", (0, 0), "natsukidad/db.png")
image natsukidad 7sd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/s.png", (0, 0), "natsukidad/db.png")
image natsukidad 7td = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/t.png", (0, 0), "natsukidad/db.png")
image natsukidad 7ud = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/u.png", (0, 0), "natsukidad/db.png")
image natsukidad 7vd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/v.png", (0, 0), "natsukidad/db.png")
image natsukidad 7wd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/a2.png", (0, 0), "natsukidad/db.png")
image natsukidad 7xd = im.Composite((960, 960), (0, 0), "natsukidad/2r.png", (0, 0), "natsukidad/4l.png", (0, 0), "natsukidad/aB.png", (0, 0), "natsukidad/db.png")

### Name definitions ###

define nd = DynamicCharacter('nd_name', image='natsukidad', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default nd_name = "Nat's Dad"

######################################################
#DDLC-MC v2 by Childish_N
image mc2 1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 1a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 1b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 1c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 1d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 1e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 1f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 1g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 1h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 1i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 1j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 1k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 1l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 1m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 1n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 1o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 1p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 1q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 1r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 1s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 1t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 1u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 1v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 1w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 1x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 1y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 1z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 1error = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 1error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 1shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 2 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 2a = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 2b = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 2c = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 2d = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 2e = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 2f = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 2g = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 2h = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 2i = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 2j = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 2k = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 2l = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 2m = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 2n = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 2o = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 2p = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 2q = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 2r = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 2s = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 2t = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 2u = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 2v = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 2w = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 2x = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 2y = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 2z = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 2error = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 2error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 2shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/1l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 3 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 3a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 3b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 3c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 3d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 3e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 3f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 3g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 3h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 3i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 3j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 3k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 3l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 3m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 3n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 3o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 3p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 3q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 3r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 3s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 3t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 3u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 3v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 3w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 3x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 3y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 3z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 3error = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 3error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 3shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/1r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 4 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 4a = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/a.png")
image mc2 4b = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/b.png")
image mc2 4c = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/c.png")
image mc2 4d = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/d.png")
image mc2 4e = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/e.png")
image mc2 4f = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/f.png")
image mc2 4g = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/g.png")
image mc2 4h = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/h.png")
image mc2 4i = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/i.png")
image mc2 4j = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/j.png")
image mc2 4k = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/k.png")
image mc2 4l = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/l.png")
image mc2 4m = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/m.png")
image mc2 4n = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/n.png")
image mc2 4o = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/o.png")
image mc2 4p = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/p.png")
image mc2 4q = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/q.png")
image mc2 4r = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/r.png")
image mc2 4s = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/s.png")
image mc2 4t = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/t.png")
image mc2 4u = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/u.png")
image mc2 4v = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/v.png")
image mc2 4w = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/w.png")
image mc2 4x = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/x.png")
image mc2 4y = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/y.png")
image mc2 4z = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/z.png")
image mc2 4error = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error.png")
image mc2 4error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 4shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/2l.png", (0, 0), "mod_assets/mc/2r.png", (0, 0), "mod_assets/mc/shock.png")

image mc2 5 = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")
image mc2 5a = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/a.png")
image mc2 5b = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/b.png")
image mc2 5c = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/c.png")
image mc2 5d = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/d.png")
image mc2 5e = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/e.png")
image mc2 5f = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/f.png")
image mc2 5g = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/g.png")
image mc2 5h = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/h.png")
image mc2 5i = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/i.png")
image mc2 5j = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/j.png")
image mc2 5k = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/k.png")
image mc2 5l = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/l.png")
image mc2 5m = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/m.png")
image mc2 5n = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/n.png")
image mc2 5o = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/o.png")
image mc2 5p = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/p.png")
image mc2 5q = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/q.png")
image mc2 5r = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/r.png")
image mc2 5s = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/s.png")
image mc2 5t = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/t.png")
image mc2 5u = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/u.png")
image mc2 5v = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/v.png")
image mc2 5w = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/w.png")
image mc2 5x = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/x.png")
image mc2 5y = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/y.png")
image mc2 5z = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/z.png")
image mc2 5error = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/error.png")
image mc2 5error1 = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/error1.png")
image mc2 5shock = im.Composite((960, 960), (0, 0), "mod_assets/mc/3.png", (0, 0), "mod_assets/mc/shock.png")

image mc2_glitch: #MC GLITCH SPRITE
    choice:
        "mod_assets/mc/old/1.png"
    choice:
        "mod_assets/mc/old/2.png"
    choice:
        "mod_assets/mc/old/3.png"
    choice:
        "mod_assets/mc/old/4.png"
    choice:
        "mod_assets/mc/old/5.png"
    0.15
    repeat

default chosen_character = ""
