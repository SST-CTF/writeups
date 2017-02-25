Future Chess!
400


A new variant of chess replaces old pieces with modern equivalents! Turning an old knights and kings game
into a modern snipers and generals game! However, we have a problem. We know the rules of the game
but we don't have a good way to check if the general is about to be killed (in check).

We provided you with the game's manual and we need you to be able to input the current state of the board and
respond back if the general is in check!

The layout of the board looks like this:

0 1 2 3 4 5 xAxis
1
2      N
3    W   E
4      S
5
yAxis

With an xAxis length of 8 (0-7) and yAxis length of 8.

We will send you over the wire a transcript containing all of the pieces.

Example input:
General(A,2,8,N)
Gunner(B,3,0,E)
Gunner(B,3,5,SW)
...

Generalized:
Name(Team,x,y,Direction)

and we expect output of what Generals are in danger, similar to:
A Check                                                    <- Team A General is in check
B Safe                                                     <- Team B General is not in harms way

We have quite a few boards needing solved so make sure you can handle plenty!

Host: 54.89.227.20

Port: 22258
