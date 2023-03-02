"""Notebook to implement bandit algorithms in the RPS game."""

from utils import RPS_exp3
import plot_simplex
import pandas as pd
import altair as alt

T = 300  # game horizon
adv_strategy = [0.4, 0.35, 0.25]  # adversary strategy [Rock, Paper, Scissors]
learning_rate = 0.4

game = RPS_exp3(learning_rate, adv_strategy, T)
game.run()

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
