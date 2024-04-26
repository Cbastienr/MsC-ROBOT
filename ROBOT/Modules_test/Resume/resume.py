import spacy

def summarize_doctor_text(doctor_text):
    # Charger le modèle de langue français
    nlp = spacy.load("fr_core_news_sm")

    # Analyser le texte du médecin
    doc = nlp(doctor_text)

    # Récupérer les phrases du texte du médecin
    doctor_sentences = [sent.text.strip() for sent in doc.sents]

    # Résumer le texte du médecin en extrayant la dernière phrase
    if doctor_sentences:
        return doctor_sentences[-1]
    else:
        return ""

def save_doctor_summary(summary_text, file_path):
    # Enregistrer le résumé dans un fichier
    with open(file_path, "w") as file:
        file.write(summary_text)