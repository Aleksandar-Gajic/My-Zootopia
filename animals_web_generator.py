import data_fetcher
import os

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


def generate_website(animal_name):
    animals_data = data_fetcher.fetch_data(animal_name)

    if len(animals_data) == 0:
        output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    else:
        output = ""
        for animal in animals_data:
            output += serialize_animal(animal)

    # Load template
    template_path = os.path.join(os.path.dirname(__file__), 'animals_template.html')
    with open(template_path, 'r') as f:
        html_template = f.read()

    # Safe replace: placeholder nikada ne ostaje
    if '__REPLACE_ANIMALS_INFO__' in html_template:
        final_html = html_template.replace('__REPLACE_ANIMALS_INFO__', output)
    else:
        final_html = html_template + "\n" + output  # fallback

    # Write output
    output_path = os.path.join(os.path.dirname(__file__), 'animals.html')
    with open(output_path, 'w') as f:
        f.write(final_html)

    print(f"Website was successfully generated to the file {output_path}")


if __name__ == "__main__":
    animal_name = input("Please enter an animal: ")
    generate_website(animal_name)