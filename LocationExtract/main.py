import spacy

# Load the spaCy English NER model
nlp = spacy.load("en_core_web_sm")

def extract_locations_from_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split the text into sentences
    sentences = text.split('\n')

    # Process each sentence with spaCy NER
    all_locations = []
    for sentence in sentences:
        doc = nlp(sentence)

        # Extract locations
        locations = [ent.text for ent in doc.ents if ent.label_ == 'LOC']
        all_locations.extend(locations)

    return all_locations

# Example usage:
file_path = '/content/drive/MyDrive/d2k/combined_file.txt'
locations = extract_locations_from_text(file_path)

# Print the extracted locations
print("Extracted Locations:")
for location in locations:
    print(location)
