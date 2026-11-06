
# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections
"""Hallucination detection via source attribution scoring."""
from typing import Set

def tokenize(text: str) -> Set[str]:
    return set(text.lower().replace(".", " ").replace(",", " ").split())

def compute_grounding_score(generated_text: str, source_context: str) -> float:
    gen_tokens = tokenize(generated_text)
    src_tokens = tokenize(source_context)
    if not gen_tokens:
        return 1.0
    overlap = gen_tokens.intersection(src_tokens)
    return len(overlap) / len(gen_tokens)

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections

# Vectorized token intersections
