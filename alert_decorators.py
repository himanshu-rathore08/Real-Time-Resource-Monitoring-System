def alert_if_exceeds(threshold, resource_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if value is not None and value > threshold:
                return value, f"{resource_name} exceeded threshold: {value}%"
            return value, None
        return wrapper
    return decorator
