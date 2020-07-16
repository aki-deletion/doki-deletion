label start:
# Day 1: Monday
    "Disclaimer: This story starts at the end of the first club meeting."
    scene black
    play sound "sfx/giggle.ogg"
    "???" "AHHHH STOP!!!"
    play sound "sfx/slap.ogg"
    scene club_day
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

    scene residential_day
    with wipeleft_scene
    play music t2
    $ mc_name = "Monika"
    $ m_name = "Author"
    "I sigh, thinking."
    "Why is life so normal?"
    "Yet even still, everything is so stressful."
    "But..."
    mc "It's boring."
    mc "Why can't it change for once?!"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    hide screen tear

    scene mon_house_bedroom
    with wipeleft_scene
    play music t10
    mc "Ah, home at last."
    "I flop down onto my bed."
    "It's so comfy..."
    "Ah, I could just stay like this forever..."
    mc "That sounds nice..."
    "No school, no club... No stress."
    "That'd be perfect."
    mc "{i}Sigh...{/i}"
    play sound knock
    stop music
    mc "...Huh?"
    "That's odd."
    "It must be at least 5pm..."
    "Who would be knocking at this time?"

    scene black
    play sound "sfx/closet_open.ogg"
    mc "WHAT THE?!"
    play sound "sfx/giggle.ogg"
    play sound scream
    
    #Day 2: Tuesday
    scene mon_house_bedroom
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
    show sayori u122111 zorder 1 at t11
    s "Hey Monika!!!"
    "I sigh."
    m "Hey Sayo--"
    m "Waaaait...{nw}"
    show sayori u114222
    extend " Since when did you start coming early?!"
    s t1221 "Umm..."
    s "Ehehe..."
    "I laugh, putting my hands on my hips."
    m "Oh, Sayori!!"
    m "What {i}has{/i} gotten into you?!"
    s u122111 "Weeeeell..."
    s "Shouldn't you be proud I got up early today!!"
    m "Wow Sayori I'm so happy for you~"
    m "I told ya not to let that depression bring you down~!"
    s u222141 "Yeah!!"
    m "Ahaha~"
    "Just then, the door opens."
    play sound closet_open
    show sayori u111111 zorder 1 at t31
    show yuri u122111 zorder 2 at t32
    show natsuki u122143 zorder 3 at t33
    n "Heeeey people, guess who's heeeeeere~!"
    s u112222 "Heeey Natsuki!!"
    show sayori at h31 behind natsuki
    "Sayori rushes up to hug Natsuki."
    show yuri su1121
    "Strangely enough, Natsuki hugs her back, instead of pushing her away as usual."
    m "Huh... Strange."
    y su3121 "H-Hello... Monika, Sayori."
    m "Welcome back Yuri~"
    s "Yuuuuriii!"
    show sayori behind Yuri
    "Sayori knocks Yuri over{nw}"
    show yuri u178335
    show sayori u227262
    extend "in her rush to hug everyone."
    "I laugh."
    hide natsuki
    show sayori zorder 1 at t21
    show yuri zorder 2 at t22
    stop music fadeout 2.0
    play music t10
    s "O-Oh no... Are you okay?!"
    y u124222 "I-I'm fine... It's fine..."
    s u124252 "I didn't mean to knock into you..."
    s u127252 "I just w-wanted to h-help m-make you f-feel w-welcomed a-and--"
    "Yuri wipes a tear from Sayori's eye."
    show yuri u272223 behind sayori
    show sayori u11333
    y "Sh... It's okay..."
    y u171223 "Everything will be okay..."
    y u172223 "I forgive you, Sayori~"
    show sayori u121321 at l21
    show yuri at t21
    s "Thanks Yuri..."
    y "You're welcome."
    hide sayori
    hide yuri
    stop music fadeout 2.0
    show natsuki u124233 zorder 1 at s11
    n "..."
    "Me and Natsuki exchange glances."
    n "..."
    show natsuki u113213
    n "...Can you...!"
    "I shake my head."
    m "I can't believe it either..."
    show natsuki u228143
    "Suddenly Natsuki bursts into laughter."
    m "Wh-What the hell is wrong with you?!"
    n u128183 "Sh-She...!"
    n "I totally ship them!!"
    m "Natsuki don't talk so loud!!"
    "But alas, it was too late."
    play music t7
    "Sayori and Yuri walk over, looking all-the-more flustered after hearing Natsuki's exclaimation."
    show sayori t2221 zorder 1 at t31
    show natsuki u113213 zorder 2 at t32
    show yuri su4232 zorder 3 at t33
    s "H-Hey... Natsuki, Monika."
    y "Wh-What were you guys saying... About us?"
    "I sigh, crossing my arms."
    m "It was Natsuki! I had nothing to do with it!!"
    n xul "H-Hey I didn't... I mean--"
    s u122111 "Hey there's no need to worry Natsuki~ We were only joking!"
    y u112111 "Yes th-that's right..."
    n u122113 "Hah I knew it!!"
    n u121113 "You bakas!"
    "Everyone laughs."
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
return
