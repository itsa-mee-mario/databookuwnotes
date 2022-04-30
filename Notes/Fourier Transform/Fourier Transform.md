# Fourier Transform
is just the fourier series as L goes to infinity.

$$\hat{f}(\omega) = F(f(x)) = \int_{-\infty}^{\infty} f(x)e^{-i\omega x} dx$$
$\hat{f}(\omega)$ contatains a continum of fourier coeeficients instead of discrete $C_k$ values like in the Fourier Series

The inverse Fourier Transform is defined as
$$f(x)= F^{-1}(\hat f (\omega)) =\frac{1}{2\pi} \int_{-\infty }^{\infty} \hat f(\omega) e^{i \omega x} d \omega$$ 
# Derivatives in Fourier Transform
$$F(D(f(x))) = \int_{-\infty}^{\infty} D(f(x))e^{-i\omega x} dx \\ = i \omega F(f(x)) $$
Derivative in the Fourier Domain is sometimes much easier to compute. it might be more accurate. (Specteral Derivative) 


# Convolution Integrals and Fourier transform

Convolution Integral:
![[Pasted image 20220426162727.png]]

FT simplified the convolution into a product of the FT of two functions.

$$F(f*g) = F(f)F(g) = \hat f \hat g$$

# Parseval's Theorem
Energy in FT of a function is equal to a factor of 2 pi
$$ \int |\hat f (x)|^{2}dx = 2 \pi \int |f(x)|^{2} dx$$
This means that if we ignore smaller Fourier Coefficients (then the first integral doesnt change much), we negligibley degrade our approximation of the function

