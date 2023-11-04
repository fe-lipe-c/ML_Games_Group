import random
import numpy as np
import pandas as pd
import altair as alt


class bidder:
    def __init__(self, id, max_bid, alpha, gamma, epsilon):
        self.id = id
        # self.private_value = random.randint(0, max_bid)
        self.private_value = max_bid * 0.6
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = []
        self.bids = []
        self.states = []
        self.rewards = []
        self.Q = np.zeros((11, 11))  # * max_bid

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
    def __init__(self, n_bidders, max_bid, alpha, gamma, epsilon):
        self.auctions = {}
        self.max_bid = max_bid
        self.bidders = [
            bidder(i, max_bid, alpha, gamma, epsilon) for i in range(n_bidders)
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
            for b in self.bidders:
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


n_bidders = 2
max_bid = 100
alpha = 0.1
gamma = 1
epsilon = 0.9
# def __init__(self, n_bidders, max_bid, alpha, gamma, epsilon):
a = auction(n_bidders, max_bid, alpha, gamma, epsilon)
a.run(100000, auction_alpha=1)
a.bidders[0].states[-10:]
a.bidders[1].states[-10:]
a.bidders[0].actions
a.bidders[0].actions[-10:]
a.bidders[1].actions[-10:]
a.bidders[0].private_value
a.bidders[1].private_value
a.bidders[0].bids
a.bidders[1].bids
a.bidders[1].bids[-10:]
a.bidders[0].rewards[-100:]
a.bidders[1].rewards[-100:]
a.bidders[1].epsilon
(18 / 100) * 10
round((winning_bid / self.max_bid) * 10)
a.bidders[0].Q
a.bidders[0].Q[8, :]
a.bidders[1].Q[10, :]
np.max(a.bidders[1].Q[2, :])

for i in range(11):
    print(f"state {i} -> {np.argmax(a.bidders[0].Q[i, :])}")

v = 2000
rounds = list(range(0, v))
rounds = rounds + rounds
bidder_id = [0] * v + [1] * v
total_actions = a.bidders[0].actions[-v:] + a.bidders[1].actions[-v:]
total_states = a.bidders[0].states[-v:] + a.bidders[1].states[-v:]
df = pd.DataFrame()
df["round"] = rounds
df["bidder_id"] = bidder_id
df["action"] = total_actions

chart_0 = (
    alt.Chart(df.query("bidder_id == 0"))
    .mark_line(color="red")
    .encode(
        alt.X("round:O"),
        alt.Y("action:Q"),
    )
    .properties(height=800, width=1000)
)
chart_1 = (
    alt.Chart(df.query("bidder_id == 1"))
    .mark_line(color="blue")
    .encode(
        alt.X("round"),
        alt.Y("action"),
    )
    .properties(height=800, width=1000)
)
chart = chart_0 + chart_1
chart.save("chart.html")

state = a.bidders[1].states[-2]
state
# next_state = self.states[-1]
# reward = self.rewards[-2]
# action = self.actions[-2]
# # if reward == 0:
# #     for s in range(state, 11):
# #         self.Q[s, action] = (1 - self.alpha) * self.Q[
# #             s, action
# #         ] + self.alpha * (
# #             reward + self.gamma * np.max(self.Q[next_state, :])
# #         )
# self.Q[state, action] = (1 - self.alpha) * self.Q[
#     state, action
# ] + self.alpha * (
#     reward + self.gamma * np.max(self.Q[next_state, :])
# )
