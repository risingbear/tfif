# rwg_engine.py — Recursive Witness Geometry (RWG v1.0)
from tfif_core import recursive_function
import math

def fibonacci(n):
    """Returns n-th Fibonacci number."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def retention_spiral(seed, cycles=4):
    """
    Generates a retention spiral using Fibonacci logic.
    Each frame represents symbolic memory stored in spin.
    """
    spiral = []
    for i in range(cycles):
        pulse = fibonacci(i + 5)  # Start from Fibonacci index 5
        collapse = recursive_function(seed, i)
        spiral.append({
            "frame": i,
            "pulse": pulse,
            "collapse_value": collapse,
            "glyph": "₃" if collapse % 3 == 0 else "⍉"
        })
    return spiral

def generate_memory_glyph(seed):
    """
    Encodes symbolic memory through recursive echo loops.
    Returns retention spiral and symbolic collapse pattern.
    """
    spiral = retention_spiral(seed)
    echo_pattern = "".join([s['glyph'] for s in spiral])
    return {
        "seed": seed,
        "spiral_frames": spiral,
        "echo_pattern": echo_pattern,
        "stability": "Stable" if echo_pattern.count("₃") >= 2 else "Unstable"
    }

# Example usage
if __name__ == "__main__":
    result = generate_memory_glyph(9)
    for k, v in result.items():
        print(f"{k}: {v}")
