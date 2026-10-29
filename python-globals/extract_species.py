import json
from pathlib import Path


def extract_pets_of_species(
    data: dict[str, dict[str, str | float]],
    species: list[str],
) -> dict[str, dict[str, str | float]]:
    """Extract records from the `data` that match the species given."""
    return {
        pet_name: pet_information
        for pet_name, pet_information in data.items()
        if pet_information["species"] in species
    }


if __name__ == "__main__":
    # Ideally, we would read this value from the command-line too.
    # But at least it's not a global variable!
    data_set = Path("pets-david.json")

    # This code is repeated from `examine_dataset.py`.
    # We should import our load_pet_data function and use that instead.
    print(f"Loading {data_set}")

    with data_set.open("r") as f:
        data = json.load(f)

    print(f"\tSuccessfully loaded {len(data)} records!")
    # End of repeated code

    species_of_interest = ["bird", "dog"]

    filtered_data = extract_pets_of_species(data, species_of_interest)
    print("Data was filtered to:\n", filtered_data)
