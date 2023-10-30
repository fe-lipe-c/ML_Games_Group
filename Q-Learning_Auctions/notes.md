# Artificial Intelligence and Auction Design

## Introduction

Setup: bidding agents with value $v = 1$ over $1$k experiments, where each involve $1$mi auctions.

Results: 

- [ ] Agents observes only their own rewards.
	- (First-price) bidders converge over time to much lower bids - this seems to be reminiscent of tacit collusion.
	- (Second-price) bidders in the repeated second-price auctions converge to bidding according to the static Nash equilibrium prediction and the revenues to the auctioneer are high. 
- [ ] Agents observe the winning bid.
	- (First-price) bidders can update the Q vector not only for the current bid, but for  all counterfactual bids (so-called synchronous updating) -> Bidders converge to highly competitive bids.

![image](img/figure1.png)

## The Model

Two bidders participate in a sequence of auctions. In every period $t \in \left\{1, \dots,\infty\right\}$ an auctioneer runs an auction to allocate a single non-divisible object to one of the bidders. Both bidders value the object at $v _{i}=1$ and the value is constant over time.

We consider a family of auction formats parameterized by $\alpha \in [1,2]$. In an $\alpha$-auction the highest bidder wins and pays a convex combination of the winning and the losing bid. The weight on the losing bid is $\alpha -1$, and the weight on the winning bid is $2-\alpha$.

The payoff of the winner of period $t$ auction is $\pi_{t} = 1 - p_{t}$, where $p_{t}$ is the price determined by the mechanism chosen by the auctioneer. The losing bidder gets a payoff of $0$. Bidders maximize the expected sum of discounted per-period payoffs with a discount factor $\gamma \in (0,1)$.

## Q-Learning

In each period two agents choose a bid $b_{t}^{i} \in B = \left\{b_{1},\dots,b_{m} \right\}$. The agents earns a stochastic reward $r_{t}$ distributed according to $F (r_{t}|b_{t}^{i},b_{t}^{-i})$.

A convenient simplification is absence of states for the algorithm.

While some papaers design the learners to keep track of past actions, in the original Q-learning formulation states are Markovian parameters of the environment. In this sense, our environment is time-independent, and the algorithms do not need any additional information about play.

# Learning Equilibria in Symmetric Auction Games using Artificial Neural Networks

d
