# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("Me")
#define NR = Character("Narration")
#       narration character unnecessary
#       putting in dialogue w/out a character name will produce narration
define F1 = Character("Joseline")
define F2 = Character("Matt")
define F3 = Character("Fiora")
define F4 = Character("Jake")
define VC = Character("Karl")
define S1 = Character("Side1")
define S2 = Character("Side2")
define CH = Character("BGNoise")
define TEACHER = Character("Teacher")
define BULLY = Character("Bully")

# The game starts here.
label start:

    jump development

    play music "Title Theme 1.wav"
    scene bedroom
    with fade

    "It's finally time to head off to the first day of high school after an exciting summer with my friends. I’m really hoping that my class is filled with my friends. The bus rounds the corner and it's off to school."

    # SCENE CHANGE HERE - SCHOOL HALLS
    
    stop music fadeout 1.0
    play music "School Theme.wav"
    image hallway = im.Scale("images/hallway1.png", 1920, 1080)
    scene hallway
    with fade

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
    
    F3 "Hey you! I so glad I have class with you. Come on inside! The teacher is about to take attendance."
    image classroom2 = im.Scale("images/classroom3.jpg", 1920, 1080)
    scene classroom2
    with fade
    
    TEACHER "Everyone take a seat. Let me take attendance."
    
    "I look around to see that four of my friends from middle shcool are in my homeroom. It looks like I scored the jackpot when it comes to homeroom placement!"
    
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
    
    "The first class went on for an eternity, and by the time second period rolled around it became apparent my friends were also feeling the pain of coming back to school."
    
    TEACHER "That means it's time for lunch. Take your things and head to the cafeteria."
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
    
    "As I start wave, I notice Karl is sitting right next to us and is already eating his turkey sandwich."
    "I must have missed him while Matt and I were talking."
    "It occurs to me that, because Karl is sitting here now, there isn't enough room for all of us to sit here."
    "Joseline is leading the rest of the group as they approach the table"
            
    show Joseline
    F1 "Oh, it looks like we're one seat short."
    
    "She looks over at Karl."
    
    F1 "Hey, could you move so we can sit together?"
     
    "Karl looks up for a second, but then goes back to eating."
     
    F1 "Come on, can you move? We're gonna sit together."
     
    VC "I've already moved twice already, and I just unpacked my lunch. Sorry."
    
    F1 "Oh, come on, don't be that guy." 
    F1 "Like, seriously, just move."
    F1 "Is this SPECIFIC SPOT that important?"
    F1 "I need that spot."
    
    "I start to see looks coming from around the cafeteria. 
     Karl gathers his lunch in a hurry and rushes to the other end of the cafeteria,
     staring at the floor, dropping some of his turkey sandwich as he goes."
    
    F1 "Finally, we can sit!"
    hide Joseline
    show Jake
    
    F4 "What is up my guys? High school seems to be off to a pretty strong start for us."
    F4 "I'm planning on joining the track team and blowing away the competition with my incredible speed!"
    F4 "Bzooooooooooooom! Ftoooooom!"
    
    "Jake had always been quick, but I'd been able to keep up with him for the most part. At least, with regard to running."
    "I never caught up to him when it came to making ridiculous noises. What a goof."
    "I'm sure the track team would be fun with him at my side."
    
    hide Jake

    label development:
            "SKIPPED!"

    show Fiora
    
    F3 "Speaking of speed, have you guys noticed that this day feels like anything but speedy?"
    F3 "It feels like a marathon just to get through all these rules for every class."
    F3 "I just want to get home and relax in bed with some Jane Austen books. "
    
    "Jane Austen again? I swear, Fiora reads one of Jane Austen's books literally every day. She's probably the most voracious reader in the whole world!"

    hide Fiora
    show Joseline



    menu:
         F1 "I was having a great day with classes until that kid had to be so rude and take that seat. I mean he kinda seems like a jerk to me don’t you think? Who just sits and doesn’t move when asked?"

         "Maybe you are exaggerating a little…":

             MC "Maybe you are exaggerating a little…"
             F1 "ppfh. I mean he did move eventually I guess."

         "You’re right, what a jerk.":

             MC "You’re right, what a jerk."
             F1 "Ya, you know what I’m talking about."

         "You were kind of a jerk to him.":

             MC "You were kind of a jerk to him."
             F1 "You gonna come out and say I AM THE JERK? I thought you were supposed to be my friend, not some little weasel."


    hide Fiora
    show Matt

    F2 "My day has been nothing but boring, the classes haven’t even shifted into 2nd gear yet. All we get are teachers who explain rules and then give a dumb icebreaker even though I know half the kids. I can’t wait to get home to the car to tweak a few things though."

    hide Matt
    show Fiora

    F1 "English class was interesting, but when the teacher told us what books we were going to be reading I had already read every single one. Guess my homework is going to be more on the light side this year."

    hide Fiora
    show Jake


    menu:
        F4 "Not a highlight reel thats for sure. I’m glad to see you guys again but I just hate classes for the most part. Nothing much to speak of today besides that incident earlier."

        "What incident?"
            MC "What incident?"
            F4 "That kid not moving from the seat for a while. I don’t know about you but that is the most action that has happened for me today."

        "That incident with the lunch seat?"
            MC "That incident with the lunch seat?"
            F4 "Ya, definitely stood out from all the dull classes I had before lunch."
    
    
    
    return
