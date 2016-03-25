# Car Racing

We implement a Python program, that simulates a car race.

The main championship consists of several races.

The contestants are located in an extral `cars.json` file that we have to load.

Our final idea is to implement a program that:

- Loads `cars.json` file
- Runs the races, typing a 'start <name> <races_count>' command
- After every race we store the result in  `result.json`, keeping the points of every contestant for the given race. 


Every driver takes a point for his place in a ranking list:

* For first place - 8
* Second place - 6
* Third place - 4.
* All other places are scored with 0.

**If someone crashes, he takes no points for the given race.**
