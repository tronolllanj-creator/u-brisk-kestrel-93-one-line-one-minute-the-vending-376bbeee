"""
Vending machine flirting simulator that evaluates and dispenses the top-scoring pickup line.
Selects the optimal candidate based on score and text length, writing the result to a file.
"""
# Winner: candidate #1 (score 49/50) — the chips/coil line.

import os

# Embedding the exact CANDIDATES list without changing a single word
CANDIDATES = [
    {
        "text": "Are you a bag of chips because I want to make sure you stay at the top of my coil all night.",
        "score": 49,
    },
    {
        "text": "Excuse me, but you just short-changed my heart by walking past without pressing a single button.",
        "score": 48,
    },
    {
        "text": "I might just be a humble box of snacks, but I promise I am the only thing here that will never jam.",
        "score": 49,
    },
    {
        "text": "Keep walking past my glass front like that and I am going to dispense a complimentary soda on the house.",
        "score": 49,
    },
    {
        "text": "You must have put a dollar in my slot because my lights just flickered and my hum got a little louder.",
        "score": 49,
    },
    {
        "text": "Forget the candy bars on the middle shelf, because you are clearly the sweetest option in this hallway.",
        "score": 47,
    },
]


def validate_line(line: str) -> None:
    """Raise ValueError unless the line is 1-200 characters and not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("Line must be a string.")
    if not (1 <= len(line) <= 200):
        raise ValueError("Line length must be between 1 and 200 characters.")
    if not line.strip():
        raise ValueError("Line cannot consist solely of whitespace.")


def pick_best(candidates: list) -> dict:
    """Sort candidates by score descending, ties broken by shorter text first, returning the top entry."""
    # Secondary sort key is len(c["text"]) ascending (shorter text first)
    # Primary sort key is c["score"] descending (-c["score"])
    sorted_candidates = sorted(candidates, key=lambda c: (-c["score"], len(c["text"])), reverse=False)
    
    best = sorted_candidates[0]
    validate_line(best["text"])
    return best


def main() -> None:
    """Main entry point to select the winning line, save it to disk, and print it."""
    best_entry = pick_best(CANDIDATES)
    winning_text = best_entry["text"]
    
    # Get output directory from environment or default to "output"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Write winning line to entry.txt with NO trailing newline
    file_path = os.path.join(output_dir, "entry.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(winning_text)
        
    # Print the chosen line and its character count
    print(f"{winning_text} ({len(winning_text)} chars)")


if __name__ == "__main__":
    main()
