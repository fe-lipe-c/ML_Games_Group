import random
import numpy as np
import pandas as pd


class bidder:
    def __init__(self, id, pv_type, alpha, gamma, epsilon):
        self.id = id
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = []
        self.bids = []
        self.states = []
        self.rewards = []
        self.Q = np.zeros((11, 11))

    def update_private_value(self, round, pv, pv_type, pv_dynamics, max_bid):
        if pv_dynamics is True:
            if pv_type == "constant":
                self.private_value = max_bid * pv
            elif pv_type == "uniform":
                self.private_value = random.randint(0, max_bid)

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

    def policy(self, state):
        if random.random() < self.epsilon:
            action = random.randint(0, 10) / 10
        else:
            action = np.argmax(self.Q[state, :]) / 10
        return action

    def q_update(self):
        if len(self.states) > 1:
            state = self.states[-2]
            next_state = self.states[-1]
            reward = self.rewards[-2]
            action = self.actions[-2]
            # if reward == 0:
            #     for s in range(state, 11):
            #         self.Q[s, action] = (1 - self.alpha) * self.Q[
            #             s, action
            #         ] + self.alpha * (
            #             reward + self.gamma * np.max(self.Q[next_state, :])
            #         )
            self.Q[state, action] = (1 - self.alpha) * self.Q[
                state, action
            ] + self.alpha * (reward + self.gamma * np.max(self.Q[next_state, :]))


class auction:
    def __init__(self, n_bidders, pv_type, pv_dynamics, max_bid, alpha, gamma, epsilon):
        self.auctions = {}
        self.max_bid = max_bid
        self.pv_dynamics = pv_dynamics
        self.pv_type = pv_type
        self.bidders = [
            bidder(i, pv_type, max_bid, alpha, gamma, epsilon) for i in range(n_bidders)
        ]

    def winner_rule(self):
        bids = [b.bids[-1] for b in self.bidders]

        if bids[0] == bids[1]:
            if len(self.bidders) > 2:
                print("Only 2 bidders supported")
                return

            r = random.random()
            if r > 0.5:
                winner_bidder = 0
            else:
                winner_bidder = 1
        else:
            winner_bidder = np.argmax(bids)

        return winner_bidder, np.max(bids)

    def run(self, periods, auction_alpha):
        for t in range(periods):
            pv = random.random()
            for b in self.bidders:
                b.update_private_value(
                    t, pv, self.pv_type, self.pv_dynamics, self.max_bid
                )
                if t != 0:
                    action = b.policy(b.states[-1])  # * b.private_value
                else:
                    action = random.randint(0, 10) / 10  # * b.private_value

                bid = action * b.private_value
                b.actions.append(int(action * 10))
                b.bids.append(bid)

            winner_bidder, winning_bid = self.winner_rule()

            for b in self.bidders:
                if b.id == winner_bidder:
                    reward = b.private_value - winning_bid
                else:
                    reward = 0

                # state = round((winning_bid / self.max_bid) * 10)
                state = round((winning_bid / b.private_value) * 10)
                if state > 10:
                    print("error")
                    return

                b.states.append(state)
                b.rewards.append(reward)
                b.q_update()
                b.update_epsilon(t, periods)
            # print(self.bidders[0].epsilon)
            # print(f'Round {t} epsilon: {b.epsilon}')
