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


def clean_temp_files():
    temp_directory = Path(
        tempfile.gettempdir()
    )

    files_found = 0
    files_deleted = 0
    bytes_deleted = 0
    files_skipped = 0
    directories_removed = 0

    for root, directories, files in os.walk(
        temp_directory,
        topdown=False
    ):

        root_path = Path(root)

        for filename in files:

            file_path = root_path / filename
            files_found += 1

            try:
                file_size = file_path.stat().st_size

                file_path.unlink()

                files_deleted += 1
                bytes_deleted += file_size

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):
                files_skipped += 1

        for directory in directories:

            directory_path = root_path / directory

            try:
                directory_path.rmdir()
                directories_removed += 1

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):
                continue

    return {
        "directory": str(temp_directory),
        "files_found": files_found,
        "files_deleted": files_deleted,
        "files_skipped": files_skipped,
        "directories_removed": directories_removed,
        "deleted_mb": round(
            bytes_deleted / (1024 * 1024),
            2
        ),
    }