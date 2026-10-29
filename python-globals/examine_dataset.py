import json
from pathlib import Path

# Global (or "module-level" variable)
DATA_FILE = Path("pets-will.json")


def load_pet_data() -> dict[str, dict[str, str | float]]:
    """Load pet data from a JSON file."""
    # Global variable used inside function.
    # Functions should be self-sufficient!
    # Note that the same principle applies to hard-coded values in functions too.
    print(f"Loading {DATA_FILE}")

    with DATA_FILE.open("r") as f:
        data = json.load(f)

    print(f"\tSuccessfully loaded {len(data)} records!")
    return data


# No main block, resulting in loose code being run when the script is imported.
data = load_pet_data()

print("Here is the data:\n", data)
