RADIOACTIVE DICE DECAY SIMULATOR
------------

DESCRIPTION:
------------
This program simulates radioactive decay using physical dice rolls.
It models how unstable (parent) isotopes decay into stable (daughter) isotopes
over time by using randomized dice behavior. The simulation tracks how many
parent isotopes are left after each round of decay and visualizes this process.

It is intended for educational use, especially in classrooms learning about
radioactivity, half-life, probability, and data modeling.

I may have skipped over something, if you notice a mistake, please let me
know!! Sorry if you found a mistake, thanks for bringing it to my attention!!

-------------------------------------------------------------------------------
"LEGAL" (BORING) STUFF:
-----------------------
(_I have to put this here_)

I hereby dedicate this code to the public domain. Feel free to use,
modify, and redistribute however you like—no strings attached.
If you find it helpful, I’d appreciate a shout‑out or link back to
this repo, but it’s not required. Use at your own risk.
_**More importantly have fun!!!**_

-------------------------------------------------------------------------------
RECOMMENDED SETUP OPTIONS:
--------------------------
Option A: Run from Python (for tech-savvy users)
 - Make sure Python is installed on your system.
    - Install matplotlib by running:
         ```pip install matplotlib```
    - Then, run the program using:
         ```python DiceDecaySimulation.py```

Option B: Run the included .EXE (for Windows users)
 - This program includes a **pre-compiled .exe** file for Windows users.
  - Just double-click the .exe and the simulation will run in a command window.
  - No Python setup, no command line required. It just works out of the box!
  - The .exe works exactly like the script!

-------------------------------------------------------------------------------
HOW IT WORKS:
-------------
The simulator follows these core steps:
1. You choose a decay model:
   - Logic 1: Even numbers represent decay.
     (Odd = Parent, Even = Daughter)
   - Logic 2: Only the number 6 represents decay.
     (1–5 = Parent, 6 = Daughter)

2. You specify how many trials you want to run. 

***NOTE: The more trials the longer it'll take to run.***

3. For each trial:
   - The program starts with 80 dice (representing 80 parent isotopes).
   - Dice are rolled.
   - Dice that meet the decay condition are removed.
   - The remaining dice are rolled again until ***no parent isotopes are left***.
   - For each trial, the percentage of parent isotopes remaining is recorded round-by-round.

4. After all trials, a decay curve is plotted using matplotlib:
   - If trials are ≤ 20: all curves are plotted and labeled.
   - If trials are > 21 trials: average, median, max, and min curves are shown along with 14 randomly chosen trials.

5. The graph is shown in a pop-up window. Use the window's "Save As" feature if you want to keep an image copy of the graph.

6. When the user closes the graph's window, they are asked if they want to run another experiment.

-------------------------------------------------------------------------------
EXPLNATION OF PROGRAM LOGIC: 
------------------------------------

1. IMPORTS
----------
    import random
    import matplotlib.pyplot as plt
    import numpy as np

2. roll_dice(num_dice)
----------------------
   Rolls a specified number of 6-sided dice and returns the list of results.

3. should_decay(value, logic)
-----------------------------
  Takes a dice value and a decay logic mode. Returns True if the dice represents
    a decayed isotope based on the selected logic.

4. simulate_decay(trial_num, decay_logic)
-----------------------------------------
   - Runs a full trial using the selected logic.
    - Prints a formatted table showing:
        * Number of dice rolled (Dice Left)
        * How many were parents (survived)
        * How many were daughters (decayed)
        * % of parents remaining (based on original 80)
        * % of daughters accumulated
        * Probability of decay this round
    - Returns a list of parent percentages per round.

5. run_experiment()
-------------------
   - Main driver of the program.
    - Prompts user for logic and number of trials.
    - Calls simulate_decay() for each trial.
    - Handles graphing:
        * trials **≤** 20 trials → show all curves
        * trials **>** 50 trials → show summary stats + 14 random trials
    - Lets user repeat the simulation or exit.

6. PROGRAM ENTRY POINT
----------------------
	   if __name__ == "__main__":
        run_experiment()

-------------------------------------------------------------------------------
TERMINOLOGY EXPLAINED:
-----------------------

- PARENT ISOTOPE:
    An undecayed unit (represented by a die that is still rolled in future rounds).

- DAUGHTER ISOTOPE:
    A decayed unit (a die that matched the decay rule and is removed).

- TRIAL:
    One full simulation of the decay process, starting with 80 dice and ending
    when none are left.

- DECAY LOGIC:
    The rule used to determine if a die decays. The two built-in options are:
      1. Odd = Parent, Even = Daughter
      2. 1–5 = Parent, 6 = Daughter

- PROBABILITY OF DECAY:
    Number of decayed dice / number of dice rolled in that round.

-------------------------------------------------------------------------------
CUSTOMIZATION NOTES:
--------------------

This program was built for clarity and is fully editable. Some ways you
can modify it for your classroom:

1. Change the starting number of dice:
    In `simulate_decay()`, change `total_dice=80` to another value.

2. Add custom decay rules:
    Modify `should_decay()` to use new logic, such as:
    - "3 and 5 cause decay"
    - "Any dice < 4 decays"

3. Track extra stats:
    Add variables to calculate:
    - Total number of rounds per trial
    - Average decay probability
    - Estimate of half-life (round when ~50% of dice remain)

-------------------------------------------------------------------------------
TIPS FOR EDUCATORS:
-------------------

- Use this simulation as a hands-on activity where students predict decay rates.
- Run different logic modes to show how changing decay probability affects curve shape.
- Ask students to calculate estimated half-lives from the plotted curves.
- Compare results from multiple trials to explore randomness and probability.
- If your students are using Windows and aren't comfortable with Python,
  direct them to the included `.exe` file. It's a double-click solution
  that runs the full simulation without needing to install anything.

-------------------------------------------------------------------------------
ISSUES? BUGS? SUGGESTIONS?
-------------------

If you run into problems, have questions, or want to suggest improvements:

1. Visit the GitHub Issues page:
   https://github.com/0987uyghjnm/DiceDecaySimulation/issues

3. Open a new issue and include:
   - A short description of the problem or suggestion
   - Any error messages (if applicable)
   - The operating system you’re using
   - Python version (if not using the .exe)
   - The more details the better (Helps me w/ diagnosing)!!

***I check the repo occasionally, since this isn’t a full-time project,  but I’ll do my best.***
------------
