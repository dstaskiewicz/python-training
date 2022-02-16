# Monty Hall problem

Background
For the purpose of today's challenge, the Monty Hall scenario goes like this:

There are three closed doors, labeled #1, #2, and #3. Monty Hall randomly selects one of the three doors and puts a prize behind it. The other two doors hide nothing.
A contestant, who does not know where the prize is, selects one of the three doors. This door is not opened yet.
Monty chooses one of the three doors and opens it. The door that Monty opens (a) does not hide the prize, and (b) is not the door that the contestant selected. There may be one or two such doors. If there are two, Monty randomly selects one or the other.
There are now two closed doors, the one the contestant selected in step 2, and one they didn't select. The contestant decides whether to keep their original choice, or to switch to the other closed door.
The contestant wins if the door they selected in step 4 is the same as the one Monty put a prize behind in step 1.
Challenge
A contestant's strategy is given by their choices in steps 2 and 4. Write a program to determine the success rate of a contestant's strategy by simulating the game 1000 times and calculating the fraction of the times the contestant wins. Determine the success rate for these two contestants:

Alice chooses door #1 in step 2, and always sticks with door #1 in step 4.

Bob chooses door #1 in step 2, and always switches to the other closed door in step 4.

Optional bonus
Find success rates for these other contestants:

Carol chooses randomly from the available options in both step 2 and step 4.

Dave chooses randomly in step 2, and always sticks with his door in step 4.

Erin chooses randomly in step 2, and always switches in step 4.

## Idea from https://old.reddit.com/r/dailyprogrammer/comments/n94io8/20210510_challenge_389_easy_the_monty_hall_problem/

Alice won 335 times.
Bob won 644 times.
Carol won 506 times.
Dave won 314 times.
Erin won 659 times.