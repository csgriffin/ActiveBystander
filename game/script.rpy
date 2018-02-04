# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("Shulk")
define NR = Character("Narration")
define F1 = Character("Fiora")
define F2 = Character("Reyn")
define F3 = Character("Sharla")
define F4 = Character("Melia")
define VC = Character("Riki")
define S1 = Character("Dunban")
define S2 = Character("Dickson")
define CH = Character("Student Chatter")
define TEACHER = Character("Teacher")
define BULLY = Character("Mumkar")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    NR "It's finally time to head off to the first day of high school after an exciting summer with my friends. I’m really hoping that my class is filled with my friends. The bus rounds the corner and it's off to school."

    # SCENE CHANGE HERE - SCHOOL HALLS

    CH "DO YOU KNOW DA WAE?"

    CH "What class are you in?"

    CH "You did not just say that."

    CH "YOU MAD BRO?"

    CH "Hope I’m not in a class with him."

    CH "(at MC) I've heard he’s just plain awful at everything... and his face."

    NR "I guess the school hallways never change. Just memes and small talk for as long as I can remember."

    NR "I approach the class and my friend, Fiora approaches me with a warm smiling face."

    F1 "MC! I so glad I have class with you. Come on inside! The teacher is about to take attendance."

    TEACHER "Everyone take a seat. Let me take attendance."

    return
