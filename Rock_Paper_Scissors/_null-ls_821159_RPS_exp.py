"""Exp3 algorithm for Rock-Paper-Scissors game.

This is an implementation of the Exp3 algorithm for the Rock-Paper-Scissors
game, where the adversary is a fixed strategy.
"""

import numpy as np
import math


class RPS_exp3:
    """RPS_exp3 algorithm."""

    def __init__(self, eta, env_dist, T):
        """Initialize the Exp3 algorithm.

        Args:
            eta: learning rate
            env_dist: fixed strategy
            T: number of iterations
        """
        self.eta = eta
        self.env_dist = env_dist
        self.arms = len(env_dist)
        self.T = T
        self.total_reward = np.zeros(self.arms)

    def Policy(self):
        """Return the policy."""
        return self.total_reward / self.T

