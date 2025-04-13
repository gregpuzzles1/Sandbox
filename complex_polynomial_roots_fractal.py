import math
import random
import time
from PIL import Image

imgx, imgy = 512, 512
image = Image.new("RGB", (imgx, imgy))
xa, xb = -2.0, 2.0
ya, yb = -2.0, 2.0

nmax = 18
pmax = 20000
maxIt = 1000
eps = 1e-7

def polynomial(z, coefficients):
    t = complex(0, 0)
    for c in coefficients:
        t = t * z + c
    return t

def durand_kerner(coefficients):
    n = len(coefficients) - 1
    roots = [complex(random.random(), random.random()) for _ in range(n)]
    roots_new = roots[:]
    it = 0

    while it < maxIt:
        converged = True
        for k in range(n):
            denominator = complex(1, 0)
            for j in range(n):
                if j != k:
                    diff = roots[k] - roots[j]
                    if diff == 0:
                        diff = complex(1e-8, 1e-8)  # Prevent division by zero
                    denominator *= diff
            correction = polynomial(roots[k], coefficients) / denominator
            roots_new[k] = roots[k] - correction
            if abs(correction) > eps:
                converged = False

        roots = roots_new[:]
        it += 1
        if converged:
            break

    return roots, it

start_time = time.time()
for _ in range(pmax):
    pd = random.randint(2, nmax)
    coefficients = [complex(random.choice([-1, 1]), 0) for _ in range(pd)] + [complex(1, 0)]

    roots, iterations = durand_kerner(coefficients)

    for root in roots:
        if math.isnan(root.real) or math.isnan(root.imag) or math.isinf(root.real) or math.isinf(root.imag):
            continue  # Skip bad roots

        kx = int((imgx - 1) * (root.real - xa) / (xb - xa))
        ky = int((imgy - 1) * (root.imag - ya) / (yb - ya))
        if 0 <= kx < imgx and 0 <= ky < imgy:
            color = (
                (iterations % 8) * 32,
                (iterations % 4) * 64,
                (iterations % 16) * 16
            )
            image.putpixel((kx, ky), color)

image.save("ComplexPolynomialRootsFractal.png", "PNG")
print("Duration in seconds:", int(time.time() - start_time))
