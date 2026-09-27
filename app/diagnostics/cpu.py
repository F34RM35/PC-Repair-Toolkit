import psutil


def get_cpu_info():
    frequency = psutil.cpu_freq()

    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "usage_percent": psutil.cpu_percent(interval=1),
        "current_frequency_mhz": round(frequency.current, 2) if frequency else None,
        "max_frequency_mhz": round(frequency.max, 2) if frequency else None,
    }