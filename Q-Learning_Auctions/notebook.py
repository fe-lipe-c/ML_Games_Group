import numpy as np
import pandas as pd
import altair as alt

m = 9
bids = [i / (m + 1) for i in range(m)]


# ## The Model
#
# Two bidders participate in a sequence of auctions. In every period $t \in \left\{1, \dots,\infty\right\}$ an auctioneer runs an auction to allocate a single non-divisible object to one of the bidders. Both bidders value the object at $v _{i}=1$ and the value is constant over time.

class bidder():

    def __init__(self, private_value):

        self.private_value = private_value

    def policy(self, observation):

class auction():
    def __init__(self):
        self.auctions = {}

    def run(self, periods, bidders_values, auction_alpha):
        for t in range(periods):
            self.auctions[t] = auction_period(bidders_values, auction_alpha)


#
# We consider a family of auction formats parameterized by $\alpha \in [1,2]$. In an $\alpha$-auction the highest bidder wins and pays a convex combination of the winning and the losing bid. The weight on the losing bid is $\alpha -1$, and the weight on the winning bid is $2-\alpha$.
#
# The payoff of the winner of period $t$ auction is $\pi_{t} = 1 - p_{t}$, where $p_{t}$ is the price determined by the mechanism chosen by the auctioneer. The losing bidder gets a payoff of $0$. Bidders maximize the expected sum of discounted per-period payoffs with a discount factor $\gamma \in (0,1)$.
