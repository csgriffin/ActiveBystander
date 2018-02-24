# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character(None, what_italic=True)
define MC = Character("Me")
define F1 = Character("Joseline")
define F2 = Character("Matt")
define F3 = Character("Fiora")
define F4 = Character("Jake")
define VC = Character("Karl")
define SB = Character("Bastian")
define S1 = Character("Loud Jock")
define S2 = Character("Obnoxious Jock")
define CH = Character(None)
define TEACHER = Character("Teacher")
define BULLY = Character("Bully")
define Z = Character("Zeke")

default lunchTalk = False
default JoselineTalk = False
default MattTalk = False
default FioraTalk = False
default JakeTalk = False
default good = False
default neutral = False
default bad = False
default good2 = False
default bad2 = False

#image defines because I don't know why it's not working without these
#image FHappy = "FHappy.png"
#image FModest = "FModest.png"
image FNorm = "FNorm.png"
image FBored = "FBored.png"
image FSad = "FSad.png"

image JBlank = "JBlank.png"
image JLaugh = "JLaugh.png"
image JMad = "JMad.png"
image JNorm = "JNorm.png"
image JShame = "JShame.png"
image JTalk = "JTalk.png"

image JoCry = "JoCry.png"
image JoDisgust = "JoDisgust.png"
image JoHappy = "JoHappy.png"
image JoMad = "JoMad.png"
image JoModest = "JoModest.png"
image JoNo = "JoNo.png"
image JoNorm = "JoNorm.png"
image JoScold = "JoScold.png"
image JoShock = "JoShock.png"
image JoSmart = "JoSmart.png"

image KNorm = "KNorm.png"
image KSad = "KSad.png"
image KShock = "KShock.png"
image KSmile = "KSmile.png"

image MBored = "MBored.png"
image MNorm = "MNorm.png"
image MAngry = "MAngry.png"
image MBlank = "MBlank.png"
image MShock = "MShock.png"

image SDown = "SDown.png"
image SMad = "SMad.png"
image SNorm = "SNorm.png"
image SSad = "SSad.png"
image SShock = "SShock.png"
image SSmile = "SSmile.png"

image ZAwk = "ZAwk.png"
image ZConfuse = "ZConfuse.png"
image ZDown = "ZDown.png"
image ZMad = "ZMad.png"
image ZNorm = "ZNorm.png"
image ZShock = "ZShock.png"
image ZSide = "ZSide.png"
image ZSmile = "ZSmile.png"

# The game starts here.
label start:
    python:
        myname = renpy.input("What is your name?")
        myname = myname.strip()
    #jump development

    play music "Title Theme 1.wav"
    scene bedroom
    with fade
    

    CH "*Beep beep beep! Beep beep beep!*"
    
    "I wake to the sound of my alarm, blaring excitedly in my ears."
    menu:
        "Today's the first day of school"
        
        "I should get up":
            "I excitedly shower, get dressed, and brush my teeth, in anticipation of the day ahead."
            "It's finally time to head off to the first day of high school after an exciting summer with my friends."
            "I’m really hoping that my class is filled with my friends."

        "5 more minutes won't hurt":
            CH "*20 minutes later*"
            "Oh shoot! I overslept!"
            "If I hurry though, I can make it to the bus on time."
            "I can't be late on the first day of school!"
    
    scene bus
    with fade
    stop music fadeout 1.0

    "The bus rounds the corner and it's off to school."

    # SCENE CHANGE HERE - SCHOOL HALLS
    
    play music "School Theme.wav"
    image hallway = im.Scale("images/hallway1.png", 1920, 1080)
    scene hallway
    with fade

    "As I wander the hall towards my homeroom class, I see various new and familiar faces..."
    
    #character intros here
    show JoNorm
    with dissolve
    "There's Joseline, prepping her makeup before the day starts..."
    F1 "Ugh, I can't believe we're back in school already. Like, seriously, this is the worst..." 
    hide JoNorm with dissolve
    
    show MNorm with dissolve
    "And there's Matt. I wonder how much progress he's made on that car he was working on?"
    F2 "Hey, man! Hope to see you in class!"
    hide MNorm with dissolve
    
    show JNorm with dissolve
    "I see my friend Jake over there. Looks like he's signing up for the track team. Maybe I'll join him..."
    F4 "Aw man! I am SO hyped for this! Bzooooooooooooom!"
    hide JNorm with dissolve
    
    show KNorm with dissolve
    "Who's this again...? Oh right! It's Karl. He's been in my class since elementary school."
    "Most people don't like him, since he doesn't talk much."
    hide KNorm with dissolve
    
    show ZNorm with dissolve
    "I haven't met this kid before. Although from the sounds of his loud friends, I can assume his name is Zeke!"
    S1 "Yo, Zeke! You hyped for track season?"
    Z "Heck yeah, bro! We're gonna tear up that track!"
    hide ZNorm with dissolve
    
    show SShock
    "WOAH! That was close."
    "While I was distracted watching those jocks, I almost ran into this kid."
    "I guess he was too busy on his phone to pay attention."
    SB "Oh, so sorry! I totally didn't see you there!"
    hide SShock with dissolve

    image classroom = im.Scale("images/classroom.png", 1920, 1080)
    scene classroom
    with fade
    "I approach the class and my friend, Fiora, approaches me with a warm smiling face."
    show FNorm
    with dissolve
    
    F3 "Hey [myname]! I am so glad I have class with you."
    F3 "I had such a wonderful summer. How was yours? Did you do anything special?"
    menu:
        "I spent my summer..."
        
        "sleeping":
            MC "I spent most of my summer sleeping..."
            F3 "Oh, you can be so lazy sometimes!"
            
        "working":
            MC "I got a summer job. I spent a lot of my time working."
            F3 "That's nice!"
            
        "going to the beach":
            MC "I spent a lot of time at the beach."
            F3 "That must've been fun!"
            
    F3 "Anyway, come on inside! The teacher is about to take attendance."
    hide FNorm 
    with dissolve
    
    TEACHER "Everyone take a seat. Let me take attendance."
    
    "I look around to see that four of my friends from middle school are in my homeroom."
    "It looks like I scored the jackpot when it comes to homeroom placement!"
            
    TEACHER "Alright, now that everyone's here, let's get started..."
    
    "The first class went on for an eternity, and by the time second period rolled around it became apparent my friends were also feeling the pain of coming back to school."
    
    TEACHER "Alright, everyone, that's the bell. Take your things and head to the cafeteria."
    image cafeteria = im.Scale("images/cafeteria.jpg", 1920, 1080)
    scene cafeteria
    with fade
    
    "Thank goodness! Now I can finally have some time to catch up with my friends and tell them some stories about my summer." 
    
    "I can see Matt waving me over to the table at the front of the cafeteria."
    show MNorm
    with dissolve
    
    MC "Hey! How was your summer?"
    F2 "It was great! I was able to fix up my AMX car over the summer with my dad. She's a real beauty!"
    F2 "How was your summer?"
    
    menu:
        "My summer..."
        
        "...was great!":
            
            MC "My summer was great!"
            F2 "Awesome!"
            
        "... could've been better...":
            
            MC "It could've been better..."
            F2 "Damn. Well hopefully this school year will be better."
            
label after_summer:
    
    F2 "Hey, I see the rest of the gang coming over here."
    hide MNorm
    with dissolve
    F2 "Can you wave at them so they see us?"
    
    show KNorm
    with dissolve
    "As I start to wave, I notice Karl is sitting right next to us and is already eating his turkey sandwich."
    "I must have missed him while Matt and I were talking."
    "It occurs to me that, because Karl is sitting here now, there isn't enough room for all of us to sit here."
    hide KNorm
    with dissolve
    "Joseline is leading the rest of the group as they approach the table"
            
    show JoNorm
    with dissolve
    F1 "Oh, it looks like we're one seat short."
    stop music fadeout 1.0

    "She looks over at Karl."
    hide JoNorm
    show JoDisgust:
        xalign 0.9
        yalign 1.0
    
    show KNorm:
        xalign 0.1
        yalign 1.0
    with dissolve
    
    play music "BullyTheme.wav"
    F1 "Ugh, could you move so we can sit together?"
     
    "Karl looks up for a second, but then goes back to eating."
    
    hide JoDisgust
    show JoScold:
        xalign 0.9
        yalign 1.0
    F1 "Come on, can you move? We're gonna sit together."
    
    hide KNorm
    show KSad:
        xalign 0.1
        yalign 1.0
    VC "I've already moved twice already, and I just unpacked my lunch. Sorry."
    
    hide JoScold
    show JoMad:
        xalign 0.9
        yalign 1.0
    F1 "Oh, come on, don't be that guy." 
    F1 "Like, seriously, just move."
    F1 "Is this SPECIFIC SPOT that important?"
    F1 "I need that spot!"
    
    "I feel like I should say something, but decide to just stand by and let things run their course."
    
    hide KSad
    with dissolve
    stop music fadeout 1.0
    "I start to see looks coming from around the cafeteria. 
     Karl gathers his lunch in a hurry and rushes to the other end of the cafeteria,
     staring at the floor, dropping some of his turkey sandwich as he goes."
    
    play music "School Theme.wav"
    hide JoMad
    show JoNorm
    F1 "Finally, I can sit!"
    hide JoNorm
    show JNorm
    with dissolve
    
    F4 "What is up my guys? High school seems to be off to a pretty strong start for us."
    F4 "I'm planning on joining the track team and blowing away the competition with my incredible speed!"
    F4 "Bzooooooooooooom! Ftoooooom!"
    
    "Jake had always been quick, but I'd been able to keep up with him for the most part. At least, with regard to running."
    "I never caught up to him when it came to making ridiculous noises. What a goof."
    "I'm sure the track team would be fun with him at my side."
    
    hide JNorm

    #label development:
    #        "SKIPPED!"

    show FNorm
    with dissolve
    
    F3 "Speaking of speed, have you guys noticed that this day feels like anything but speedy?"
    F3 "It feels like a marathon just to get through all these rules for every class."
    F3 "I just want to get home and relax in bed with some Jane Austen books. "
    
    "Jane Austen again? I swear, Fiora reads one of Jane Austen's books literally every day."
    "She's probably the most voracious reader in the whole world!"

    hide FNorm
    with dissolve
    
    "While we eat, I decide to talk to a couple of my friends about their day so far..."
    
    menu:
        "Matt and Fiora seem busy talking..."
        
        "Joseline":
            jump JoselineLunch
            
        "Jake":
            jump JakeLunch

label JoselineLunch:
    show JoDisgust with dissolve
    F1 "I was having a great day with classes until that kid had to be so rude and take that seat."
    F1 "I mean, he kinda seems like a jerk to me, don’t you think? Who just sits and doesn’t move when asked?"
            
    menu:
        "What did I think of that situation..."
              
        "Maybe she was exaggerating a little...":
            MC "I think you might have been exaggerating a little..."
            F1 "Ppfh. I mean, he did move eventually, I guess."
            hide JoDisgust with dissolve
                  
        "She's right. What a jerk!":
            $ bad = True
            MC "You're right. What a jerk!"
            hide JoDisgust
            show JoHappy
            F1 "Yeah! You know what I'm talking about!"
            hide JoHappy with dissolve
                 
        "She was kind of a jerk to him.":
            MC "Seemed to me like YOU were the one being a jerk there."
            hide JoDisgust
            show JoMad
            F1 "You're gonna come out and call ME the jerk?! I thought you were my friend, not some little weasel."
            hide JoMad with dissolve
            
    $ JoselineTalk = True
    if lunchTalk:
        jump afterLunch
    else:
        $ lunchTalk = True
        jump secondFriend

#label MattLunch:
#    show MBored with dissolve
#    F2 "My day has been nothing but boring; the classes haven’t even shifted into 2nd gear yet."
#    F2 "All we get are teachers who explain rules and then give a dumb icebreaker, even though I know half the kids."
#    hide MBored 
#    show MNorm
#    F2 "I can’t wait to get home to the car to tweak a few things though."
#    hide MNorm with dissolve
#    $ MattTalk = True
#    if lunchTalk:
#        jump afterLunch
#    else:
#        $ lunchTalk = True
#        jump secondFriend
    
#label FioraLunch:
#    show FBored with dissolve
#    F3 "English class was interesting, but when the teacher told us what books we were going to be reading I had already read every single one."
#    hide FBored
#    show FNorm
#    F3 "Guess my homework is going to be more on the light side this year!"
#    hide FNorm with dissolve
#    $ FioraTalk = True
#    if lunchTalk:
#        jump afterLunch
#    else:
#        $ lunchTalk = True
#        jump secondFriend
    
label JakeLunch:
    show JShame with dissolve
    F4 "Not a highlight reel, thats for sure."
    F4 "I’m glad to see you guys again, but I just hate classes for the most part."
    F4 "Nothing much to speak of today besides that incident earlier."
    menu:
        "What incident?":
            MC "What are you talking about?"
            F4 "That kid who wouldn't move from Joseline's seat. I dunno about you, but that's the most action I've seen today."
                    
        "That incident with the lunch seat?":
            MC "You mean just now with Karl?"
            F4 "Yeah. Definitely stood out from all the dull classes I had before lunch."
            
    hide JShame with dissolve
    $ JakeTalk = True
    if lunchTalk:
        jump afterLunch
    else:
        $ lunchTalk = True
        jump secondFriend
    
label secondFriend:
    if JoselineTalk:
        menu:
            "Next I talked to..."
            
            "Jake":
                jump JakeLunch
                
    if JakeTalk:
        menu:
            "Next I talked to..."
            
            "Joseline":
                jump JoselineLunch
                
label afterLunch:
    scene classroom with fade
    stop music fadeout 1.0
    "The bell rings, signaling the end of our lunch period, and we all head back to class."
    play music "Goodbye.wav"
    image School = im.Scale("images/school.png", 1920, 1080)
    scene School with fade
    "Before long, my school day is over and it's time to head home. I guess seeing my friends made the rest of the day go by faster."
    
    stop music fadeout 1.0
    scene bedroom with fade
    "The next day..."
    play music "Title Theme 1.wav"
    
    CH "*Beep beep beep! Beep beep beep!*"
    
    "My diligent alarm wakes me up at the usual time"
    "I slept great last night!"
    "I'm excited to go to school and talk to my friends at lunch today."
    "After getting ready, it's time to fuel up for the day and eat some breakfast."
    menu:
        "What should I eat for breakfast?"
        
        "Cereal":
            "I pour out a bowl of my favorite cereal, add some milk, and chow down."
            "That hit the spot!"

        "Scrambled eggs and toast":
            "It takes a little extra effort to get the eggs and toast all ready in time, but it was worth it!"
    
    scene bus with fade
    stop music fadeout 1.0
    "The bus comes by at it's usual time and takes me to school."
    "The first half of my day is boring, but goes by quickly. Before I know it, the bell rings for lunch and I'm off to see my friends."
    
    scene cafeteria with fade
    play music "School Theme.wav"
    "Lunch today is spaghetti and meatballs."
    show FNorm:
        xalign 0.1
        yalign 1.0
    show MNorm:
        xalign 0.9
        yalign 1.0
    "I see Fiora reading a 'Series of Unfortunate Events' book, and next to her is Matt."
    "He's scarfing down some pizza with.. are those oreos and french fries?!"
    "He's always had such odd tastes..."
    "I strike up a conversation with Matt as I approach the table."
    hide FNorm with dissolve
    show MNorm:
        xalign 0.5
        yalign 1.0
    F2 "Hey bud!" 
    F2 "I fixed up the car with some new spark plugs."
    F2 "I was working on the AMX 'til midnight, but then my mom made me go to bed."
    F2 "Hey, do you wanna come over to my place after school and help me out with the car?"
    menu:
        "What should I do?"
        
        "Nah, I've got a lot of work to do. We can hang out another time.":
            MC "Sorry, I've got a lot of work I need to get done. But I can hang out this weekend!"
            F2 "Alright, sounds like a plan!"
            hide MNorm 
            with dissolve
            
        "I can get my work done another time.":
            MC "Sure! Sounds like a plan."
            F2 "Awesome!"
            hide MNorm with dissolve
            
    F2 "Let's talk about it more later. I see the rest of the group coming."
    show KNorm
    with dissolve
    "Yet again, while talking to Matt, somehow Karl snuck in, sat down, and started on his lunch."
    hide KNorm
    show KSad with dissolve:
        xalign 0.1
        yalign 1.0
    show JoDisgust with dissolve:
        xalign 0.9
        yalign 1.0
    stop music fadeout 1.0
    "Joseline sighs once she notices Karl."
    "She's looking particularly impatient today."
    play music "BullyTheme.wav"
    F1 "Karl, are we going to have to do this again today?"
    VC "But..but... I finally found a seat after being sent away from 5 other tables."
    VC "Can I please just sit here and eat in peace?"
    VC "No one wants me around..."
    if bad:
        MC "Karl, you should just move. These are our seats."
        hide KSad
        show KShock:
            xalign 0.1
            yalign 1.0
        hide JoDisgust
        show JoScold:
            xalign 0.9
            yalign 1.0
        F1 "Yeah, Karl. Everybody wants you out because you just sit down without asking."
        F1 "You're just being straight up rude!"
        hide KShock with dissolve
        stop music
        "Karl picks up his lunch and leaves the lunchroom."
        hide JoScold with dissolve
        "There’s a brief pause as the kids in the lunchroom watch him go, but then conversation resumes as normal."
        play music "School Theme.wav"
    else:
        menu:
            "What should I do...?"
            
            "Karl should just move. We were going to sit here":
                $ bad = True
                MC "Karl, you should just move. These are our seats."
                hide KSad
                show KShock:
                    xalign 0.1
                    yalign 1.0
                hide JoDisgust
                show JoScold:
                    xalign 0.9
                    yalign 1.0
                F1 "Yeah, Karl. Everybody wants you out because you just sit down without asking."
                F1 "You're just being straight up rude!"
                hide KShock with dissolve
                stop music
                "Karl picks up his lunch and leaves the lunchroom."
                hide JoScold with dissolve
                "There’s a brief pause as the kids in the lunchroom watch him go, but then conversation resumes as normal."
                play music "School Theme.wav"
            
            "Karl can stay here. We can just move.":
                $ neutral = True
                MC "Karl, you can stay here. Come on, guys, let's go find another table."
                F1 "Ugh, fine. There's a table over there."
                F1 "Getting into this same fight over and over isn't worth the stress, and he's not going to change his mind."
                F1 "We'll just sit over there from now on."
                hide JoDisgust with dissolve
                hide KSad with dissolve
                stop music
                play music "School Theme.wav"
                "Joseline leads us to a table towards the back of the cafeteria, complaining about Karl the whole way."
                "I look back to see Karl still eating, but he looks so lonely sitting by himself."
                
            "Karl can sit with us if we all go sit over there.":
                stop music
                MC "Hey, wait. There's a table over there with enough seats for all of us."
                hide JoDisgust
                show JoMad:
                    xalign 0.9
                    yalign 1.0
                F1 "Wait, what? But I don't want to move."
                show MNorm with dissolve
                F2 "Also, we don't know anything about Karl. He could be super weird!"
                F2 "No offense, Karl..."
                hide MNorm with dissolve
                show FNorm with dissolve
                F3 "Are you sure you want to invite Karl to sit with us?"
                hide FNorm
                menu:
                    "What do I think of Karl?"
                    
                    "Maybe they're right.":
                        $ neutral = True
                        MC "Yeah, maybe you're right. We'll go sit there without him."
                        hide JoMad
                        show JoDisgust:
                            xalign 0.9
                            yalign 1.0
                        F1 "Ugh, fine. Let's go."
                        hide JoDisgust with dissolve
                        hide KSad with dissolve
                        play music "School Theme.wav"
                        "Joseline leads us to a table towards the back of the cafeteria, complaining about Karl the whole way."
                        "I look back to see Karl still eating, but he looks so lonely sitting by himself."
                    
                    "He seems good to me.":
                        $ good = True
                        MC "Yeah, I'm sure. After all, how will we get to know him if we don't spend time with him?"
                        play music "School Theme.wav"
                        hide KSad
                        show KNorm:
                            xalign 0.1
                            yalign 1.0
                        show MNorm with dissolve
                        F2 "Well, if you think so, I'm down. Couldn't hurt to make some new friends."
                        hide MNorm
                        show JNorm with dissolve
                        F4 "Yeah! I bet Karl's a pretty legit guy, once you get to know him."
                        hide JNorm
                        show FNorm with dissolve
                        F3 "If you say so, [myname]. Karl, I'd love to hear your thoughts on Victorian literature."
                        hide FNorm with dissolve
                        hide JoMad
                        show JoDisgust:
                            xalign 0.9
                            yalign 1.0
                        F1 "Ugh, fine. If you all are okay with it, I guess he can sit with us..."
                        show MNorm with dissolve
                        F2 "Come on, Karl. We can all go sit together. I can tell you all about my AMX car I've been working on!"
                        VC "AMX? What's that...?"
                        hide JoNorm with dissolve
                        hide KNorm with dissolve
                        "Together we all head over to the table near the back of the cafeteria with enough seats for all of us."
                        "Karl looks up for the first time since he's joined us, with a small, shy smile on his face."
                        "He also seems much happier, now that he's got some new friends. He fit in wonderfully at lunch and got along well with everyone, even Joseline."
    
    
    "Lunch continues, and before I know it, it's time to return to class."
    stop music fadeout 1.0
    play music "Goodbye.wav"
    scene School with fade
    "After lunch, the end of the day came quickly and I went about my evening as planned."
    scene School with fade
    stop music fadeout 1.0
        
    if good:
        "From that day on, Karl started spending time with our group."
        "He's really smart and helps us all with our homework during lunch."
        "He really opened up to us, and everyone really likes him. I think he'll be a part of our group for a long time."
        
    if neutral:
        "From that day on, at lunch I could always find Karl sitting alone at our old table."
        "No one ever sat with him. I wonder if all this time, he just wanted some friends."
        
    if bad:
        "From that day on, no one ever saw Karl at lunch anymore. Rumor has it he spends his lunch periods eating in the bathroom, alone, where no one can see his tears."
        
    #
    # CHAPTER 2
    #
    
    play music "Title Theme 1.wav"
    scene bedroom
    with fade

    CH "*Beep beep beep! Beep beep beep!*"
    
    "I wake to the sound of my alarm, blaring excitedly in my ears."
    menu:
        "It's been one week since school started and I’ve finally chosen to join the track team at school. It will be a nice way to get some exercise and hang out with my good friend Jake. I wonder what I should choose to eat for breakfast today."
        
        "Nothing":
           "I'm not hungry today and I really don’t want to be late for the bus."

        "Cereal":
            "That bowl of cereal hit the spot. I should be able to face today and track practice with lots of energy."
            
        "Bagel":
            "That bagel hit the spot. I should be able to face today and track practice with lots of energy."
            
    
    scene bus
    with fade
    stop music fadeout 1.0

    "The bus rounds the corner and it's off to school."

    #label development:
    
    play music "School Theme.wav"
    image hallway = im.Scale("images/hallway1.png", 1920, 1080)
    scene hallway
    with fade

    "The school day flies by as usual and it comes time for me to head to track practice with Jake."
    
    show JNorm
    with dissolve
    
    F4 "Hey [myname], I had the most lame day ever. Every class I had gave me mountains of homework and it's the second week of class."
    F4 "High school is so much harder than middle school and SOOO much more boring. Only reason I made it through the day was because I knew I could run really fast at track practice today."
    
    menu:
        "I should tell Jake about my day."
        
        "Same here.":
            MC "Ya, classes are the worst now, I feel you. I can’t believe how much homework they give out to waste our time in high school. We have lives you know?"
            F4 "You get me [myname], school is not my entire life. Anyway I guess we are here at practice. We should introduce ourselves to the team."
        
        "I barely got any homework.":
            MC "None of my classes are really that bad. I’ve got some really nice teachers and reasonable amounts of homework, I only got a short reading assignment today and a few math problems."
            F4 "LUCKY! You always get the good classes."
            "Before I can mention to him that we have almost all of the same classes we arrive at the track field. Jake and I run over to meet the other members of the track team."
            
            
    image campus = im.Scale("images/campus.png", 1920, 1080)
    scene campus
    with fade
            
    "A whole lot of bulky kids are huddled near the center of the track field chatting with each other. One kid is on his phone at the side, sitting on the ground estranged from the main group."
    
    show ZNorm
    with dissolve
    
    Z "Hey bros, wassup!  I’m Zeke and I’m the captain of the track team and the fastest person on the planet. What are your scroungy looking selves doing here? Ayy, I’m just kidding welcome to the team."
    
    show JNorm with dissolve:
        xalign .1
        yalign 1.0
    
    F4 "Hey dude! I’m Jake and this is my friend [myname]. We are gonna give you a run for your money on your self proclaimed title."
    MC "Hey. Don’t underestimate us just because we are freshmen, Zeke."
    Z "Ok bros, lets stop with these lame introductions and get straight into warmup."
    
    "The first track practice started with warmups, followed by laps around the track for a while. Basically everyone was able to keep up with the pack, except that one kid on the phone earlier."
    "I never got to talk with him but by the end of practice he was weezing, completely out of energy. I headed to the locker room to change out of my workout clothes."

    image lockerRoom = im.Scale("images/lockerRoom.jpg", 1920, 1080)
    scene lockerRoom
    with fade
    
    
    show ZNorm
    with dissolve
    
    Z "Nice practice guys. Let's cool down in here."
    
    hide ZNorm with dissolve
    
    stop music fadeout 1.0
    
    
    "I change into clothes to head back home after practice."
    "As I’m changing out of my sweaty clothes, I here some chanting from the far corner of the room. Jake looks ready to leave though and I would enjoy to walk home with him." 
    
    
    play music "BullyTheme.wav"
    
    
    menu:
        
        "I think I’ll…."
        
        "Head home with Jake.":
            MC "Jake let's head out. I’m tired let’s go back home together. I’ll walk to your house before heading home."
            
            show JNorm with dissolve
            
            F4 "Sounds awesome dude! Wanna race to the school entrance?"
            
            menu:
                
                "Do I still have enough energy to race Jake?"
                
                "Let's do it!":
                    MC "You're on!"
                    "Before I can finish my call to action, Jake is bolting towards the school entrance. I guess it's going to be an uphill battle for this win. I walk with Jake home and then go home to sleep for tomorrow."
                    
                "I'm too tired for that.":
                    "Before I even open my mouth, Jake is bolting towards the school entrance. I guess it's going to be a race even if I don’t want it. I walk with Jake home and then go home to sleep for tomorrow."
            
        "Stick around to see what is happening in the back.":
            "I decide to let Jake go home alone today and check out what's happening with the chanting in the back."
            "I go to the back to see that kid with the phone run past me in a flurry, bumping into me on his way out. Zeke and the track team are laughing in the back."
            
            menu:
                "What should I do now?"
                
                "Ask Zeke what they were chanting about.":
                    MC "What was all that chanting about?"
                    
                    show ZNorm with dissolve
                    
                    Z "Yo bro, we were just having fun chatting with Bastian. He’s TOTALLY our type of guy, right bros?"
                    
                    menu:
                    
                        S1 "Ya just some locker room talk. Everything is cool between guys am I right?"
                        
                        "Inquire further.":
                            MC "So what was the talk specifically about? He seemed in a hurry to get out of here."
                            Z "Oh, that was Bastian running out just now."
                            Z "What a joke. Considering how much of a track legend his older brother was, he’s so washed up."
                            Z "We got him to send out some texts telling the girl he likes to meet him so he can dump her."
                            Z "Maybe then he won’t be so glued to that phone during practice and start trying for once."
                            menu:
                                "Tell Zeke you dissaprove.":
                                    MC "Why are you messing with his life?"
                                    Z "Oh it will be so funny. Just wait for tomorrow."
                                    MC "Zeke go tell him to not do that. He’s just wants to be a part of this group and you are going to ruin his high school life the second it started."
                                    Z "Didn’t think you were such a buzzkill, but I guess I’ll go and tell him. Sheesh. Ppphfff."
                                    "I rushed out after Zeke but I guess we were already too late. Bastian had already gone home so it would be necessary to stop him before anything happened that he couldn’t take back."
                                    
                                "Extract yourself from the conversation":
                                    MC "Ok. I’m going to get going."
                                    "The track team antics aren't what I joined the team for."
                                    "I'll just head home and try to stay out of this drama."
                            
                        "Sounds like nothing.":
                            MC "Ok just checking in. I’m gonna head out."
                            Z "Later bro!"
                            "I head back home alone, finish up my homework and hit the sack. Track practice was a whole lot of extra work."
                    
                "Go and run after the phone kid.":
                    
                    
                    "I run after the kid on his phone to see what happened back there. I gesture him over to me at the school entrance to try and grasp what happened."
                    
                    scene School with fade
                    
                    show SNorm
                    with dissolve
                    
                    SB "What do you want with me?"
                    MC "I’m just here to check in with you, you seemed in a hurry to get out of the locker room and I never did catch your name at practice."
                    
                    menu:
                    
                        SB "It’s Bastian, I’m a freshman. Don’t bother with me I’m not worth it."
                        
                        "Find out what happened.":
                            MC "What happened? You can tell me, I’m a freshman too."
                            SB "Well, they told me to insult the girl I've had a crush on since middle school in order to be a part of the team."
                            SB "I know I'm no track star like my brother, but I really wanna work hard to get in shape and help the team."
                            SB "My father is really pushing my brother's reputation on me, and I want to be able to live up to his expectations."
                            SB "I just want to have a place to belong so badly, but I don’t want to insult the girl I like."
                            
                            menu:
                                "What should I do...?"
                                
                            
                                "Try to help.":
                                    MC "That sounds awful. Can I help you in anyway? "
                                    
                                    menu:
                                    
                                        SB "It would be great if you could do something to help that still lets me stay on the track team. I don’t think I have the heart to face her right now."
                                        
                                        "Agree.":
                                            MC "You have my word."
                                            SB "Thank you. This means a lot."
                                            
                                        "Disagree.":
                                            MC "This seems like a personal problem that you should handle yourself."
                                            
                                            label secondChoiceLabel:
                                            
                                            SB "I’m tired of being alone. This is my one chance to finally have friends and I’m willing to do anything and everything to achieve that."
                                            
                                            menu:
                                                
                                                SB "Even...even if it means losing the one person I care about. Can you please do me this one favor?"
                                                
                                                "Agree.":
                                                    MC "Fine."
                                                    SB "Thank you. This means a lot."
                                                    SB "I told her to meet me at my locker on the second floor at the beginning of the school day."
                                                    SB "It's locker number 248."
                                                    "That's right outside homeroom. How convenient; helping Bastian won't make me late for class."
                                                    
                                                "Disagree.":
                                                    MC "No way."
                                                    SB "Why did you even bother coming to check on me if your intention was to make me feel worse. Just leave me alone."
                                    
                                "He must be really desperate to do this.":
                                    MC "Wow, you must be really desperate to be in such a dilemma."
                                    jump secondChoiceLabel
                        
                        "Let him be.":
                            MC "OK, I'll respect your decision. Have a good day."
    
    
                            
    scene School with fade
    stop music fadeout 1.0
    "I go home for the night."
                            
    label development:
                            
    play music "Title Theme 1.wav"
    scene bedroom
    with fade
    
    "Another day, another a dollar."
    "That is what I would say if I were paid to learn."
    "Honestly I should really get paid for dealing with so much drama within the span of one week."
    
    stop music fadeout 1.0
    play music "School Theme.wav"
    image hallway = im.Scale("images/hallway1.png", 1920, 1080)
    scene hallway
    with fade
    
    "I walked into school and traverse the crowded hallways as usual to get to my locker."
    "It’s only been a week, but I already feel like I’m stuck in a rut."
    "As I walk up to my locker, I look around and see Fiora putting her books away in her locker."
    "Nearby I see Bastian with a few members of the track team whispering to each other."
    
    show SNorm with dissolve
    
    S1 "Hey! You ready, Bastian? This is your big moment!"
    S2 "Yeah! You do this and you’ll officially be one of us!"
    CH "One of us ! One of us! One of us!"
    SB "O...ok."
    
    "Bastian walks over slowly to Fiora. As he reaches her Fiora looks up with a smile on her face."
    
    show FNorm with dissolve:
        xalign 0.1
        yalign 1.0
    
    F3 "Hi Bastian!  I haven’t seen you in awhile. How was your Summer?"
    "Bastian only looks on at Fiora sweaty and nervous as he tries to vocalize his thoughts."
    F3 "Are you feeling alright Bastian? You’re looking kind of sweaty."
    F3 "I have a small towel you can borrow. I heard you joined the track team so  you must be working hard. "
    SB "I...I don't want your dirty towel."
    
    menu:
        
        "Fiora’s smile quickly switches to a dejected frown."
        
        "Intervene.":
            $ good2 = True
            "I immediately walk up to Fiora and Bastian just before he can say anything else hurtful to Fiora. "
            "I look at Bastian and then Fiora and grab the towel out of her hands and hand it to Bastian."
            MC "What he meant to say was that he wouldn’t want to dirty such a nice clean towel. Isn’t that right Bastian?"
            "Bastian sighing with relief wipes his brow with Fiora’s towel "
            SB "Ye...yeah that’s right. "
            F3 "Oh don’t worry about it keep it as long as you need too! So what’s it like being on the track team?"
            SB "It’s fun but I think I’m gonna quit the members are kind of jerks."
            F3 "Oh that’s too bad well if you ever want hang out after school my friends and I are always available. "
            SB "That’d be awesome!"
            MC "Hehe ye. Looks like my job is done."
            
            hide FNorm with dissolve
            hide SNorm with dissolve
            
            "I walk over to the group of track jocks looking confused as to what’s happening and give them a stern look. "
            MC "Don’t just think someone like me is going to stay a bystander as you bully others into doing your bidding."
            
        "Avoid the drama.":
            $ bad2 = True
            MC "Meh, not my problem. I wonder what they’re serving for lunch today? I hope it’s pizza pockets."
            
            hide FNorm with dissolve
            hide SNorm with dissolve
            
            "Knowing it wasn’t my place to get involved with the situation. I walked past a crying Fiora and a depressed looking Bastian."
            "The track jockey spectators just kept laughing as Bastian laid it on thick. Who knew he had it in him to be so cruel."
            
    scene cafeteria with fade
    stop music fadeout 1.0
        
    if good and good2:
        "Later that day during lunch I walked up to the usual table and looked on smiling. Bastian and Fiora were laughing together and Karl was smiling while having a conversation with Joseline, Matt and Jake."
        "Old friends, new friends. High school is looking like it won't be so bad."
        
    if neutral and good2:
        "Later that day during lunch I walked up to the usual table and looked on smiling. Bastian and Fiora were laughing together while having a conversation with Joseline, Matt and Jake."
        
    if bad and good2:
        "Later that day during lunch I walked up to the usual table. Bastian and Fiora were having a conversation with Joseline, Matt and Jake."
        
    if good and bad2:
        "Later that day during lunch everyone in our usual friend group was sitting at a table except for Fiora."
        "Joseline said that she was crying in the girl’s bathroom and wouldn’t come out."
        "Rumour has it that Bastian was the cause, but no one can ask him because he always goes home immediately after school even though he’s part of the track team now."
        "At least Karl looked pretty happy today, now tha he finally has some friends to talk to."
        "I think I made the right choice letting him into the group."
        "He and Matt turned out to be a couple of car nerds, and Karl has been helping him out with his AMX."
        "I wonder if the outcome would have been better if I was more active in stopping Bastian."

        
    if bad2:
        "Later that day during lunch everyone in our usual friend group was sitting at a table except for Fiora."
        "Joseline said that she was crying in the girl’s bathroom and wouldn’t come out."
        "Rumour has it that Bastian was the cause, but no one can ask him because he always goes home immediately after school even though he’s part of the track team now."
        "I wonder if the outcome would have been better if I was more active in stopping Bastian."
    
    return
