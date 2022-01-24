# PCA
1. Statistical Intepretation of SVD
2. heirarchical coordinate system
3. dimentionality reduction technique

$$
X = \begin{bmatrix}... x_{1}... \\ ...x_{2}... \\ ...x_{3}...\end{bmatrix}
$$
where $x_{k}$ are results from a single experiment, have some statistical variance.

---
## Procedure
1. Find mean row
	$$\bar{x} = \frac{1}{n}\sum\limits_{j=1}^n x_j$$
2. Construct Average Matrix
	$$ \bar{X} = \begin{bmatrix}1\\.\\.\\1\end{bmatrix} \begin{bmatrix}... \bar x ...\end{bmatrix}$$
3. Obtain mean centered matrix B
	$$B = X- \bar X$$
	> Assumes gaussian data (mean variance is zero)

4. Covariance Matrix of B
	$$C = B^{T}B$$
5. Eigen-Decomposition of Covariance matrix of B
	$$CV=VD$$
	Largest Eigenvector: $v_{1}^{T}B^{T}Bv_1$

6. Principal Components
	$$P= BV$$
	$$B = U\Sigma V^{T}= TV $$
	$$\lambda= \sigma^2$$ where $\sigma^2$ is variance

How to decide how many principal components to use:
	$$
		 \frac{\sum\limits_{r} \lambda_{r}}{\sum\limits_{k} \lambda_{k}}
	$$

this fraction represents "what part of the total variance do the first r principal components describe"

