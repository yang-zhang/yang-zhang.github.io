
# coding: utf-8

# ### Completely scalar case
# Let
# $$
# g(x)=x^3+3x^2+5x,\
# h(x)=x^{-2}
# $$
# and
# $$
# f(x)=h(g(x))=(x^3+3x^2+5x)^{-2}.
# $$
# We want to know $f'(x)$. And we know
# $$
# g'(x)=3x^2+6x+5, \
# h'(x)=-2x^{-3}.
# $$
# The chain rule says
# $$
# f'(x)=h'(g(x))g'(x)=-2(g(x)^{-3})g'(x)=-2(x^3+3x^2+5x)^{-3}(3x^2+6x+5)
# $$

# ### Output is scalar
# Let 
# $$
# \mathbf g(\mathbf x): \mathbb{R}^3 \rightarrow \mathbb{R}^2=[g_1(\mathbf x), g_2(\mathbf x)]^\top=[x_1^3+2x_2^2+5x_3, 2x_1^3+x_3^2]^\top,
# $$
# $$
# h(\mathbf x): \mathbb{R}^2 \rightarrow \mathbb{R}^1 = x_1 + x_2^2,
# $$
# and
# $$
# f(\mathbf x): \mathbb{R}^3 \rightarrow \mathbb{R}^1 = h(\mathbf g(\mathbf x))= x_1^3+2x_2^2+5x_3 + (2x_1^3+x_3^2)^2.
# $$
# 
# We want to know the Jacobian matrix or derivative matrix of $f(\mathbf x)$
# $$
# \mathbf D_f(\mathbf x)=\begin{bmatrix}
# \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \frac{\partial f}{\partial x_3}
# \end{bmatrix}.
# $$
# 
# And we know the Jacobian matrix of $\mathbf g(\mathbf x)$
# $$
# \mathbf D_{\mathbf g}(\mathbf x)=\begin{bmatrix}
# \frac{\partial g_1}{\partial x_1} & \frac{\partial g_1}{\partial x_2} & \frac{\partial g_1}{\partial x_3} \\
# \frac{\partial g_2}{\partial x_1} & \frac{\partial g_2}{\partial x_2} & \frac{\partial g_2}{\partial x_3} \\
# \end{bmatrix}=
# \begin{bmatrix}
# 3x_1^2 & 4x_2 & 5 \\
# 6x_1^2 & 0 & 2x_3 \\
# \end{bmatrix},
# $$
# and the Jacobian matrix or derivative matrix of $h(\mathbf x)$
# $$
# \mathbf D_h(\mathbf x)=\begin{bmatrix}
# \frac{\partial h}{\partial x_1} & \frac{\partial h}{\partial x_2}
# \end{bmatrix}=
# \begin{bmatrix}
# 1 & 2x_2 \\
# \end{bmatrix},
# $$
# The chain rule says
# $$
# \mathbf D_f(\mathbf x)=
# \begin{bmatrix}
# \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \frac{\partial f}{\partial x_3}
# \end{bmatrix}=
# \mathbf D_h(\mathbf g(\mathbf x))\mathbf D_g(\mathbf x)= \begin{bmatrix}
# 1 & 4x_1^3+2x_3^2 \\
# \end{bmatrix}
# \begin{bmatrix}
# 3x_1^2 & 4x_2 & 5 \\
# 6x_1^2 & 0 & 2x_3 \\
# \end{bmatrix} = 
# \begin{bmatrix}
# 3x_1^2+24x_1^5+12x_1^2x_3^2 & 4x_2& 5 + 8x_1^3x_3 + 4x_3^3
# \end{bmatrix}.
# $$
# And this can be verified by directly differentiating $f(\mathbf x)=x_1^3+2x_2^2+5x_3 + (2x_1^3+x_3^2)^2$.

# ### Genaral case
# Let 
# $$
# \mathbf g(\mathbf x): \mathbb{R}^3 \rightarrow \mathbb{R}^2=[g_1(\mathbf x), g_2(\mathbf x)]^\top=[x_1^3+2x_2^2+5x_3, 2x_1^3+x_3^2]^\top,
# $$
# $$
# \mathbf h(\mathbf x): \mathbb{R}^2 \rightarrow \mathbb{R}^2 = [x_1 + x_2^2, 2x_2]^\top,
# $$
# and
# $$
# \mathbf f(\mathbf x): \mathbb{R}^3 \rightarrow \mathbb{R}^2 = \mathbf h(\mathbf g(\mathbf x))= [x_1^3+2x_2^2+5x_3 + (2x_1^3+x_3^2)^2, 4x_1^3+2x_3^2]^\top.
# $$
# 
# We want to know the Jacobian matrix or derivative matrix of $\mathbf f(\mathbf x)$
# $$
# \mathbf D_{\mathbf f}(\mathbf x)=\begin{bmatrix}
# \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3} \\
# \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3} 
# \end{bmatrix}.
# $$
# 
# And we know the Jacobian matrix of $\mathbf g(\mathbf x)$
# $$
# \mathbf D_{\mathbf g}(\mathbf x)=\begin{bmatrix}
# \frac{\partial g_1}{\partial x_1} & \frac{\partial g_1}{\partial x_2} & \frac{\partial g_1}{\partial x_3} \\
# \frac{\partial g_2}{\partial x_1} & \frac{\partial g_2}{\partial x_2} & \frac{\partial g_2}{\partial x_3} \\
# \end{bmatrix}=
# \begin{bmatrix}
# 3x_1^2 & 4x_2 & 5 \\
# 6x_1^2 & 0 & 2x_3 \\
# \end{bmatrix},
# $$
# and the Jacobian matrix or derivative matrix of $\mathbf h(\mathbf x)$
# $$
# \mathbf D_{\mathbf h}(\mathbf x)=\begin{bmatrix}
# \frac{\partial h_1}{\partial x_1} & \frac{\partial h_1}{\partial x_2} \\
# \frac{\partial h_2}{\partial x_1} & \frac{\partial h_2}{\partial x_2}
# \end{bmatrix}=
# \begin{bmatrix}
# 1 & 2x_2 \\
# 0 & 2 
# \end{bmatrix},
# $$
# The chain rule says
# $$
# \mathbf D_{\mathbf f}(\mathbf x)=
# \begin{bmatrix}
# \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3} \\
# \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3} 
# \end{bmatrix}=
# \mathbf D_{\mathbf h}(\mathbf g(\mathbf x))\mathbf D_{\mathbf g}(\mathbf x)= \begin{bmatrix}
# 1 & 4x_1^3+2x_3^2 \\
# 0 & 2
# \end{bmatrix}
# \begin{bmatrix}
# 3x_1^2 & 4x_2 & 5 \\
# 6x_1^2 & 0 & 2x_3 \\
# \end{bmatrix} = 
# \begin{bmatrix}
# 3x_1^2+24x_1^5+12x_1^2x_3^2 & 4x_2& 5 + 8x_1^3x_3 + 4x_3^3 \\
# 12x_1^2 & 0 & 4x_3
# \end{bmatrix}.
# $$
# And this can be verified by directly differentiating $\mathbf f(\mathbf x)=[x_1^3+2x_2^2+5x_3 + (2x_1^3+x_3^2)^2, 4x_1^3+2x_3^2]^\top$.
