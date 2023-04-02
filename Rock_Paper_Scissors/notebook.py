"""Notebook to implement bandit algorithms in the RPS game."""

from utils import RPS_player, RPS_game
import plot_simplex
import pandas as pd
import altair as alt
from collections import deque

# [18, -10, -1]
player_0 = RPS_player(
    eta=0.1, init_dist=[15, -1, 2], id=0, memory_size=1000, fixed_policy=False
)
player_1 = RPS_player(
    eta=0.1, init_dist=[0.8, 0.1, 0.1], memory_size=1000, id=1, fixed_policy=False
)

game = RPS_game(T=1000, players=[player_0, player_1], reward_scheme=[0, 0.1, -0.1])
game.run()

chart_simplex_0 = plot_simplex.plot(
    player_0.policy_history, color="blue", init_caption=""
)
chart_simplex_1 = plot_simplex.plot(
    player_1.policy_history, color="red", init_caption=""
)
chart = chart_simplex_0.total_chart + chart_simplex_1.total_chart
# chart_simplex_1.total_chart.configure_view(strokeWidth=0).properties(
#     background="#202025"
# ).save("charts/rps_path_.html")

chart.configure_view(strokeWidth=0).properties(background="#202025").save(
    "charts/rps_path_.html"
)

# Plot regret

df = pd.DataFrame()
df["regret"] = player_1.regret_history
# df["true_rewards"] = game.true_rewards
df["index"] = df.index
df["legend"] = "regret"

df_max = pd.DataFrame()
df_max["regret"] = player_1.regret_max
df_max["index"] = df_max.index
df_max["legend"] = "max regret"

df_total = pd.concat([df, df_max])

chart = (
    alt.Chart(df_total[df_total["regret"] <= 2], title="Regret")
    .mark_line()
    .encode(
        alt.X("index", title="round"),
        alt.Y("regret", title="pseudo-regret", scale=alt.Scale(domain=(0, 2))),
        color="legend",
    )
)
chart.configure_axis(
    grid=False,
    labelColor="white",
    titleColor="white",
).configure_legend(labelColor="white", titleColor="white").configure_title(
    color="white",
).configure_view(
    strokeWidth=0,
).properties(
    background="#202025",
).save(
    "charts/regret_cumsum.html"
)

teste = chart_simplex_1.total_chart.properties(
    width=200, height=200
) | chart.properties(width=200, height=200)
teste.configure_axis(
    grid=False,
    labelColor="white",
    titleColor="white",
).configure_legend(labelColor="white", titleColor="white").configure_title(
    color="white",
).configure_view(
    strokeWidth=0,
).properties(
    background="#202025",
).save(
    "charts/simplex_regret.html"
)


# Stochastic RPS game
# T = 300  # game horizon
# adv_strategy = [0.4, 0.35, 0.25]  # adversary strategy [Rock, Paper, Scissors]
# learning_rate = 0.4

# game = RPS_exp3(learning_rate, adv_strategy, T)
# game.run()

chart_simplex = plot_simplex.plot(game.policy_history)
chart_simplex.total_chart.save("charts/simplex_path_test.html")

[round(i, 4) for i in game.env_mean]


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
