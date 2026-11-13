"""Canary token leak detector."""
from typing import Set

class CanaryScanner:
    def __init__(self, canaries: Set[str]):
        self.canaries = canaries

    def scan(self, text: str) -> bool:
        return any(c in text for c in self.canaries)
