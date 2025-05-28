# Handles 369 phase detection

def check_phase_gate(value):
    if value % 9 == 0:
        return 'Gate 9 triggered'
    elif value % 6 == 0:
        return 'Gate 6 triggered'
    elif value % 3 == 0:
        return 'Gate 3 triggered'
    return 'No gate'
