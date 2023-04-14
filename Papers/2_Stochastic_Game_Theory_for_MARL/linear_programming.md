# Linear Programming

Linear programming is a mathematical technique used to optimize a given objective function subject to a set of constraints. It is used to find the maximum or minimum value of a linear objective function subject to a set of linear constraints. Linear programming is used in a variety of fields, including economics, engineering, and operations research. It is also used to solve problems in finance, marketing, and other areas. Linear programming can be used to solve problems involving multiple objectives, such as maximizing profits or minimizing costs. It can also be used to solve problems involving multiple constraints, such as resource allocation or scheduling. Linear programming is a powerful tool for solving complex problems.

**Definition 1** Linear programming is a mathematical technique used to optimize a given objective function $f(x)$ subject to a set of constraints $g_i(x) \leq b_i$ for $i = 1, \dots, m$, where $x \in \mathbb{R}^n$ is the vector of decision variables. The goal is to find the vector $x^*$ that maximizes or minimizes the objective function $f(x)$ subject to the constraints $g_i(x) \leq b_i$.
`
import wikipedia
wiki = wikipedia.page("Linear programming")
text = wiki.content
print(text)
`
Linear programming (LP), also called linear optimization, is a method to achieve the best outcome (such as maximum profit or lowest cost) in a mathematical model whose requirements are represented by linear relationships. Linear programming is a special case of mathematical programming (also known as mathematical optimization).

More formally, linear programming is a technique for the optimization of a linear objective function, subject to linear equality and linear inequality constraints. Its feasible region is a convex polytope, which is a set defined as the intersection of finitely many half spaces, each of which is defined by a linear inequality. Its objective function is a real-valued affine (linear) function defined on this polyhedron. A linear programming algorithm finds a point in the polytope where this function has the smallest (or largest) value if such a point exists.

Linear programs are problems that can be expressed in canonical form as: Find a vector $x$ that maximizes $c^{T}x$ subject to $Ax \leq b$ and $x \geq 0$.
    
Here the components of $x$ are the variables to be determined, $c$ and $b$ are given vectors (with $c^{T}$ indicating that the coefficients of $c$ are used as a single-row matrix for the purpose of forming the matrix product), and $A$ is a given matrix. The function whose value is to be maximized or minimized ($x \mapsto c^{T}x$ in this case) is called the objective function. The inequalities Ax ≤ b and x ≥ 0 are the constraints which specify a convex polytope over which the objective function is to be optimized. In this context, two vectors are comparable when they have the same dimensions. If every entry in the first is less-than or equal-to the corresponding entry in the second, then it can be said that the first vector is less-than or equal-to the second vector.

Linear programming can be applied to various fields of study. It is widely used in mathematics and, to a lesser extent, in business, economics, and some engineering problems. Industries that use linear programming models include transportation, energy, telecommunications, and manufacturing. It has proven useful in modeling diverse types of problems in planning, routing, scheduling, assignment, and design.

== History ==

The problem of solving a system of linear inequalities dates back at least as far as Fourier, who in 1827 published a method for solving them, and after whom the method of Fourier–Motzkin elimination is named.

In 1939 a linear programming formulation of a problem that is equivalent to the general linear programming problem was given by the Soviet mathematician and economist Leonid Kantorovich, who also proposed a method for solving it. It is a way he developed, during World War II, to plan expenditures and returns in order to reduce costs of the army and to increase losses imposed on the enemy. Kantorovich's work was initially neglected in the USSR. About the same time as Kantorovich, the Dutch-American economist T. C. Koopmans formulated classical economic problems as linear programs. Kantorovich and Koopmans later shared the 1975 Nobel prize in economics. In 1941, Frank Lauren Hitchcock also formulated transportation problems as linear programs and gave a solution very similar to the later simplex method. Hitchcock had died in 1957, and the Nobel prize is not awarded posthumously.

From 1946 to 1947 George B. Dantzig independently developed general linear programming formulation to use for planning problems in the US Air Force. In 1947, Dantzig also invented the simplex method that, for the first time efficiently, tackled the linear programming problem in most cases. When Dantzig arranged a meeting with John von Neumann to discuss his simplex method, Neumann immediately conjectured the theory of duality by realizing that the problem he had been working in game theory was equivalent. Dantzig provided formal proof in an unpublished report "A Theorem on Linear Inequalities" on January 5, 1948. Dantzig's work was made available to public in 1951. In the post-war years, many industries applied it in their daily planning.

Dantzig's original example was to find the best assignment of 70 people to 70 jobs. The computing power required to test all the permutations to select the best assignment is vast; the number of possible configurations exceeds the number of particles in the observable universe. However, it takes only a moment to find the optimum solution by posing the problem as a linear program and applying the simplex algorithm. The theory behind linear programming drastically reduces the number of possible solutions that must be checked.

The linear programming problem was first shown to be solvable in polynomial time by Leonid Khachiyan in 1979, but a larger theoretical and practical breakthrough in the field came in 1984 when Narendra Karmarkar introduced a new interior-point method for solving linear-programming problems.

== Uses ==

Linear programming is a widely used field of optimization for several reasons. Many practical problems in operations research can be expressed as linear programming problems. Certain special cases of linear programming, such as network flow problems and multicommodity flow problems, are considered important enough to have much research on specialized algorithms. A number of algorithms for other types of optimization problems work by solving linear programming problems as sub-problems. Historically, ideas from linear programming have inspired many of the central concepts of optimization theory, such as duality, decomposition, and the importance of convexity and its generalizations. Likewise, linear programming was heavily used in the early formation of microeconomics, and it is currently utilized in company management, such as planning, production, transportation, and technology. Although the modern management issues are ever-changing, most companies would like to maximize profits and minimize costs with limited resources. Google also uses linear programming to stabilize YouTube videos.

== Standard form ==
Standard form is the usual and most intuitive form of describing a linear programming problem. It consists of the following three parts:
$/dots$
