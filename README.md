# M.A.R.V.I.N

A language to have fun with. Mostly just to simulate science experiments

# Important stuff to know before you delve into the documentation

* This language is a prototyoe and is still really buggy
* Try not to leave any spaces between signs like = and more. eg. `variable="some value"`
* In any case with parens - () always leave a comma at the end except for when its empty. eg. (var,).

# variables

* these accept integer values ,string values and booleans
* define them like this:`var=1` or `var="abcd"`
* there arent any scopes like global and local scopes yet, we might add that in the future

# defining functions

* These are blocks of code that are to be executed when called. They serve as blocks of code for many purposes.
* define a function like:
```
create function(args,)=>{
  //code to execute
}

//or

create functionWithNoArgs()=>{
  //procedure
}
```
* these arguments will become variables once the function is called and you can access them throughout the code after the function is called
* they are actually more like procedures in this language than functions
# calling functions
* a lot of the errors in syntax while defining functions are ignored 
* to call a function you must give the function's name along with any arguments values
* there are two types of argument structures - one for strings and integers (both positive and negative) and one for variables, **do not** mix the two
* an example of this would be:
```
function("arg",)
//or
arg="arg"
function(arg,)
//or
functionWithNoArgs()
```

# conditionals
* these conditions use functions as the blocks of code to be executed when any one of them executes
* this executes if the condition specified for it is true. To complete this condition once you have stated it you must define an else. The else serves as an endif, like saying that the if is over and you can finish trying to make a decision
* an example for the code for this would be:
```
create func()=>{
  output("true",)
}
create func2()=>{
  output("false",)
}
if(1>2)=>{func}
else=>{func2}

```
* there is also `elf` which is basically else if:
```
create func3()=>{
  output("false",)
}
if(1>2)=>{func}
elf(3>2)=>{func3}
else=>{func2}
```

# output
* to output stuff you simply write:
```
//for outputting strings,integers and booleans
output(1,)
output("str",)
//for outputting variables
var="I AM A VARIABLE AHH"
output(var,)
```

# counter controlled loop
* as per my computer science book, an example of a counter controlled loop is a for loop
* for right now in this prototype, we only have counter controlled loops, however we do want to add condition controlled loops as well (eg. while loops)
* This is what the structure of the for loop should be like:
```
for(i=<initial value>;<end value>)=>{
//procedures
}
```
* an example of its usage would be:
```
for(i=0;42)=>{
  output("the value is:",)
  output(i,)
}
```

# use a marvin library

* say you have some marvin code that you want to include in your new marvin file, but its too much to copy and paste and you dont want to go through all that effort, you can simply use our `mod`function to import it
* simply write `mod <filename>` and dont include the extension. Say your marvin code is in the file `sirius.vin` and you want it in the `main.vin` file. All you have to do is write:
```
mod sirius
```
* make sure the file is in the same directory(folder) as your main.vin file

# use python code
* As of right now our language isnt complete and is far from perfect, if you do find some limitations in the language, you can always make a library for all the users in python that has features that our language may not have.
* note that this is for only till we are completely satisfied with our language. However, if you all really like this feature, please say so and we will consider not removing it
* now this is the same as including a marvin file just a different function : 
```
modpy <python filename>
```
* once you do this the python code will be executed and you can call the python functions
# calling python functions:
* to call a python function from the file you imported using `modpy` you simply  add a `#` before it. 
* suppose I have a python function called `out(argument)` to print something out, I can simply write it as:
```
#out("print me out",)
```

# fun features
* now you would have thought that the documentation would have ended here, but all that we had before was just what any general purpose language would have. However, this is not a general purpose language. This is not for building complex xommercial applications or writing code to make robots move(even though you could do both those tasks with it if you wanted...)
* Even though we didnt have much time to or any idea how to, we still made these extra fun parts of the language that shows what we really want it to be - something to experiment with and have fun with. Something to make science more interesting. I would wriote more on what this language is but I cant wait to show you all the fun you can have with these features
* they are for animating and simulating particles or whatever you want these to be with physics. 
* We didnt add as much physics as we wanted to but we did manage to create the basic stuff
* now lets get to the coding!
## making objects
* to see objects on the screen you must define them first and the `obj` command will help you make them
* this is how it us structured:
```
obj <object_name>=(<x Coordinate>,<y Coordinate>)
```
* an example of this would be:
```
obj circle=(1,1,)
//this creates a circle object in coordinate (1,1)
```
## see the objects
* before you can even define these objects, you must first be able to set up the viewing of them. If you intend to play around with the objects then before you define tjem you must write the following command on top of them - `physics()`. This also sets up the collision detection and keeps the objects in frame. 
* you would place it in the code like this:
```
physics()
obj circle=(1,1,)
//now this code will be extended on while teaching the rest of the concepts
```

## moving the objects
* to move the objects you use almost the same code as you did while defining it with the same command
* to move circle you can simply write - `obj circle=(1,1)` and this will move it forward by x value 1 and y value one. Also try it out with negative values
* so the coordinate you write in it ais basically a vector

## moving the objects randomly
* to move your objects randomly in a brownian motion style, simply write - `rand <name of object>`
* example:
```
rand circle
```
## using animate
* none of you movements will be shown if you dont animate the objects, to do this create a function called `animate` and put all you code inside it
* The movement will be a tad bit slow on replit for some reason, but it will still be shown. However sometimes this doesnt work on replit and if you wait till the repl session is over, it will work.
* an example of using animate would be:
```
create animate()=>{
  rand c1
}
```
# custom touch commands
* suppose an object touches another and you want it to do something when this happens... You can define a custom touch function that does exactly that
* the `touch` command lets you do this
* the structure of a touch command is:
```
touch <circle which was touched>=><name of function to be executed>
```
* There is also an inbuilt variable called `nowTouched` which gives the string value of the other circle which collided
* an example of using this would be:
```
create onTouch()=>{
  output(nowTouched)
}
touch circle=>onTouch
//nothing would really happen since circle is all alone with no other object
```

## change colour
* one last feature -  change the colour of an object
* to do this the command used is `changeCLR`
* the structure is:
```
changeCLR <object name>(<red(0-255)>,<green(0-255)>,<blue(0-255)>,)
```
* example:
```
changeCLR circle(68, 85, 255,)
//hooloovoo blue
//or
changeCLR nowTouched(255,0,0,)
//red
```

#THE end
* hope you enjoyed reading this. And I hope you enjoy using and playing w3ith marvin!
