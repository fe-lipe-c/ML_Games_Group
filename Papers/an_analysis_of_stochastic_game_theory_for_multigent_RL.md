# An Analysis of Stochastic Game Theory for Multiagent Reiforcement Learning
https://www.cs.cmu.edu/~mmv/papers/00TR-mike.pdf
## Abstract

Learning behaviors in a multiagent environment is crucial for developing and adapting multiagent systems. Reinforcement learning techniques have addressed this problem for a single agent acting in a stationary environment, which is modeled as a Markov decision process (MDP). But, multiagent environments are inherently non-stationary since the other agents are free to change their behavior as they also learn and adapt. Stochastic games, first studied in the game theory community, are a natural extension of MDPs to include multiple agents. In this paper we contribute a comprehensive presentation of the relevant techniques for solving stochastic games from both the game theory community and reinforcement learning communities. We examine the assumptions and limitations of these algorithms, and identify similarities between these algorithms, single agent reinforcement learners, and basic game theory techniques.

## 1 Introduction

The problem of an agent learning to act in an unknown world is both challenging and interesting. Reinforcement learning has been successful at finding optimal control policies for a single agent operating in a stationary environment, specifically a Markov decision process.

Learning to act in multiagent systems offers additional challenges; see the following surveys [17, 19, 27]. Multiple agents can be employed to solve a single task, or an agent may be required to perform a task in a world containing other agents, either human, robotic, or software ones. In either case, from an agent’s perspective the world is not stationary. In particular, the behavior of the other agents may change, as they also learn to better perform their tasks. This type of multiagent nonstationary world creates a difficult problem for learning to act in these environments.

> The world gets non-stationary for agent $i$ because the other agents' policies change in response to the $i$'s actions. But if you incorporate the other agents' policies in the environment, and the update of this policies follows a defined algorithm, we can assume that the environment is stationary, since agent $i$ can learn the other agents' dynamics, as she would in a single agent environment. 

However, this nonstationary scenario can be viewed as a game with multiple players. Game theory has aimed at providing solutions to the problem of selecting optimal actions in multi-player environments. In game theory, there is an underlying assumption that the players have similar adaptation and learning abilities. Therefore the actions of each agent affect the task achievement of the other agents. It seems therefore promising to identify and build upon the relevant results from game theory towards multiagent reinforcement learning.

Stochastic games extend the single agent Markov decision process to include multiple agents whose actions all impact the resulting rewards and next state. They can also be viewed as an extension of game theory’s simpler notion of matrix games. Such a view emphasizes the difficulty of finding optimal behavior in stochastic games, since optimal behavior depends on the behavior of the other agents, and vice versa. This model then serves as a bridge combining notions from game theory and reinforcement learning.

> Matrix games are a type of game theory in which two players take turns making decisions, and the outcome of the game is determined by the payoff matrix. The payoff matrix is a table that shows the payoff for each combination of decisions made by the two players. The goal of the game is to find the optimal strategy for each player that maximizes their payoff.

> The author states that stochastic games can be viewed as an extension of matrix games. Is worth noting that a matrix game doesn't necessarily follows a MDP. Most of the matrix games' examples are bandit problems that, even in the presence of contexts, doesn't have a Markov property.

A comprehensive examination of the multiagent learning techniques for stochastic games does not exist. In this paper we contribute such an analysis, examining techniques from both game theory and reinforcement learning. The analysis both helps to understand existing algorithms as well as being suggestive of areas for future work.

In section 2 we provide the theoretical framework for stochastic games as extensions of both MDPs and matrix games. Section 3 summarizes algorithms for solving stochastic games from the game theory and reinforcement learning communities. We discuss the assumptions, goals, and limitations of these algorithms. We also taxonomize the algorithms based on their game theoretic and reinforcement learning components. Section 4 presents two final algorithms that are based on a different game theoretic mechanism, which address a limitation of the other algorithms. Section 5 concludes with a brief summary and a discussion of the future work in multiagent reinforcement learning.

## 2 Theoretical Framework

In this section we setup the framework for stochastic games. We first examine MDPs, which is a single-agent, multiple state framework. We then examine matrix games, which is a multiple-agent, single state framework. Finally we introduce the stochastic game framework which can be seen as the merging of MDPs and matrix games.

### 2.1 Markov Decision Processes

A Markov decision process is a tuple, $(\mathcal{S},\mathcal{A},T,R)$ where $\mathcal{S}$ is a set of states, $\mathcal{A}$ is a set of actions, $T$ is a transition function $\mathcal{S} \times \mathcal{A} \times \mathcal{S} \to [0,1]$, and $R$ is a reward function $\mathcal{S} \times \mathcal{A} \to \mathbb{R}$. The transition function defines a probability distribution over next states as a function of the current state and the agent’s action. The reward function defines the reward received when selecting an action from the given state. Solving MDPs consists of finding a policy, $\pi : \mathcal{S} \to \mathcal{A}$, which determines the agent's actions so as to maximize discounted future reward, with discount factor $\gamma$.

> Here the reward function is defined as a deterministic function, but would be more general to define it as a stochastic one. This is important because in the multiagent framework this will be probably the case. Another aspect of the RL and MARL is the presence of non observables states, where the agents just receives a partial state from the environment (observation), and most likely the reward function on the observations will be stochastic.

MDPs are the focus of much of the reinforcement learning work [11, 20]. The crucial result that forms the basis for this work is the existence of a stationary and deterministic policy that is optimal. It is such a policy that is the target for RL algorithms.

### 2.2 Matrix Games

A matrix game or strategic game (see [14] for an overview) is a tuple $(n, \mathcal{A}_{1,\dots,n},R_{1,\dots,n})$, where $n$ is the number of players, $\mathcal{A}_{i}$ is the set of actions available to player $i$ (and $\mathcal{A}$ is the joint action space $\mathcal{A}_{1}\times \dots \times \mathcal{A}_{n}$), and $R_{i}$ is the player $i$'s payoff function $\mathcal{A} \to \mathbb{R}$. The players select actions from their available set with the goal to maximize their payoff which depends on all the players' actions. These are often called matrix games, since the $R_{i}$ functions can be written as $n$-dimensional matrices.

> We could extend this definition to include a set of contexts $\mathcal{C}$, where $R_{i}$ is player $i$'s payoff function $\mathcal{A} \times \mathcal{C} \to \mathbb{R}$. The context dynamics would be independent of the game dynamics. Imagine for example an auction represented by the tuple $(\mathcal{C}, \mathcal{A}, R)$, where $\mathcal{A}= [0,1]^{n}$ is the joint bid space, $\mathcal{C} = \left\{v^{\text{apple}}, v^{\text{orange}}\right\}$ is the item been auctioned, with $v^{k} = v^{k}_{1},\dots,v^{k}_{n}$ been the private value vector for item $k$, and $R = R_{1}\times \dots \times R_{n}$, with $R_{i} = \left[v_{i}^{c} - a_{i}\right]\cdot\mathbb{I}_{\left\{i =\text{winner}  \right\}}$ is the reward function to agent $i$.

Unlike MDPs, it is difficult to define what it means to “solve” a matrix game. A stationary strategy can only be evaluated if the other players’ strategies are known. This can be illustrated in the two-player matching pennies game. Here each player may select either Heads or Tails. If the choices are the same then Player 1 takes a dollar from Player 2. If they are different then Player 1 gives a dollar to Player 2. The matrices for this game are shown in Figure 1. If Player 2 is going to play Heads, then Player 1’s optimal strategy is to play Heads, but if Player 2 is going to play Tails, then Player 1 should play Tails. So there is no optimal pure strategy, independent of the opponent.

Players can also play mixed strategies, which select actions according to a probability distribution. It is clear that in the above game there is also no optimal mixed strategy that is independent of the opponent. This leads us to define an opponent-dependent solution, or set of solutions:

**Definition 1** For a game, define the best-response function for player $i$, $BR_{i}(\sigma_{-i})$, to be the set of all, possibly mixed, strategies that are optimal given the other player(s) play the possibly mixed joint strategy $\sigma_{-i}$

The major advancement that has driven much of the development of matrix games and game theory is the notions of a best-response equilibrium, or Nash equilibrium:

**Definition 2** A Nash equilibrium is a collection of strategies (possibly mixed) for all players, $\sigma_{i}$, with,
$$
\begin{equation*}
	\sigma_{i} \in BR_{i}(\sigma_{-i})
\end{equation*}
$$
So, no player can do better by changing strategies given that the other players continue to follow the equilibrium strategy.

What makes the notion of equilibrium compelling is that all matrix games have a Nash equilibrium, although there may be more than one.

Types of Matrix Games. Matrix games can be usefully classified according to the structure of their payoff functions. Two common classes of games are purely collaborative and purely competitive games. In purely collaborative games, all agents have the same payoff function, so an action in the best interest of one agent is in the best interest of all the agents.

In purely competitive games, there are two agents, where one’s payoff function is the negative of the other (i.e. $R_{1} = - R_{2}$). The game in Figure 1 is an example of one such game. Purely competitive games are also called zero-sum games since the payoff functions sum to zero. Other games, including purely collaborative games, are called general-sum games. One appealing feature of zero-sum games is that they contain a unique Nash equilibrium. This equilibrium can be found as the solution to a relatively simple linear program. Finding equilibria in general-sum games requires a more difficult quadratic programming solution [6].
