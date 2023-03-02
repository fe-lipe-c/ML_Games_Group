"""Exp3 algorithm for Rock-Paper-Scissors game.

This is an implementation of the Exp3 algorithm for the Rock-Paper-Scissors
game, where the adversary is a fixed strategy.
"""

import numpy as np
import math
import scipy.special as sp


class RPS_exp3:
    """RPS_exp3 algorithm.

        Reward rule for Rock-Paper-Scissors game:
    1:      Actions - 0: Rock, 1: Paper, 2: Scissors
            Reward - 1: Win, 0: Draw, -1: Lose
            Player1 plays P1 and Player1 plays P2: (P1,P2)
            Draw: (0,0), (1,1), (2,2)
            Player1 wins: (0,2), (1,0), (2,1)
            Player2 wins: (0,1), (1,2), (2,0)
    """

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
        self.policy = np.ones(self.arms) / self.arms
        # self.policy = np.random.rand(3)
        # self.policy = self.policy / self.policy.sum()
        self.policy_history = []
        self.regret = []
        self.true_rewards = []
        self.actions_exp = 0
        self.arms_means()

    def reward(self, action, env_action):
        """Return the reward of the action."""
        if action == env_action:  # Draw
            return 0
        elif action == (env_action + 1) % self.arms:  # Player 1 wins
            return 0.1
        else:  # Player 1 loses
            return -0.1

    def arms_means(self):
        """Return the mean reward of each arm."""
        mu_R = self.env_dist[0] * 0 + self.env_dist[1] * -0.1 + self.env_dist[2] * 0.1
        mu_P = self.env_dist[0] * 0.1 + self.env_dist[1] * 0 + self.env_dist[2] * -0.1
        mu_S = self.env_dist[0] * -0.1 + self.env_dist[1] * 0.1 + self.env_dist[2] * 0
        self.env_mean = [mu_R, mu_P, mu_S]

    def policy_update(self):
        """Update the policy."""

        x = self.eta * self.total_reward
        self.policy = np.exp(x - sp.logsumexp(x))
        self.policy /= np.sum(self.policy)

    def pseudo_regret(self, action):
        """Return the regret of the action."""
        self.actions_exp += self.env_mean[action]
        self.regret.append(
            len(self.true_rewards) * max(self.env_mean) - self.actions_exp
        )

    def run(self):
        """Run the Exp3 algorithm."""
        for t in range(self.T):
            self.policy_update()
            self.policy_history.append([self.policy])
            action = np.random.choice(self.arms, p=self.policy)
            env_action = np.random.choice(self.arms, p=self.env_dist)
            reward = self.reward(action, env_action)
            self.true_rewards.append(reward)
            self.pseudo_regret(action)
            self.total_reward[action] += reward / self.policy[action]

            if t % ((self.T - 1) / 10) == 0:
                print(
                    f"Iteration: {t}, Policy: Rock:{np.round(self.policy[0],3)}, Paper:{np.round(self.policy[1],3)}, Scissors:{np.round(self.policy[2],3)}"
                )
