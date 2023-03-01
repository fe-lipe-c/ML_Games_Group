"""Notebook to implement bandit algorithms in the RPS game."""

from utils import RPS_exp3
import plot_simplex
import pandas as pd
import altair as alt

T = 3001  # game horizon
adv_strategy = [0.1, 0.7, 0.2]  # adversary strategy [Rock, Paper, Scissors]
learning_rate = 0.4

game = RPS_exp3(learning_rate, adv_strategy, T)
game.run()

chart_simplex = plot_simplex.plot(game.policy_history)
chart_simplex.total_chart.save("charts/simplex_path_test.html")

game.true_rewards

df = pd.DataFrame()
df["regret"] = game.regret
df["true_rewards"] = game.true_rewards
df["index"] = df.index

chart = alt.Chart(df).mark_line().encode(alt.X("index"), alt.Y("regret"))
chart.save("charts/regret.html")
