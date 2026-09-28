import os
import tempfile
from pathlib import Path


def analyze_temp_files():

    temp_directory = Path(
        tempfile.gettempdir()
    )

    file_count = 0
    total_bytes = 0

    for root, directories, files in os.walk(
        temp_directory
    ):

        for filename in files:

            try:

                file_path = Path(root) / filename

                total_bytes += file_path.stat().st_size

                file_count += 1

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):
                continue

    total_mb = total_bytes / (
        1024 * 1024
    )

    return {
        "directory": str(temp_directory),
        "file_count": file_count,
        "total_mb": round(
            total_mb,
            2
        ),
    }