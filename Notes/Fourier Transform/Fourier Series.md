# Fourier Series
$$<f(x), g(x)> = \int_{a}^{b} f(x).\bar{g(x)} dx $$
![[Pasted image 20220131132613.png]]
> Approximate an arbitrary two-pi periodic function $f(x)$

$$f(x) = \frac{A_{0}}{2} + \sum\limits_{k=1}^{n}(A_{k}cos(kx)+ B_{k}sin (kx))$$
where 
$$A_{k}= \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)cos(kx)dx = <f(x), cos(kx)>\frac{1}{||cos(kx)||^2}$$
$$B_{k}= \frac{1}{\pi}\int_{-\pi}^{\pi}f(x)sin(kx)dx= <f(x), sin(kx)>\frac{1}{||sin(kx)||^2}$$

### making sense:
When we have a vector, we can represent it easily given two orthagonal basis vectors.
![[Pasted image 20220131133235.png]]
The choice of basis vector does not matter, and we can find the representation of the vector in any basis by taking the projection along the direction of basis vector and multiplying by unit basis. Fourier series is the same, but where we are in the function space, and instead of the vector, we can represent functions in any orthagonal basis. Sin and Cosin are orthagonal functions and so, a combination of infinite sins and cosins can exactly give the function we need, and a truncated version gives a good approximation to the function.


## Changing the bounds on the series:
$$f(x) = \frac{A_{0}}{2} + \sum\limits_{k=1}^{n}(A_{k}cos(2\pi \frac{kx}{L})+ B_{k}sin (2\pi \frac{kx}{L}))$$
We change the bounds such that the functiion is periodic between 0 and L. And,

$$A_{k}= \frac{2}{L}\int_{0}^{L}f(x)cos(2\pi \frac{kx}{L})dx$$
$$B_{k}= \frac{2}{L}\int_{0}^{L}f(x)sin(2\pi \frac{kx}{L})dx$$
---
## Inner Products of Functions (in Hilbert Space)
 Definition of inner product of functions is very consistent with definition for inner product for vectors.

 For real valued data:

 ![[Pasted image 20220201151908.png]]

tells us how similar two functions are, like in the case of vector inner product (dot prod)

  ![[Pasted image 20220201154957.png]]
  