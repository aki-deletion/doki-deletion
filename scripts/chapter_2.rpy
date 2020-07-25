label ch2:
    $ s_points = 0
    $ n_points = 0
    $ y_points = 0
    $ mc_points = 0

    scene black
    stop music fadeout 2.0
    mc "It's okay..."
    mc "Let it all out..."
    window hide
    pause 2.5
    "We stay like this for some time, [player] cradling me in his arms..."
    m "..."
    m "*sniff*"
    window hide
    pause 1.5

    scene residential_day
    with fade
    show mc 1m zorder 1 at h11
    pause 1.5
    show mc 1n at s11
    pause 1.5
    "When I look up, [player] looks... calm."
    "Which makes me panic even more."
    "Is this normal!? I've never felt true love before..."
    "But it's so nice..."
    window hide
    pause 1.0
    show mc 2j at h11
    pause 1.5
    mc "...Monika?"
    "Snapping out of my trance, I hastily wipe my eyes on my sleeve."
    m "I-I'm fine... It's fine..."
    m "I'm okay..."
    show mc 2c at h11
    mc "You sure?"
    "I nod weakly."
    window hide
    pause 1.0
    show mc 3g at s11
    pause 1.5
    mc "As long as you're sure..."
    "I nod again."
    m "Yep~ I'm sure."

    scene black
    "We walk the rest of the way in awkward silence."
    "Eventually, we cut off into our seperate classes."

    scene bg class_day
    with wipeleft
    play music t2
    "Ah, another school day ended."
    "As I pack up my stuff, my mind drifts back to this morning..."
    m "Ahh..."
    m "He's sooooo cute~"
    "???" "Who is?!"
    "Startled, I whisk around."
    show sayori turned lup happ om oe zorder 1 at h11
    s "Heeeey my girl~"
    show sayori turned lup rup happ om ce at h11
    s "How's it going sis?!"
    "I laugh."
    m "Um..."
    m "I'm not your sister or your girl, Sayori."
    show sayori turned lup laug cm oe at h11
    s "I knooooow~"
    s "It's a joke~!"
    m "{i}Ohhhhhhhh!!!{/i}"
    window hide
    pause 1.0
    show sayori turned lup happ om oe at h11
    pause 1.5
    show sayori turned lup rup laug om oe at h11
    pause 1.5
    "We both laugh."
    s 1a "Sooo, wanna come to the club?"
    "I nod."
    m "I wouldn't miss it for the world~"

    scene bg club_day
    with wipeleft
    play sound closet_open
    play music t3
    show sayori turned om ce zorder 1 at h41
    show yuri turned lup rup happ om oe zorder 2 at h42
    show natsuki cross ff happ om oe zorder 3 at h43
    show mc 1a zorder 4 at h44
    pause 1.5
    "All" "Hey Monika~"
    m "Hey guys!"
    m "You all seem happy today~"
    show natsuki turned happ om ce at h43
    show yuri turned lup happ om ce at h42
    show mc 1o at h44
    pause 1.5
    n "That's because we {i}are,{/i} baka!!"
    s "We've got something special for you Monika~"
    mc "Th-This wasn't my idea I swear!!"
    "Hmm...?"
    m "Okay..."
    m "Go ahead."
    window hide
    hide yuri
    hide sayori
    hide natsuki
    show mc 1m zorder 1 at h11
    pause 1.5
    show mc 3n at h11
    pause 1.5
    mc "{i}We're no strangers to looooove~{/i}"
    mc "{i}You know the ruuules and so doooo I~{/i}"
    show mc 1o at h11
    mc "{i}A full commitment's what I'm thinking ooofffff~{/i}"
    mc "Ya wouldn't get this from any other guuyyy~"
    "I laugh."
    m "Did you just--"
    show mc 2p at s11
    mc "Maybe~"
    show mc 1m at s11
    "[player] grabs my hand."
    m "Wh-What are yo--"
    mc "Shh..."
    show mc 1n at h11
    mc "It's okay..."
    mc "I love you..."

    window hide
    scene black
    with dissolve
    pause 3.0
    mc "Chu~"
    window hide
    pause 3.0

    scene bg club_day
    show mc 2n zorder 1 at h41
    show sayori turned rup happ om oe zorder 2 at h42
    show natsuki turned rhip happ cm ce zorder 3 at h43
    show yuri turned rup happ cm ce zorder 4 at h44
    pause 1.5
    "All" "..."
    m "...[player]..."
    "Tears blur my vision."
    m "Oh [player], not again..."
    "I jump into his welcoming arms."

    window hide
    scene bg club_day2
    with dissolve_scene_full
    show sayori turned lup rup lsur om oe zorder 1 at s31
    show yuri shy neut n5 zorder 2 at h32
    show natsuki turned shoc cm oe zorder 3 at h33
    "Sayori, Yuri, Natsuki" "...!!!"
    s "N-No way..."
    n turned shoc cm ce "L-Look away... I'm not looking!!"
    window hide
    pause 1.0
    show yuri turned lup rup cry cm ce at s32
    show natsuki turned lhip rhip anno om oe at h33
    n "Why are you {i}crying{/i} Yuri?!"
    show sayori turned rup lsur cm oe at h31
    show yuri turned lup cry cm oe at h32
    y "I-It just *sobs* so heartwarming *sniffs*"
    show natsuki cross fta at s33
    n "J-Jeez baka..."
    n "Don't make things more uncomfy okay?"
    "Yuri nods."
    "Me and [player] walk over, me wiping my puffy eyes on my blazer jacket and [player] still holding me close."
    show sayori 1a zorder 1 at h41
    show yuri 1a zorder 2 at h42
    show natsuki 1a zorder 3 at h43
    show mc 1a zorder 4 at l44
    m "Hey girls..."
    show mc 2g at s44
    "[player] goes up to Yuri."
    mc "Hey Yuri... Don't cry."
    show mc 1a
    mc "You don't want me to cry too, right?"
    show yuri 1b at s42
    y "Y-yes..."
    y "Thank you [player]..."
    show mc 3c at h44
    mc "Don't mention it ahaha."

    hide sayori
    hide yuri
    hide natsuki
    hide mc

    "We continue our daily activities."
    "Natsuki reading manga in the corner,"
    "Yuri preparing tea,"
    "and Sayori chatting away to [player]."
    "This is all normal..."
    window hide
    menu girls_choice_clubroom_day1:
        "What are MC and Sayori talking about?":
            $ s_points += 5
            $ mc_points += 5
            jump mc_sayori_talk
        "Looks like Natsuki has a new manga":
            $ n_points += 5
            jump natsuki_manga

label mc_sayori_talk:
    "Come to think of it..."
    "I somehow feel kinda {i}jealous.{/i}"
    "Even though I know [player] loves me..."
    "He's just always hanging around with the other girls."
    "It just doesn't seem fair..."
    m "But then again, it's not fair to take them away from him either..."
    "Dammit I'm stuck in a loophole!!"
    "Sighing, I stand up, heading over to them."
    window hide
    show sayori turned lup rup happ om ce zorder 1 at h21
    show mc 2l zorder 2 at h22
    pause 1.5
    s "And then I said, Omigosh come on Monikaaaa!! We're gonna be laaaaate!!"
    show mc 1l at h22
    mc "Ahaha~ So Monika used to be not-so-athletic, huh?"
    show sayori turned lup happ om oe
    s "Yeah!!"
    s "She was worse than me ahaha~"
    show mc 2j at s22
    mc "U-Umm Sayori..."
    show sayori turned lup rup curi om oe at h21
    s "Hm--"
    window hide
    pause 1.0
    show sayori turned lup rup lsur cm oe at h21
    pause 1.5
    show sayori turned lup rup pani om oe at h21
    pause 1.5
    s "M-Monika?!"
    "I sigh, crossing my arms."
    m "So... {nw}"
    show sayori turned lup pani cm oe at s21
    show mc 3e at s22
    extend "Do you remember how I told you,"
    m "What would happen if you told anyone about that incident?"
    pause 1.0
    show sayori turned lup pani om ce at h21
    pause 1.5
    s "I'm so sorry Monika!!"
    show mc 2h at h22
    mc "Monika, I forced it outta her!!"
    mc "You can't punish he--"
    "I laugh."
    m "Jeez, you really think I give a fuck Sayori?"
    window hide
    pause 1.0
    show sayori turned lsur cm oe at h21
    show mc 1m at s22
    pause 1.5
    show sayori turned happ om ce at h21
    pause 1.5
    s "Oh Monika!!"
    s "You're so dumb!!"
    show mc 1a at h22
    mc "Yeah~"
    m "Not as dumb as {i}you both.{/i}"
    "I flick my hair and walk away, {nw}"
    hide mc
    hide sayori
    extend "leaving the two dummies to rattle on about their little gossips."
    "Gosh... They're so babyish sometimes."
    "But that's why I love them~"
    window hide
    pause 1.5
    call end_meeting_day1

label natsuki_manga:
    m "Hmm..."
    m "I wonder what Natsuki is reading today."
    "I walk over to the pink-haired girl, {nw}"
    show natsuki turned ff neut cm oe zorder 1 at s11
    extend "who's silently reading in a corner."
    "At first she doesn't seem to notice my presence."
    pause 1.5
    m "...Natsuki?"
    window hide
    pause 1.0
    show natsuki turned ff pani om ce at h11
    pause 1.5
    "Natsuki, startled, throws her book in the air, {nw}"
    show natsuki at t21
    show yuri turned lup rup pani om oe zorder 2 at h22
    extend "which lands on Yuri, knocking her tea over."
    window hide
    pause 1.0
    show natsuki turned pani om oe at h21
    show yuri turned pani cm oe at h22
    pause 1.5
    "Before I can move out the way, the brown liquid spills all over me."
    window hide
    pause 1.0
    show natsuki turned pani cm ce at h21
    show yuri turned nerv cm oe at h22
    pause 1.5
    n "M-Monika!!"
    n "I'm so sorry!!!"
    m "...Yuck..."
    show yuri turned nerv cm ce at s22
    y "I-I'll go grab a towel..."
    window hide
    pause 1.0
    show yuri zorder 1 at lhide
    hide yuri
    show natsuki cross flus cm oe at h11
    pause 1.5
    m "Natsuki..."
    m "I didn't mean to scare you."
    m "This is my fault..."
    window hide
    pause 1.0
    show natsuki cross angr om oe at h11
    pause 1.5
    n "Ya think?"
    show natsuki turned rhip angr om ce at h11
    n "The only reason we got into this mess is because of you!!"
    "I chuckle."
    m "I guess..."
    window hide
    pause 1.0
    show natsuki cross fta at s11
    n "Hmph!"
    window hide
    pause 1.0
    show natsuki at t21
    show yuri turned lup rup flus om oe zorder 2 at l22
    pause 1.5
    y "Here you go, Monika."
    "I gratefully grab the towel and begin drying myself."
    m "Thank you, Yuri."
    show yuri 1a at h22
    y "You're welcome, Monika."
    "I stand up."
    m "Well, I'd better go get chance."
    show natsuki 1a at h21
    "Nat & Yuri" "Okay."
    show natsuki zorder 1 at lhide
    hide natsuki
    show yuri zorder 1 at lhide
    hide yuri
    call end_meeting_day1

label end_meeting_day1:
    window hide
    show sayori 1a zorder 1 at t41
    show natsuki 1a zorder 2 at t42
    show yuri 1a zorder 3 at t43
    show mc 1a zorder 4 at t44
    m "Okay, everyone!"
    m "It seems the day is finally over."
    m "I expect to see you all tomorrow~"
    m "Goodnight!!"
    show sayori zorder 1 at lhide
    hide sayori
    show natsuki zorder 1 at lhide
    hide natsuki
    show yuri zorder 1 at lhide
    hide yuri
    show mc zorder 1 at lhide
    hide mc
    "Everyone heads home."
    "I sigh, packing up my stuff."
    m "I would've at least expected [player] to walk me home..."
    m "..."
    "I lock up the room and head home."

    play music "bgm/credits.ogg"
    "Author" "Thank you all for playing Doki Doki! Deletion: Rewrite!!"
    "Author" "I hope you all enjoyed the gameplay."
    "Author" "Any complaints can go to Project Leader, Yosorro#7096"
    "Author" "Credits can be found in credits.txt, in the game folder."
    "Author" "Part 2 will be released next month, follow u/monipy_inc on Reddit for updates."
    "Author" "I hope you all have a lovely day, and enjoy the classic song 'Your Reality' from best girl Monika."
    "Doki Doki! Deletion: Rewrite!! - Demo v1.0"
    pause 160.0
    window hide
    return
