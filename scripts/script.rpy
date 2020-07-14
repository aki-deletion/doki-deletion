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
    
    "I wake up, startled."
    m "It was... A dream?!"
    "I sigh, relieved."
    m "Phew... What a dream {i}that{/i} was though..."
return
