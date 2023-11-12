import random
import numpy as np
import pandas as pd


class bidder:
    def __init__(self, id, alpha, gamma, epsilon):
        self.id = id
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = []
        self.bids = []
        self.states = []
        self.rewards = []
        self.Q = np.ones((11, 11, 11)) * 10  # (state_1, state_2, action)
        self.Q_count = np.zeros((11, 11, 11))  # (state_1, state_2, action)

    def update_private_value(self, round, pv, pv_type, pv_dynamics, max_bid):
        if pv_dynamics is True:
            if pv_type == "constant":
                self.private_value = max_bid * pv
            elif pv_type == "uniform":
                self.private_value = random.randint(10, max_bid - 10)

        else:
            if round == 0:
                if pv_type == "constant":
                    self.private_value = max_bid * pv
                elif pv_type == "uniform":
                    self.private_value = random.randint(0, max_bid)

    def update_epsilon(self, round, total_rounds):
        self.epsilon = self.epsilon * (1 - (round / (5 * total_rounds)))
        self.epsilon = max(self.epsilon, 0.10)
        if round / total_rounds > 0.8:
            self.epsilon = 0.0

    def policy(self, state_1, state_2):
        if random.random() < self.epsilon:
            action = random.randint(0, 10) / 10
        else:
            value_max = np.max(self.Q[state_1, state_2, :])
            max_index = [
                i for i, j in enumerate(self.Q[state_1, state_2, :]) if j == value_max
            ]
            action = random.choice(max_index) / 10
            # action = np.argmax(self.Q[state_1, state_2, :]) / 10
        return action

    def q_update(self):
        if len(self.states) > 1:
            state = self.states[-2]
            next_state = self.states[-1]
            reward = self.rewards[-2]
            action = self.actions[-2]
            self.Q[state[0], state[1], action] = (1 - self.alpha) * self.Q[
                state[0], state[1], action
            ] + self.alpha * (
                reward + self.gamma * np.max(self.Q[next_state[0], next_state[1], :])
            )


class auction:
    def __init__(self, n_bidders, pv_type, pv_dynamics, max_bid, alpha, gamma, epsilon):
        self.auctions = {}
        self.max_bid = max_bid
        self.pv_dynamics = pv_dynamics
        self.pv_type = pv_type
        self.bidders = [
            bidder(
                i,
                alpha,
                gamma,
                epsilon,
            )
            for i in range(n_bidders)
        ]

    def winner_rule(self):
        bids = [b.bids[-1] for b in self.bidders]
        max_bid = max(bids)
        max_index = [i for i, j in enumerate(bids) if j == max_bid]
        winner_bidder = random.choice(max_index)
        best_bid = bids[winner_bidder]
        bids.pop(winner_bidder)
        worst_bid = min(bids)

        return winner_bidder, best_bid, worst_bid

    def run(self, periods, auction_alpha):
        for t in range(periods):
            pv = random.random()
            for b in self.bidders:
                b.update_private_value(
                    t, pv, self.pv_type, self.pv_dynamics, self.max_bid
                )
                if t != 0:
                    action = b.policy(b.states[-1][0], b.states[-1][1])
                else:
                    action = random.randint(0, 10) / 10  # * b.private_value

                bid = action * b.private_value
                b.actions.append(int(action * 10))
                b.bids.append(bid)

            winner_bidder, winning_bid, worst_bid = self.winner_rule()

            for b in self.bidders:
                if b.id == winner_bidder:
                    reward = b.private_value - winning_bid
                else:
                    reward = 0

                state_1 = min(
                    round((winning_bid / b.private_value) * 10),
                    10,
                )
                state_2 = min(
                    round((worst_bid / b.private_value) * 10),
                    10,
                )

                b.states.append((state_1, state_2))
                b.rewards.append(reward)
                b.q_update()
                b.update_epsilon(t, periods)
