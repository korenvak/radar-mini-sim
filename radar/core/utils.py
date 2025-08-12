import random

def lerp(x0, x1, a):
    """Linear interpolation: x0 + a*(x1-x0)"""
    return x0 + a*(x1-x0)

def rng(seed):
    """Deterministic RNG object, independent of global state"""
    return random.Random(seed)

def solve_2x2(A,b):
    """Solve 2x2 linear system A*x = b using Cramer's rule."""
    a, b_val = A[0]  # First row of A
    c, d = A[1]  # Second row of A
    e, f = b # Two-dimensional vector
    det = a * d - b_val * c
    if abs(det) < 1e-12:
        raise ValueError("singular or ill-conditioned 2x2 matrix")
    x = (e * d - b_val * f) / det
    y = (a * f - e * c) / det

    return x, y


