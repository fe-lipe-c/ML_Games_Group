from RPS_exp import RPS_exp3
import plot_simplex

T = 5001
game = RPS_exp3(0.005, [0.333334, 0.333333, 0.333333], T)
game = RPS_exp3(0.03, [0.1, 0.1, 0.8], T)

game.run()
# df_policy = pd.DataFrame(np.concatenate(game.policy_history))
# df_policy
game.policy_history[-5:]

chart_simplex = plot_simplex.plot(game.policy_history)
chart_simplex.base_chart.save("simplex.html")
chart_simplex.df_history
chart_simplex.coordinates[-5:]
total_chart = chart_simplex.base_chart + chart_simplex.chart_history
chart_simplex.total_chart.save("simplex_history.html")
