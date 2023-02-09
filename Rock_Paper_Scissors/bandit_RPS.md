# Rock-Paper-Scissors
## Learning to play through bandit algorithms

Rock-Paper-Scissors (RPS) is a fairly simple game that can be used as an environment to implement some learning algorithms. In this game two players simultaneously choose one of three options: rock, paper, or scissors. The winner is determined by the following rules:

	- Rock beats scissors
	- Scissors beats paper
	- Paper beats rock


We can model this game in the bandit framework :

> **Definition 1** The game of RPS is a tuple $(\mathcal{N}, \mathcal{A}, \mathbb{S}, R)$, where $\mathcal{N} = \{1,2\}$ is the set of players, $\mathcal{A}_{j} = \{R,P,S\}$ is the set of actions for each player $j \in \mathcal{N}$, $\mathbb{S}_{j} = \{\pi \in \mathbb{R}^{3}: \sum_{i \in \mathcal{A}} \pi_{i}= 1, \pi_{i} \geq 0, \text{ for } i \in \mathcal{A} \}$ is the space of strategies (a probability simplex) for each player $j \in \mathcal{N}$ and $R_{j}$ is the reward function.

This is a zero-sum game that is played in one round, over $T$ times, where $T \in [0, +\infty)$. At each time $t \in [0, T]$, each player $j \in N$ draws, simultaneously, an action $a_{j,t} \sim \pi_{j,t}$. After each player reveals her action, each receives a reward following the function $R_{j}:(A^1,A^2) \longrightarrow \{-1, 0, 1\}$. Note that at each $t$, the players may have different strategies. 

