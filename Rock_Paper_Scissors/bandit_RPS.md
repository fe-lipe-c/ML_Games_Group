# Rock-Paper-Scissors
### Learning to play through bandit algorithms

#### Initial Setup
Rock-Paper-Scissors (RPS) is a fairly simple game that can be used as an environment to implement some learning algorithms. In this game two players simultaneously choose one of three options: rock, paper, or scissors. The winner is determined by the following rules:

	- Rock beats scissors
	- Scissors beats paper
	- Paper beats rock


We can model this game in the bandit framework. A bandit problem can be defined as follows:

**Definition 1 (Bandit Problem)** A bandit problem is a tuple $(\mathcal{A},\Pi ,\mathcal{C}, \mathcal{R})$, where $\mathcal{A}$ is the set of arms (or actions), $\mathcal{C}$ is the set of contexts and $\mathcal{R}: \mathcal{A} \times \mathcal{C} \to \Delta(\mathbb{R})$ is the reward function, where $\Delta(\mathbb{R})$ is the space of probability distributions over $\mathbb{R}$. 

This is a sequential decision problem where a learner interacts with an environment over $n$ rounds, $n \in \mathbb{N}$. In each round $t \in [n]$ the learner receives a context $c_{t} \in \mathcal{C}$, that can be seen as the state of the environment, chooses an action $a_{t} \in \mathcal{A}$ and the environment then reveals a reward $x_{t} \sim \mathcal{R}(a_{t}, c_{t})$.  

The context space can be unitary, resulting in the irrelevance of the context for the agent's decision making. Thus we can define $\mathcal{R}(a,c) = \mathcal{R}(a)$, for $c \in \mathcal{C}$ and every $a \in \mathcal{A}$, incorporating the only context to the law of the rewards. This happens in the classic slot machine example, where the learner has $K$ arms to chose from, and the context doesn't matter. On the other hand, for example, if we would play the same $K$ slot machines, but in one round we would play them in Bangu, Brazil, and in the other in Las Vegas, US, then we would have different context that would may affect the reward.

Another remark about the context is that $\mathbb{P}(c_{t+1}|a_{t}) = \mathbb{P}(c_{t+1})$, for every $t \in [n]$. This means that the learner has no influence over the context dynamics. This contrasts with the Reinforcement Learning (RL) framework, where the learner can influence the state dynamics through her actions. 

The reward associated with the action chosen are always revealed and the rewards associated with the other actions not chosen may or may not be revealed to the learner. The later, when revealed, is an important information to the learner, since she can make a better update of the estimated reward distribution for each arm, even if she never play most of them.

The way the reward function behaves determines the type of bandit problem that the learner is facing. If the reward function remains the same regardless of the learner's actions, then the learner is facing a stochastic bandit problem. If the reward function adapts to the learner's actions, then the learner is facing a adversarial bandit problem. One example for the former are $K$ slot machines and for the later is the RPS game.

Returning to the RPS game, we set the tuple $(\mathcal{A}, \mathcal{C}, \mathcal{R})$ as follows: $\mathcal{A} = \{R,P,S\}$, $\mathcal{C} = \{I_{1}, I_{2}, \dots\}$, the set of different adversaries, and the reward functions is defined as follows:

| Reward (X) | $\mathbb{P}(X\|R,I_{j})$ | $\mathbb{P}(X\|P,I_{j})$ | $\mathbb{P}(X\|S,I_{j})$ |
| :-:        | :-:                      | :-:                      | :-:                      |
| 0          | $\pi_{j}(R)$             | $\pi_{j}(P)$             | $\pi_{j}(S)$             |
| 1          | $\pi_{j}(S)$             | $\pi_{j}(R)$             | $\pi_{j}(P)$             |
| -1         | $\pi_{j}(P)$             | $\pi_{j}(S)$             | $\pi_{j}(R)$             |

where $\mathbb{P}(X|A,I_{j})$ is the probability that the learner receives a reward $X$ given that she chose the arm $A$, playing against the adversary $I_{j}$, and $\pi_{j}(\cdot)$ is the adversary policy.


