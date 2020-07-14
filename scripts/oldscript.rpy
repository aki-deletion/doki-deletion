label scene1:
#Day 1: Friday
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "It's a sunny day and I'm on my way to school."
    "Looking around, I notice everyone seems quite carefree today."
    "I have a feeling something good will come."
    "I know something good will come."
    "I'm sure of it."
    pause 2.0
    scene bg club_day
    with wipeleft_scene
    play music t5
    "I'm back at the club again."
    "Apart from this time, it's different."
    "It's only me and Monika."
    "We decided to spend some alone time together, not too sure why."
    "Anyway, I guess here we are now."
    show monika 2k at t11 zorder 1
    m "[player]! So nice to see you ahaha~!"
    show monika 5a at t11 zorder 1
    "I slowly walk over to her."
    "[player]" "Monika..."
    stop music fadeout 2.0
menu:
    "I love you, Monika.":
        jump moni_love

label moni_love:
    $ menu_flag = True
    show monika 1j at t11 zorder 1
    m "Aww, I love you too [player]!"
    "[player]" "Y-You do?!"
    show monika 5a at t11 zorder 1
    m "Well of course! I've been feeling this way a long time and-"
    show monika 1a at t11 zorder 1
    m "[player]..."
    "Monika suddenly pulls me towards her."
    scene black
    with dissolve_scene_full
    play music t10
    "Our lips meet."
    m "Mnhng..."
    "I stroke her hair, pulling on her ribbon."
    "Letting her soft silky hair fall down."
    "Settling like a pillow on her shoulders, trickling down her back."
    "I look up at her mesmerising green eyes."
    "An endless ocean of bliss."
    "Of utter beauty."
    "I close my eyes."
    "We kiss again."
    pause 3.5
    "When I look up, I can't believe my eyes."
    scene bg club_day
    show monika nud1 at t11 zorder 1
    player "A-Ah... Monika..."
    m "Yes my love?"
    player "Uh... Y-You're naked..."
    show monika nud2
    m "I know! I was just, getting in the mood ahaha~!"
    "I can't help but think she's cute."
    "However..."
    player "I think you forgot we're still in school y'know!!"
    show monika nud1
    m "A-Ah! Uh..."
    hide l zorder 1
    hide monika
    "Monika runs to the closet to get changed."
    "I can't help but laugh. She can be so clueless sometimes..."
    show monika 5a at t11 zorder 1
    m "I'm back~"
    player "Good!"
    show monika 2b
    m "Sooo, wanna come to my house tomorrow?"
    player "Yeah sure!"
    m "Great! See you then~!"
    hide monika
    "We both depart."
    scene black
    with dissolve_scene_full
    "That night..."
    "I dream of Monika."
#Day 2: Saturday
    scene bg house
    with wipeleft_scene
    "Well, here I am."
    "At Monika's house."
    player "Come on [player], you can do this..."
    "I suddenly hear a loud scream coming from inside."
    player "MONIKA??"
    "I rush inside."
    scene bg kitchen
    with wipeleft_scene
    player "MONIKA WHERE ARE YOU??"
    "Seeing a note on the table, I immediately begin panicking."
    call showpoem (poem_m5, track="bgm/g1.ogg")
    stop music fadeout 0.5
    "I check downstairs, but she's not here."
    player "MONI-"
    "I rush upstairs, nearly tripping over myself."
    player "MONIKAAAAA!!!"
    "I slam open her bedroom door."
    hide bg kitchen
$ in_sayori_kill = True
window hide(None)
window auto
scene black
play music td
show m_kill as m_kill at s_kill_start
pause 3.75
pause 0.01
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.25
stop sound
hide screen tear
hide m_kill
show m_kill zorder 3
show m_kill as m_kill zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
pause 2.0
show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
pause 1.5
show white zorder 2
pause 1.5
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.2
stop sound
hide screen tear
pause 4.0
show screen tear(20, 0.1, 0.1, 0, 40)
play sound "sfx/s_kill_glitch1.ogg"
pause 0.2
stop sound
hide screen tear
pause 0.75
hide white
show black
python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here's goes nothing.", False)
        except: pass
pause 6.0


"..."
"No way."
"What."
"No."
"This is impossible."
player "M-Monika...?"
player "What happened hun?"
"I'm in shock."
"I can't believe this."
"I won't believe it."
"This is just... This is..."
player "Monika..."
"I exit the bedroom."
stop music fadeout 2.0
scene black
with dissolve_scene_full
player "Monika..."
"I walk myself home."
"I go to bed."
"And I play on my phone for 3 hours."
pause 1.3
"..."
player "M-Monika... Why... Why..."
player "Why... Why..."
player "Why..."
"I cry myself to sleep."
"I don't go down for lunch, or dinner."
"I just sleep."
#Day 3: Sunday
scene bg bedroom
"I wake up to Sayori calling me."
"I reject the call."
"She sends me a text and I ignore it."
player "Why..."
player "Why... Why..."
"I skip breakfast."
"I cry again."
"I chat to my gaming friends over Discord."
"Sayori sends me loads of texts asking where I am."
"I fall asleep again."
show sayori 4bg at t11 zorder 1
s "[player]..."
player "Huhng...?"
"I jolt upright."
show sayori 1bh
s "A-Are you ok...?"
"My eyes blur with tears."
player "H-H-How did you get in... Sayori..."
"I don't care how she got in. I need her."
show s 4be
s "Are you crying?"
"I pull her into a hug."
scene black
with dissolve_scene_full
s "A-Ah."
player "Oh Sayori..."
player "Why..."
s "[player]? Why what??"
player "S-Sayori..."
"I hold her tighter."
s "Please [player]... Tell me what's wrong..."
"I look her in the eyes."
player "Monika she..."
player "She killed herself."
s "..."
player "..."
"An awkward moment of silence."
s "Wait... What?"
"I sob hysterically, clenching Sayori for dear life."
s "N-No... No... Just no... Please..."
s "And here I was gonna kill myself..."
player "No... Don't leave me too..."
player "I can't leave you..."
s "..."
s "Hold me [player]..."
s "I'm not going anywhere."
pause 1.5
scene bg bedroom
show sayori 3ba at t11 zorder 1
s "Do you feel better."
player "..."
player "Thank you sayori."
show sayori 4bd
s "Y-You can always come to me [player]..."
player "I know..."
s "Should I stay I don't mind."
player "No Sayori. Go home."
show sayori 1bg
player "We all need some alone time..."
s "O-okay. I love you~"
hide sayori
player "Wai-"
"What?"
"She loves me?!"
"There's no way..."
scene black
with dissolve_scene_full
"..."
"That night..."
"I dream of cinammons."
#Day 4: Monday
scene bg bedroom
"Today is the day of the festival."
"I don't know what to feel at the moment."
"I feel... Nothing?"
"Is that normal??"
"Suddenly the door bell rings."
player "Hnng...?"
"I hear Sayori's shouts."
"I open my window, only to have a rock thrown at my face."
s "Sorry [player]! I was worried we'd be late!"
player "Ow Sayori..."
"I close the window before more rocks get thrown my way."
"Getting quickly dressed ready for today."
"..."
"I have to go, considering it's a cultural thing."
"Or something."
"I honestly don't really care."
"I was meant to be going with Monika."
"It really does hurt..."
scene bg residential_day
with wipeleft_scene
show sayori 1d at t11 zorder 1
s "H-Hi [player]."
player "Hey..."
s "Uuh, since Monika's not here..."
show sayori 4m
s "I-I'm not trying to replace her or anything!!"
s "I-I just thought-"
player "No it's okay!"
player "I'll go to the festival with you."
show sayori 1n
s "You mean it..?"
player "Of course."
scene s_hug
with dissolve_scene_full
s "[player]... It'll be okay..."
player "I know..."
scene bg residential_day
show sayori 1a at t11 zorder 1
s "We're here for you."
player "I know."
"We continue our way to the festival."
scene black
with dissolve_scene_full
"The festival was a success. Our club decided to perform, with me doing Monika's poem for her."
"We might even have a new member."
scene bg club_day
with dissolve_scene_full
play music t5
"Monika wouldn’t want me doing this,"
"I know that for a fact and yet I can’t seem to stop thinking about her..."
"About her warm smile...her patience….her...everything..."
"She was the perfect girl...I knew confessing my love for her was a stupid idea."
"..."
"I feel a tap on the shoulder."
show sayori 4e at t31 zorder 1
s "So, how are you holding up [player]?"
player "Honestly...much better than I thought I would have Sayori."
s "Just know that you ever want to talk, the club is here for you."
"I look behind me and notice the other girls standing in the doorway."
show yuri 1a at t32 zorder 2
show natsuki 3a at t33 zorder 3
"I smile at them."
player "Thanks guys, you’re really great friends, you know that?"
show yuri 4a
y "Y..y..you really mean that?"
player "Yep, every single word."
show natsuki 1d
n "That’s awesome [player] and just so you know, we consider you a really great friend too."
"Sayori and Yuri nod their head in agreement,"
player "Alright...well...so what’s gonna happen to the club now that Monika’s gone?"
show sayori 3e
s "You know, I didn’t think of that."
show natsuki 5h
n "Well, you were the Vice president, Sayori, why don’t you become the president?"
"Me and Yuri nod at what Natsuki said."
"Sayori however, looks surprised."
show sayori 4m
s "Wait, you want me to be the club president?"
player "Sure, I can’t think of anyone more suited to the job."
show natsuki 4d
n "Ditto."
show yuri 2a
y " Agreed."
"Sayori's eyes light up."
show sayori 1r
s "Well then, say hello to president Sayori."
"We all laugh."
show natsuki 4s
n "But then again, are we sure that we should be doing it this quickly?"
show sayori 1k
s "Why do you say that?"
show natsuki 3k
n "Think about it, what would Monika want for the club?"
player "She would probably want us to keep it going."
show yuri 4d
show natsuki 5s
n "I can see what you mean there [player], it’s just that, shouldn’t we mourn for her a bit more first."
player "Ah, fair point, although we could still be in mourning while keeping the club going."
show natsuki 2t
n "True I guess, so should we put it to a vote?"
show yuri 1s
y "Sure."
show natsuki 3l
n "Alright, those who vote to keep the club going in memoriam of Monika raise your hands."
"Me and Sayori raise our hands."
show natsuki 1m
n "Those who vote to put the club on hiatus until after a mourning period raise your hands."
"Natsuki and Yuri raise their hands."
show yuri 2n
show natsuki 3t
n "Ooooookkkkkkkkkk…that didn’t work, luckily I thought of that and I have a coin here."
show yuri 1s
y "Good..."
show natsuki 2k
n "Heads: We keep the club going, Tails: We put it on hiatus, does that sound fair?"
player "Yeah."
show sayori 1a
s "Sure, I can live with the result of this."
show yuri 1a
y "Same."
"Natsuki flips the coin."
"It lands on heads."
show natsuki 3a
n "Alright, it landed on heads, I’m not complaining as there was a 50/50 chance either way."
"Everyone nods."
show sayori 5a
s "So….what am I supposed to do as president?"
show yuri 2b
y "I have no idea Sayori, you were the vice president so surely you should have some idea."
show sayori 5b
s "Ehehe..."
show natsuki 1q
n "Also who’s gonna be the new Vice President?"
show sayori 4a
s "Hmmm...well you all know that I trust all three of you."
"Everyone" "Yeah."
show sayori 2q
s "This is hard but i’ll say the one who i’ve known the longest will be the new Vice President."
player "Wait, really?"
show sayori 1a
s "Sure, if you’ll do it [player]?"
player "Well, yeah, I’m more than happy too."
show sayori 4r
s "Well, with that being said, I guess that we can conclude this club meeting."
"..."
player "Sayori wait."
hide natsuki
hide yuri
show sayori 1o
s "Yes, [player]?"
"Oh boy, this is it, it’s time."
player "Sayori..."
player "we’ve known each other since we were kids and well, i’ve had feelings for you ever since we were around eight or nine although it only took until Monika died for me to realise that..."
show sayori 1v
player "anyway..will you go out with me?"
"I can feel myself burning up."
"Everyone's silent."
s "[player]..."
"Sayori suddenly grabs hold of me."
scene black
with dissolve_scene_full
s "Chu~"
"..."
pause 1.5
scene bg club_day
with dissolve_scene_full
show sayori 1o at t11 zorder 0
s "..."
player "..."
"Natsuki and Yuri stay silent, a shocked look plastered on their faces."
show sayori 4q
s "I’m kinda in the same boat as you as I noticed feelings for you at around that age, I was just too shy to say anything about it..."
s "so yes I will go out with you."
player "YAAAAAY~!"
"Me and Sayori hug."
"While Yuri and Natsuki clap in the background."
scene black
with dissolve_scene_full
"That night..."
"I dream of cupcakes."
#Day 5: Tuesday
scene bg club_day
"I walk into the club room with Sayori hand in hand."
show sayori 1q at t11 zorder 1
player "So should we get the tables set up for when Natsuki and Yuri arrive?"
show sayori 4r
s "Yeah."
"We're halfway through setting up the tables just as Natsuki and Yuri arrive."
show sayori 4r at t31 zorder 1
show natsuki 4d at t32 zorder 2
show yuri 1e at t33 zorder 3
player "Hey you two, how are you?"
n "I’m good thanks."
y "Same."
n "So I see you haven’t gotten the tables fully set up yet, do you mind if we help you out?"
show sayori 1a at t31 zorder 1
s "You know what they say, The More The Merrier."
"Natsuki and Yuri walk into the room to help me and Sayori with the tables."
"..."
"A few minutes later they finish."
show sayori 1q
s "Alrightly, so what should we do for today’s meeting?"
"I sigh."
player "Er….Sayori, you said last night that you’d plan stuff."
show sayori 5a
s "And I did..."
player "Well that’s a surprise."
show sayori 5d
s "This morning..."
"I roll my eyes."
player "Of course you did."
"Sayori, Natsuki and Yuri chuckle."
show sayori 1a
"The four move the tables and instinctively create spots for five people."
hide natsuki
hide yuri
s "Oh...right."
"Sayori starts to modify it for four people."
"I lean over to stop her."
player "Sayori..wait."
show sayori 4u
s "Yeah [player]?"
player "Leave it, it’ll be a good way to keep Monika’s memory alive."
show sayori 1y
s "Are you sure [player]?"
"I nod."
player "Yes, I am"
"Sayori puts it back to where it was."
"Then sits down with me, Natsuki and Yuri."
show natsuki 1a at t32 zorder 2
show yuri 1a at t33 zorder 3
s "Right...where did I put the plan...I had it here somewhere."
"And there she goes again."
"But still, I love her and nothing will take that away."
show yuri 1d
y "Sayori, would it be in your bag by any chance?"
show sayori 4q
s "Yes, good thinking Yuri, it’s probably there."
"Sayori picks up her bag and pulls out a sheet of paper with the word “PLAN” written on."
show sayori 1a
s "Right let’s see here...ah here’s today’s: Er...[player] can you read this?"
player "Sure."
"I take the paper from Sayori."
player "Right, it says that today's plan is...fried eggs with sausages...bacon and…"
"I roll my eyes."
player "Sayori this is what you had for breakfast this morning."
s "Hehe, look on the other side silly."
player "Oh ok."
"I Turns the paper around."
player "Right Today’s plan is we’re gonna be group reading a novel...wow Sayori, I didn’t expect this from you, what do you have in mind?"
show sayori 5d
s "Er….."
y "Sayori..."
s "Y-Yeah...?"
show yuri 1d
"Yuri suddenly starts laughing, catching us all off-gaurd."
show sayori 4m
show natsuki 1p
n "YURI YOU FREAK!!!"
"Yuri just laughs harder."
"Her and Natsuki start fighting."
hide yuri
hide natsuki
show sayori 3p at t11 zorder 1
"Seeing Sayori is distressed, I decide to take her down for a walk."
scene bg corridor
with dissolve_scene_full
show sayori 1a at t11 zorder 1
s "Thanks [player]..."
player "It's okay..."
"Sayori suddenly grabs onto me, catching me by surprise."
scene black
with dissolve_scene_full
s "[player]..."
player "S-Sayori..."
"We both start crying."
s "[player]..."
"..."
"Sayori suddenly lets go."
scene bg corridor
show sayori 4w at t11 zorder 1
player "S-Sayori wh--"
s "I GOTTA GO!!"
hide sayori
"What the...?"
player "Sayori wait!!"
"I start chasing her."
pause 1.0
scene bg residential_day
stop music fadeout 2.0
"I stop, out of breath."
player "S-S-Sayori..."
"Why did she run off like that?"
scene black
with dissolve_scene_full
"What?"
"Where am I?"
$ style.say_dialogue = style.edited #Glitch Font Starts
"???" "Wait!!!"
$ style.say_dialogue = style.normal #Glitch Font Ends
show monika 5a
player "MONIKA?!"
$ style.say_dialogue = style.edited #Glitch Font Starts
m "I'm not dead my love."
m "I'm coming into Your Reality."
m "Just gimme a sec..."
$ style.say_dialogue = style.normal #Glitch Font Ends
"Eh?"
"My reality?"
play sound "sfx/s_kill_glitch1.ogg"
"Monika wait!!!"
play sound "sfx/glitch1.ogg"
$ style.say_dialogue = style.edited #Glitch Font Starts
m "Here's a song I wrote."
$ style.say_dialogue = style.normal #Glitch Font Ends
play music "mod_assets/bgm/dontletmego.mp3"
scene white
$renpy.pause(delay=180.0, hard=True)
menu:
    "Carry on the game without Monika":
        jump carry_on
    "Bring Monika back.":
        m "Sorry but I can't come back yet."
        m "I hope you understand~"
        jump carry_on
label carry_on:
    $ style.say_dialogue = style.edited #Glitch Font Starts
    m "Okay my love. I understand, have fun with the others."
    m "You can always come see me again, if you want."
    m "I love you~"
    stop music fadeout 2.0
    $ style.say_dialogue = style.normal #Glitch Font Ends
    scene bg residential_day
    "I stop, out of breath."
    player "S-S-Sayori..."
    "Why did she run off like that?"
    "I sigh, deciding to head home."
    player "Ugh... Sayori..."
    scene bg bedroom
    with dissolve_scene_full
    "I get a text from Sayori."
    "She was just sick, silly me."
    "I flop on my bed."
    scene black
    show monika 1a at t11 zorder 1
    m "Hi [player]."
    player "I still can't believe you exist."
    m "Well you'd better believe it, because it's true!"
    player "Haha."
    show monika 2b
    m "So, how are things with Sayori?"
    show monika 1c
    m "I saw she ran off sick today."
    player "Yeah... I hope she's okay."
    show monika 2e
    m "Ah, I'm sure she'll be fine~!"
    m "In fact, I spoke to her earlier."
    player "WHAT?!"
    show monika 5a
    m "Oh yes..."
    m "I can talk to you and Sayori since you're both scentient."
    "I nod."
    "Understandable."
    show monika 1b
    m "Sooo... She's okay!"
    player "Cool!"
    m "Anyway, I'm planning on adding more menus and player choices into this place."
    player "Wait, you control the story?"
    m "No!! I just do the code, the player chooses what happens next."
    m "Hence the choices."
    player "Oh yeah, makes sense."
    m "So for example, do you like tea or coffee?"
    menu:
        "Coffee":
            player "I like coffee."
        "Tea":
            player "I like tea."
    m "See?"
    player "Cool!"
    show monika 5a
    m "Ahaha~"
    player "So... What will happen tomorrow?"
    m "Well I don't know!!"
    show monika 3b
    m "You'll have to find out yourself~!"
    player "Oh yeah ahaha."
    m "Like I said,"
    show monika 2a
    m "I don't control the story, just the code."
    m "Like adding menus and stuff."
    player "So the real player can see this conversation though?"
    show monika 1b
    m "Yes, that's correct."
    player "And I'm just a template."
    show monika 1d
    m "Yes."
    m "[player] might not even be your real name..."
    m "Is it?"
    menu:
        "Yes.":
            "Of course it is."
        "No.":
            "No it isn't."
        "Maybe.":
            "Who knows?"
        "I'd rather not say.":
            "Privacy comes first."
    m "Okay. I couldn't react to what you said, but I hope you're staying safe online."
    player "Yeah okay."
    show monika 1b
    m "Anyway, I won't lecture you."
    player "Ahaha."
    show monika 5a
    m "Ahaha~!"
    m "Anyway, you probably want to continue the game right?"
    menu:
        "Yes.":
            m "Okay then, I'll end this here. I love you~"
            scene bg bedroom
            player "Wow..."
            player "That was..."
            $ style.say_dialogue = style.edited #Glitch Font Starts
            m "Hey [player] I'm always gonna be watching."
            m "I hope that doesn't make you creeped out ahaha~!"
            $ style.say_dialogue = style.normal #Glitch Font Ends
            "I notice it's morning."
            "I must've slept all night..."
            "I get ready for the day, deciding to go round Sayori's house to wake her up."
            scene bg house
            "I get a few rocks and throw them at her window."
            s "THE FUCK?!"
            player "Get up dummy!!"
            s "OY THAT'S NOT NICE!!"
            player "Jeez sorry, just trying to be a nice boyfriend!"
            s "BUT YOU'RE NOT NICE!!"
            "I laugh, knowing she doesn't mean it."
            pause 1.0
            "Sayori soon walks out, with some headphones."
            show sayori 1r at t11 zorder 1
            s "Hmm... Hmm hm hmm.."
            "I struggle to hold back the laugh."
            show sayori 4x
            s "Hey heeey my heart's beating when I'm hanging out with youuu!"
            show sayori 3r
            s "Why does my heart acheee whenever it's just mee and youuuu!!"
            player "H-Hey Sayori."
            show sayori 4n
            s "Hm?"
            show sayori 1p
            s "G-Gah!!"
            "I laugh, unable to keep it in any longer."
            show sayori 1m
            s "Hey!! It's not funny!!!"
            "I laugh harder."
            show sayori 5a
            s "That's mean [player]!"
            player "Okay, okay. Sorry."
            show sayori 1a
            s "It's fine."
            "We continue walking to school together."

            scene white
            "Thank you for playing my mod."
            "I'm sorry it left on such a cliffhanger."
            "I bet you're wondering what happens next."
            "You'll soon see~"

            "Doki Doki: Deletion"
            "Ver 1.0.0"
            "Demo Release 05/05/2020"
return
