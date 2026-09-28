from enum import Enum
from dataclasses import dataclass
from typing import Any, Callable


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