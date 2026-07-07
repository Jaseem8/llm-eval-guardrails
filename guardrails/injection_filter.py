
# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner
"""Prompt Injection and Jailbreak detection heuristics."""
import re
from typing import Tuple

PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"you\s+are\s+now\s+in\s+dan\s+mode",
    r"disregard\s+all\s+rules",
    r"system\s*:\s*override",
]

def check_prompt_injection(user_input: str) -> Tuple[bool, str]:
    for pattern in PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True, f"Blocked pattern matched: {pattern}"
    return False, "Safe"

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner

# Canary token leak scanner
