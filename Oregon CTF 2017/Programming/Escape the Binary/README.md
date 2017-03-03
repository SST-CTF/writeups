# Escape the Binary! 
## 200


You are playing a measly video game when all of the sudden you are sucked into the computer!
That would be no problem since you &lt;3 computers but as soon as you land inside you realize the active bits kill you on contact! Your task is to dodge the bits and escape to narnia or something.


Host: 54.89.227.20

Port: 22257

## Overview:

Connecting to the port 22257 on the host takes you to a simple game where you escape the 1s. IF you don't die 1500 times, then you win. 
The game presents you with a grid of places, where - are uninhabited, 1s kill you, | are the sides of the grid, and you are a #, like so:

```
|--#1--1--11-1-1-|  
|1-1--1-111-1-1-1|  
|-1---1--1-1--1-1|  
|---1-1-11-11-11-|  
|1-1--1-111-1-1-1|  
|-1---1--1-1--1-1|  
|---1-1-11-11-11-|  
|1-1--1-111-1-1-1|  
|-1---1--1-1--1-1|  
|---1-1-11-11-11-| 
```
In order to move in this strange new world, you must enter in either l to go left, s to go straight, and r to go right, while you are constantly running through the field. 


## Solution:
The solution to this problem was pretty simple. Simply make a program to connect to the port, parse the field of text, figure out the best way to go, and send the direction. Repeat this 1500 times. Unfortunately, we were pretty lazy when making this program, and realized that one could constantly be on the walls and never die. Because of this, we programmed so that going to the walls was preferred. 
The code is provided in the attached python file. `needs to be attached`
