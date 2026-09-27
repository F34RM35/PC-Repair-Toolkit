import psutil


def bytes_to_gb(value):
    return round(value / (1024 ** 3), 2)


def get_storage_info():
    drives = []

    partitions = psutil.disk_partitions(all=False)

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)

            drives.append({
                "device": partition.device,
                "mountpoint": partition.mountpoint,
                "filesystem": partition.fstype,
                "total_gb": bytes_to_gb(usage.total),
                "used_gb": bytes_to_gb(usage.used),
                "free_gb": bytes_to_gb(usage.free),
                "usage_percent": usage.percent,
            })

        except (PermissionError, OSError):
            continue

    return drives