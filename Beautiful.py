
# coding: utf-8

# # Beautiful Mathematics Typesetting
# [Tex](https://en.wikipedia.org/wiki/TeX)
# 
# [LaTex](https://www.latex-project.org/)
# 
# [Motivating Examples](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Typesetting%20Equations.html)

# ### The Lorenz Equations
\begin{align}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{align}
# \begin{align}
# \dot{x} & = \sigma(y-x) \\
# \dot{y} & = \rho x - y - xz \\
# \dot{z} & = -\beta z + xy
# \end{align}

# ### The Cauchy-Schwarz Inequality
\begin{equation*}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation*}
# \begin{equation*}
# \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
# \end{equation*}

# ### Cross Product Formula
\begin{equation*}
\mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
\frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0
\end{vmatrix}
\end{equation*}
# \begin{equation*}
# \mathbf{V}_1 \times \mathbf{V}_2 =  \begin{vmatrix}
# \mathbf{i} & \mathbf{j} & \mathbf{k} \\
# \frac{\partial X}{\partial u} &  \frac{\partial Y}{\partial u} & 0 \\
# \frac{\partial X}{\partial v} &  \frac{\partial Y}{\partial v} & 0
# \end{vmatrix}
# \end{equation*}

# ### Probability of getting (k) heads when flipping (n) coins
\begin{equation*}
P(E)   = {n \choose k} p^k (1-p)^{ n-k}
\end{equation*}
# \begin{equation*}
# P(E)   = {n \choose k} p^k (1-p)^{ n-k}
# \end{equation*}

# ### Identity of Ramanujan
# [Srinivasa Ramanujan](https://en.wikipedia.org/wiki/Srinivasa_Ramanujan)
# 
# Self-taught, no formal training in mathematics, made contributions to:
# - mathematical analysis
# - number theory
# - infinite series
# - continued fractions
\begin{equation*}
\frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} =
1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
{1+\frac{e^{-8\pi}} {1+\ldots} } } }
\end{equation*}
# \begin{equation*}
# \frac{1}{\Bigl(\sqrt{\phi \sqrt{5}}-\phi\Bigr) e^{\frac25 \pi}} =
# 1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
# {1+\frac{e^{-8\pi}} {1+\ldots} } } }
# \end{equation*}

# ### Maxwell’s Equations
\begin{align}
\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\   \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
\nabla \cdot \vec{\mathbf{B}} & = 0
\end{align}
# \begin{align}
# \nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} & = \frac{4\pi}{c}\vec{\mathbf{j}} \\   \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\
# \nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\
# \nabla \cdot \vec{\mathbf{B}} & = 0
# \end{align}

# In[ ]:




