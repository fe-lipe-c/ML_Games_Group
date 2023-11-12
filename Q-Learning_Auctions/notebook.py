import numpy as np
import random
import altair as alt
from auction import auction

n_bidders = 3
max_bid = 100
alpha = 0.1
gamma = 0.9
epsilon = 0.9

pv_type = "constant"
pv_dynamics = False

# def __init__(self, n_bidders, pv_type, pv_dynamics, max_bid, alpha, gamma, epsilon):
a = auction(n_bidders, pv_type, pv_dynamics, max_bid, alpha, gamma, epsilon)
a.run(100000, auction_alpha=1)

a.bidders[0].states[100:110]
a.bidders[1].states[100:110]
a.bidders[2].states[100:110]
a.bidders[2].actions[100:110]
a.bidders[0].actions[-10:]
a.bidders[1].actions[-10:]
a.bidders[2].actions[-10:]
a.bidders[0].private_value
a.bidders[1].private_value
a.bidders[1].bids[-10:]
[round(i, 2) for i in a.bidders[0].Q[9, :]]
a.bidders[0].Q[3, :]
a.bidders[1].Q[5, 6, :]
np.max(a.bidders[1].Q[2, :])

for i in range(11):
    for j in range(11):
        if i < j:
            continue

        value_max = np.max(a.bidders[0].Q[i, j, :])
        max_index = [i for i, j in enumerate(a.bidders[0].Q[i, j, :]) if j == value_max]
        print(f"state {i, j} -> {max_index}")


a.bidders[0]
np.argmax

# action = np.argmax(self.Q[state_1, state_2, :]) / 10

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


n_bid
# New matrix with n_bid dimentsion
Q = np.zeros((n_bid, n_bid))

Q = np.zeros((3, 3, 3))
Q
for i in range(3):
    for j in range(3):
        for t in range(3):
            n = random.randint(0, 20)
            Q[i, j, t] = n

t = [random.randint(0, 4) for i in range(10)]
t
