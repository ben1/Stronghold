# Stronghold
An experimental adventure.

## Concept
The idea is to create a text-based game that has the narrative impetus of a 'choice-based' game, but without the fixed paths that generally come with that.

The reason for wanting a narrative flow to the game is to avoid the problems that typical text adventure games have where the player is wandering around looking for things and trying combinations of verbs and nouns until something works. Choice-based text games have a branching graph structure where the merging of branches is used to prevent an exponential explosion of possible scenes. Often, some scenes set some state that is used to modify future scenes, change future choices that are available, or redirect to a different scene. Regardless, the graph structure is relatively static, as well as being limited in the number of possible routes. 

In order to create a dynamic graph of scenes in the game, a narrative manager needs to be employed to choose the best scene to move to next. It must take into account the current world state in order to find potential scenes that would make sense to move to, as well as using the scene history to choose a scene that fulfils the rising/falling tension cycle of a typical narrative and guides the narrative towards a satisfying end.

## Implementation
The basic framework was fairly easy to put together. 

### Technology
The prototype uses PySide, Python bindings for Qt to create GUI elements. 

### Architecture
The **GameState** class is the root object containing information about the state of the game. It acts as a dictionary of miscellaneous information as well as a state-machine for the current scene.

The **GameView** class attaches to the GameState and creates Qt elements to display them as well as handling user input.

The **LogGameView** class attaches to the GameState and simply logs events to a file.

The **SceneTemplateRegistry**  automatically collects all scene templates based on an annotation that must be applied to each scene template class.

The **Scene** is an organizational unit for action in the game. It ties together a 
few Actors and a series of events. The exact actors that may be involved in a
scene depends on how the scene was initialized, and how the events play out
depends on the starting conditions as well as how the actors act.

**Events** of different types that occur within a Scene either mutate the game state, displaying some text, or get user input.

**Actors** contain some basic information about the actor as well as their relationships to other actors (from their perspective).

The remainder of the game is made up of scene template classes.

## Results
While the framework was easy to put together, it was hard to write scenes so generic in nature that they could appear in multiple different situations. The scenes that were written could only fit in one place in a story. The reason for this is that a lot of state and scripting would be needed to flesh out a generic scene template enough to use it in multiple different ways. In order to do this, the game world that is simulated behind the scenes needs to be relatively complex, and a lot of time needs to be spent scripting scene templates and making sure they make sense in different situations. It is currently unknown how much extra effort would be needed to create a dynamic set of scenes for this framework that generates reasonable narratives.

## Future Work

* Attempt to write a more complex set of scenes to push the limits of the framework.
* Add a narrative manager.
* Create a GUI for editing scenes, because while python is flexible, it is still clumsy to use for adding content.

