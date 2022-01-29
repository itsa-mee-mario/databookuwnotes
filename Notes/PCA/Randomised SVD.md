Data is becoming higher and higher dimensional very fast.
SVD hopes that there are low rank patterns in this data, and there might be low intrinsic rank (mostly the same information in even higher dim)

Randomised SVD is a way to reduce computing time

Randomised SVD randomly samples the coulmn space of data matrix and with high probability, find the subspace that will be spanned by the dominnat columns of the SVD

relies on high dimentional geometry, compressed sensing, sparse matrix, etc.

## Computing
1. Compute random projection P that we can multiply with column space of X
	$P \in R^{m\times r}$

	$Z = XP$

	find QR factorisation of Z
	$Z = QR$
		Q is a orthonormal basis for Z, and by extension, X

	![[Pasted image 20220129194507.png]]

2. Project original data matrix X on orthogonal subspace Q
	$Y = Q^{T}X$
	Y has a very small dim r

	$Y = U_{y}\Sigma V^T$ 
	(due to high dim geometry things, $\Sigma V^T$ is same as for X if $U_{y}$ is orthanormal basis that spans the columns of X)

3. $U_{x}= QU_{y}$	 
![[Pasted image 20220129195013.png]]


## Over-sampling:
Make projection matrix a little bigger than rank r

## Power iternation:
taking powers of X allows us to make the singular value curve more favourable 

![[Pasted image 20220129195715.png]]

