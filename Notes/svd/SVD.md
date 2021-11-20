# Singular Value Decomposition

---

1. Data reduction
2. Data-driven generalization of [[Fourier Transform]]
3. Tailored to specefic problem 
4. Guaranteed to exist
5. Unique
6. Simple and interpretable linear algebra


---

## Uses of SVD
Solve linear system of equation $AX=B$ for non-square A matrices, especially for linear regression.

scalable asf

The basis for [[Principal Component Analysis]].

Face Rec, Reccomender systems, PageRank, etc. 

---

# the math

Define a data matrix $X$ as a colection of column vectors
$$X = \begin{bmatrix}
x_1&
x_2
&...
\end{bmatrix}$$

Where $x_{k} \in R^n$  

---

$X$ could come from a real world system like a fluid flow, evolving in time; or any kind of matrix data, really

---

### SVD allows us to 
$$X = U\Sigma V^T$$
$$
= \begin{bmatrix}.&.&.&.\\ u_1&u_2&.&u_{n}\\ .&.&.&. \end{bmatrix}

\begin{bmatrix}
\sigma_{1}&.&. \\
 . & \sigma_{2}&. \\
 .&.&.\\
 .&. & \sigma_{m}\\
 0&0&0
 \end{bmatrix}


\begin{bmatrix}
. & .  & . & .  \\
v_{1} & v_{2} & . & v_{n}\\
. & .  & . & .  \\

\end{bmatrix}^T 
$$
![[Pasted image 20211119232938.png]]

where $u, v$ are unitry matrices (unitary means the transpose is the inverse)

$\Sigma$ is diagonal, non-negative and in decreasing order

---

$u$ is called left singular vector
$v$ is called right singular vector
and $\Sigma$ is a matrix of singular values and its columns contain the relevant importance of the columns in $u, v$


--- 

(because the singular matrix is in decreasing order, the relative importance of the columns of the other two matrices are also in that order)

---

 ### Interpreation of the martrix equation
 Case 1: Fluid Flow
 
1.	$U$ contains the states of the system (maybe images, converted into a column vector), in the case of flow fields evolving in time, we can call them "eigen-flows"
	
2. the amount of energy of the flow capured by the columns of matrix $X$ are related to corresponding decreasing values of $\sigma$ 

3. $v_1$ would be the time series of how the first mode ($u_{1}$) evolves in the flow (each of the snapshots in $X$ has a certain amount of $u_{1}$ in it, and the amount of how that mode varies in time is given by $V$)

---

Case 2: Faces
1. $U$ contains eigen-faces
2. $\sigma$ s contain the relative importance 
3. each column of $V^{T}$ contains the exact mixture of all the columns in the eigen-face matrix to give the corresponding column in the data matrix

---

