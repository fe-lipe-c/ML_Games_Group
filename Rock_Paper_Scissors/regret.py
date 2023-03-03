"""Calculate regret for a given strategy."""


class Regret:
    """Calculate regret for a given strategy."""

    def __init__(self, M):
        """Initialize the regret class."""

        self.nr_players = M

    def pseudo_regret(self, policies):
        """Return the pseudo-regret of the action."""
        self.sum_actions_means += self.env_mean[action]
        self.regret.append(
            len(self.true_rewards) * max(self.env_mean) - self.actions_exp
        )

    def arms_means(self):
        """Return the mean reward of each arm."""
        mu_R = (
            self.adversary_policy[0] * 0
            + self.adversary_policy[1] * -0.1
            + self.adversary_policy[2] * 0.1
        )
        mu_P = (
            self.adversary_policy[0] * 0.1
            + self.adversary_policy[1] * 0
            + self.adversary_policy[2] * -0.1
        )
        mu_S = (
            self.adversary_policy[0] * -0.1
            + self.adversary_policy[1] * 0.1
            + self.adversary_policy[2] * 0
        )
        self.env_mean = [mu_R, mu_P, mu_S]
