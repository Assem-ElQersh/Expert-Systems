"""
Knowledge Base for the Symptoms Checker Expert System.

Each Rule encodes a medical condition with:
  - conditions : dict mapping symptom name → expected boolean value
  - conclusion : the condition name (string)
  - description: brief plain-language explanation
  - advice     : recommended action for the user
  - weight     : importance / severity scalar used by the inference engine
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Rule:
    conditions: Dict[str, bool]
    conclusion: str
    description: str
    advice: str
    weight: float


# Master list of all available symptoms shown in the UI
ALL_SYMPTOMS: list[str] = [
    "Fever",
    "High Fever (>39°C)",
    "Cough",
    "Dry Cough",
    "Productive Cough",
    "Fatigue",
    "Sneezing",
    "Runny Nose",
    "Nasal Congestion",
    "Sore Throat",
    "Headache",
    "Muscle Aches",
    "Shortness of Breath",
    "Loss of Taste/Smell",
    "Chest Tightness",
    "Itchy / Watery Eyes",
    "Skin Rash",
    "Nausea / Vomiting",
    "Diarrhea",
    "Chills",
]

RULES: list[Rule] = [
    Rule(
        conditions={
            "Fever": True,
            "Cough": True,
            "Fatigue": True,
            "Muscle Aches": True,
            "Chills": True,
        },
        conclusion="Influenza (Flu)",
        description=(
            "Influenza is a contagious viral infection that attacks the respiratory "
            "system. It typically comes on suddenly and can cause severe illness."
        ),
        advice=(
            "Rest, stay hydrated, and take over-the-counter fever reducers. "
            "See a doctor if symptoms worsen or you are in a high-risk group."
        ),
        weight=5,
    ),
    Rule(
        conditions={
            "Sneezing": True,
            "Runny Nose": True,
            "Sore Throat": True,
            "Nasal Congestion": True,
        },
        conclusion="Common Cold",
        description=(
            "The common cold is a viral infection of the upper respiratory tract. "
            "It is usually mild and resolves within 7–10 days."
        ),
        advice=(
            "Rest, drink fluids, and use saline nasal sprays. "
            "Symptoms are self-limiting; antibiotics are not effective."
        ),
        weight=4,
    ),
    Rule(
        conditions={
            "Fever": True,
            "Dry Cough": True,
            "Fatigue": True,
            "Loss of Taste/Smell": True,
            "Shortness of Breath": True,
        },
        conclusion="COVID-19 (Possible)",
        description=(
            "COVID-19 is caused by the SARS-CoV-2 coronavirus. Key distinguishing "
            "symptoms include loss of taste/smell and shortness of breath."
        ),
        advice=(
            "Isolate yourself, wear a mask, and get tested as soon as possible. "
            "Seek emergency care if you experience severe breathing difficulty."
        ),
        weight=5,
    ),
    Rule(
        conditions={
            "Sneezing": True,
            "Runny Nose": True,
            "Itchy / Watery Eyes": True,
            "Nasal Congestion": True,
        },
        conclusion="Seasonal Allergies",
        description=(
            "Allergic rhinitis (hay fever) is triggered by airborne allergens such as "
            "pollen, dust, or pet dander, causing inflammation of the nasal passages."
        ),
        advice=(
            "Try antihistamines or nasal corticosteroid sprays. Limit outdoor exposure "
            "during high pollen count days. Consult an allergist for persistent symptoms."
        ),
        weight=4,
    ),
    Rule(
        conditions={
            "Sore Throat": True,
            "Fever": True,
            "Headache": True,
            "Sneezing": False,
            "Runny Nose": False,
        },
        conclusion="Strep Throat",
        description=(
            "Strep throat is a bacterial infection caused by Group A Streptococcus. "
            "It typically presents without cold symptoms and may include throat patches."
        ),
        advice=(
            "See a doctor for a rapid strep test. If positive, a course of antibiotics "
            "(e.g., penicillin) is required to prevent complications."
        ),
        weight=4,
    ),
    Rule(
        conditions={
            "Cough": True,
            "Productive Cough": True,
            "Fever": True,
            "Shortness of Breath": True,
            "Chest Tightness": True,
        },
        conclusion="Pneumonia (Possible)",
        description=(
            "Pneumonia is an infection that inflames the air sacs in one or both lungs. "
            "It can be caused by bacteria, viruses, or fungi."
        ),
        advice=(
            "Seek medical attention promptly. A chest X-ray and physical examination "
            "are needed for diagnosis. Treatment depends on the underlying cause."
        ),
        weight=5,
    ),
    Rule(
        conditions={
            "Cough": True,
            "Shortness of Breath": True,
            "Chest Tightness": True,
            "Wheezing": True,
        },
        conclusion="Asthma Exacerbation",
        description=(
            "An asthma flare-up involves narrowing of the airways, causing difficulty "
            "breathing, wheezing, and chest tightness."
        ),
        advice=(
            "Use your prescribed rescue inhaler immediately. If symptoms do not improve "
            "within 20 minutes, seek emergency medical care."
        ),
        weight=5,
    ),
    Rule(
        conditions={
            "Headache": True,
            "Nausea / Vomiting": True,
            "Fatigue": True,
            "Fever": False,
        },
        conclusion="Migraine",
        description=(
            "A migraine is a neurological condition causing intense, throbbing headaches "
            "often accompanied by nausea, vomiting, and sensitivity to light or sound."
        ),
        advice=(
            "Rest in a dark, quiet room. Over-the-counter pain relievers or prescription "
            "triptans can help. Identify and avoid personal triggers."
        ),
        weight=3,
    ),
    Rule(
        conditions={
            "Nausea / Vomiting": True,
            "Diarrhea": True,
            "Fatigue": True,
            "Fever": True,
        },
        conclusion="Gastroenteritis (Stomach Flu)",
        description=(
            "Gastroenteritis is inflammation of the stomach and intestines usually caused "
            "by a viral or bacterial infection. It causes rapid fluid loss."
        ),
        advice=(
            "Stay well-hydrated with water or oral rehydration solutions. Avoid solid "
            "foods until vomiting subsides. See a doctor if symptoms last more than 48 hours."
        ),
        weight=4,
    ),
    Rule(
        conditions={
            "Skin Rash": True,
            "Fever": True,
            "Fatigue": True,
            "Muscle Aches": True,
        },
        conclusion="Viral Exanthem / Measles-like Illness",
        description=(
            "A viral exanthem is a widespread rash caused by a viral infection. Several "
            "conditions including measles and rubella present this way."
        ),
        advice=(
            "Consult a doctor promptly, especially if unvaccinated. Isolate to avoid "
            "spreading the infection to others."
        ),
        weight=4,
    ),
    Rule(
        conditions={
            "Fever": True,
            "High Fever (>39°C)": True,
            "Headache": True,
            "Muscle Aches": True,
            "Chills": True,
            "Fatigue": True,
        },
        conclusion="Malaria / Dengue (Possible)",
        description=(
            "High cyclical fevers with severe headache, muscle pain, and chills can "
            "indicate mosquito-borne illnesses such as malaria or dengue fever."
        ),
        advice=(
            "Seek immediate medical evaluation, especially if you have recently traveled "
            "to a tropical region. Blood tests are required for diagnosis."
        ),
        weight=5,
    ),
    Rule(
        conditions={
            "Sore Throat": True,
            "Fatigue": True,
            "Fever": True,
            "Headache": True,
            "Muscle Aches": True,
        },
        conclusion="Mononucleosis (Mono)",
        description=(
            "Infectious mononucleosis ('mono') is caused by the Epstein-Barr virus. "
            "It often causes prolonged fatigue and swollen lymph nodes."
        ),
        advice=(
            "Rest is the primary treatment. Avoid contact sports due to risk of spleen "
            "rupture. Recovery can take several weeks — follow up with a doctor."
        ),
        weight=4,
    ),
]
