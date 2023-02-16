"""Notebook to implement bandit algorithms in the RPS game."""

from utils import RPS_exp3
import plot_simplex

T = 5001  # game horizon
adv_strategy = [0.3, 0.4, 0.3]  # adversary strategy [Rock, Paper, Scissors]
learning_rate = 0.1

game = RPS_exp3(learning_rate, adv_strategy, T)
game.run()

chart_simplex = plot_simplex.plot(game.policy_history)
chart_simplex.total_chart.save("charts/simplex_path.html")
