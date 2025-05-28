# Tracks symbolic entropy and phase coherence
from tfif_core import compute_IV

def check_entropy(entropy_level):
    if entropy_level < 0.3:
        return 'Collapse risk'
    return 'Stable'
