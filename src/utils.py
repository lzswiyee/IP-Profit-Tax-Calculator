def validate(value):
    try:
        val = float(value)
        return val if val >= 0 else None
    except (ValueError, TypeError):
        return None

def normalize(value):
    return max(0.0, float(value))

