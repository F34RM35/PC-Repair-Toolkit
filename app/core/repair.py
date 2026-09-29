from enum import Enum
from dataclasses import dataclass, field
from typing import Any, Callable
from datetime import datetime


class RepairRisk(Enum):
    READ_ONLY = "READ_ONLY"
    SAFE = "SAFE"
    ELEVATED = "ELEVATED"
    DESTRUCTIVE = "DESTRUCTIVE"


class RepairStatus(Enum):
    AVAILABLE = "AVAILABLE"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CANCELLED = "CANCELLED"


@dataclass
class RepairAction:
    name: str
    description: str
    risk: RepairRisk
    function: Callable[[], Any]


@dataclass
class RepairResult:
    name: str
    status: RepairStatus
    message: str = ""
    data: Any = None
    error: str | None = None
    risk: RepairRisk | None = None
    started_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(timespec="seconds")
    )
    completed_at: str | None = None
    duration_seconds: float | None = None