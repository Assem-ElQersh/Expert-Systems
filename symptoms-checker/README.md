# Symptoms Checker — Expert System

A rule-based medical triage expert system that analyses a user's reported symptoms and returns a ranked list of possible conditions with confidence scores.

## Architecture

| File | Role |
|---|---|
| `knowledge_base.py` | Domain knowledge — 12 rules covering flu, cold, COVID-19, allergies, strep, pneumonia, and more |
| `inference_engine.py` | Rules Engine — weighted forward-chaining that scores and ranks every rule against the active symptom set |
| `app.py` | User Interface — Streamlit web application |

## How It Works

1. The user selects symptoms from a grouped checklist in the sidebar.
2. The **Inference Engine** evaluates all rules in the **Knowledge Base** using weighted scoring.
3. Each rule's confidence is computed as: `(matched_conditions / total_conditions) × weight`, normalised to a percentage.
4. Results above the configurable threshold are displayed in ranked order with confidence progress bars.

## Running the App

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

## Knowledge Base Coverage

| Condition | Key Distinguishing Symptoms |
|---|---|
| Influenza (Flu) | Fever, cough, fatigue, muscle aches, chills |
| Common Cold | Sneezing, runny nose, sore throat, congestion |
| COVID-19 | Dry cough, loss of taste/smell, shortness of breath |
| Seasonal Allergies | Sneezing, itchy/watery eyes, runny nose, no fever |
| Strep Throat | Sore throat + fever, absence of cold symptoms |
| Pneumonia | Productive cough, shortness of breath, chest tightness |
| Asthma Exacerbation | Wheezing, chest tightness, shortness of breath |
| Migraine | Headache, nausea, no fever |
| Gastroenteritis | Nausea, diarrhea, fever, fatigue |
| Viral Exanthem | Skin rash, fever, muscle aches |
| Malaria / Dengue | High fever, severe headache, chills, travel history |
| Mononucleosis | Sore throat, extreme fatigue, fever, headache |

## Disclaimer

This system is for **educational purposes only** and does not constitute medical advice. Always consult a qualified healthcare professional for diagnosis and treatment.
