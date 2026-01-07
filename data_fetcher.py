import requests

API_KEY = "34tXITCkKSrsquItg33v9oiuzF244Zs31GOawgMx"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': { ... },
        'locations': [ ... ],
        'characteristics': { ... }
    }
    """
    url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return data
        else:
            return []
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []