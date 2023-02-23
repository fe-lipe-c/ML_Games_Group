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

The context space can be unitary, resulting in the irrelevance of the context for the agent's decision making. Thus we can define $\mathcal{R}(a,c) = \mathcal{R}(a)$, for $c \in \mathcal{C}$ and every $a \in \mathcal{A}$, incorporating the only context to the law of the rewards. This happens in the classic slot machine example, where the learner has $K$ arms to chose from, and the context doesn't matter. On the other hand, for example, if we would play the same $K$ slot machines, but in different geographical regions, then we would have different context that could affect the reward.

Another remark about the context is that $\mathbb{P}(c_{t+1}|c_{t},a_{t}) = \mathbb{P}(c_{t+1}|c_{t})$, for every $t \in [n]$. This means that the learner has no influence over the context dynamics. This contrasts with the Reinforcement Learning (RL) framework, where the learner can influence the state dynamics through her actions. 

The reward associated with the action chosen are always revealed and the rewards associated with the other actions not chosen may or may not be revealed to the learner. The later, when revealed, is an important information to the learner, since she can make a better update of the estimated reward distribution for each arm, even if she never play most of them.

The way the reward function behaves determines the type of bandit problem that the learner is facing. If the reward function remains the same regardless of the learner's actions, then the learner is facing a stochastic bandit problem. On the other hand, if the reward function adapts to the learner's actions, then the learner is facing a adversarial bandit problem. Other way to see an adversarial bandit is that at each round the adversary chooses the reward to each action. One example for the former are $K$ slot machines and one for the later is the RPS game.

Returning to the RPS game, we set the tuple $(\mathcal{A}, \mathcal{C}, \mathcal{R})$ as follows: $\mathcal{A} = \{R,P,S\}$, $\mathcal{C} = \{I_{1}, I_{2}, \dots\}$, the set of different adversaries, and the reward functions is defined as follows:
$$
\begin{align*}
\mathcal{R}(R,I_{j}) = [\pi_{j,R}(0),\pi_{j,P}(-1),\pi_{j,S}(1)]\\
\mathcal{R}(P,I_{j}) = [\pi_{j,R}(1),\pi_{j,P}(0),\pi_{j,S}(-1)]\\
\mathcal{R}(S,I_{j}) = [\pi_{j,R}(-1),\pi_{j,P}(1),\pi_{j,S}(0)]
\end{align*}
$$
where $\pi_{j,A}$ is the adversary j's probability of playing action $A$ (adversary policy) and the number in parentesis is the outcome if this action is choosen. This is a Game Theory notation for a lottery. In this case, each time the learner choses an action, she is actually choosing a lottery over the outcomes $\{-1,0,1 \}$

#### Learner's Objective and Policy

The objective of the learner is to maximize her total reward $S_{n} = \sum_{t=1}^{n}X_{t}$.

Given the bandit problem, the learner needs a strategy to make the best decisions, with the aim to maximize her total reward. Since the learner is constrained by a finite number of interactions with the environment, she has to balance exploration with exploitation. Exploration is needed to gather data over actions, with the objective of finding the best action (or set of best actions), while exploitation is required to extract the maximum amount of reward from the environment, by choosing the best (inferred) action.

The strategy is set by a policy "function $\pi : ([k]\times [0,1])^{*} \to \mathcal{P_{k-1}}$, mapping history sequences to distributions over actions (regardless of measurability)." (Lattimore & Szepesvari)

We can evaluate the learner's policy by using the regret, that can be defined in different ways. In the stochastic setting the learner's policy is evaluated relative to the best policy $\pi^{*}$, whereas in the adversarial case we compare the learner's actions with the best actions in hindsight.
$$
\begin{align*}
	R_{n}(\pi) = n \max_{i \in [k]} \mu_{i} - \mathbb{E}\left[\sum_{t=1}^{n}x_{t}\right] \qquad \text{(Stochastic Regret)}
\end{align*}
$$
$$
\begin{align*}
	R_{n}(\pi) = \max_{i \in [k]}\sum_{t=1}^{n}x_{ti} - \mathbb{E}_{\pi}\left[ \sum_{t=1}^{n}x_{tA_{t}} \right] \qquad \text{(Adversarial Regret)} 
\end{align*}
$$

### Exp3 Algorithm

The Exp3 (Exponential-weight algorithm for exploration and exploitation) is an adversarial Bandit Algorithm. Consider a policy $\pi$ such that, for action $i$ at time $t$,
$$ \pi_{i,t} = \mathbb{P}(A_t = i | A_1,R_1,\dots,A_{t-1},R_{t-1})$$
where $\pi_{i,t}>0$, for all $i$ and $t$. Consider that the learner only observes the reward of the action sampled from her policy. The importance-weighted estimator of $r_{i,t}$, the true reward of action $i$ at time $t$, is
$$
\begin{equation}
\hat{R}_{i,t} = \frac{\mathbb{I}_{\{A_{t} = i\}} R_{t}}{\pi_{i,t}},
\end{equation}
$$
This is an unbiased estimate of $r_{i,t}$ conditioned on the history observed after $t-1$ rounds. Indeed,
$$
\begin{align*}
	\mathbb{E}\left[\hat{R}_{i,t}|A_1,R_1,\dots,A_{t-1},R_{t-1}\right] &= \mathbb{E}_{t}\left[\hat{R}_{i,t}\right] \\
	&= \mathbb{E}_{t}\left[\frac{\mathbb{I}_{\{A_{t} = i\}} R_{t}}{\pi_{i,t}}\right]\\
	&= \mathbb{E}_{t}\left[\mathbb{I}_{\{A_{t} = i\}}\right] \frac{\mathbb{E}[R_{t}]}{\pi_{i,t}}\\
	&= r_{i,t}
\end{align*}
$$
Despite being a unbiased estimator, it may be a high variance estimator. Its variance is $\mathbb{V}[\hat{R}_{i,t}]= \frac{r^{2}_{i,t}(1-\pi_{i,t})}{\pi_{i,t}}$, that can be extremely large when $\pi_{i,t}$ is small and $r_{i,t}$ is bounded away from zero [Lattimore & Szepesvari]. An alternative unbiased estimator is
$$
\begin{equation}
	\hat{R}_{i,t} = 1 - \frac{\mathbb{I}_{\left\{A_{t}=i \right\}}}{\pi_{i,t}}(1- R_{t})
\end{equation}
$$
 
Now consider $\hat{S}_{i,t} = \sum_{s=1}^{t}\hat{R}_{i,t}$, the total estimated reward for action $i$ by the end of round $t$. We can use this estimate to update the policy $\pi_{i,t}$, by using the following update rule:
$$
\begin{equation*}
	\pi_{i,t} = \frac{ \exp\left(\eta\hat{S}_{i,t-1}\right)}{\sum_{j=1}^{k}\exp\left(\eta\hat{S}_{j,t-1}\right)}
\end{equation*}
$$
where $\eta$ is the exploitation rate: when is high, it favors exploitation, while when is low it favors exploration. This hyperparameter can be fixed or vary through time, thus depending on the number of arms and/or the horizon. The EXP3 algorithm is summarized in the following figure, using the alternative estimator for $r_{i,t}$.

![Exp3 Algorithm](img/exp_algo.png)

### Simulation

Using the Exp3 Algorithm, we simulate a RPS game with one adversary that has a fixed policy. The game is played over 5000 rounds, the adversary's policy is $\pi_{0} = [\pi_{0,\tiny R}, \pi_{0,\tiny P}, \pi_{0,\tiny S}] = [0.3,0.4,0.3]$ and the learner's learning rate is $0.1$. The following figure a path for the learner's policy.

![Learner's Policy](img/learner_policy.png)
