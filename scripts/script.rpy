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
        stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t5

    show yuri u224144 at t11 zorder 2

    y "Now where did I put my...?"
    y u222111 "Ah, here we are!"

    window hide
    show yuri u221171 at t11 zorder 2
    pause 0.1
    show yuri u221171g at t11 zorder 2
    with dissolve
    pause 0.25

    y u112113g "Perfect."
    y u112161g "With these, I'll be able to read in style!"

    window hide
    show yuri u111142g at t31 zorder 3
    pause 0.25
    show yuri u111142g at s31 zorder 3
    pause 0.75

    show yuri u113144g

    show natsuki u221111 at t44 zorder 3
    pause 0.25
    show sayori u114131 at t43 zorder 2
    pause 0.25

    show natsuki u222111 at f44 zorder 3

    n "There she is."
    n u222133 "Ready to play a trick on her?"

    show natsuki u221133 at t44 zorder 2
    show sayori t1111 at f43 zorder 3

    s "I don't know, doesn't this seem sort of... mean?"

    show sayori t3221 at t43 zorder 2
    show natsuki u222152 at f44 zorder 3

    n "Don't worry, she's gonna think it's funny!"

    show natsuki u221132 at t44 zorder 2
    show sayori u123112 at f43 zorder 3

    s "Well... Okay, but I'm only gonna do it once."

    window hide
    show sayori u114132 at t43 zorder 3
    pause 0.25

    show sayori u114132 at t42 zorder 2
    pause 0.5

    show natsuki u228132
    show sayori u224164 at s42 zorder 2
    pause 1.25

    show sayori u117344 at h42 zorder 2
    show yuri u113121g
    s "BOO!!!"

    show natsuki u222131
    show yuri u228128g at h31 zorder 3
    show sayori u227131 at t32 zorder 2

    y "Kyaaaa!"

    show yuri u227158g
    show natsuki u221141

    "In the chaos of the moment, Yuri dropped her book and knocked her teacup into the air."
    "Ballistic tea spilled on both Yuri and Sayori."

    show sayori u114234
    show yuri u125116g at f31 zorder 3
    show natsuki u221141 at t33 zorder 2

    y "Natsuki!"

    show yuri u123116g at t31 zorder 2
    show natsuki xu2132 at f33 zorder 3

    n "What? I didn't do nothin'!"

    show natsuki xu1112 at t33 zorder 2
    show yuri u125116g at f31 zorder 3

    y "This has your malaise written all over it."

    show yuri u123146g at t31 zorder 2
    show sayori u114131
    show natsuki xu4112 at f33 zorder 3

    n "'Malaise'...?"

    show natsuki u226112 at t33 zorder 2
    show yuri u125146g at f31 zorder 3

    y "Ugh... Now I need to change..."

    show yuri u123144g at lhide zorder 1
    hide yuri

    show sayori u113222 at f32 zorder 3

    s "I'd... better go get cleaned up too."

    show sayori u111141 at lhide zorder 1
    hide sayori

    pause 0.5

    show natsuki u226153 at t22 zorder 2
    pause 0.5

    show natsuki u221113
    pause 0.25

    m "Hey, Natsuki?"

    show natsuki u115224 at f22 zorder 3

    n "Yes, Club President?"

    show natsuki u116113 at t22 zorder 2

    m "I found this bookmark with bunny faces laying loose in the closet earlier."
    m "Is it yours?"

    show natsuki xu3212 at f22 zorder 3

    n "Why would I own a dumb ol' girly bookmark like that?"

    show natsuki xu6232 at t22 zorder 2

    m "..."
    m "... Is it yours?"

    show natsuki xu4234 at f22 zorder 3

    n "... Yes."

    show natsuki xu6214 at t22 zorder 2

    m "I'll put it in your bag."

    show natsuki xu6234 at t44 zorder 2
    pause 0.5

    pause 0.5

    show sayori c111111 at l42 zorder 2
    pause 0.5

    show yuri h113114g at l41 zorder 2
    pause 0.25

    show yuri h225114g at f41 zorder 3
    y "Monika, I demand you reprimand your club member."

    show yuri h223114g at t41 zorder 2
    show sayori c114111
    show natsuki u113211 at f44 zorder 3

    n "'Reprimand'...?"

    show natsuki u116111 at t44 zorder 2

    m "Sayori doesn't need to be reprimanded, Yuri."

    show sayori c113152 at f42 zorder 4

    s "I'm sorry, Yuri..."

    show sayori c116152 at t42 zorder 2
    show yuri h225115g at f41 zorder 3

    y "N... Not her, the other one!"

    show sayori c114152
    show yuri h223115g at t41 zorder 2
    show natsuki u113122 at f44 zorder 3

    n "Hey, I didn't even do anything!"
    n xu4132 "You're just mad at me for that 'mayonaise' thing."

    show natsuki xu6132 at t44 zorder 2
    show yuri sh4131 at f41 zorder 3

    y "Malaise!"

    show yuri sh2222 at t41 zorder 2
    show natsuki u117122 at f44 zorder 3

    n "See? You're STILL mad about it!"

    show natsuki xu6132 at t44 zorder 2

    m "Now Natsuki, Yuri {i}did{/i} have to change clothes because of what you made Sayori do."

    show sayori c115122 at f42 zorder 4

    s "Yeah, and I got splashed too..."

    show sayori c116112 at t42 zorder 2
    show natsuki u117222 at f44 zorder 4
    show yuri h221115g

    n "All right! All right, all right!"
    n u11s331 "I'm sorry, okay? Jeez... It was just a dumb prank..."

    show natsuki xus235 at t44 zorder 2

    m "Yuri?"

    show natsuki xu6214
    show yuri h112171g at f41 zorder 3

    y "Ah... Yes, I forgive you Natsuki."

    show natsuki xu6234
    show sayori c111112

    y h124171g "And Sayori, you don't even need to worry about it."

    show sayori c115111
    show natsuki xu6113

    y h122111g "However, Natsuki, I {i}have{/i} been waiting to hear your thoughts on the next {i}Chronicles of Narnia{/i} section."
    y h222161g "Wouldn't it be a kind apology to get started on that?"

    show yuri h111111g at t41 zorder 2
    show natsuki u224132 at f44 zorder 4
    show sayori c111141

    n "Ah, crud."

    show natsuki u226132 at t44 zorder 2

    m "Sounds like you'd better get reading! Ahaha!"
    m "I'll go refill your teacup, Yuri."

    pause 0.25

    show sayori c111111
    show yuri h222171g at f41 zorder 3

    y "And I should get back to my own reading as well."


    window hide

    show yuri h221171g at thide zorder 1
    hide yuri
    pause 0.25

    show sayori c111141 at t21 zorder 2
    pause 0.25
    show natsuki u226112 at t22 zorder 2
    pause 0.25

    show sayori c111111
    show natsuki xul at f22 zorder 3

    n "Dumb Monika, taking her side like that."

    show sayori c114111

    n u222132 "Sayori, how about you distract her while I sneak up and give her skirt a flip? Y'know, just to really embarrass her!"

    show natsuki u226133 at t22 zorder 2
    show sayori c227231 at hf21 zorder 3

    s "Uwaaah! No, no more pranks!"

    window hide
    show sayori c116231 at t21 zorder 2
    pause 0.25
    show sayori c116262 at lhide zorder 1
    hide sayori
    pause 0.25

    show natsuki u224133 at t11 zorder 2

    pause 0.25

    n "Uh..."
    n u224113 "Well, I guess that book's not gonna read itself."
    n u222113 "I'll figure out how to get her back later!"

    window hide
    show natsuki u221143 at thide zorder 1
    hide natsuki
    pause 0.25

    scene black
    with dissolve_scene_full

    scene bg club_day
    show sayori c123211 zorder 1 at f11
    s "Oh jeez, that sure was dramatic."
    show sayori c111111 at t11
    "I sigh."
    m "You can say that again..."
    show sayori c222141 at f11
    s "Oh jeez, that sure was dramatic!"
    s c212171 "Ehehe~"
    show sayori c2212111 at t11
    m "Oh Sayori..."
    show yuri h122112 zorder 1 at f21
    show sayori zorder 2 at t22
    y "Well, I guess it's time to pack up."
    show yuri h1212112 at t21
    show sayori c227231 at f22
    s "Waaaait!! It's {I}home-time?{/i|}"
    show yuri h212121 at f21
    y "Apparently so~"
    show yuri h211121 at t21
    "I glance up at the clock."
    m "Hey she's right..."
    show sayori c112141 at f22
    s "Yaaaaay~!"
    window hide
    show sayori zorder 1 at lhide
    hide sayori
    show yuri zorder 1 at t11
    "Sayori rushes out of the room."
    "I laugh."
    show yuri h215348 at f11
    y "I sure hope Natsuki is okay..."
    show yuri h113348 at t11
    "I sigh, putting my hands on my hips."
    m "I'm sure she's fine!"
    m "Hey here's something Yuri,"
    show yuri h12433
    extend " maybe you could visit her house?"
    show yuri sh2222 at s11
    y "I-I can't..."
    y sh2300 "I'm so sorry..."
    m "Why not, Yuri?"
    "Uh oh."
    "I need to come up with a good bribe..."
    m "You can always visit [player] afterwards~ He's been off"
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 10.0
    hide screen tear
    extend " sick but I'm sure he'd love your visit!"
    show yuri h22a281 at h11
    y "Y-you think he would mind?"
    "I laugh."
    "I've got you now Yuri..."
    m "Of course he wouldn't mind! He does like you after all ahaha~"
    show yuri at h11
    y h21c2b1 "{b}He likes me?!{/b}"
    y "Ohhh yes I'm going right away!!"
    window hide
    show yuri zorder 1 at lhide
    hide yuri
    m "Yuri you're there to check on Nat--"
    "I sigh for the hundredth time today."
    m "Oh Yuri..."
    m "You're completely"
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 10.0
    hide screen tear
    extend " clueless."
    m "Ahaha~"
    "I pack up my bag and tidy round the classroom, before locking the door and heading home."

    scene black
    with dissolve_scene_full
    stop music
    m "After all..."
    m "Maybe things aren't so normal after all."
    play sound "sfx/giggle.ogg"
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    pause 30.0
    hide screen tear
    
    scene mon_house_bedroom
    play music t2
    m "Mm..."
    m "Glad to be home at last."
    "I flop down onto the bed, exhausted."
    m "Maybe a little nap won't hurt ..."
    
    window hide
    scene black
    stop music
    return


