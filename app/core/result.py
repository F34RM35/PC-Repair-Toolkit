from enum import Enum
from dataclasses import dataclass
from typing import Any


class DiagnosticStatus(Enum):
    PASS = "PASS"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


@dataclass
class DiagnosticResult:
    name: str
    status: DiagnosticStatus
    data: Any = None
    message: str = ""
    error: str | None = None