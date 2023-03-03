"""Notebook to implement bandit algorithms in the RPS game."""

from utils import RPS_player, RPS_game
import plot_simplex
import pandas as pd
import altair as alt
from collections import deque

player_0 = RPS_player(
    eta=0.08, init_dist=[18, -10, -1], id=0, deque_size=100, fixed_policy=False
)
player_1 = RPS_player(
    eta=0.08, init_dist=[0.8, 0.1, 0.1], deque_size=100, id=1, fixed_policy=False
)

game = RPS_game(T=2000, players=[player_0, player_1], reward_scheme=[0, 0.1, -0.1])
game.run()

chart_simplex_0 = plot_simplex.plot(
    player_0.policy_history, color="blue", init_caption=""
)
chart_simplex_1 = plot_simplex.plot(
    player_1.policy_history, color="red", init_caption=""
)
chart = chart_simplex_0.total_chart + chart_simplex_1.total_chart
chart.save("charts/simplex_path_test_player1.html")
player_0.weighted_estimator

player_0.policy_history[-1]
player_1.actions_history
# [0,
#  1,
#  0,
#  1,
#  0,
#  1,

player_0.actions_history
# [0,
#  0,
#  0,
#  0,
#  1,
#  2,
player_1.rewards_history
# [0,
#  0.1,
#  0,
#  0.1,
#  -0.1,
#  -0.1,

# eta, init_dist, fixed_policy=False)

# Stochastic RPS game
# T = 300  # game horizon
# adv_strategy = [0.4, 0.35, 0.25]  # adversary strategy [Rock, Paper, Scissors]
# learning_rate = 0.4

# game = RPS_exp3(learning_rate, adv_strategy, T)
# game.run()

chart_simplex = plot_simplex.plot(game.policy_history)
chart_simplex.total_chart.save("charts/simplex_path_test.html")

[round(i, 4) for i in game.env_mean]

df = pd.DataFrame()
df["regret"] = game.regret
df["true_rewards"] = game.true_rewards
df["index"] = df.index

chart = (
    alt.Chart(df)
    .mark_line()
    .encode(alt.X("index", title="round"), alt.Y("regret", title="pseudo-regret"))
)
chart.save("charts/regret.html")
teste = chart_simplex.total_chart.properties(width=300, height=300) | chart
teste.save("charts/simplex_regret.html")

# Adversarial RPS game

T = 300  # game horizon
adv_strategy = [0.4, 0.35, 0.25]  # adversary strategy [Rock, Paper, Scissors]
learning_rate = 0.4

learner = RPS_exp3(learning_rate, adv_strategy, T)
game.run()

import numpy as np

teste = [deque(maxlen=3), deque(maxlen=3), deque(maxlen=3)]

teste[1].append(100)
sum(teste[1])

np.array(
    [
        sum(teste[0]),
    ]
)
d = deque([0, 0, 0], maxlen=3)
d.append(103)
d
