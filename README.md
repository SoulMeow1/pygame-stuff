# What is the point of this?
Just to practice some OOP and design patterns. Originally I wanted to create a game but looks like im all out of motivation and time :/

## Features used: Factory pattern
OptionFactory is the default and other Option subclasses inherit from it and fulfill their own niches. Under OptionFactory class, many getter and setter functions are created and the code looks long as hell. 
But the subclasses are much shorter as you only have to declare the option's action function which is where all the misc stuff happens. 

## Features used: Lots of encapsulation
Creating a game option is as easy as declaring what kind of option is it (like change screen resolution) ->  what is  its name -> what colour is it -> then append it to a Menu class object. 
You have many additional features like specifying its drawn location, declaring its font and fontsize.

Creating a Menu is as easy as appending options you want -> align them for neatness -> execute the menu

This whole exercise feels like im creating a game engine instead of creating a game so maybe next time I should've just used a game engine from the get go.
 
