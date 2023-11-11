# Playing auctions through  Q-Learning

This post has the objective of implementing a Q-Learning algorithm in an auction environment. The aution theory is one of the more important fields in economics, and it has been studied for a long time. This theory studies the behavior of agents in auctions, and one of its main objectives is to design optimal auctions. Usually this study is made in a static way, generally in one-shot auctions. One of the goals of this paper is to examine the behavior of a particular set of learning agents in sequential auctions, using only the reinforcement learning framework and comparing the results with the expected economic theory outcome.

The Q-Learning algorithm is a reinforcement learning algorithm that learns the optimal policy of an agent through interaction with the environment. The agent learns the optimal policy by maximizing the expected return, which is the sum of the rewards received by the agent. The Q-Learning algorithm is a model-free algorithm, which means that the agent doesn't need to know the environment dynamics to learn the optimal policy.

## Reinforcement Learning: A General Framework

A general RL problem, with full observability, can be defined as follows:

Definition 1 (Reinforcement Learning Problem) A RL problem is defined by a tuple $\left(\mathbb{G},\mathbb{S},\mathbb{A},\mathcal{P},\Pi,\mathcal{R},\gamma,\mathbb{T},\mu \right)$, where $\mathbb{G} = \{g_{0},g_{1}\}$ is the set with the environment $g_{0}$ and the agent $g_{1}$, $\mathbb{S}$ is the set of states, $\mathbb{A}$ is the set of actions, $\mathcal{P}: \mathbb{S} \times \mathbb{A} \to \Delta(\mathbb{S})$ is the environment state transition function, where $\Delta (\mathbb{S})$ is the space of probability distributions over $\mathbb{S}$, $\Pi = \Delta (\mathbb{S})$ is the agent's policy space, $\mathcal{R}: \mathbb{S} \times \mathbb{A} \times \mathbb{S} \to \Delta (\mathbb{R})$ is the reward function, $\gamma \in [0,1]$ is the discount factor, $\mathbb{T}$ is the time set and $\mu \in \Delta (\mathbb{S})$ is the distribution of the initial state $s_{0} \in \mathbb{S}$.


In RL there are two entities: the environment and the agent. The environment is nature, where the agent inhabits and interacts with it. Both entities can live in a continuous or discrete time, that in turn has a finite or infinite horizon. From now on, in this post, we'll use the discrete time framework and I won't write about continuous time RL.  

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

To act in the environment, the agent chooses a policy $\pi \in \Pi$, that maps the current state to a probability distribution over the action space: at $t \in \mathcal{T}$, after choosing a policy and observing $s_{t}$, an action $a_{t}$ is drawn from $\pi_{t}(s_{t})$.



## References

[1] Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.

[2] Littman, M. L. (1994). Markov games as a framework for multi-agent reinforcement learning. In Machine learning proceedings 1994 (pp. 157-163). Elsevier.


$\Pi: \mathcal{T} \to \Delta(\mathbb{A})$
