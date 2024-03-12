
# Playing auctions through  Q-Learning

This post aims to simulate sequential first-price and second-price auction where the bidders develop a strategy through Reinforcement Learning (RL). Auction theory is a pivotal area of economics that has undergone extensive study. It delves into the strategies of participants in auctions, with a prime objective of crafting optimal auction mechanisms. However, most analyses within this field have historically been static, with a predominant focus on one-shot auctions, which do not account for the dynamic nature of bidder behavior over time. One of the objectives of this research is to explore how a specific group of learning agents behaves in sequential auctions when guided solely by the principles of reinforcement learning. We then compare the emergent behaviors with the expected economic theory outcome. This approach not only provides insights into the dynamics of auction-based interactions but also tests the efficacy of RL in replicating complex economic phenomena.

The Q-Learning algorithm is a reinforcement learning algorithm that learns the optimal policy of an agent through interaction with the environment. The agent learns the optimal policy by maximizing the expected return, which is the sum of the rewards received by the agent. The Q-Learning algorithm is a model-free algorithm, which means that the agent doesn't need to know the environment dynamics to learn the optimal policy.

The Q-Learning algorithm is the simplest RL algorithm, and is a natural starting point to study bidders behaviors in sequential auctions. It is a model-free reinforcement learning technique that enables an agent to ascertain the optimal policy through direct interaction with its environment. By aiming to maximize the expected return - the cumulative sum of rewards it receives - the agent incrementally refines its strategy based on the outcomes of its actions.

## Reinforcement Learning: A General Framework

A general RL problem, with full observability, can be defined as follows:

**Definition 1 (Reinforcement Learning Problem)** A RL problem is defined by a tuple $\left(\mathbb{G},\mathbb{S},\mathbb{A},\mathcal{P},\Pi,\mathcal{R},\gamma,\mathbb{T},\mu \right)$, where $\mathbb{G} = \{g_{0},g_{1}\}$ is the set with the environment $g_{0}$ and the agent $g_{1}$, $\mathbb{S}$ is the set of states, $\mathbb{A}$ is the set of actions, $\mathcal{P}: \mathbb{S} \times \mathbb{A} \to \Delta(\mathbb{S})$ is the environment state transition function, where $\Delta (\mathbb{S})$ is the space of probability distributions over $\mathbb{S}$, $\Pi = \Delta (\mathbb{S})$ is the agent's policy space, $\mathcal{R}: \mathbb{S} \times \mathbb{A} \times \mathbb{S} \to \Delta (\mathbb{R})$ is the reward function, $\gamma \in [0,1]$ is the discount factor, $\mathbb{T}$ is the time set and $\mu \in \Delta (\mathbb{S})$ is the distribution of the initial state $s_{0} \in \mathbb{S}$.


In RL there are two entities: the environment and the agent. The environment is nature, where the agent inhabits and interacts with it. Both entities can live in a continuous or discrete time, that in turn has a finite or infinite horizon. From now on we'll use the discrete time framework.

The environment is embedded with a state space $\mathbb{S}$, which dynamics are govern by the transition probability function $\mathcal{P}$. In discrete time, at every time $t \in \mathbb{T}$, the environment is at a state $s_{t} \in \mathbb{S}$, with the initial state $s_{0} \sim \mu$. Given the state $s_{t}$, an action $a_{t}$ is performed by the agent, the environment state transitions to $s_{t+1} \sim \mathbb{P}(\cdot | s_{t},a_{t})$ and the agent receives a reward $r_{t+1} \sim \mathbb{P}(\cdot | s_{t},a_{t},s_{t+1})$. This process continues indefinitely or until termination, defining, thus, at every $t \in \mathbb{T}$, a trajectory $\tau_{t} = \left\{s_{0},a_{0}, s_{1},r_{1},a_{1},\dots,s_{t},r_{t},a_{t},s_{t+1},r_{t+1} \right\}$.

Let $\mathcal{T}_{t}$ be the set of all trajectories of lenght $t$:
$$
\begin{equation*}
	\mathcal{T}_{t} = \left\{\tau_{t} : \tau_{t}=(s_{0},a_{0}, s_{1},r_{1},a_{1},\dots,s_{t},r_{t},a_{t},s_{t+1},r_{t+1})\right\}
\end{equation*}
$$
The trajectory space $\mathcal{T}$ is defined as the union of all $\mathcal{T}_{t}$, for $t \in \mathbb{T}$:
$$
\begin{equation*}
	\mathcal{T} = \bigcup_{t \in \mathbb{T}} \mathcal{T}_{t}
\end{equation*}
$$

To act in the environment, the agent chooses a policy $\pi \in \Pi$, that maps the current state to a probability distribution over the action space. A RL algorithm, like Q-Learning, can be defined as function that maps a realized trajectory to a policy, such as $L: \mathcal{T} \to \Delta(\mathbb{A})$. Then, at every $t \in \mathbb{T}$, given a trajectory $\tau_{t}$, the agent chooses $\pi_{t}$ through $L(\tau_{t})$, observes $s_{t}$ and draws an action $a_{t} \sim \pi_{t}(s_{t})$.

## Partially Observable Reinforcement Learning

## Multi-Agent Reinforcement Learning

## MARL to RL

## Auction Theory
### First Price Auction
### Second Price Auction

## Methodology

We will simulate three types of first-price auctions. The first one is the classic setup, where each bidder knows his own type but doesn't know the other bidders' types. In the second setup the winning bid is revealed to all the bidders. An in the third setup the worst and best bid (the winning one) are revealed to all the bidders.



### Auction Environment
### Classic Setup
### Observation of the Best Bid 
### Observation of the Best and Worst Bid






## References

[1] Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.

[2] Littman, M. L. (1994). Markov games as a framework for multi-agent reinforcement learning. In Machine learning proceedings 1994 (pp. 157-163). Elsevier.

[3] Menezes, Flavio M. and Monteiro, Paulo K. (2005). An Introduction to Auction Theory. Oxford University Press.




$\Pi: \mathcal{T} \to \Delta(\mathbb{A})$
