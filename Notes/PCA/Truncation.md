# Optimal Truncation
Is a large and important choice to make in using SVD and PCA
Deciding how many singular values to keep, i.e. where to truncate, is one of
the most important and contentious decisions when using the SVD. There are
many factors, including specifications on the desired rank of the system, the
magnitude of noise, and the distribution of the singular values. Often, one trun-
cates the SVD at a rank r that captures a pre-determined amount of the vari-
ance or energy in the original data, such as 90% or 99% truncation.

---

### Optimal Hard Threshold
A matrix with a low-rank structure contaminated with Gaussian white noise, 
$$X = X_{true}+ \gamma X_{noise}$$
where $\gamma$ is the magnitude of noise

Then the optimal threshold is given by
1. if $X ∈ R^{n \times n}$ ,
$$\tau = \frac{4}{\sqrt3} \sqrt{n} \gamma$$
2. 	![[Pasted image 20220126190535.png]]


3. ![[Pasted image 20220126190556.png]]


---

