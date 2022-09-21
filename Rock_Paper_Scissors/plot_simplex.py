"""Plot a probability simplex."""

import numpy as np
import pandas as pd
import altair as alt


class plot:
    """Plot probability simplex and the a policy trajectory."""

    def __init__(self, policy_history):
        """Initialize setup."""
        self.policy_history = policy_history
        self.base()
        self.transform_ternary_plot()
        self.plot_history()

    def base(self):
        """Plot the extremes os the simplex and its bondaries."""
        equilateral_extremes = np.array(
            [[1, 0], [0.5, np.sqrt(3) / 2], [0, 0], [1, 0]],
        )
        plot_order = [1, 2, 3, 4]
        df_equilateral = pd.DataFrame(equilateral_extremes, columns=["x", "y"])
        df_equilateral["order"] = plot_order

        self.base_chart = (
            alt.Chart(df_equilateral)
            .mark_line(point=True)
            .encode(
                alt.X("x", scale=alt.Scale(domain=[0, 1]), axis=None),
                alt.Y(
                    "y",
                    scale=alt.Scale(domain=[0, np.sqrt(3) / 2]),
                    axis=None,
                ),
                order="order",
            )
        )

    def transform_ternary_plot(self):
        """Transform data to allow a ternary plot.

        We will apply the following formula to the data:
        (a,b,c) -> (1/2 * (2b + c)/(a+b+c), sqrt(3)/2 * c/(a+b+c))
        source: https://en.wikipedia.org/wiki/Ternary_plot
        """
        self.coordinates = [
            [
                np.array(
                    [
                        ((1 / 2) * (2 * policy[0][1] + policy[0][2]))
                        / np.sum(policy[0], axis=0),
                        (np.sqrt(3) * policy[0][2]) / (2 * np.sum(policy[0], axis=0)),
                        ind,
                    ]
                )
            ]
            for ind, policy in enumerate(self.policy_history)
        ]
        self.df_history = pd.DataFrame(
            np.concatenate(self.coordinates, axis=0),
            columns=["x", "y", "order"],
        )

    def plot_history(self):
        """Plot policy history."""
        self.chart_history = (
            alt.Chart(self.df_history)
            .mark_circle(size=6, color="red")
            .encode(
                alt.X("x", scale=alt.Scale(domain=[0, 1]), axis=None),
                alt.Y(
                    "y",
                    scale=alt.Scale(domain=[0, np.sqrt(3) / 2]),
                    axis=None,
                ),
            )
        )  # order="order")
        self.total_chart = self.base_chart + self.chart_history
        self.total_chart.configure_axis(grid=False).configure_view(strokeWidth=0)
