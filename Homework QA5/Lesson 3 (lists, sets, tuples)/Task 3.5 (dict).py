from typing import Dict


def create_film_dict() -> Dict[str, object]:
    """
    Create a dictionary containing information about a favorite film.

    :returns:
    film(dict): A dictionary with keys 'title', 'director', 'year', 'budget', 'main actor', 'slogan', where each
    key has a value containing information about the corresponding attribute of the film.
    """

    # Create a dictionary with the information about the film
    film = {
        'title': 'Edge of Tomorrow',
        'director': 'Unknown',
        'year': 2013,
        'budget': 100500,
        'main actor': 'Tom Cruz',
        'slogan': 'Live. Die. Repeat.'
    }
    return film


# Call the function to create the movie dictionary
film = create_film_dict()

# Print the keys of the dictionary
print(f"\nKeys of the dictionary: {', '.join(film.keys())}\n")

# Print the values of the dictionary
print(f"\nValues of the dictionary: {', '.join(str(x) for x in film.values())}\n")

# Print the key-value pair of the dictionary
print("\nKey-value pairs of the dictionary:")
for key, value in film.items():
    print(f"{key.title()}: {value}")
