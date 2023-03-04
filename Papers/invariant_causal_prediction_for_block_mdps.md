# Invariant Causal Prediction for Block MDPs
https://arxiv.org/abs/2003.06016
## Abstract
Generalization across environments is critical to the successful application of reinforcement learning algorithms to real-world challenges. In this paper, we consider the problem of learning abstractions that generalize in block MDPs, families of environments with a shared latent state space and dynamics structure over that latent space, but varying observations. We leverage tools from causal inference to propose a method of invariant prediction to learn *model-irrelevance state abstractions* (MISA) that generalize to novel observations in the multi-environment setting. We prove that for certain classes of environments, this approach outputs with high probability a state abstraction corresponding to the causal feature set with respect to the return. We further provide more general bounds on model error and generalization error in the multi-environment setting, in the process showing a connection between causal variable selection and the state abstraction framework for MDPs. We give empirical evidence that our methods work in both linear and nonlinear settings, attaining improved generalization over single- and multi-task baselines.

## Introduction

The canonical reinforcement learning (RL) problem assumes an agent interacting with a single MDP with a fixed observation space and dynamics structure. This assumption is difficult to ensure in practice, where state spaces are often large and infeasible to explore entirely during training. However, there is often a latent structure to be leveraged to allow for good generalization. 

>What the author means by latent structure? Latent structure refers to the underlying structure of an environment that is not directly observable. This structure can be used to generalize across different environments with similar dynamics.

As an example, a robot's sensors may be moved, or the lighting conditions in a room may change, but the physical dynamics of the environment are still the same. These are examples of environment-specific characteristics that current RL algorithms often overfit to.

In the worst case, some training environments may contain spurious correlations that will not be present at test time, causing catastrophic failures in generalization~\cite{azhang2018natrl,Song2020Observational}. To develop algorithms that will be robust to these sorts of changes, we must consider problem settings that allow for multiple environments with a shared dynamics structure. 

Recent prior works~\cite{amit2018mlpacbayes,yin2019meta} have developed generalization bounds for the multi-task problem, but they depend on the number of tasks seen at training time, which can be prohibitively expensive given how sample inefficient RL is even in the single task regime. To obtain stronger generalization results, we propose to consider a problem which we refer to as 'multi-environment' RL: like multi-task RL, the agent seeks to maximize return on a set of environments, but only some of which can be trained on. 

> What is generalization bounds? Generalization bounds are mathematical statements that provide upper and lower bounds on the expected generalization error of a learning algorithm. These bounds can be used to analyze the performance of a learning algorithm in a given problem setting.

We make the assumption that there exists some latent causal structure that is shared among all of the environments, and that the sources of variability between environments do not affect reward. This family of environments is called a *Block MDP* ~\cite{du2019pcid}, in which the observations may change, but the latent states, dynamics, and reward function are the same. A formal definition of this type of MDP will be presented in \cref{sec:problem_setup}. 

Though the setting we consider is a subset of the multi-task RL problem, we show in this work that the added assumption of shared structure allows for much stronger generalization results than have been obtained by multi-task approaches. Naive application of generalization bounds to the multi-task reinforcement learning setting is very loose because the learner is typically given access to only a few tasks relative to the number of samples from each task.

Indeed, \citet{cobbe2018genrl,czhang2018genrl} find that agents trained using standard methods require many thousands of environments before succeeding at 'generalizing' to new environments. 

The main contribution of this paper is to use tools from *causal inference* to address generalization in the Block MDP setting, proposing a new method based on the *invariant causal prediction* literature. In certain linear function approximation settings, we demonstrate that this method will, with high probability, learn an optimal state abstraction that generalizes across all environments using many fewer training environments than would be necessary for standard PAC bounds. We replace this PAC requirement with requirements from causal inference on the *types* of environments seen at training time. We then draw a connection between bisimulation and the minimal causal set of variables found by our algorithm, providing bounds on the model error and sample complexity of the method. We further show that using analogous invariant prediction methods for the nonlinear function approximation setting can yield improved generalization performance over multi-task and single-task baselines. We relate this method to previous work on learning representations of MDPs~\cite{gelada2019deepmdp,luo2018algorithmic} and develop multi-task generalization bounds for such representations. Code is available at \burl{https://github.com/facebookresearch/icp-block-mdp}.

> What is causal inference? Causal inference is the process of inferring causal relationships between variables from observational data. It is used to identify the underlying causes of observed phenomena and to make predictions about how changes in one variable will affect another.

> What are the tools of causal inference? Tools of causal inference include graphical models, structural equation models, and counterfactual reasoning. These tools can be used to identify causal relationships between variables, estimate the strength of those relationships, and make predictions about how changes in one variable will affect another.

> What are standard PAC bounds? PAC (Probably Approximately Correct) bounds are mathematical statements that provide upper and lower bounds on the expected generalization error of a learning algorithm. These bounds can be used to analyze the performance of a learning algorithm in a given problem setting.


## Background
### State Abstractions and Bisimulation

State abstractions have been studied as a way to distinguish relevant from irrelevant information~\cite{li2006stateabs} in order to create a more compact representation for easier decision making and planning. \citet{bertsekas1989bounds,Roy06sabounds} provide bounds for approximation errors for various aggregation methods, and \citet{li2006stateabs} discuss the merits of *abstraction discovery* as a way to solve related MDPs.

Bisimulation relations are a type of state abstraction that offers a mathematically precise definition of what it means for two environments to 'share the same structure'~\cite{larsen1989bisim,Givan2003EquivalenceNA}. We say that two states are bisimilar if they share the same expected reward and equivalent distributions over the next bisimilar states. 

For example, if a robot is given the task of washing the dishes in a kitchen, changing the wallpaper in the kitchen doesn't change anything relevant to the task. One then could define a bisimulation relation that equates observations based on the locations and soil levels of dishes in the room and ignores the wallpaper. These relations can be used to simplify the state space for tasks like policy transfer \citep{castro2010using}, and are intimately tied to state abstraction. For example, the *model-irrelevance abstraction* described by \citet{li2006stateabs} is precisely characterized as a bisimulation relation.

----------
**Definition 1 (Bisimulation Relations)** [~\citep{Givan2003EquivalenceNA}]
Given an MDP $\mathcal{M}$, an equivalence relation $B$ between states is a bisimulation relation if for all states $s_1,s_2\in\mathcal{S}$ that are equivalent under $B$ (i.e. $s_1Bs_2$), the following conditions hold for all actions $a\in\mathcal{A}$:
$$
\begin{align*}
    R(s_1,a)&=R(s_2,a) \\
    \mathcal{P}(G|s_1,a)&=\mathcal{P}(G|s_2,a),\forall G\in\mathcal{S}/B
\end{align*}
$$
Where $\mathcal{S}/B$ denotes the partition of $\mathcal{S}$ under the relation $B$, the set of all groups of equivalent states, and where $\mathcal{P}(G|s,a)=\sum_{s'\in G}\mathcal{P}(s'|s,a).$

----------

Whereas this definition was originally designed for the single MDP setting to find *bisimilar* states within an MDP, we are now trying to find bisimilar states across different MDPs, or different experimental conditions. One can intuitively think of this carrying over by imagining all experimental conditions $i$ mapped to a single super-MDP with state space $\mathcal{S}=\cup_i\mathcal{S}_i$ where we give up the irreducibility assumption, i.e. we can no longer reach every state $s_i$ from any other state $s_j$.

Specifically, we say that two MDPs $M_1$ and $M_2$ are bisimilar if there exist bisimulation relations $B_1$ and $B_2$ such that $M_1/B_1$ is isomorphic to $M_2/B_2$. *Bisimilar  MDPs* are therefore MDPs which are behaviourally the same. 

> Give me an concrete example of bisimulation relations: 
> A concrete example of a bisimulation relation is the equivalence relation between two states $s_1$ and $s_2$ in an MDP where the reward and transition probabilities are the same for all actions. In this case, the bisimulation relation $B$ would equate $s_1$ and $s_2$ since they are behaviourally equivalent.


### Causal Inference Using Invariant Prediction

\citet{peters2016icp} first introduced an algorithm, Invariant Causal Prediction (ICP), to find the *causal feature set*, the minimal set of features which are causal predictors of a target variable, by exploiting the fact that causal models have an invariance property~\cite{pearl2009do,scholkopf2012causal}. \citet{arjovsky2019irm} extend this work by proposing invariant risk minimization (IRM, see (1)), augmenting empirical risk minimization to learn a data representation free of spurious correlations. They assume there exists some partition of the training data $\mathcal{X}$ into *experiments* $e \in \mathcal{E}$, and that the model's predictions take the form $Y^e = \mathbf{w}^\top \bm{\phi}{(X^e)}$. IRM aims to learn a representation $\bm{\phi}$ for which the optimal linear classifier, $\mathbf{w}$, is invariant across $e$, where optimality is defined as minimizing the empirical risk $R^e$. We can then expect this representation and classifier to have low risk in new experiments $e$, which have the same causal structure as the training set.
$$
\begin{align*}
    &\min_{{\begin{subarray}{l}\bm{\phi}: \mathcal{X} \rightarrow \mathbb{R}^d\\
    \mathbf{w} \in \mathbb{R}^d \end{subarray}}} \sum_{e \in \mathcal{E}} R^e(\mathbf{w}^\top \bm{\phi}(X^e)) \\
    &\text{ s.t. } \mathbf{w} \in \underset{\bar{\mathbf{w}} \in \mathbb{R}^d}{\text{arg min }} R^e(\bar{\mathbf{w}}^\top \bm{\phi}(X^e)) \quad \forall e \in \mathcal{E}. \tag{1}
\end{align*}
$$
> What is invariant risk minimization?
>Invariant Risk Minimization (IRM) is a method for learning a data representation free of spurious correlations. It is based on the assumption that there exists some partition of the training data into experiments, and that the model's predictions take the form $Y^e = \mathbf{w}^\top \bm{\phi}{(X^e)}$. IRM aims to learn a representation $\bm{\phi}$ for which the optimal linear classifier, $\mathbf{w}$, is invariant across experiments, where optimality is defined as minimizing the empirical risk $R^e$. We can then expect this representation and classifier to have low risk in new experiments $e$, which have the same causal structure as the training set.

> What do you mean by the 'classifier to have low risk in new experiments'?
> Having low risk in new experiments means that the classifier is expected to perform well on unseen data from experiments that have the same causal structure as the training set. This is because the representation and classifier learned by IRM are invariant across experiments, meaning that they should be able to generalize to new experiments.

> What is empirical risk?
> Empirical risk is a measure of the expected loss of a model on a given dataset. It is calculated by taking the average of the losses over all data points in the dataset. This can be expressed as:
$$
\text{Risk} = \frac{1}{n}\sum_{i=1}^n \ell(y_i, \hat{y}_i)
$$
> where $\ell$ is the loss function, $y_i$ is the true label for the $i$th data point, and $\hat{y}_i$ is the predicted label.

The IRM objective in (1) can be thought of as a constrained optimization problem, where the objective is to learn a set of features $\phi$ for which the optimal classifier in each environment is the same. Conditioned on the environments corresponding to different interventions on the data-generating process, this is hypothesized to yield features that only depend on variables that bear a causal relationship to the predicted value. Because the constrained optimization problem is not generally feasible to optimize, \citet{arjovsky2019irm} propose a penalized optimization problem with a schedule on the penalty term as a tractable alternative.

## Problem Setup

We consider a family of environments $\mathcal{M}_\mathcal{E} = \{(\mathcal{X}_e, \mathcal{A}, \mathcal{R}_e, \mathcal{T}_e, \gamma) | \; e \in \mathcal{E}\}$, where $\mathcal{E}$ is some index set. For simplicity of notation, we drop the subscript $e$ when referring to the union over all environments $\mathcal{E}$. Our goal is to use a subset $\mathcal{E}_{\text{train}} \subset \mathcal{E}$ of these environments to learn a representation $\phi:\mathcal{X} \rightarrow \mathbb{R}^d$ which enables generalization of a learned policy to *every* environment. We denote the number of training environments as $N:=|\mathcal{E}_{\text{train}}|$. We assume that the environments share some structure, and consider different degrees to which this structure may be shared.

### The Block MDP

Block MDPs~\citep{du2019pcid} are described by a tuple $\langle \mathcal{S}, \mathcal{A}, \mathcal{X}, p, q, R \rangle$ with a finite, unobservable state space $\mathcal{S}$, finite action space $\mathcal{A}$, and possibly infinite, but observable space $\mathcal{X}$. $p$ denotes the latent transition distribution $p(s'|s,a)$ for $s,s'\in\mathcal{S}, a\in\mathcal{A}$, $q$ is the (possibly stochastic) emission function that gives the observations from the latent state $q(x|s)$ for $x\in\mathcal{X}, s\in\mathcal{S}$, and $R$ the reward function.  A graphical model of the interactions between the various variables can be found in \cref{fig:irm_model_irrelevant}.

----------
**Assumption Block structure** ~\citep{du2019pcid} 
Each observation $x$ uniquely determines its generating state $s$. That is, the observation space $\mathcal{X}$ can be partitioned into disjoint blocks $\mathcal{X}_s$, each containing the support of the conditional distribution $q(\cdot|s)$.

----------

This assumption gives us the Markov property in $\mathcal{X}$. 

We translate the block MDP to our multi-environment setting as follows. If a family of environments $\mathcal{M}_\mathcal{E}$ satisfies the block MDP assumption, then each $e \in \mathcal{E}$ corresponds to an emission function $q_e$, with $S,A, \mathcal{X}$ and $p$ shared for all $M \in \mathcal{M}_\mathcal{E}$. We will move the potential randomness from $q_e$ into an auxiliary variable $\eta \in \Omega$, with $\Omega$ some probability space, and write $q_e(\eta, s)$. Further, we require that if $\text{range}(q_e (\cdot, s)) \cap \text{range}(q_{e'}(\cdot, s')) \neq \emptyset$, then $s = s'$. 

The objective is to learn a useful state abstraction to promote generalization across the different emission functions $q_e$, given that only a subset is provided for training. \citet{Song2020Observational} also describes a similar POMDP setting where there is an additional observation function, but assume information can be lost. We note that this problem can be made arbitrarily difficult if each $q_e$ has a disjoint range, but will focus on settings where the $q_e$ overlap in structured ways -- for example, where $q_e$ is the concatenation of the noise and state variables: $q_e(\eta, s) = s \oplus f(\eta)$.

### Relaxations
