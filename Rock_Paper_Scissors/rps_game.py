from RPS_exp import RPS_exp3
import plot_simplex

T = 5001
game = RPS_exp3(0.005, [0.333334, 0.333333, 0.333333], T)
game = RPS_exp3(0.03, [0.3, 0.4, 0.3], T)

game.run()

chart_simplex = plot_simplex.plot(game.policy_history)
chart_simplex.total_chart.save("simplex_history.html")
