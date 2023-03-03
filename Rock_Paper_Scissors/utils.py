"""Exp3 algorithm for Rock-Paper-Scissors game.

This is an implementation of the Exp3 algorithm for the Rock-Paper-Scissors
game, where the adversary is a fixed strategy.
"""

import numpy as np
import math
import scipy.special as sp
from collections import deque


class RPS_player:
    """RPS_player class."""

    def __init__(self, eta, init_dist, id, deque_size=1000, fixed_policy=False):
        """Initialize the Exp3 algorithm.

        Args:
            eta: learning rate
            init_dist: initial strategy
        """
        self.player_id = id
        self.eta = eta
        self.arms = len(init_dist)
        # self.weighted_estimator = np.zeros(self.arms)
        self.weighted_estimator = [
            deque(maxlen=deque_size),
            deque(maxlen=deque_size),
            deque(maxlen=deque_size),
        ]
        if id == 0:
            self.weighted_estimator[0].append(init_dist[0])
            self.weighted_estimator[1].append(init_dist[1])
            self.weighted_estimator[2].append(init_dist[2])
        self.policy = np.array(init_dist)
        self.policy_history = []
        self.regret_history = []
        self.rewards_history = []
        self.actions_history = []
        self.fixed_policy = fixed_policy

    def policy_update(self):
        """Update the EXP3 policy."""
        if not self.fixed_policy:

            w_array = np.array(
                [
                    sum(self.weighted_estimator[0]),
                    sum(self.weighted_estimator[1]),
                    sum(self.weighted_estimator[2]),
                ]
            )
            x = self.eta * w_array
            self.policy = np.exp(x - sp.logsumexp(x))
            self.policy /= np.sum(self.policy)
        else:
            pass

    def weighted_estimator_update(self):
        self.weighted_estimator[self.actions_history[-1]].append(
            self.rewards_history[-1] / self.policy[self.actions_history[-1]]
        )


# class RPS_exp3:
class RPS_game:
    """RPS_exp3 algorithm.

        Reward rule for Rock-Paper-Scissors game:
    1:      Actions - 0: Rock, 1: Paper, 2: Scissors
            Reward - 1: Win, 0: Draw, -1: Lose
            Player1 plays P1 and Player1 plays P2: (P1,P2)
            Draw: (0,0), (1,1), (2,2)
            Player1 wins: (0,2), (1,0), (2,1)
            Player2 wins: (0,1), (1,2), (2,0)
    """

    def __init__(self, T, players, arms=3, reward_scheme=[0, 0.1, -0.1]):
        """Initialize the Exp3 algorithm.

        Args:
            eta: learning rate
            env_dist: fixed strategy
            T: number of iterations
        """
        # self.eta = eta
        self.arms = arms
        self.T = T
        self.players = players
        self.scheme = reward_scheme
        # self.weighted_estimator = np.zeros(self.arms)
        # self.policy = np.ones(self.arms) / self.arms
        # self.policy_history = []
        # self.regret = []
        # self.true_rewards = []

        # adversary
        # self.adversary_policy = env_dist
        # self.adversary_weighted_estimator = np.zeros(self.arms)
        # self.policy_history = []

    def reward(self, action, adversary_action):
        """Return the reward of the action."""

        if action == adversary_action:  # Draw
            return self.scheme[0]
        elif action == (adversary_action + 1) % self.arms:  # Player 1 wins
            return self.scheme[1]
        else:  # Player 1 loses
            return self.scheme[2]

    # def arms_means(self):
    #     """Return the mean reward of each arm."""
    #     mu_R = (
    #         self.adversary_policy[0] * 0
    #         + self.adversary_policy[1] * -0.1
    #         + self.adversary_policy[2] * 0.1
    #     )
    #     mu_P = (
    #         self.adversary_policy[0] * 0.1
    #         + self.adversary_policy[1] * 0
    #         + self.adversary_policy[2] * -0.1
    #     )
    #     mu_S = (
    #         self.adversary_policy[0] * -0.1
    #         + self.adversary_policy[1] * 0.1
    #         + self.adversary_policy[2] * 0
    #     )
    #     return [mu_R, mu_P, mu_S]

    # def policy_update(self):
    #     """Update the policy."""
    #
    #     x = self.eta * self.weighted_estimator
    #     self.policy = np.exp(x - sp.logsumexp(x))
    #     self.policy /= np.sum(self.policy)

    # def pseudo_regret(self, action):
    #     """Return the regret of the action."""
    #     self.sum_actions_mean = 0
    #     self.arms_means()
    #     self.actions_exp += self.env_mean[action]
    #     self.regret.append(
    #         len(self.true_rewards) * max(self.env_mean) - self.actions_exp
    #     )
    def run(self):
        """Run the RPS game."""
        for t in range(self.T):
            for i in range(len(self.players)):
                self.players[i].policy_update()
                self.players[i].policy_history.append([self.players[i].policy])
                self.players[i].actions_history.append(
                    np.random.choice(self.arms, p=self.players[i].policy)
                )
            reward = self.reward(
                self.players[0].actions_history[-1], self.players[1].actions_history[-1]
            )
            self.players[0].rewards_history.append(reward)
            self.players[1].rewards_history.append(-reward)
            # self.pseudo_regret(action)
            # adversary_action = self.players[0].actions_history[-1]
            # learner_action = self.players[1].actions_history[-1]
            # self.players[0].weighted_estimator[adversary_action] += (
            #     reward / self.players[0].policy[adversary_action]
            # )
            # self.players[1].weighted_estimator[learner_action] += (
            #     -reward / self.players[1].policy[learner_action]
            # )
            self.players[0].weighted_estimator_update()
            self.players[1].weighted_estimator_update()

            # for i in range(len(self.players)):
            #     self.players[i].policy_update()

            # if t % ((self.T - 1) / 10) == 0:
            #     print(
            #         f"Iteration: {t}, Policy: Rock:{np.round(self.policy[0],3)}, Paper:{np.round(self.policy[1],3)}, Scissors:{np.round(self.policy[2],3)}"
            #     )

    # def run(self):
    #     """Run the Exp3 algorithm."""
    #     for t in range(self.T):
    #         self.policy_update()
    #         self.policy_history.append([self.policy])
    #         action = np.random.choice(self.arms, p=self.policy)
    #         adversary_action = np.random.choice(self.arms, p=self.adversary_policy)
    #         reward = self.reward(action, adversary_action)
    #         self.true_rewards.append(reward)
    #         self.pseudo_regret(action)
    #         self.weighted_estimator[action] += reward / self.policy[action]
    #
    #         if t % ((self.T - 1) / 10) == 0:
    #             print(
    #                 f"Iteration: {t}, Policy: Rock:{np.round(self.policy[0],3)}, Paper:{np.round(self.policy[1],3)}, Scissors:{np.round(self.policy[2],3)}"
    #             )
