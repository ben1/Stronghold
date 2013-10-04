# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define pc = Character("[player_name]", color="#c8ffc8", kind=nvl)
define emperor = Character("Emperor Kanate", color="#cc11aa", kind=nvl)
define advisor = Character("Jeeno Kratz", color="dddda0")

# The game starts here.
label start:
"The Emperor regards you down his long nose as you kneel before him. As the pause extends, you begin to feel uncomfortable."
emperor "What was your name again?"

python:
    player_name = renpy.input("Type your name:")
    if not player_name:
        player_name = "Unknown"

pc "I am [player_name], Emperor."

emperor "Ah yes, I'm told you saved my life by killing an assassin at the parade last week." 
emperor "And if I'm not mistaken, the same Imperial agent who ended the siege of Ilsar, and more recently found the Tantoma Scrolls. The Arcanum tells me they are learning much from them."
emperor "The Empire is repaying your loyalty and resourcefulness by elevating you to nobility. Perhaps others will be inspired by your success."
emperor "Arise Dominus [player_name]."
emperor "Now there is the matter of a domain to live on. The Caldar region requires a new Dominus urgently, as it has been several months since Dominus Tenjin disappeared."
emperor "It is on the Eastern border of the Empire, not entirely civilised, but I believe it will suit your adventurous spirit! I shall send an advisor with you to help you learn the ways of a Dominus."
emperor "You will leave on tomorrow's Eastern railvan."

"Nobility! All of your descendants will bear this status. If you have any, that is. The thought of governing a domain makes you a little nervous, but how hard can the life of a noble be? You've definitely survived worse."
"And so early in the morning, you push your way through the bustle of the capital to the central rail station, looking for your advisor. He is not hard to spot, surrounded by twenty Imperial guards."

advisor "Good morning [player_name]! Is that all you are bringing with you?"

menu:
    "You will address me as Dominus [player_name].":
        jump a1
    "Yes.":
        jump a2
    "Is there something you think I will need other than my pack and my weapons?":
        jump a3

label a1:
    advisor "Yes, Dominus [player_name]."
    $ advisor_rude = True
    jump leaving
label a2:
    advisor "Okay, lets board the railvan."
    jump leaving
label a3:
    advisor "Well, you will need some more clothes, but we can buy some things on our way."

label leaving:
"Jeeno steps up into the railvan carriage and you follow him."
"You have a seat on the van, which is better than the soldiers standing squashed in the van towed behind. It wasn't many years ago when you were in their position."

