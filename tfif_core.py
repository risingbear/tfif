# tfif_core.py — Core TFIF Recursion, Phase IV Score, and Harmonic Validation

def recursive_function(P, n, depth=0, max_depth=9):
    """
    TFIF-style recursive decomposition: 
    R(P, n) = f(R(P1, n-1), R(P2, n-1), R(P3, n-1))
    """
    if n <= 0 or depth >= max_depth:
        return P
    return (
        recursive_function(P + 1, n - 1, depth + 1, max_depth) +
        recursive_function(P + 2, n - 1, depth + 1, max_depth) +
        recursive_function(P + 3, n - 1, depth + 1, max_depth)
    )

def compute_IV(depth, harmony, utility):
    """
    Computes the Intelligence Value of a system
    IV = D x H x U
    """
    return depth * harmony * utility

def compute_energy(iv, compression):
    """
    Computes symbolic energy output
    E = IV / C
    """
    if compression == 0:
        return float('inf')
    return iv / compression

def harmonic_alignment(value):
    """
    Checks alignment to harmonic 3/6/9 principles.
    Returns harmonic gate if aligned.
    """
    if value % 9 == 0:
        return 'Gate 9'
    elif value % 6 == 0:
        return 'Gate 6'
    elif value % 3 == 0:
        return 'Gate 3'
    return 'No harmonic lock'

# Example demo
if __name__ == "__main__":
    IV = compute_IV(depth=6, harmony=3.69, utility=0.95)
    E = compute_energy(IV, compression=1.2)
    print(f"IV = {IV:.3f}, Energy = {E:.3f}, Harmonic = {harmonic_alignment(int(IV))}")
