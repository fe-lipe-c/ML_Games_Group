"""bandit algorithm.

A Bandit algorithm thar uses ______ to select the best arm.
"""

import numpy as np


class Player:
    """RPS Players that uses a multi-armed bandit algorithm."""
    
    def __init__(self, actions=3):
        """Initialize the player."""
        self.actions = actions
        self.arm_values = np.zeros(self.actions)
        self.counts = np.zeros(self.actions)
        self.values = np.zeros(self.actions)
    
    def select_arm(self):
        """Select the best arm."""

        pass
    
    def update(self, chosen_action, reward):
        """Update the chosen arm."""
        self.counts[chosen_action] += 1
        n = self.counts[chosen_action]
        value = self.values[chosen_action]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward
        self.values[chosen_arm] = new_value
    
    def run(self):
        """Run the bandit algorithm."""
        chosen_arms = np.zeros(self.runs)
        rewards = np.zeros(self.runs)
        for i in range(self.runs):
            chosen_arm = self.select_arm()
            reward = np.random.normal(self.arm_values[chosen_arm])
            self.update(chosen_arm, reward)
            chosen_arms[i] = chosen_arm
            rewards[i] = reward
        return chosen_arms, rewards
    
    def __str__(self):
        """Return the string representation of the bandit algorithm."""
        return "Multi-armed bandit algorithm."
    
    def __repr__(self):
        """Return the string representation of the bandit algorithm."""
        return "MultiArmedBandit(arms={}, runs={})".format(self.arms, self.runs)k
