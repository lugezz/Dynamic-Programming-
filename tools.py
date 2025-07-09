from datetime import datetime


def timed_step(label, func, *args, **kwargs):
    start = datetime.now()
    print(f"{label}: ", end='', flush=True)
    result = func(*args, **kwargs)
    end = datetime.now()
    step_time = end - start
    print(f"{result}. Done in {step_time.total_seconds() * 1000:.6f} milliseconds")
    return result
