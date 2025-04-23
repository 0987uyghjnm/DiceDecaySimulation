# ======== PROGRAM: Radioactive Dice Decay Simulator ==========
# Simulates radioactive decay using dice.
# Two logic modes:
#   1 - Odd (Parent) / Even (Daughter)
#   2 - 1–5 (Parent) / 6 (Daughter)
# Rolls dice round-by-round, logs decay per trial, and plots the curves.
# Includes adaptive legend logic, plus summary curves for large trial sets.
# =============================================================

import random
import matplotlib.pyplot as plt
import numpy as np

# ======== roll_dice() ==========
# Rolls 'num_dice' 6-sided dice and returns the results.
# ===============================
def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]


# ======== should_decay() ==========
# Determines if a dice roll value causes decay based on logic:
#  - "1": Even = decay
#  - "2": Only 6 = decay
# ==================================
def should_decay(value, logic):
    if logic == "1":
        return value % 2 == 0
    elif logic == "2":
        return value == 6
    else:
        raise ValueError("Invalid decay logic.")


# ======== simulate_decay() ==========
# Runs one trial of decay:
# Rolls dice each round, removes daughters, logs stats, returns decay curve.
# ====================================
def simulate_decay(trial_num, decay_logic, total_dice=80):
    remaining = total_dice
    roll_num = 0
    decay_curve = []

    logic_label = "Odd (Parent) / Even (Daughter)" if decay_logic == "1" else "1-5 (Parent) / 6 (Daughter)"
    print(f"\n=== Trial {trial_num} ({logic_label}) ===")
    print(f"{'Roll(s)':<8}{'Dice Left':<12}{'Parents':<10}{'Daughters':<12}"
          f"{'% Parents Left':<18}{'% Daughters Left':<20}{'Prob (decay)':<16}")
    print(f"{'0':<8}{remaining:<12}{remaining:<10}{0:<12}{100.00:<18.2f}{0.00:<20.2f}{0.0000:<16.4f}")
    print("-" * 90)

    decay_curve.append(100.0)
    roll_num += 1

    while remaining > 0:
        dice = roll_dice(remaining)
        decayed = sum(1 for d in dice if should_decay(d, decay_logic))
        survivors = remaining - decayed
        percent_remaining = (survivors / total_dice) * 100
        percent_daughters = 100 - percent_remaining
        prob = decayed / remaining if remaining > 0 else 0

        print(f"{roll_num:<8}{remaining:<12}{survivors:<10}{decayed:<12}"
              f"{percent_remaining:<18.2f}{percent_daughters:<20.2f}{prob:<16.4f}")

        decay_curve.append(percent_remaining)
        remaining = survivors
        roll_num += 1

    return decay_curve


# ======== run_experiment() ==========
# Main experiment loop:
# Prompts user for decay logic, number of trials, runs simulations, and plots results.
# ==================================
def run_experiment():
    print("\n" + "=" * 65)
    print("  WELCOME TO THE DICE DECAY SIMULATION  ".center(65))
    print("=" * 65)
    print("This simulation models radioactive decay using virtual dice.")
    print("You’ll choose a decay rule and see how 'parent isotopes' decay over time.")
    print("Each roll simulates the passage of time. Have fun!!\n")

    while True:
        print("\nChoose an experiment to run (3 to exit): ")
        print("\n1:  Odd (Parent) / Even (Daughter)")
        print("2:  1-5 (Parent) / 6 (Daughter)")
        decay_logic = input("\nEnter choice (1 or 2): ").strip()

        if decay_logic not in ["1", "2"]:
            print("Exiting....")
            return

        try:
            trials = int(input("\nHow many trials do you want to run? "))
            if trials <= 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Try again")
            continue

        all_decay_curves = []
        for trial in range(1, trials + 1):
            decay_curve = simulate_decay(trial, decay_logic)
            all_decay_curves.append(decay_curve)

        max_len = max(len(c) for c in all_decay_curves)
        padded_curves = [c + [0]*(max_len - len(c)) for c in all_decay_curves]
        np_curves = np.array(padded_curves)

        plt.figure(figsize=(10, 6))

        if trials <= 20:
            for idx, curve in enumerate(all_decay_curves):
                plt.plot(range(len(curve)), curve, label=f'Trial {idx+1}', alpha=0.6)
            legend_title = "Trial Curves"
        else:
            avg_curve = np.mean(np_curves, axis=0)
            med_curve = np.median(np_curves, axis=0)
            max_curve = np.max(np_curves, axis=0)
            min_curve = np.min(np_curves, axis=0)

            # Summary curves
            plt.plot(avg_curve, label="Average Decay", color='black', linewidth=2)
            plt.plot(med_curve, label="Median Decay", color='orange', linestyle='--', linewidth=2)
            plt.plot(max_curve, label="Max Decay", color='green', linestyle=':', linewidth=2)
            plt.plot(min_curve, label="Min Decay", color='red', linestyle=':', linewidth=2)

            # Legend section label with a visible line
            plt.plot([], [], linewidth=0, label=' ')
            plt.plot([], [], linewidth=0, label='14 Random Trials')

            random_indices = random.sample(range(trials), 14)
            for idx in random_indices:
                plt.plot(range(len(all_decay_curves[idx])), all_decay_curves[idx],
                         label=f'Trial {idx + 1}', alpha=0.4, linestyle='-')
            legend_title = "Summary"

        plt.title('Parent Isotope Decay Over Time')
        plt.xlabel('Roll(s)')
        plt.ylabel('% Parent Isotopes Remaining')
        plt.grid(True)
        plt.legend(title=legend_title)
        plt.tight_layout()
        plt.show()

        again = input("\nRun another experiment? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("\nExiting...")
            break


# Entry point to start the simulation when the script is run.
if __name__ == "__main__":
    run_experiment()
