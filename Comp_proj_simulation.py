import numpy as np

def get_user_input():
    num_computers = int(input("Enter number of computers: "))
    infection_prob = float(input("Enter infection probability (0 to 1): "))
    recovery_per_day = int(input("Enter number of computers repaired daily: "))
    return num_computers, infection_prob, recovery_per_day


def virus_simulation(num_computers=20, infection_prob=0.1, recovery_per_day=5, num_simulations=10000):
    total_days = []  # To track the number of days for each simulation
    total_infected_counts = []  # To track the number of unique computers infected
    all_computers_infected_flags = []  # To track if all computers got infected at least once

    for _ in range(num_simulations):
        # Initialize the simulation
        infected = set([0])  # Start with computer c_1 infected (index 0)
        total_infected = set(infected)  # Track all unique infections
        days = 0

        # Single simulation while-loop
        while infected:
            days += 1

            # Morning: Virus spreads
            new_infections = set()
            for clean_computer in range(num_computers):
                if clean_computer not in infected:  # Clean computer
                    # Check if it gets infected from any currently infected computer
                    if any(np.random.rand() < infection_prob for _ in infected):
                        new_infections.add(clean_computer)
            
            # Update infected set with new infections
            infected.update(new_infections)
            total_infected.update(new_infections)  # Track all unique infections

            # Afternoon: Technician cleans
            if len(infected) <= recovery_per_day:
                # All infected computers are cleaned
                infected.clear()
            else:
                # Randomly clean 5 infected computers
                cleaned_computers = set(np.random.choice(list(infected), size=recovery_per_day, replace=False))
                infected -= cleaned_computers

        # Record results for this simulation
        total_days.append(days)  # Number of days to clean the network
        total_infected_counts.append(len(total_infected))  # Total number of unique computers infected
        all_computers_infected_flags.append(len(total_infected) == num_computers)  # Did all computers get infected?

    # Compute the averages
    avg_days = np.mean(total_days)
    avg_infected_count = np.mean(total_infected_counts)
    prob_all_computers_infected = np.mean(all_computers_infected_flags)

    return avg_days, avg_infected_count, prob_all_computers_infected

# Run the simulation
num_simulations = 10000
avg_days, avg_infected_count, prob_all_computers_infected = virus_simulation(num_simulations=num_simulations)

# Print results
print(f"Average days to clean network: {avg_days:.2f}")
print(f"Average number of unique computers infected: {avg_infected_count:.4f}")
print(f"Probability all computers get infected at least once: {prob_all_computers_infected:.8f}")

num_computers_user, infection_prob_user, recovery_per_day_user = get_user_input()
avg_days, avg_infected_count, prob_all_computers_infected = virus_simulation(num_computers_user, infection_prob_user, recovery_per_day_user, num_simulations=num_simulations)
print(f"Average days to clean network: {avg_days:.2f}")
print(f"Average number of unique computers infected: {avg_infected_count:.4f}")
print(f"Probability all computers get infected at least once: {prob_all_computers_infected:.8f}")