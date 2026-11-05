import os
import tempfile
from pathlib import Path


def _get_windows_directory():
    """
    Return the Windows installation directory.
    """

    return Path(
        os.environ.get(
            "WINDIR",
            r"C:\Windows"
        )
    )


def _get_windows_update_cache():
    """
    Return the Windows Update download cache directory.
    """

    return (
        _get_windows_directory()
        / "SoftwareDistribution"
        / "Download"
    )


def _scan_directory(directory):
    """
    Read-only scan of a directory.

    Returns:
        file_count
        total_bytes
    """

    file_count = 0
    total_bytes = 0

    if not directory.exists():
        return 0, 0

    for root, directories, files in os.walk(directory):

        for filename in files:

            file_path = Path(root) / filename

            try:

                total_bytes += file_path.stat().st_size
                file_count += 1

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):
                continue

    return file_count, total_bytes


def analyze_temp_files():
    """
    Analyze the current user's temporary files.

    READ_ONLY:
    No files are modified or deleted.
    """

    temp_directory = Path(
        tempfile.gettempdir()
    )

    file_count, total_bytes = _scan_directory(
        temp_directory
    )

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
    """
    Delete files from the current user's
    temporary directory.

    Files that are locked, missing, or
    inaccessible are skipped.
    """

    temp_directory = Path(
        tempfile.gettempdir()
    )

    files_found = 0
    files_deleted = 0
    files_skipped = 0
    directories_removed = 0
    deleted_bytes = 0

    for root, directories, files in os.walk(
        temp_directory,
        topdown=False
    ):

        for filename in files:

            file_path = Path(root) / filename

            files_found += 1

            try:

                file_size = file_path.stat().st_size

                file_path.unlink()

                files_deleted += 1
                deleted_bytes += file_size

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):

                files_skipped += 1

        for directory in directories:

            directory_path = Path(root) / directory

            try:

                directory_path.rmdir()

                directories_removed += 1

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):
                continue

    deleted_mb = deleted_bytes / (
        1024 * 1024
    )

    return {
        "directory": str(temp_directory),
        "files_found": files_found,
        "files_deleted": files_deleted,
        "files_skipped": files_skipped,
        "directories_removed": directories_removed,
        "deleted_mb": round(
            deleted_mb,
            2
        ),
    }


def analyze_disk_cleanup():
    """
    Analyze common Windows cleanup locations.

    READ_ONLY:
    No files are modified or deleted.
    """

    windows_directory = _get_windows_directory()

    user_temp = Path(
        tempfile.gettempdir()
    )

    windows_temp = (
        windows_directory / "Temp"
    )

    update_cache = _get_windows_update_cache()

    cleanup_locations = [
        (
            "User Temp",
            user_temp,
        ),
        (
            "Windows Temp",
            windows_temp,
        ),
        (
            "Windows Update Cache",
            update_cache,
        ),
    ]

    locations = []

    total_files = 0
    total_bytes = 0

    for name, directory in cleanup_locations:

        file_count, size_bytes = _scan_directory(
            directory
        )

        exists = directory.exists()

        size_mb = size_bytes / (
            1024 * 1024
        )

        locations.append(
            {
                "name": name,
                "directory": str(directory),
                "exists": exists,
                "file_count": file_count,
                "size_mb": round(
                    size_mb,
                    2
                ),
            }
        )

        total_files += file_count
        total_bytes += size_bytes

    return {
        "locations": locations,
        "total_files": total_files,
        "potential_cleanup_mb": round(
            total_bytes / (
                1024 * 1024
            ),
            2
        ),
    }


def analyze_windows_update_cache():
    """
    Analyze the Windows Update download cache.

    READ_ONLY:
    No files are modified or deleted.
    """

    update_cache = _get_windows_update_cache()

    if not update_cache.exists():

        return {
            "directory": str(update_cache),
            "exists": False,
            "files": 0,
            "size_mb": 0.0,
        }

    files, total_bytes = _scan_directory(
        update_cache
    )

    return {
        "directory": str(update_cache),
        "exists": True,
        "files": files,
        "size_mb": round(
            total_bytes / (
                1024 * 1024
            ),
            2
        ),
    }


def clean_windows_update_cache():
    """
    Clean the Windows Update download cache.

    The SoftwareDistribution directory itself
    is preserved.

    Files that are locked, missing, or
    inaccessible are skipped.

    The directory is rescanned after cleanup
    so the result contains verification data.
    """

    update_cache = _get_windows_update_cache()

    if not update_cache.exists():

        return {
            "directory": str(update_cache),
            "exists": False,
            "files_found": 0,
            "files_deleted": 0,
            "files_skipped": 0,
            "deleted_mb": 0.0,
            "remaining_files": 0,
            "remaining_mb": 0.0,
        }

    files_found = 0
    files_deleted = 0
    files_skipped = 0
    deleted_bytes = 0

    for root, directories, files in os.walk(
        update_cache
    ):

        for filename in files:

            file_path = Path(root) / filename

            files_found += 1

            try:

                file_size = file_path.stat().st_size

                file_path.unlink()

                files_deleted += 1
                deleted_bytes += file_size

            except (
                PermissionError,
                FileNotFoundError,
                OSError,
            ):

                files_skipped += 1

    deleted_mb = deleted_bytes / (
        1024 * 1024
    )

    remaining_files, remaining_bytes = _scan_directory(
        update_cache
    )

    remaining_mb = remaining_bytes / (
        1024 * 1024
    )

    return {
        "directory": str(update_cache),
        "exists": True,
        "files_found": files_found,
        "files_deleted": files_deleted,
        "files_skipped": files_skipped,
        "deleted_mb": round(
            deleted_mb,
            2
        ),
        "remaining_files": remaining_files,
        "remaining_mb": round(
            remaining_mb,
            2
        ),
    }