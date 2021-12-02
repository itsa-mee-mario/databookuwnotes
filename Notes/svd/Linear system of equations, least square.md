 ## Linear system of eqn 
 $$A x = b$$
 solving for $x$ where $A, b$ are known
 
 1. if $A$ is a square matrix: number of unknows is equal to number of equations
 2. if $A$ is invertible, solution is $A^-1 b$

### SVD allows us to generalize this for non square A matrices

1. Under determined system of equations, $n< m$: short, fat $A$ matrix:
	not enough values for a unique solution. in general theres inf solutions 
	![[Pasted image 20211123101119.png]]
	![[Pasted image 20211124112712.png]]
2. Overdetermined case: tall, skinny matrix A: in general will have a unique value
	![[Pasted image 20211123103728.png]]
	![[Pasted image 20211124112749.png]]

# Take the SVD of A
allows us to ~approximately~ find the inverse of $A$ (called pseudo-inverse) that fits $X$ and lets us find the closest possible solution.
$$A = U\Sigma V^T $$
$$U\Sigma V^T x= b$$

$$V \Sigma^{-1} U^{T}U \Sigma V^{T}x= V\Sigma^{-1} U^{T} b = A^{\dagger}b$$

$$A^{\dagger}= V \Sigma^{-1}U^{T}$$
($A^{\dagger}$ is called the moore-penrose pseudo-inverse)



># $$\tilde{X} = V\Sigma^{-1}U^{T}b = A^{\dagger}b $$

Where $\tilde{X}$ is the best possbile approximation

$$A\tilde X = \hat U \hat \Sigma V^{T}\Sigma^{-1}\hat{U^T}b=\hat U \hat U^{T} b$$

so the value is not exactly equal to $b$ and is only an approximation
the $\hat U \hat U^{T}$ term represents an orthagonal projection of the target vector $b$ on 

---


## over determined case:
$$A\tilde{x} = U \Sigma V^{T}V \Sigma^{-1}U^{T}b = UU^{T}b$$


$$UU^{T}\ne b$$

$UU^T$ is the projection on $b$ on span of $\hat  U$ (same as span of $A$)


