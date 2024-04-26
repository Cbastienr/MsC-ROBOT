import spacy
import os

def segment_text_with_nlp(text):
    # Charger le modèle de langue français
    nlp = spacy.load("fr_core_news_sm")

    # Analyser le texte
    doc = nlp(text)

    # Segmenter le texte en fonction des balises "Patient:" et "Médecin:"
    patient_text = ""
    doctor_text = ""
    current_speaker = None

    for token in doc:
        print(f"Token : {token.text}, Entité : {token.ent_type_}, Pos : {token.pos_}")

        if token.text.strip() == "Patient:":
            current_speaker = "Patient"
        elif token.text.strip() == "Médecin:":
            current_speaker = "Médecin"
        elif current_speaker == "Patient":
            patient_text += token.text + " "
        elif current_speaker == "Médecin":
            doctor_text += token.text + " "

    return patient_text.strip(), doctor_text.strip()

def segment_text_from_file(file_path):
    # Lire le contenu du fichier
    with open(file_path, "r") as file:
        text = file.read()

    # Appeler la fonction segment_text_with_nlp
    return segment_text_with_nlp(text)

# Utilisation :
patient_text, doctor_text = segment_text_from_file("transcription.txt")
print("Texte du patient:")
print(patient_text)
print("\nTexte du médecin:")
print(doctor_text)