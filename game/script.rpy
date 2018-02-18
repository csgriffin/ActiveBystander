﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define narrator = Character(None, what_italic=True)
define MC = Character("Me")
define F1 = Character("Joseline")
define F2 = Character("Matt")
define F3 = Character("Fiora")
define F4 = Character("Jake")
define VC = Character("Karl")
define S1 = Character("Side1")
define S2 = Character("Side2")
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
            "Shit! I overslept!"
            "If I hurry though, I can make it to the bus on time."
            "I can't be late on the first day of school!"
    
    scene black
    with fade
    stop music fadeout 1.0

    "The bus rounds the corner and it's off to school."

    # SCENE CHANGE HERE - SCHOOL HALLS
    
    play music "School Theme.wav"
    image hallway = im.Scale("images/hallway1.png", 1920, 1080)
    scene hallway
    with fade

    "As I wander the hall towards my homeroom class, I hear the chatter of the other students around me..."
    
    CH "DO YOU KNOW DA WAE?"

    CH "What class are you in?"

    CH "You did not just say that."

    CH "YOU MAD BRO?"

    CH "Hope I’m not in a class with him."

    CH "I've heard he’s just plain awful at everything... and his face."

    "I guess the school hallways never change. Just memes and small talk for as long as I can remember."

    "I approach the class and my friend, Fiora, approaches me with a warm smiling face."
    image classroom = im.Scale("images/classroom.jpg", 1920, 1080)
    scene classroom
    with fade
    image Fiora = im.Scale("images/fiora temp.png", 720, 720)
    show Fiora
    with dissolve
    
    F3 "Hey [myname]! I so glad I have class with you."
    F3 "I had such a wonderful summer. How was yours? Did you do anything special?"
    python:
        mysummer = renpy.input("What should I tell Fiora I did this summer?")
        mysummer = mysummer.strip()
    F3 "[mysummer]?"
    F3 "Sounds like a lot of fun!"
    F3 "Anyway, come on inside! The teacher is about to take attendance."
    image classroom2 = im.Scale("images/classroom3.jpg", 1920, 1080)
    scene classroom2
    with fade
    
    TEACHER "Everyone take a seat. Let me take attendance."
    
    "I look around to see that four of my friends from middle shcool are in my homeroom."
    "It looks like I scored the jackpot when it comes to homeroom placement!"
    
    TEACHER "Joseline?"
    image Joseline = im.Scale("images/joseline temp.png", 720, 720)
    show Joseline
    with dissolve
    
    F1 "Here!"
    hide Joseline
    with dissolve
    
    TEACHER "Matt?"
    image Matt = im.Scale("images/matt temp.png", 720, 720)
    show Matt
    with dissolve
    
    F2 "Hi"
    hide Matt
    with dissolve
    
    TEACHER "Fiora?"
    show Fiora
    with dissolve
    
    F3 "Present!"
    hide Fiora
    with dissolve
    
    TEACHER "Jake?"
    image Jake = im.Scale("images/jake temp.png", 720, 720)
    show Jake
    with dissolve
    
    F4 "'Sup!"
    hide Jake
    with dissolve
    
    TEACHER "[myname]?"
    python:
        attendance = renpy.input("Oh! The teacher is calling my name. I should say something")
        attendance = attendance.strip()
    
    MC "[attendance]!"
        
    TEACHER "Alright, now that everyone's here, let's get started..."
    
    "The first class went on for an eternity, and by the time second period rolled around it became apparent my friends were also feeling the pain of coming back to school."
    
    TEACHER "Alright, everyone, time for lunch. Take your things and head to the cafeteria."
    image cafeteria = im.Scale("images/cafeteria.jpg", 1920, 1080)
    scene cafeteria
    with fade
    
    "Thank goodness! Now I can finally have some time to catch up with my friends and tell them some stories about my summer." 
    
    "I can see Matt waving me over to the table at the front of the cafeteria."
    show Matt
    with dissolve
    
    MC "Hey! How was your summer?"
    
    F2 "It was great! I was able to fix up my AMX car over the summer with my dad. She's a real beauty!"
    
    F2 "How was your summer?"
    
    menu:
        "My summer..."
        
        "...was great!":
            
            show Matt
            MC "My summer was great!"
            F2 "Awesome!"
            
        "... could've been better...":
            
            show Matt
            MC "It could've been better..."
            F2 "Damn. Well hopefully this school year will be better."
            
label after_summer:
    
    show Matt
    F2 "Hey, I see the rest of the gang coming over here."
    hide Matt
    with dissolve
    F2 "Can you wave at them so they see us?"
    
    image Karl = im.Scale("images/karl temp.png", 720, 720)
    show Karl
    with dissolve
    "As I start to wave, I notice Karl is sitting right next to us and is already eating his turkey sandwich."
    "I must have missed him while Matt and I were talking."
    "It occurs to me that, because Karl is sitting here now, there isn't enough room for all of us to sit here."
    hide Karl
    with dissolve
    "Joseline is leading the rest of the group as they approach the table"
            
    show Joseline
    with dissolve
    F1 "Oh, it looks like we're one seat short."
    stop music fadeout 1.0

    "She looks over at Karl."
    show Joseline:
        xalign 0.9
        yalign 1.0
    
    show Karl:
        xalign 0.1
        yalign 1.0
    with dissolve
    
    play music "BullyTheme.wav"
    F1 "Hey, could you move so we can sit together?"
     
    "Karl looks up for a second, but then goes back to eating."
     
    F1 "Come on, can you move? We're gonna sit together."
     
    VC "I've already moved twice already, and I just unpacked my lunch. Sorry."
    
    F1 "Oh, come on, don't be that guy." 
    F1 "Like, seriously, just move."
    F1 "Is this SPECIFIC SPOT that important?"
    F1 "I need that spot!"
    
    "I feel like I should say something, but decide to just stand by and let things run their course."
    
    hide Karl
    with dissolve
    stop music fadeout 1.0
    "I start to see looks coming from around the cafeteria. 
     Karl gathers his lunch in a hurry and rushes to the other end of the cafeteria,
     staring at the floor, dropping some of his turkey sandwich as he goes."
    
    play music "School Theme.wav"
    F1 "Finally, I can sit!"
    hide Joseline
    show Jake
    with dissolve
    
    F4 "What is up my guys? High school seems to be off to a pretty strong start for us."
    F4 "I'm planning on joining the track team and blowing away the competition with my incredible speed!"
    F4 "Bzooooooooooooom! Ftoooooom!"
    
    "Jake had always been quick, but I'd been able to keep up with him for the most part. At least, with regard to running."
    "I never caught up to him when it came to making ridiculous noises. What a goof."
    "I'm sure the track team would be fun with him at my side."
    
    hide Jake

    #label development:
    #        "SKIPPED!"

    show Fiora
    with dissolve
    
    F3 "Speaking of speed, have you guys noticed that this day feels like anything but speedy?"
    F3 "It feels like a marathon just to get through all these rules for every class."
    F3 "I just want to get home and relax in bed with some Jane Austen books. "
    
    "Jane Austen again? I swear, Fiora reads one of Jane Austen's books literally every day."
    "She's probably the most voracious reader in the whole world!"

    hide Fiora
    with dissolve
    
    "While we eat, I decide to talk to a couple of my friends about their day so far..."
    
    menu:
        "First I talked to..."
        
        "Joseline":
            jump JoselineLunch
            
        "Matt":
            jump MattLunch
            
        "Fiora":
            jump FioraLunch
            
        "Jake":
            jump JakeLunch

label JoselineLunch:
    show Joseline with dissolve
    F1 "I was having a great day with classes until that kid had to be so rude and take that seat."
    F1 "I mean, he kinda seems like a jerk to me, don’t you think? Who just sits and doesn’t move when asked?"
            
    menu:
        "What did I think of that situation..."
              
        "Maybe she was exaggerating a little...":
            MC "I think you might have been exaggerating a little..."
            F1 "Ppfh. I mean, he did move eventually, I guess."
                  
        "She's right. What a jerk!":
            MC "You're right. What a jerk!"
            F1 "Yeah! You know what I'm talking about!"
                 
        "She was kind of a jerk to him.":
            MC "Seemed to me like YOU were the one being a jerk there."
            F1 "You're gonna come out and call ME the jerk?! I thought you were my friend, not some little weasel."
    hide Joseline with dissolve
    $ JoselineTalk = True
    if lunchTalk:
        jump afterLunch
    else:
        $ lunchTalk = True
        jump secondFriend

label MattLunch:
    show Matt with dissolve
    F2 "My day has been nothing but boring; the classes haven’t even shifted into 2nd gear yet."
    F2 "All we get are teachers who explain rules and then give a dumb icebreaker, even though I know half the kids."
    F2 "I can’t wait to get home to the car to tweak a few things though."
    hide Matt with dissolve
    $ MattTalk = True
    if lunchTalk:
        jump afterLunch
    else:
        $ lunchTalk = True
        jump secondFriend
    
label FioraLunch:
    show Fiora with dissolve
    F3 "English class was interesting, but when the teacher told us what books we were going to be reading I had already read every single one."
    F3 "Guess my homework is going to be more on the light side this year!"
    hide Fiora with dissolve
    $ FioraTalk = True
    if lunchTalk:
        jump afterLunch
    else:
        $ lunchTalk = True
        jump secondFriend
    
label JakeLunch:
    show Jake with dissolve
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
            
    hide Jake with dissolve
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
            
            "Matt":
                jump MattLunch
            
            "Fiora":
                jump FioraLunch
            
            "Jake":
                jump JakeLunch
    
    if MattTalk:
        menu:
            "Next I talked to..."
            
            "Joseline":
                jump JoselineLunch
            
            "Fiora":
                jump FioraLunch
            
            "Jake":
                jump JakeLunch
    
    if FioraTalk:
        menu:
            "Next I talked to..."
            
            "Joseline":
                jump JoselineLunch
            
            "Matt":
                jump MattLunch
                
            "Jake":
                jump JakeLunch
                
    if JakeTalk:
        menu:
            "Next I talked to..."
            
            "Joseline":
                jump JoselineLunch
                
            "Matt":
                jump MattLunch
            
            "Fiora":
                jump FioraLunch
                
label afterLunch:
    scene black with fade
    stop music fadeout 1.0
    "The bell rings, signaling the end of our lunch period, and we all head back to class."
    play music "Goodbye.wav"
    image School = im.Scale("images/school.png", 1920, 1080)
    scene School with fade
    "Before long, my school day is over and it's time to head home. I guess seeing my friends made the rest of the day go by faster."
    
    stop music fadeout 1.0
    scene black with fade
    "The next day..."
    play music "Title Theme 1.wav"
    scene bedroom with fade
    
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
    
    scene black with fade
    stop music fadeout 1.0
    "The bus comes by at it's usual time and takes me to school."
    "The first half of my day is boring, but goes by quickly. Before I know it, the bell rings for lunch and I'm off to see my friends."
    
    scene cafeteria with fade
    play music "School Theme.wav"
    "Lunch today is the leftover spaghetti and meatballs from dinner last night."
    show Fiora:
        xalign 0.1
        yalign 1.0
    "I see Fiora reading a 'Series of Unfortunate Events' book, and next to her is Matt."
    show Matt:
        xalign 0.9
        yalign 1.0
    "He's scarfing down some pizza with.. are those oreos and french fries?!"
    "He's always had such odd tastes..."
    "I strike up a conversation with Matt as I approach the table."
    hide Fiora with dissolve
    show Matt:
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
            
        "I can get my work done another time.":
            MC "Sure! Sounds like a plan."
            F2 "Awesome!"
            
    F2 "Let's talk about it more later. I see the rest of the group coming."
    hide Matt
    show Karl
    with dissolve
    "Yet again, while talking to Matt, somehow Karl snuck in, sat down, and started on his lunch."
    show Karl:
        xalign 0.1
        yalign 1.0
    show Joseline:
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
    menu:
        "What should I do...?"
        
        "Karl should just move. We were going to sit here":
            $ bad = True
            MC "Karl, you should just move. These are our seats."
            F1 "Yeah, Karl. Everybody wants you out because you just sit down without asking."
            F1 "You're just being straight up rude!"
            hide Karl with dissolve
            stop music
            "Karl picks up his lunch and leaves the lunchroom."
            hide Joseline with dissolve
            "There’s a brief pause as the kids in the lunchroom watch him go, but then conversation resumes as normal."
            play music "School Theme.wav"
        
        "Karl can stay here. We can just move.":
            $ neutral = True
            MC "Karl, you can stay here. Come on, guys, let's go find another table."
            F1 "Fine. There's a table over there."
            F1 "Getting into this same fight over and over isn't worth the stress, and he's not going to change his mind."
            F1 "We'll just sit over there from now on."
            hide Joseline with dissolve
            hide Karl with dissolve
            stop music
            play music "School Theme.wav"
            "Joseline leads us to a table towards the back of the cafeteria, complaining about Karl the whole way."
            "I look back to see Karl still eating, but he looks so lonely sitting by himself."
            
        "There's a table over there that can seat all of us.":
            $ good = True
            stop music
            MC "Hey, wait. There's a table over there with enough seats for all of us."
            F1 "Wait, what? But I don't want to move."
            play music "School Theme.wav"
            show Matt with dissolve
            F2 "I'm down. Couldn't hurt to make some new friends."
            hide Matt
            show Jake with dissolve
            F4 "Yeah! Karl seems like a pretty legit guy."
            hide Jake
            show Fiora with dissolve
            F3 "What a splendid idea! Karl, I'd love to hear your thoughts on Victorian literature?"
            hide Fiora with dissolve
            VC "..."
            F1 "Ugh, fine. If you all are okay with it, I guess I am too."
            F1 "Come on, Karl. We can all go sit together."
            hide Joseline with dissolve
            hide Karl with dissolve
            "Together we all head over to the table near the back of the cafeteria with enough seats for all of us."
            "Karl looks up for the first time since he's joined us, with a small, shy smile on his face."
            "He also seems much happier, now that he's got some new friends. He fit in wonderfully at lunch and got along well with everyone, even Joseline."
    
    
    "Lunch continues, and before I know it, it's time to return to class."
    stop music fadeout 1.0
    play music "Goodbye.wav"
    scene School with fade
    "After lunch, the end of the day came quickly and I went about my evening as planned."
    scene black with fade
    stop music fadeout 1.0
    
    "CONCLUSION"
    
    if good:
        "From that day on, Karl started spending time with our group."
        "He's really smart and helps us all with our homework during lunch."
        "He really opened up to us, and everyone really likes him. I think he'll be a part of our group for a long time."
        
    if neutral:
        "From that day on, at lunch I could always find Karl sitting alone at our old table."
        "No one ever sat with him. I wonder if all this time, he just wanted some friends."
        
    if bad:
        "From that day on, no one ever saw Karl at lunch anymore. Rumor has it he spends his lunch periods eating in the bathroom, alone, where no one can see his tears."
        
        

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
            
    
    scene black
    with fade
    stop music fadeout 1.0

    "The bus rounds the corner and it's off to school."
    
    play music "School Theme.wav"
    image hallway = im.Scale("images/hallway1.png", 1920, 1080)
    scene hallway
    with fade

    "The school day flies by as usual and it comes time for me to head to track practice with Jake."
    
    show Jake
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
            
            
    image campus = im.Scale("images/school entrance2.jpg", 1920, 1080)
    scene campus
    with fade
            
    "A whole lot of bulky kids are huddled near the center of the track field chatting with each other. One kid is on his phone at the side, sitting on the ground estranged from the main group."
    
    image Zeke = im.Scale("images/zeke temp.png", 720, 720)
    show Zeke
    with dissolve
    
    Z "Hey bros, wassup!  I’m Zeke and I’m the captain of the track team and the fastest person on the planet. What are your scroungy looking selves doing here? Ayy, I’m just kidding welcome to the team."
    F4 "Hey dude! I’m Jake and this is my friend [myname]. We are gonna give you a run for your money on your self proclaimed title."
    MC "Hey. Don’t underestimate us just because we are freshmen, Zeke."
    Z "Ok bros, lets stop with these lame introductions and get straight into warmup."
    
    "The first track practice started with warmups into laps around the track for a while. Basically everyone was able to keep up with the pack for the hour or so we practiced except that one kid on the phone earlier."
    "I never got to talk with him but by the end of practice he was weezing, completely out of energy. I headed to the locker room to change out of my workout clothes."          
    
    
    
    return
