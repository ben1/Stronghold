# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    "How shall the brave adventurer be known as?"

menu:    
    
    "Sir":
        jump sir
    "Lady":
        jump lady

label sir:
    "Hi Sir."
    return

label lady:
    "Hi Lady."
    return
