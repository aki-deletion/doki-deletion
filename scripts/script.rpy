label start:

    $ anticheat = persistent.anticheat


    $ chapter = 0
    $ moni = False


    $ _dismiss_pause = config.developer



    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"


    $ quick_menu = True


    $ style.say_dialogue = style.normal


    $ in_sayori_kill = None


    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 1:
        call day_menu
    else:
        call day_menu
        return

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return

$ confessed = False

label ch1:
    scene black
    stop music fadeout 2.0
    "Disclaimer: This story starts at the end of the first club meeting."
    scene black
    play sound "sfx/giggle.ogg"
    "???" "AHHHH STOP!!!"
    play sound "sfx/slap.ogg"
    scene bg club_day
    play music t3
    show monika 3r at f41
    show natsuki 1u at t42
    show sayori 4u at t43
    show yuri 1b at t44
    m "..."
    m "Let's all go home..."
    m "We've had quite the day."
    "Everyone nods."
    show yuri zorder 1 at lhide
    hide yuri
    show sayori zorder 1 at lhide
    hide sayori
    show natsuki zorder 1 at lhide
    hide natsuki
    show monika 4q zorder 1 at t11
    "Everyone leaves."
    "I walk up to Monika, who seems clearly stressed out."
    mc "M-Monika?"
    m 2d "Oh hey [player]."
    m "Why don't you head on home?"
    m "It'll be better for all of us if we rest."
    "I nod."
    mc "Okay..."
    mc "Bye."
    "I leave the room and head home."

    scene black
    with dissolve
    "???" "Hello, [player]."
    "???" "This is the author here, and I'm just here to explain a few things."
    show monika 5a
    "Author" "See Monika?"
    "Author" "You're going to be playing as her now."
    "Author" "Why, you ask?"
    "Author" "Hah, you'll see."
    "Author" "That's all I needed to tell you for now."
    "Author" "This is the author signing out."

    scene bg residential_day
    with wipeleft_scene
    play music t2
    "I sigh, thinking."
    "Why is life so normal?"
    "Yet even still, everything is so stressful."
    "But..."
    m "It's boring."
    m "Why can't it change for once?!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    hide screen tear

    scene mon_bedroom_day
    with wipeleft_scene
    play music t10
    m "Ah, home at last."
    "I flop down onto my bed."
    "It's so comfy..."
    "Ah, I could just stay like this forever..."
    m "That sounds nice..."
    "No school, no club... No stress."
    "That'd be perfect."
    m "{i}Sigh...{/i}"
    play sound knock
    stop music
    m "...Huh?"
    "That's odd."
    "It must be at least 5pm..."
    "Who would be knocking at this time?"

    scene black
    play sound closet_open
    m "WHAT THE?!"
    play sound "sfx/giggle.ogg"
    m "AAAAAAAAAAAAAAAAAAHHHHH!!!"


    scene mon_bedroom_day
    "I wake up with a start."
    m "What the...?"
    "Wait..."
    "It was a dream?!"
    m "Yes it was a dream!!"
    "Although a pretty weird one... But still!"
    m "I am so happy!!"
    "I jump out of bed and begin to get ready, fuelled by the adrenaline the dream gave me."
    m "Today is gonna be a good day!!"
    m "I know it shall!!"

    scene bg club_day
    play music t3
    show sayori turned ldown rup happ cm ce zorder 1 at t11
    s "Hey Monika!!!"
    "I sigh."
    m "Hey Sayo--"
    m "Waaaait...{nw}"
    show sayori tap nerv cm oe
    extend " Since when did you start coming early?!"
    s tap nerv om oe "Umm..."
    s "Ehehe..."
    "I laugh, putting my hands on my hips."
    m "Oh, Sayori!!"
    m "What {i}has{/i} gotten into you?!"
    s turned lup rup happ om ce "Weeeeell..."
    s "Shouldn't you be proud I got up early today!!"
    m "Wow Sayori I'm so happy for you~"
    m "I told ya not to let that depression bring you down~!"
    s turned lup rdown happ om ce "Yeah!!"
    m "Ahaha~"
    "Just then, the door opens."
    play sound closet_open
    show sayori turned neut ma e1a b1a zorder 1 at t31
    show yuri shy happ cm oe zorder 2 at t32
    show natsuki turned lhip happ om oe zorder 3 at t33
    n "Heeeey people, guess who's heeeeeere~!"
    s turned lup rup happ om ce "Heeey Natsuki!!"
    show sayori behind natsuki at h31
    "Sayori rushes up to hug Natsuki."
    show yuri shy neut cm ce
    "Strangely enough, Natsuki hugs her back, instead of pushing her away as usual."
    m "Huh... Strange."
    y shy neut m3 e4 "H-Hello... Monika, Sayori."
    m "Welcome back Yuri~"
    s "Yuuuuriii!"
    show sayori behind Yuri
    "Sayori knocks Yuri over{nw}"
    show yuri turned lup rup flus cm oe at h32
    show sayori turned vsur om ce at h31
    extend "in her rush to hug everyone."
    "I laugh."
    hide natsuki
    show sayori zorder 1 at t21
    show yuri zorder 2 at t22
    stop music fadeout 2.0
    play music t10
    s "O-Oh no... Are you okay?!"
    y turned lup flus om oe "I-I'm fine... It's fine..."
    s turned lup rup flus cm oe "I didn't mean to knock into you..."
    s turned lup cry om oe "I just w-wanted to h-help m-make you f-feel w-welcomed a-and--"
    "Yuri wipes a tear from Sayori's eye."
    show yuri turned neut mf e1a behind sayori
    show sayori turned lup rup pani om oe at h21
    y "Sh... It's okay..."
    show sayori turned sedu cm oe
    y turned neut mb "Everything will be okay..."
    y "I forgive you, Sayori~"
    show sayori turned shoc om ce at t21
    show yuri turned lsur om oe at t22
    s "Thanks Yuri..."
    y turned lup rup neut mn e2b "You're welcome."
    hide sayori
    hide yuri
    stop music fadeout 2.0
    show natsuki turned neut me e1c zorder 1 at s11
    n "..."
    "Me and Natsuki exchange glances."
    n "..."
    show natsuki turned neut mn at h11
    n "...Can you...!"
    "I shake my head."
    m "I can't believe it either..."
    show natsuki turned neut mr e4b
    "Suddenly Natsuki bursts into laughter."
    m "Wh-What the hell is wrong with you?!"
    n "Sh-She...!"
    n "I totally ship them!!"
    m "Natsuki don't talk so loud!!"
    "But alas, it was too late."
    play music t7
    "Sayori and Yuri walk over, looking all-the-more flustered after hearing Natsuki's exclaimation."
    show sayori turned lup worr om oe zorder 1 at t31
    show natsuki turned lhip rhip flus cm oe zorder 2 at t32
    show yuri turned anno cm oe zorder 3 at t33
    s "H-Hey... Natsuki, Monika."
    y "Wh-What were you guys saying... About us?"
    "I sigh, crossing my arms."
    m "It was Natsuki! I had nothing to do with it!!"
    n cross angr om oe "H-Hey I didn't... I mean--"
    s turned happ om oe "Hey there's no need to worry Natsuki~ We were only joking!"
    y turned happ om oe "Yes th-that's right..."
    n turned lhip rhip happ om ce "Hah I knew it!!"
    n "You bakas!"
    "Everyone laughs."

    hide window
    stop music fadeout 2.0
    play music t3
    hide sayori
    hide natsuki
    hide yuri
    "We all settle down into our daily activities."
    "Yuri reading her book,"
    "Natsuki fishing for manga in the closet,"
    "And Sayori sitting in her desk writing."
    "This is all normal..."
    m "But to be honest, I like it this way."

    "Soon enough, it's home time."
    "As we all pack our things ready to go, Sayori bounces up to me."
    show sayori turned lup rup neut mb
    s "Hey, Monika~"
    "I wave."
    m "Hey Sayori! What's up?"
    show sayori turned lup nerv mf e1c
    s "Well... It's actually..."
    m "Hmm?"
    stop music
    s tap dist om oe "It's about [player]."
    m "...What?"
    m "What about him?"
    s tap nerv m4 e2 b3 "Weeeeell... He's in a bit of a hard spot right now."
    "I gulp."
    m "Wh-what do you mean...?"
    s turned rup nerv om oe "He's..."
    s turned lup rup nerv om ce "He's kinda..."
    s "...On puberty..."
    "I laugh."
    m "Oh come on Sayori, we're all on puberty!!"
    s turned pani cm oe "..."
    m "..."
    s turned nerv om ce "...Monika..."
    s "[player] is 15..."
    s "And he's only just started puberty..."
    s turned nerv cm ce "Add it all up..."
    m "...!!!"
    m "Omigosh!!"
    show sayori tap om oe
    m "Sayori!! Why didn't you tell me before?!"
    s turned angr om ce "You should've known!!"
    play music t7
    s "It's not my fault you don't pay attention to anything!!"
    m "..."
    m "You..."
    m "Of course I pay attention!!"
    m "Are you implying I don't care about [player]?!"
    s tap angr om ce "YES!!!"
    s turned cry om ce "You always ignore him!!"
    show sayori turned cry cm oe at s11
    s "I thought you loved him..."
    stop music fadeout 2.0
    m "..."
    m "Sayori..."
    s turned anno cm oe "Look..."
    s turned anno om oe "If you really care about [player]..."
    s "Then come round his house tonight."
    s "I won't come, so you can have some time alone."
    s turned angr cm oe "Don't let me down, Monika."
    show sayori zorder 1 at lhide
    hide sayori
    "..."
    m "Did she just..."
    "It's the truth."
    "Right?"
    "I need to see [player]."
    m "I do love him..."
    m "I really do."

    window hide
    pause 1.5

    scene bg bedroom
    with wipeleft
    play music t9
    show mc 5d zorder 1 at t11
    mc "So..."
    mc "..."
    m "..."
    "Why is it so awkward?"
    "It's not... It's not meant to be like this!!"
    "I need to save this situation!!!"
    m "So, Sayori told me you just started puberty..."
    show mc 5i at h11
    mc "What?!"
    show mc 2m
    mc "Oh, {i}Sayori{/i} ..."
    mc "Do you really believe whatever shit she comes out with, Monika?"
    m "...Hm...?"
    "...Wait..."
    m "{i}Ohhhh!!!{/i}"
    m "So she {i}lied?!{/i}"
    show mc 5j at h11
    mc "What?"
    mc "It wasn't a {i}lie{/i} exactly..."
    m "Oh {i}really?{/i}"
    show mc 2k
    mc "Yeah..."
    mc "She just likes exaggerating the truth, that's all~"
    m "..."
    m "...Exaggerating?"
    show mc 1l
    mc "Yeah!"
    mc "She's always been like it."
    m "Well, yeah I guess..."
    m "I-I guess she has!!"
    "I laugh at my own stupidity."
    m "Yeah, I knew it was pretty hard to believe..."
    show mc 5n
    mc "W-Well..."
    mc "She must've {i}wanted{/i} you to come round for some reason..."
    m "Hmm...?"
    m "To be honest, I kinda expect her to jump out your closet with a camera."
    show mc 2k
    mc "Yeah, true."
    mc "She can be like that sometimes..."
    show mc 2l
    mc "But it's all in fun, right?!"
    "I nod."
    m "Right!!"
    show mc 1a
    mc "Anyway, I'll probably be back at school tomorrow."
    m "Really?"
    show mc 2k
    mc "Yeah!"
    m "Which brings me onto the question..."
    show mc 5g
    mc "Why wasn't I at school? Right..."
    show mc 2j
    mc "I was kinda poorly today..."
    "I gasp."
    m "W-Well that makes sense..."
    m "Oh, I'm sorry I should've seen you sooner..."
    show mc 2l
    mc "Oh don't worry about {i}that{/i} ..."
    show mc 1l
    mc "I really didn't mind~"
    show mc 2k
    mc "In fact, it was quite nice having some time to myself~!"
    m "Oh yeah true."
    m "Sometimes we all need time alone right?"
    show mc 5k
    mc "Of course!!"
    m "Anyway... It's getting pretty late."
    m "I'd best get going."
    show mc 1a
    mc "You sure?"
    m "Yeah..."
    show mc 5a
    mc "Well okay..."
    show mc 2n
    mc "Once again, thanks for coming."
    m "You're welcome!"

    window hide
    pause 1.5
    stop music fadeout 2.0

    scene bg residential_rain
    with wipeleft_scene
    "I step outside."
    m "Ah crap, it's raining {i}again...{/i}"
    "Wrapping my blazer around me and holding my bag over my head, I run out into the downfall."

    scene bg bridge_night
    with wipeleft_scene
    "It's stopped raining by the time I get halfway home."
    m "Why does [player] live so damn far...!"
    "Ugh, I'm still soaked."
    "Trudging through the cold night, I pass the bridge."
    m "Huh...?"
    "I look over the side."
    "..."
    m "Maybe..."
    "NO!"
    "WHAT AM I THINKING?!"
    m "Sayonara..."
    "NOOOOO--"
    "I jump over the edge."

    scene bg ocean
    with dissolve_scene_full
    "WHAT AM I DOING?!"
    "I CAN'T SWIM!!!"
    "I try to kick upwards,"
    "But it's no use."
    "This is my end."
    "As the world fades away around me, the last thing I see is a figure with purple hair on the corner of my eye."

    window hide
    scene white
    show yuri shy casual neut n2 m4 e3 zorder 1 at t11
    y "...Monika?"
    y "Monika wake up!!"
    show yuri shy casual neut n5 at s11
    y "*sobs* D-Don't leave me..."
    y "P-Please..."
    y "*cries hysterically*"
    show yuri turned casual cry cm ce at h11
    y "PLEASE MONIKA!!"
    y "WAKE UP!!!"
    "???" "Yuri don't shout!!"
    show yuri turned casual cry cm oe zorder 2 at s22
    show natsuki turned casual cry om oe zorder 1 at s21
    n "Y-Yuri *sobs* don't disturb the other p-patients *sniffs*"
    show yuri shy casual neut n5
    y "She's dead Natsuki..."
    y "Can't you hear it?"
    n turned casual cry cm ce "Hear what...?"
    show yuri turned casual cry om oe
    y "Exactly!!"
    y "She has no heart rate..."
    y "So the machine stopped beeping."
    window hide
    pause 1.0
    show natsuki turned casual cry om ce at s21
    show yuri turned casual cry cm oe at s22
    pause 1.5
    show natsuki zorder 2 at s32
    show yuri zorder 3 at s33
    show sayori turned casual lup cry cm oe zorder 1 at s31
    s "I couldn't find anyone who could help..."
    y "It's okay Sayori..."
    y "At least you tried."
    window hide
    pause 1.0
    show sayori turned casual lup rup cry cm ce at h11
    pause 1.5
    show natsuki cross fs cm ce at s11
    pause 1.5
    show yuri turned cry cm ce at h11
    pause 1.5
    "All" "We'll miss you, Monika."

    window hide
    scene black
    with fade
    pause 1.0
    play sound "sfx/s_kill_glitch1.ogg"
    "???" "Monika..."
    "..."
    "...Hm?"
    "Where am I?"
    "???" "Monika..."
    "Am I dead?"
    "I jumped off a bridge..."
    "Why?"
    "It's not like I was depressed..."
    "I don't understand."
    "???" "Monika..."
    "Huh?"
    "Someone's calling me?"
    m "Who's there?!"
    "???" "I am God."
    m "HUH?!"
    "God" "I am here to spare your life."
    "What does he mean...?"
    "Wait..."
    m "BUT I DON'T WANNA BE SPARED!!"
    "God" "Monika..."
    "God" "You have got a whole life ahead of you."
    "God" "I shouldn't tell you this but..."
    "God" "[player] loves you..."
    m "WHAT?!"
    m "N-No way..."
    "God" "So do the other girls..."
    "God" "Are you really going to just leave them?"
    m "B-But..."
    "God" "Right now... They are weeping."
    "God" "Do you really want to leave them like that?"
    "God" "Leave them to suffer?"
    m "..."
    "Do I?"
    "I'm not sure..."
    "I never realised..."
    m "No."
    m "Please bring me back."
    "God" "Very well then."
    "God" "GOUTUS!!!"
    "BOOM!"

    scene ward_day
    with dissolve_scene_full
    play music t9
    "I slowly open my eyes."
    "Where am I...?"
    "Wait..."
    m "I'm... Alive?!"
    "???" "*sniff*"
    "Hmm?"
    "I turn around."
    window hide
    pause 1.0
    show natsuki turned fs cry cm ce zorder 1 at h11
    pause 1.5
    show natsuki turned fs cry cm oe at h11
    n "Huh...?"
    window hide
    show natsuki turned ff cry cm oe at s11
    n "M-Monika...?"
    show natsuki turned ff cry cm ce at h11
    "Natsuki rushes up to hug me."
    m "Natsuki..."
    n turned ff cry om ce "M-Monika..."
    n "This is a dream..."
    n "I'm having another dream..."
    n "I--"
    window hide
    show natsuki turned ff angr om oe at h11
    n "OWW!!!"
    n "WHAT'D YOU DO THAT FOR?!"
    "I laugh weakly."
    m "I pinched you."
    m "Now you're not dreaming~"
    "I try my best smile."
    show natsuki cross ff angr om ce at h11
    n "..."
    n "Wh-Whatever baka..."
    m "Oh {i}Natsuki...{/i}"
    play sound closet_open
    show natsuki zorder 1 at t31
    show yuri turned lup neut om oe at l32
    show sayori turned neut cm oe at l33
    y turned lup neut om oe "Nat we got th--"
    window hide
    show yuri turned lsur om oe at h32
    show sayori turned lsur om oe at h33
    pause 1.5
    show sayori turned pani om oe at h33
    show yuri turned pani om oe at h32
    pause 1.5
    m "Umm..."
    m "Hey girls."
    y "..."
    show yuri turned nerv cm oe at s32
    y "M-Monika?!"
    show sayori turned lup rup cry om oe at h33
    s "NO!!"
    s "THIS ISN'T POSSIBLE!!!"
    show natsuki turned rhip angr om oe at h31
    n "Sayori!!"
    n "Don't shout!!"
    show sayori turned lup pout om oe at s33
    s "S-Sorry Natsuki..."
    show natsuki cross neut om oe at h31
    n "Don't mention it."
    show yuri shy neut om oe at s32
    y "So..."
    y "M-Monika..."
    "I sigh."
    m "I dunno how I got out alive either."
    window hide
    show yuri turned lup rup happ om ce at h32
    show natsuki turned hip rhip om oe at h31
    show sayori turned lup rup happ om oe at h33
    "All" "We're glad you're alive though Monika~"

    scene black
    with fade
    stop music fadeout 2.0
    "It's been nearly a month."
    "I fully recovered from my accident, and recently started back at school."
    "I've had fun with all the girls..."
    "Everything is nearly normal."
    "Except..."

    scene bg club_day
    with dissolve_scene_full
    play music t3
    show sayori turned lup rup neut om oe at s11
    s "Hey Monika..."
    "Sayori grabs my arm."
    m "Hm?"
    m "What is it Sayori?"
    show sayori turned lup nerv om oe at h11
    s "Have you seen [player] recently?"
    "I pause, thinking."
    m "Well..."
    m "To be honest, he hasn't been showing up ever since... {nw}"
    show sayori turned lup rup cry cm oe at s11
    extend "y'know..."
    s "Yeah true..."
    s "I'll check on him."
    "I nod."
    m "Thanks Sayori."
    m "I'm sure he'll be fine~"
    s turned rup doub om oe "Yeah... Sure."
    show sayori zorder 1 at lhide
    hide sayori
    stop music fadeout 2.0

    window hide
    scene black
    with wipeleft
    "Try as I might, I couldn't sleep that night."
    m "Mmm..."
    m "I hope [player] is okay..."
    "Jumping out of bed, I hurriedly get dressed and rush for the door."
    window hide
    pause 1.5

    scene house_night
    with wipeleft_scene
    "I stop outside, out of breath."
    m "God..."
    m "Please don't call me here for nothing."
    "I hesitate, before knocking on the door."
    window hide
    pause 1.5
    "No answer."
    "I try the handle,"
    play sound closet_open
    extend " and to my surprise, it opens."
    "I sigh."
    m "It's now or never..."
    "I..."
    "Gently open the door."

    scene bg bedroom
    with wipeleft
    show mc 1o zorder 1 at t11
    mc "{i}--I sold my soul for Poetry,{/i}"
    mc "{i}this hell is members only.{/i}"
    mc "{i}Why did I say Okie Dokiiiiiiiiiee?!{/i}"
    "I slowly back out of the room."
    show mc 1w zorder 1 at h11
    mc "Huh?"
    "I start running."

    scene bg bridge_night
    with dissolve_scene_full
    m "Oh... My... God..."
    "What did I just witness?!"
    "More importantly, why did I run away??"
    "Sighing, I pass the bridge."
    m "Not again..."
    "Shaking my head, I run across it as fast as I can."

    scene mon_bedroom_night
    with wipeleft
    "I get back into my pyjamas, pulling the quilt over me."
    "My heart is thumping."
    "{i}What is wrong with me?!{/i}"
    "Wow..."
    "He loves me..."
    m "I love you too, [player]."
    m "I promise, I won't run away anymore..."
    m "I'll make sure you see the best side of me..."
    m "I really, really love you..."


    scene mon_bedroom_day
    with fade
    "I wake up to the wretched beeping of the alarm."
    "Sighing, I pull myself out of bed."
    m "Hnngh..."
    "Yawning, I begin my daily routine:"
    "Getting dressed, having breakfast, etc."
    m "Nothing has changed..."
    m "It's still boring."
    "I smile to myself."
    m "But it won't be like that for much longer."

    scene bg residential_day
    with wipeleft
    play music t2g2
    "???" "Heeeeeeey~"
    "I see an annoying "
    $ renpy.pause(delay=30.0, hard=True)
    extend "boy running up to me from the distance,"
    "waving his arms around like he's totally oblivious to any attention he might attract."
    "I sigh, thinking of leaving him behind, but instead just waiting on the sidewalk for him to catch up to me."
    show mc 2c zorder 1 at s11
    mc "Ah... I finally caught up with you~"
    "I laugh."
    m "So I {i}guess{/i} you didn't do those excersies I told you?"
    show mc 2h at h11
    mc "W-Well..."
    mc "Ehehe..."
    "I push him playfully."
    m "Oh, [player]!!"
    show mc 1l at h11
    mc "Stooopp ahaha~"
    "We both smile cheesily."
    m "God this is {i}soooo{/i} cliche."
    show mc 2g at s11
    mc "Yeah i guess it is..."
    m "..."
    mc "..."
    pause 1.5
    "Why is this so awkward?!"
    "Aaaaah!!!"
    hide mc
    play music t2g3
    "We carry on walking in silence."
    menu:
        "Confess":
            jump maybe_confession
        "Not now":
            jump dismiss

    label maybe_confession:
        "I stop walking."
        "Now's the time..."
        "Come on Monika, you can do this..."
        m "[player]?"
        window hide
        show mc 1m zorder 1 at h11
        pause 1.5
        show mc 1n at h11
        pause 1.5
        mc "Yes, Monika?"
        "I gulp."
        "Come on, don't miss this chance..."
        menu:
            "I love you, [player]":
                jump mc_confess
            "Umm... Do we have maths today?":
                show mc 3b at s11
                mc "Monika..."
                mc "Why would you ask that?"
                show mc 3l at h11
                mc "Of course we do~"
                "I laugh nervously."
                "Yeah..."
                jump dismiss

    label mc_confess:
        $ confessed = True
        play music t10
        show mc 1o at h11
        mc "Monika..."
        mc "I love you too~"
        "I step back in surprise."
        m "Y-You do?!"
        mc "Yes!!"
        show mc 1m at s11
        mc "I've always loved you..."
        mc "I was just too scared to say it aloud."
        "I sniff."
        m "Oh [player]..."
        show mc 1i at h11
        mc "M-Monika..."
        mc "Are you oka--"
        "I pull him into a hug."

        window hide
        scene black
        with fade
        m "Oh [player]..."
        m "*sniff*"
        mc "...Monika?"
        m "I love you..."
        m "I'm so s-sorry..."
        m "F-For everything..."
        m "*sob*"
        mc "Don't be sorry Monika..."
        mc "I love you too..."
        mc "I forgive you."
        "At this I completely break down."
        m "Why did I jump off that bridge..."
        m "Why..."
        m "I'm sorry..."
        "I'm slobbering into [player]'s arms, but he just holds me, sheilding me from prying eyes of students."
        mc "It's okay..."
        mc "Let it all out..."
        window hide
        pause 3.0
        "End of chapter."
        return


    label dismiss:
        "We continue walking in silence."
        "..."

        scene black
        stop music fadeout 2.0
        "I never got to tell [player] my feelings."
        "{b}Not good Ending.{/b}"

    window hide
    scene black
    with dissolve_scene_full
    call endgame from _call_endgame
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
