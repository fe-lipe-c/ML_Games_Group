## Review of Differential Equations

In the basic model of a control system, as soon as a control function $u = u(t)$ is assigned, the evolution can be determined by solving the O.D.E.
$$
\begin{equation}
	\dot{x} = g(t,x) = f(x,u(t)) \tag{2.1}
\end{equation}
$$

--- 

**Definition (ODE Solution)** 
Let $\Omega$ be an open set in $\mathbb{R} \times \mathbb{R}^{n}$. Given a function $g: \Omega \longrightarrow \mathbb{R}^{n}$, by a (Carathéodory) solution of the O.D.E.
$$
\begin{equation}
	\dot{x} = g(t,x) \tag{2.2}
\end{equation}
$$
we mean an absolutely continuous function $t \longrightarrow x(t)$, defined on some interval $[t_0, t_1]$, which satisfies (2.2) almost everywhere. Equivalently, we require that 
$$
\begin{equation}
	x(t) = x(t_0) + \int_{t_0}^{t} g(s,x(s)) \, ds \tag{2.3}
\end{equation}
$$
for all $t \in [t_0, t_1]$ where the function is defined.

---

In the classical theory of ordinary differential equations, it is assumed that the function $g$ is continuous w.r.t. both variables. For applications to theory of control, however, it is important to consider also the case where $g$ is only measurable w.r.t. the variable $t$. This more general setting is needed for two main reasons:

> The function $u(\cdot)$ may take values in a discrete set. All non-constant controls are necessarily discontinuous.

> In several optimization problems, the existence of an optimal control can be established only within the class of all measurable functions $u(\cdot)$. Quite often, the optimal control is actually discontinuous.

When a measurable control function $u = u(t)$ is inserted in the equation describing a control system, we obtain an O.D.E. of the form (2.1), whose right hand side is only measurable w.r.t. the time t.

### 2.1 Fundamental Theory

---
**Basic Assumptions** 
Throughout this section we assume that the function $g: \Omega \longrightarrow \mathbb{R}^{n}$ satisfies the following conditions:

**(A)** For every $x$ the function $f \rightarrow g(t,x)$ defined on the section
$$
\begin{equation}
	\Omega_{x} = \left\{t : (t,x) \in \Omega \right\}
\end{equation}
$$
is measurable. For every $t$, the function $x \rightarrow g(t,x)$ defined on the section
$$
\begin{equation}
	\Omega_{t} = \left\{x : (t,x) \in \Omega \right\}
\end{equation}
$$
is continuous.

**(B)** For every compact $K \subset \Omega$ there exist constants $C_{K},L_{K}$ such that 
$$
\begin{equation}
\begin{split}
	|g(t,x)| \leq C_{K},\\
	|g(t,x) - g(t,y)| \leq L_{K}|x-y| \tag{2.3}
\end{split}
\end{equation}
$$
for all $(t,x),(t,y) \in K$.

---

**Theorem 2.1.1. (Existence of Solutions)** Given a map $g: \Omega \rightarrow \mathbb{R}^{n}$, consider the Cauchy problem
$$
\begin{equation}
	\begin{split}
		\dot{x} = g(t,x),\\ \tag{2.4}
		x(t_0) = x_0,
	\end{split}
\end{equation}
$$
for some $(t_0,x_0) \in \Omega$.

**(i)** If $g$ satisfies the assumptions (A), (B), then there exists $\epsilon > 0$ such that (2.4) has a local solution $x(\cdot)$ defined for $t \in [t_0, t_0 + \epsilon]$.

**(ii)** Assume, in addition, that the function $g$ is defined on the entire space $\mathbb{R} \times \mathbb{R}^{n}$ and there exist constants $C,L$ such that 
$$
\begin{equation}
	\begin{split}
		|g(t,x)| \leq C,\\
		| g(t,x) - g(t,y) | \leq L | x-y | \tag{2.5}
	\end{split}
\end{equation}
$$
for all $t,x,y$. Then, for every $T > t_0$, the initial value problem (2.4) has a global unique solution $x(\cdot)$ defined for all $t \in [t_0, T]$. Moreover, the solution depends continuously on the initial data $x_0$.

---

The next lemma provides a useful tool for estimating the distance between two solutions of a differential equation. It represents the main ingredient in several uniqueness proofs.

---

**Lemma 2.1.2. (Gronwall)** 
Let $z(\cdot)$ be an absolutely continuous nonnegative function such that
$$
\begin{equation}
	\begin{split}
		z(t_0) \leq \gamma,\\
		\dot{z} \leq \alpha(t)z(t) + \beta(t) \tag{2.11}
	\end{split}
\end{equation}
$$
for a.e. $t \in [t_0, T]$, for some integrable functions $\alpha, \beta$, and some constant $\gamma \geq 0$. Then for every $t \in [t_0, T]$ the following holds
$$
\begin{equation}
	z(t) \leq \gamma \exp{\left( \displaystyle\int_{t}^{t_0} \alpha(s) ds \right)} + \displaystyle\int_{t_0}^{t} \beta(s) \exp{\left(\int_{t_0}^{s} \alpha(\sigma) d\sigma\right)}ds. \tag{2.12}
\end{equation}
$$

---

---

**Theorem 2.1.3 (Uniqueness)**
Let $g: \Omega \rightarrow \mathbb{R}^{n}$ satisfy the assumptions (A) and (B), as in Theorem 2.1.1. Let $x_1(\cdot), x_2(\cdot)$ be solutions of (2.4), defined on the intervals $[t_0,t_1],[t_0,t_2]$, respectively. If $T = \min{\{t_1,t_2\}}$, then $x_1(t) = x_2(t)$ for all $t \in [t_0,T]$.

---

In general, the solution to the Cauchy problem (2.4) is defined only locally, for $t$ in a neighborhood of the initial time $t_0$. If a solution cannot be extended beyond a certain time $T$, two cases may arise

1. As $t \rightarrow T-$, the point $(t,x(t))$ approaches the boundary $\partial\Omega$ of the domain $\Omega$ where $g$ is defined.
2. As $t \rightarrow T-$, the solution blows up, i.e. $|x(t)| \rightarrow \infty$.

---
**Theorem 2.1.4 (Maximal Solutions)** Let the basic assumptions $(A), (B)$ hold. Let $T > t_0$ be the supremum of all times $\tau$ such that (2.4) has a solution $x(\cdot)$ defined on $[t_0, \tau]$. Then, either $T = \infty$, or else 
$$
\begin{equation}
	\lim_{t \rightarrow T-} \left( |x(t)| + \displaystyle\frac{1}{d((t,x(t)), \partial \Omega)} \right) = \infty \tag{2.14}
\end{equation}
$$

---

In the case where $g$ is defined on the entire domain $[t_0,\infty]\times \mathbb{R}^{n}$, to establish the global existence of the solution to $(2.4)$ it thus suffices to prove that $x(\cdot)$ remains bounded on bounded intervals of time. In general, a-priori estimates on the size of $|x(t)|$ can be obtained by a comparison with a scalar O.D.E., as we now describe.

---
**Theorem 2.1.5. (A-priori Bounds)** Let $g: \Omega \rightarrow \mathbb{R}^{n}$ satisfy the basic assumptions (A)-(B). Let $\psi:[t_0,t_1] \times \mathbb{R} \rightarrow \mathbb{R}$ be a scalar function, measurable in $t$ and continuous in $x$, such that
$$
\begin{equation}
	\psi(t,r) \geq \max_{|x|=r} |g(t,x)| \tag{2.16}
\end{equation}
$$
for all $t,r$. Let $r:[t_0,t_1] \rightarrow \mathbb{R}$ be an absolutely continuous function such that
$$
\begin{equation}
	\begin{split}
		\dot{r}(t) \geq \psi(t,r)\\
		r(t_0) \geq |x_0| \tag{2.17}
	\end{split}
\end{equation}
$$
for a.e. $t\in[t_0,t_1]$. If the set $K = \{(t,x): t_0 \leq t \leq t_1, |x| \leq r(t)\}$ is contained in $\Omega$, then the Cauchy problem (2.4) has a solution $x(\cdot)$ defined on the entire interval $[t_0,t_1]$, which satisfies
$$
\begin{equation}
	|x(t)| \leq r(t) \tag{2.18}
\end{equation}
$$
for all $t \in [t_0,t_1]$.

In many applications, useful estimates can be obtained from the above theorem by a judicious choice of the function $r(\cdot)$.

**Corollary 2.1.6.** Assume that the function $g = g(t,x)$ satisfies the bound 
$$
\begin{equation}
	|g(t,x)| \leq C(1+|x|) \tag{2.22}
\end{equation}
$$
for some constant C and all $x \in \mathbb{R}^{n}$. Then any solution of (2.4) satisfies the a priori estimate
$$
\begin{equation}
	|x(t)| \leq e^{|t-t_0|}\left(1 + |x(t_0)|\right). \tag{2.23}
\end{equation}
$$

### Linear Systems

In this section we consider differential equations of the form
$$
\begin{equation}
 \dot{x}=A(t)x \tag{2.24}
\end{equation}
$$
$$
\begin{equation}
	\dot{p} = -p(t)A(t) \tag{2.25}
\end{equation}
$$
where $t \rightarrow A(t)$ is a measurable map from an interval $[a,b]$ into the set of $n \times n$ matrices.

The norm of a matrix $A$ is defined as
$$
\begin{equation*}
	\vert| A \vert| = \max_{|x|=1} |Ax| = \max_{|p|=1}|pA|
\end{equation*}
$$
In the special case where the $n \times n$ matrix $A(t) \equiv A$ is independent of time, the solution to the Cauchy problem
$$
\begin{equation}
	\begin{split}
		\dot{x} = Ax\\
		x(0) = x \tag{2.26}
	\end{split}
\end{equation}
$$
can be written in the form  
$$
\begin{equation}
	x(t) = e^{tA}x \tag{2.27}
\end{equation}
$$
where $e^{tA} = \sum_{k=0}^{\infty}\frac{t^{k}A^{k}}{k!}$, the limit of absolutely convergent series.

---
**Theorem 2.2.1. (Existence of Solutions for Linear Systems)** Assume that $\vert| A(t) \vert| \leq L$ for some constant $L$ and all $t \in [a,b]$. Then, for any $t_0 \in [a,b]$ and every initial condition $x_0 \in \mathbb{R}^{n}$, the Cauchy problem
$$
\begin{equation}
	\begin{split}
		\dot{x} = A(t)x\\
		x(t_0) = x_0 \tag{2.29}
	\end{split}
\end{equation}
$$
has a unique solution defined on the entire interval $[a,b]$. This solution satisfies
$$
\begin{equation}
	|x(t)| \leq e^{L|t-t_0|} |x_0|  \tag{2.30}
\end{equation}
$$

---

---
**Theorem 2.2.2. (Adjoint Systems)** 
Let $(\cdot), p(\cdot)$ be any two solutions of (2.24), (2.25) respectively, defined on the same interval of time: $t \in [a,b]$. Then their inner product $p(t)\cdot x(t)$ is constant.

---

Since the system in (2.24) is linear and homogeneous, the set of solutions is a linear space. In other words, if $(\cdot)$ and $y(\cdot)$ are solutions of (2.24), then the linear combination $\lambda x + \mu y$ provides yet another solution, for every choice of $\lambda, \mu \in \mathbb{R}$ To obtain the general solution to a Cauchy problem, it thus suffices to construct a set of $n$ linearly independent solutions. This motivates the following construction. Let $e_1, e_2, \dots, e_{n}$ be the elements of athe standard basis in \mathbb{R}^{n}. For a fixed time $s$ and each $j=1,\dots,n$ call $t \rightarrow v_{j}(t,s)$ the solution to the Cauchy problem
$$
\begin{equation*}
	\begin{split}
		\dot{v}_{j}(t) = A(t)v_{j}(t)\\
		v_{j}(s) = e_{j}
	\end{split}
\end{equation*}
$$
Construct the $n \times n$ matrix $M(t,s)$ whose columns are given by the vectors $v_1,v_2,\dots,v_{n}$. Namely
$$
\begin{equation*}
	M(t,s) = \left( v_1(t,s), | v_2(t,s) | \cdots | v_{n}(t,s)\right)
\end{equation*}
$$
This is called the fundamental matrix solution of (2.24). For a fixed value of $s$, the map $t \rightarrow M(t,s)$ provides a matrix-valued solution to the problem
$$
\begin{equation}
\begin{split}
	\frac{\partial M(t,s)}{\partial t} = A(t)M(t,s)\\ \tag{2.31}
	M(s,s) = I 
\end{split}
\end{equation}
$$
where $I$ denotes the $n \times n$ identity matrix.

---
**Theorem 2.2.3. (Properties of the Fundamental Matrix Solution)** 
Assume that the matrices $A(t)$ are uniformly bounded, with coefficients depending measurably on $t \in [a,b]$. Then for every $\xi \in \mathbb{R}^{n}$, the function $x(t) = M(T,s)\xi$ provides the solution to the Cauchy problem
$$
\begin{equation}
	\begin{split}
		\frac{d}{dt}x(t) = A(t)x(t)\\
		x(s) = \xi \tag{2.32}
	\end{split}
\end{equation}
$$
The fundamental matrix solution $M$ satisfies
$$
\begin{equation}
	M(t,s)M(s,r) = M(t,r), \text{ for all } t,s,r \in [a,b]\\ \tag{2.33}
\end{equation}
$$
$$
\begin{equation}
	\frac{\partial M(t,s)}{\partial s} = -M(t,s)A(t) \tag{2.34} 
\end{equation}
$$
Moreover, if $h:[a,b] \rightarrow \mathbb{R}^{n}$ is integrable, then any function satisfying
$$
\begin{equation}
	x(t) = M(t,\tau)x(\tau) + \int_{\tau}^{t} M(t,s)h(s)ds \tag{2.35}
\end{equation}
$$
is a solution to 
$$
\begin{equation}
	\dot{x} = A(t)x(t) + h(t) \tag{2.36}
\end{equation}
$$

---

By Theorem 2.2.1. each bounded, measurable matrix-valued function $A(\cdot)$ determines a fundamental matrix solution $M(\cdot,\cdot)$. The next result states that $M$ depends continuously on $A$, in the appropriate norms.

---
**Theorem 2.2.4. (Continuous Dependence of the Fundamental Matrix Solution)** 
The map $A(\cdot) \rightarrow M(\cdot,\cdot)$ is continuous w.r.t. the distances
$$
\begin{equation}
	\begin{split}
		||A(\cdot) - A^{'}(\cdot)||_{L^{1}} = \int_{a}^{b} ||A(t) - A^{'}(t)||dt,\\
		||M(\cdot,\cdot) - M^{'}(\cdot,\cdot)||_{C^{0}} = \max_{a \leq s, t\leq b} ||M(t,s) - M^{'}(t,s)||\\
	\end{split}
\end{equation}
$$

---

### Differentiability with respect to initial data

A common problem in the theory of optimal control is to test whether a given control function $u^{*}(\cdot)$ is optimal. This is usually done by comparing the trajectory $t \rightarrow x(t,u^{*})$  with other nearby trajectories.

The basic ingredient in this analysis is a detailed description of how the solution of the Cauchy problem
$$
\begin{equation}
\begin{split}
	\dot{x}(t) = g(t,x(t))\\
	x(\tau) = \xi \tag{2.39}
\end{split}
\end{equation}
$$
changes, as the initial data $\tau \xi$ are varied. We denote by $t \rightarrow x(t,\tau,\xi)$ the solution of (2.39), while $D_{x}g(t,x)$ is the $n \times n$ Jacobian matrix of first order partial derivatives $\partial g_{i}/ \partial x_{j}$ at the point $(t,x)$.

---
**Theorem 2.3.1. (Directional Derivatives)** 
Let $g: \Omega \rightarrow \mathbb{R}^{n}$ satisfy the basic assumptions (A)-(B) and be continuously differentiable w.r.t. $x$. Let $\dot{x}(\cdot) = x(\cdot,t_0,x_0)$ be the solution of (2.4), defined for $t \in [t_0,t_1]$. For $v_0 \in \mathbb{R}^{n}$, call $v(\cdot)$ the solution of the linear Cauchy problem.
$$
\begin{equation}
	\begin{split}
		\dot{v}(t) = D_{x}g(t,\hat{x}(t)) \cdot v(t)\\
		v(t_0) = v_0 \tag{2.40}
	\end{split}
\end{equation}
$$
Then
$$
\begin{equation}
	\lim_{\epsilon \rightarrow 0+} \left|\frac{x(t,t_0,x_0+\epsilon v_0) - \hat{x}(t)}{\epsilon} - v(t) \right|= 0 \tag{2.41}
\end{equation}
$$
the limit being uniform for $t \in [t_0,t_1], |v_0| \leq 1$.

---

For each $t \in [t_0, t_1]$, Theorem 2.3.1 states the existence of all directional derivatives for the map $\xi \rightarrow x(t,t_0,\xi)$. In the next theorem, we observe that these derivatives depend continuously on the point $x_0$ where they are computed, and conclude that the map is differentiable.

---
**Theorem 2.3.2. (Differentiability w.r.t. the Initial Point)** 

---

The next result is concerned with the differentiability of the solution $x(\cdot, \tau, \xi)$ w.r.t. the initial time $\tau$, under the additional assumption that $g$ is continuous also w.r.t. time.

--- 
**Theorem 2.3.3. (Differentiability w.r.t. the Initial Time)** 

---


### A Transversality Theorem

Let $g:[t_0,t_1] \times \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$ be a continuously differentiable vector field, and let $\mathcal{M} \subset \mathbb{R}^{n+1}$ be a n-dimensional manifold.

More precisely, assume that there exists a $\mathcal{C}^1$ mapping $\phi: \mathbb{R}^{n+1} \rightarrow \mathbb{R}$ such that $\mathcal{M}$ can be represented as the zero level set of $\phi$:
$$
\begin{equation}
	\mathcal{M} = \left\{(t,x) : \phi(t,x) = 0 \right\}, \tag{2.50}
\end{equation}
$$
and such that the gradient of $\phi$ does not vanish on any point of $\mathcal{M}$:
$$
\begin{equation}
	(\phi_{t}, \nabla_{x}\phi)(t,x) = (\phi_{t},\phi_{x_1},\dots,\phi_{x_{n}})(t,x) \neq (0,0,\dots,0) \tag{2.51}
\end{equation}
$$
for all $(t,x) \in \mathcal{M}$.

Let $x(\cdot)$ be a solution to the differential equation 
$$
\begin{equation}
	\dot{x}(t) = g(t,x(t)) \tag{2.52}
\end{equation}
$$
If $(\tau,x(\tau))\in \mathcal{M}$, we say that $x(\cdot)$ intersects $\mathcal{M}$ transversally at the point $(\tau,x(\tau))$ if
$$
\begin{equation}
	\phi_{t}(\tau,x(\tau)) + \nabla_{x} \phi(\tau,x(\tau))\cdot g(\tau,x(\tau)) \neq 0 \tag{2.53}
\end{equation}
$$
This means that the vector $(1,g(\tau,x(\tau)))$ is not tangent to $\mathcal{M}$ at the point $(\tau,x(\tau))$. The next theorem states that "almost all" trajectories of (2.52) have only transversal intersections with $\mathcal{M}$.

---
**Theorem 2.4.1 (Generic Transversality of Trajectories)** Let $g = g(t,x)$ be continuously differentiable w.r.t. both $t$ and $x$. Assume that, for every $x_0$ in an open ball $B \subset \mathbb{R}^{n}$, the solution $t \rightarrow x(t,t_0,x_0)$ of (2.52) with initial condition $x(t_0)= x_0$ is defined on the whole interval $[t_0,t_1]$. Let $\mathcal{M} \subset \mathbb{R}^{n+1}$ be an n-dimensional embedded manifold, as in (2.50)-(2.51). Call $\mathcal{N}$ the set of all points $x_0 \in B$ such that $(\tau,x(\tau,t_0,x_0)) \in \mathcal{M}$ for some $\tau \in [t_0,t_1]$, but the intersection is not transversal. Then measure$(\mathcal{N})=0$




















## Appendix A

### A.1 Normed Spaces

---
**Definition (Cauchy Sequence)** 
A sequence of points $(x_{n})_{n \geq 1}$ is called a Cauchy sequence if, for every $\epsilon > 0$ there exists an integer $N$ larger enough so that
$$
\begin{equation*}
	\|x_{n} - x_{m}\| < \epsilon
\end{equation*}
$$
whenever $n,m \geq N$.

---

---
**Definition (Banach Space)** 
We say that the normed space $X$ is complete if every Cauchy sequence converges to some limit point in $X$. A complete normed space is called a Banach space.

---
### A.2 Banach's Contraction Mapping Theorem

---
**Theorem A.2.1. (Contraction Mapping Theorem)** 
Let  $X$ be a Banach space, $\Lambda$ a metric space, and let $\Phi: \Lambda \times X \rightarrow X$ be a continuous mapping such that, for some $\kappa <1$,
$$
\begin{equation}
	\| \Phi(\lambda,x) - \Phi(\lambda,y) \| \leq \kappa \| x - y \| \tag{A.4}
\end{equation}
$$
$\forall \lambda, x, y$. Then, for each $\lambda \in \Lambda$ there exists a unique fixed point $x(\lambda) \in X$ such that
$$
\begin{equation}
	x(\lambda) = \Phi(\lambda,x(\lambda)) \tag{A.5}
\end{equation}
$$
The map $\lambda \rightarrow x(\lambda)$ is continuous. Moreover, for any $\lambda \in \Lambda$, $y \in X$ one has
$$
\begin{equation}
	\|y-x(\lambda)\| \leq \frac{1}{1-\kappa}\|y - \Phi(\lambda,y)\|. \tag{A.6}
\end{equation}
$$

---
