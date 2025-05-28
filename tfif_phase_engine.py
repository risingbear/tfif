# tfif_phase_engine.py — Harmonic Gate Detection + Symbolic Output

def check_phase_gate(value, return_symbol=False):
    """
    Checks whether the input number triggers a TFIF harmonic phase gate.
    Also returns symbolic glyphs if enabled.

    Parameters:
    - value (int or float): The number to check
    - return_symbol (bool): Whether to return a symbolic glyph instead of text

    Returns:
    - str: Phase gate result or symbolic glyph
    """
    if value % 9 == 0:
        return '°|' if return_symbol else 'Gate 9 triggered'
    elif value % 6 == 0:
        return '°^' if return_symbol else 'Gate 6 triggered'
    elif value % 3 == 0:
        return '°' if return_symbol else 'Gate 3 triggered'
    else:
        return '⌀' if return_symbol else 'No gate'

def phase_resonance_score(value):
    """
    Calculates harmonic resonance score (0 to 1) for a given input.
    Measures closeness to 3/6/9 structure.

    Returns:
    - float: Resonance score
    """
    distance = min(
        abs(value % 3),
        abs(value % 6),
        abs(value % 9)
    )
    return 1.0 - (distance / 9)

# Example usage
if __name__ == "__main__":
    for v in [27, 18, 12, 10]:
        gate = check_phase_gate(v, return_symbol=True)
        score = round(phase_resonance_score(v), 3)
        print(f"{v}: {gate} (Resonance: {score})")
