# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

declare MC = Character("Shulk")
declare NR = Character("Narration")
declare F1 = Character("Fiora")
declare F2 = Character("Reyn")
declare F3 = Character("Sharla")
declare F4 = Character("Melia")
declare VC = Character("Riki")
declare S1 = Character("Dunban")
declare S2 = Character("Dickson")
declare CH = Character("Student Chatter")
declare BULLY = Character("Mumkar")

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

    # These display lines of dialogue.

    e "Welcome to Active Bystander!"

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
