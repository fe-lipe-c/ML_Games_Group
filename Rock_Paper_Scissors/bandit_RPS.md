# Rock-Paper-Scissors
### Learning to play through bandit algorithms

Rock-Paper-Scissors (RPS) is a fairly simple game that can be used as an environment to implement some learning algorithms. In this game two players simultaneously choose one of three options: rock, paper, or scissors. The winner is determined by the following rules:

	- Rock beats scissors
	- Scissors beats paper
	- Paper beats rock


We can model this game in the bandit framework. A bandit problem can be defined as follows:

**Definition 1 (Bandit Problem)** A bandit problem is a tuple $(\mathcal{A}, \mathcal{C}, \mathcal{R})$, where $\mathcal{A}$ is the set of arms (or actions), $\mathcal{C}$ is the set of contexts and $\mathcal{R}: \mathcal{A} \times \mathcal{C} \to \mathbb{R}$ is the reward function. 

This is a sequential decision problem where a learner interacts with an environment over $n$ rounds, $n \in \mathbb{N}$. In each round $t \in [n]$ the learner receives a context $c_{t} \in \mathcal{C}$, that can be seen as the state of the environment, chooses an action $a_{t} \in \mathcal{A}$ and the environment then reveals a reward $\mathcal{R}(a_{t}, c_{t}) = x_{t} \in \mathbb{R}$.  

The context space can be unitary, resulting in the irrelevance of the context for the agent's decision making. Thus we can define $\mathcal{R}(a,c) = \mathcal{R}(a)$, for $c \in \mathcal{C}$ and every $a \in \mathcal{A}$, incorporating the only context to the law of the rewards. This happens in the classic slot machine example, where the learner has $K$ arms to chose from, and the context doesn't matter. On the other hand, if we would play the same kinds of $K$ slot machines, but in one round we would play in Bangu, Brazil, and in the other in Las Vegas, US, then we would have different context that would affect the reward.

Another remark about the context is that $\mathbb{P}(c_{t+1}|a_{t}) = \mathbb{P}(c_{t+1})$, for every $t \in [n]$. This means that the learner has no influence over the context dynamics. This contrasts with the Reinforcement Learning (RL) framework, where the learner can influence the state dynamics through her actions. 

The reward associated with the action chosen are always revealed and the rewards associated with the other actions not chosen may or may not be revealed to the learner. The later, when revealed, is an important information to the learner, since she can make a better update of the estimated reward distribution for each arm, even if she never play most of of them.

Returning to the RPS game, we set the tuple $(\mathcal{A}, \mathcal{C}, \mathcal{R})$ as follows: $\mathcal{A} = \{R,P,S\}$, $\mathcal{C} = \{I_{1}, I_{2}, \dots\}$, the set of different adversaries, and:
$$
\tiny\mathcal{R}(R,I_{j}) =
\tiny\begin{cases}
	0, \qquad \text{if $I_{j}$ plays $R$}\\
	1, \qquad \text{if $I_{j}$ plays $S$}\\
	-1, \qquad \text{if $I_{j}$ plays $P$}\\
\end{cases}
\qquad, \mathcal{R}(P,I_{j}) =
\begin{cases}
	1, \qquad \text{if $I_{j}$ plays $R$}\\
	-1, \qquad \text{if $I_{j}$ plays $S$}\\
	0, \qquad \text{if $I_{j}$ plays $P$}\\
\end{cases}
\qquad, \mathcal{R}(S,I_{j}) =
\begin{cases}
	-1, \qquad \text{if $I_{j}$ plays $R$}\\
	0, \qquad \text{if $I_{j}$ plays $S$}\\
	1, \qquad \text{if $I_{j}$ plays $P$}\\
\end{cases}
$$

algorithms can be split in two categories: stochastic and adversarial. In the stochastic case, 

> **Definition 1** The game of RPS is a tuple $(\mathcal{N}, \mathcal{A}, \mathbb{S}, R)$, where $\mathcal{N} = \{1,2\}$ is the set of players, $\mathcal{A}_{j} = \{R,P,S\}$ is the set of actions for each player $j \in \mathcal{N}$, $\mathbb{S}_{j} = \{\pi \in \mathbb{R}^{3}: \sum_{i \in \mathcal{A}} \pi_{i}= 1, \pi_{i} \geq 0, \text{ for } i \in \mathcal{A} \}$ is the space of strategies (a probability simplex) for each player $j \in \mathcal{N}$ and $R_{j}$ is the reward function.

This is a zero-sum game that is played in one round, over $T$ times, where $T \in [0, +\infty)$. At each time $t \in [0, T]$, each player $j \in N$ draws, simultaneously, an action $a_{j,t} \sim \pi_{j,t}$. After each player reveals her action, each receives a reward following the function $R_{j}:(A^1,A^2) \longrightarrow \{-1, 0, 1\}$. Note that at each $t$, the players may have different strategies. 

