# Kelvin logic layer
from tfif_core import compute_IV

def simulate_thermal_energy(depth, harmony, utility, compression):
    iv = compute_IV(depth, harmony, utility)
    return iv / compression
