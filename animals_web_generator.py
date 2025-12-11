import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''

for animal in animals_data:

    # Name
    if "name" in animal:
        output += f"Name: {animal['name']}\n"

    # Diet
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"

    # First location
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f"Location: {animal['locations'][0]}\n"

    # Type
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"

    output += "\n"

with open('animals_template.html', 'r') as f:
    html_template = f.read()

final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as f:
    f.write(final_html)

print("HTML file 'animals.html' generated successfully!")