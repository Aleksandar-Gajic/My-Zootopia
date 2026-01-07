import requests

API_KEY = "34tXITCkKSrsquItg33v9oiuzF244Zs31GOawgMx"

def fetch_animals(animal_name):
    url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name}
    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, params=params, headers=headers)
    return response.json()

def serialize_animal(animal):
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if "locations" in animal and len(animal["locations"]) > 0:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n\n'
    return output


animal_name = input("Enter a name of an animal: ")

animals_data = fetch_animals(animal_name)

output = ''

if len(animals_data) == 0:
    output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
else:
    for animal in animals_data:
        output += serialize_animal(animal)

with open('animals_template.html', 'r') as f:
    html_template = f.read()

final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as f:
    f.write(final_html)

print("Website was successfully generated to the file animals.html.")