import random
import numpy as np
import pandas as pd
import altair as alt

random_int
n_actions = 10
actions = [i / 10 for i in range(n_actions + 1)]

# action: proportion of the private value: a \in [0,1]
# state: (number of bidders, private value, winning bid - bid,
Q = np.zeros((10, 10))
random.random()


class bidder:
    def __init__(self, id, alpha, gamma, epsilon):
        self.id = id
        self.private_value = random.randint(0, 100)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = []
        self.bids = []
        self.states = []
        self.rewards = []
        self.Q = np.zeros((10, 11))

    def policy(self, state):
        if random.random() < self.epsilon:
            action = random.randint(0, 10) / 100
            # self.actions.append(action)
            return action
        else:
            action = np.argmax(self.Q[state, :]) / 100
            # self.actions.append(action)
            return action

    def q_update(self):
        if len(self.states) > 1:
            state = self.states[-2]
            next_state = self.states[-1]
            reward = self.rewards[-2]
            action = int(self.actions[-2] * 100)
            self.Q[state, action] = (1 - self.alpha) * self.Q[
                state, action
            ] + self.alpha * (reward + self.gamma * np.max(self.Q[next_state, :]))


class auction:
    def __init__(self, n_bidders, alpha, gamma, epsilon):
        self.auctions = {}
        self.bidders = [bidder(i, alpha, gamma, epsilon) for i in range(n_bidders)]

    def winner_rule(self):
        bids = [b.actions[-1] for b in self.bidders]
        return np.argmax(bids), np.max(bids)

    def run(self, periods, auction_alpha):
        for t in range(periods):
            for b in self.bidders:
                if t != 0:
                    action = b.policy(b.states[-1])  # * b.private_value
                    bid = action * b.private_value
                    b.actions.append(action)
                    b.bids.append(bid)
                else:
                    action = random.randint(0, 10) / 100  # * b.private_value
                    bid = action * b.private_value
                    b.actions.append(action)
                    b.bids.append(bid)

            winner_bidder, winning_bid = self.winner_rule()

            for b in self.bidders:
                if b.id == winner_bidder:
                    reward = b.private_value - winning_bid
                    state = 0
                    b.states.append(state)
                    b.rewards.append(reward)
                    b.q_update()

                else:
                    reward = 0
                    state = winning_bid - b.bids[-1]
                    b.states.append(state)
                    b.rewards.append(reward)
                    b.q_update()


n_bidders = 2
alpha = 0.4
gamma = 0.9
epsilon = 0.05
a = auction(n_bidders, alpha, gamma, epsilon)
a.run(10, auction_alpha=1)
a.bidders[1].states
a.bidders[1].private_value
a.bidders[0].bids
a.bidders[1].bids

teste = 0 - 100
round(np.abs(teste))


#
# We consider a family of auction formats parameterized by $\alpha \in [1,2]$. In an $\alpha$-auction the highest bidder wins and pays a convex combination of the winning and the losing bid. The weight on the losing bid is $\alpha -1$, and the weight on the winning bid is $2-\alpha$.
#
# The payoff of the winner of period $t$ auction is $\pi_{t} = 1 - p_{t}$, where $p_{t}$ is the price determined by the mechanism chosen by the auctioneer. The losing bidder gets a payoff of $0$. Bidders maximize the expected sum of discounted per-period payoffs with a discount factor $\gamma \in (0,1)$.
