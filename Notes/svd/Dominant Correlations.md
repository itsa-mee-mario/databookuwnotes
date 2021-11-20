# Dominant Correlations

$$
X = U\Sigma V^{T}
$$
We can think of $U,V$ as eigenvectors of a correlation matrix given by $X\times X^T$

### Correlation matrix


#### $X^{T}X$ (short, fat matrix ($m \times n$) times long skinny matrix($n \times m$) = $m\times m$ (square matrix, small))
![[Pasted image 20211117013714.png]]

This is a correlation matrix among the COLUMNS of $X$ 
$$
X^{T} X = \begin{bmatrix}. & . & x_1 & .  & .\\ . & . & . & . & . \\  .& . & x_m & . & .\end{bmatrix}_{m\times n}
\begin{bmatrix}. & .  & . \\ . &  . & .\\ x_1  & . & x_m \\ . & . & . \\ . & . & .\end{bmatrix}_{n\times m}

$$

![[Pasted image 20211117014553.png]]


>Every entry in the correlation matrix is an INNER PRODUCT between two columns of the matrix $X$
$$x_{i}^{T} x_{j}= <x_{i,}x_{j}>$$


in the example where the data matrix is a collection of faces, the element $(i, j)$ in the correlation matrix is the inner-product between person-i and person-j's faces. the magnitude of this product represents the similarity in the faces. 

