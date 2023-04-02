"""Plot a probability simplex."""

import numpy as np
import pandas as pd
import altair as alt


class plot:
    """Plot probability simplex and the a policy trajectory."""

    def __init__(
        self,
        policy_history,
        color,
        width=400,
        height=400,
        init_caption="Initial Policy",
    ):
        """Initialize setup."""
        self.width = width
        self.height = height
        self.policy_history = policy_history
        self.base()
        self.transform_ternary_plot()
        self.start_text = pd.DataFrame(
            [
                {
                    "start": self.policy_history[0][0][0],
                    "end": self.policy_history[0][0][1],
                    "action": init_caption,
                }
            ]
        )
        self.rock_text = pd.DataFrame([{"start": 0, "end": 0, "action": "R"}])
        self.paper_text = pd.DataFrame([{"start": 1, "end": 0, "action": "P"}])
        self.scissors_text = pd.DataFrame(
            [{"start": 0.5, "end": np.sqrt(3) / 2, "action": "S"}]
        )
        self.color = color
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

        self.chart_start = (
            alt.Chart(self.df_history[0:1])
            .mark_point(size=25, color="white")
            .encode(
                alt.X("x", scale=alt.Scale(domain=[0, 1]), axis=None),
                alt.Y(
                    "y",
                    scale=alt.Scale(domain=[0, np.sqrt(3) / 2]),
                    axis=None,
                ),
            )
            .properties(width=self.width, height=self.height)
        )  # order="order")
        self.chart_history = (
            alt.Chart(self.df_history)
            .mark_line(color=self.color)
            .encode(
                alt.X("x", scale=alt.Scale(domain=[0, 1]), axis=None),
                alt.Y(
                    "y",
                    scale=alt.Scale(domain=[0, np.sqrt(3) / 2]),
                    axis=None,
                ),
                order="order",
            )
            .properties(width=self.width, height=self.height)
        )  # order="order")
        self.chart_text_R = (
            alt.Chart(self.rock_text)
            .mark_text(align="right", size=15, dx=-5, color="white")
            .encode(
                alt.X("start:Q"),
                alt.Y("end:Q"),
                text="action:N",
            )
        )
        self.chart_text_P = (
            alt.Chart(self.paper_text)
            .mark_text(align="left", size=15, dx=5, color="white")
            .encode(
                alt.X("start:Q"),
                alt.Y("end:Q"),
                text="action:N",
            )
        )
        self.chart_text_S = (
            alt.Chart(self.scissors_text)
            .mark_text(size=15, dy=-10, color="white")
            .encode(
                alt.X("start:Q"),
                alt.Y("end:Q"),
                text="action:N",
            )
        )
        self.chart_text_start = (
            alt.Chart(self.start_text)
            .mark_text(
                size=8, dx=10, dy=10, align="left", baseline="top", color="white"
            )
            .encode(
                alt.X("start:Q"),
                alt.Y("end:Q"),
                text="action:N",
            )
        )
        self.total_chart = (
            self.base_chart
            + self.chart_history
            + self.chart_start
            + self.chart_text_R
            + self.chart_text_P
            + self.chart_text_S
            + self.chart_text_start
        )
        self.total_chart.configure_axis(grid=False).configure_view(
            strokeWidth=0
        ).properties(background="#202025")
