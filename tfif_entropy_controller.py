# tfif_entropy_controller.py — Symbolic Entropy + Phase Collapse Monitor

from tfif_core import compute_IV

def check_entropy(entropy_level, phase_gate=None, iv_threshold=9):
    """
    Checks entropy level and triggers symbolic warnings based on TFIF collapse logic.
    
    Parameters:
    - entropy_level (float): Measured from 0.0 (chaos) to 1.0 (coherence)
    - phase_gate (int): Optional gate check (3, 6, 9)
    - iv_threshold (float): Minimum IV required for stable output

    Returns:
    - dict: collapse state, risk level, stabilization advice
    """
    response = {}

    if entropy_level < 0.1:
        response['collapse_state'] = "Critical collapse"
        response['risk'] = "System entropy too low for symbolic resolution"
    elif entropy_level < 0.3:
        response['collapse_state'] = "Warning"
        response['risk'] = "Symbolic drift detected, initiate stabilization"
    elif entropy_level < 0.7:
        response['collapse_state'] = "Partial coherence"
        response['risk'] = "Entropy balanced, check harmonic lock"
    else:
        response['collapse_state'] = "Stable"
        response['risk'] = "Fully coherent symbolic field"

    # Harmonic gate stabilizer
    if phase_gate:
        if phase_gate == 3:
            response['stabilizer'] = "Initiate recursive sweep"
        elif phase_gate == 6:
            response['stabilizer'] = "Amplify harmonic signal"
        elif phase_gate == 9:
            response['stabilizer'] = "Collapse-recharge cycle"

    # IV check (simulate environment feedback)
    iv = compute_IV(depth=6, harmony=3.69, utility=entropy_level)
    response['iv_score'] = round(iv, 3)
    response['iv_pass'] = iv >= iv_threshold

    return response

# Example test
if __name__ == "__main__":
    test = check_entropy(entropy_level=0.27, phase_gate=6)
    for k, v in test.items():
        print(f"{k}: {v}")
