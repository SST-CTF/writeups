Archer contest!
100


100 men and women of varying heights entered an archery competition. Each was allowed to shoot 10 arrows
at a target 25m away.

We installed two cameras for the competition, one looking at the archer, the other looking at the target.
Unfortunately, John stepped on the flash drive containing footage of the arrows hitting the target at last week's
Christmas party. Luckily, we still have the footage of the shooters. We have done you the favor of breaking
down the films and extracting the heights of each archer along with the velocity and angle of each of their
shots. Could you do us the favor of figuring out who won the competition and what their score was? Thanks!

We send you the height from the ground to the tip of the arrow (archer height) then each new line contains
the "velocity angle" of the arrow. The angle is up from horizontal.

Sent over standard IO it looks something like this example:
1.350                   <- Archer 0
25.500 11.150           <- Shot 0
30.210 8.950            <- Shot 1
... 8 more shots
0.955                   <- Archer 1
21.640 14.082           <- Shot 0
29.311 17.000           <- Shot 1
... 8 more shots
... 98 more archers

All we need from you is the archer id (0-99) and the total score of that archer:
21 105                  <- "id score"

The height from the ground to the first of four scoring rings in the target is 2m. From
there, each of 4 rings is 0.2m thick, with a bullseye diameter of 0.4m.

The score values are as follows:
Bullseye: 20
Center Ring: 10
Ring 2: 5
Ring 3: 3
Ring 4: 1
Miss: -1


Host: 54.89.227.20

Port: 22256

