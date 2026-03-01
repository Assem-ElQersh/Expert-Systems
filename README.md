# Expert Systems

A collection of rule-based expert systems built in Python, each demonstrating how artificial intelligence can encode domain knowledge to advise non-expert users — mirroring the architecture shown below.

<p align="center">
  <img src="Image%20for%20illustration.png" alt="Expert System Architecture" width="600">
</p>

## What Is an Expert System?

An expert system is an AI program that emulates the decision-making ability of a human expert in a specific domain. It operates through three core components:

| Component | Role | Implementation |
|---|---|---|
| **Knowledge Base** | Stores domain facts and rules provided by a human expert | `knowledge_base.py` |
| **Rules Engine (Inference Engine)** | Evaluates rules against user-supplied facts to reach conclusions | `inference_engine.py` |
| **User Interface** | Collects input from the non-expert user and presents advice | `app.py` (Streamlit) |

### Data Flow

```
Non-expert User
      │
      │  Sample Input (symptoms / trait answers)
      ▼
┌─────────────────┐        ┌──────────────────┐        ┌────────────────────┐
│  User Interface │◄──────►│   Rules Engine   │◄──────►│  Knowledge Base    │
│    (app.py)     │        │(inference_engine)│        │(knowledge_base.py) │
└─────────────────┘        └──────────────────┘        └────────────────────┘
      │                                                         ▲
      │  Advice / Recommendations                               │
      ▼                                                  Knowledge from
Non-expert User                                          a Domain Expert
```

---

## Systems in This Repository

### 🩺 Symptoms Checker

> `symptoms-checker/`

A medical triage expert system that analyses reported symptoms and returns a ranked list of possible conditions with confidence scores and recommended actions.

- **12 rules** covering flu, cold, COVID-19, allergies, strep throat, pneumonia, and more
- Weighted forward-chaining inference with configurable confidence threshold
- Streamlit UI with grouped symptom checkboxes and progress-bar confidence display

```bash
cd symptoms-checker
pip install -r requirements.txt
streamlit run app.py
```

---

### 🎯 Career Path Advisor

> `career-advisor/`

A career guidance expert system that matches a user's interests, skills, values, personality, and education to personalised career recommendations with step-by-step roadmaps.

- **12 career rules** spanning technology, healthcare, law, engineering, education, and more
- Weighted trait-matching inference with adjustable match threshold
- Streamlit UI with trait-selection dropdowns and expandable career roadmaps

```bash
cd career-advisor
pip install -r requirements.txt
streamlit run app.py
```

---

## Repository Structure

```
Expert-Systems/
├── README.md
├── LICENSE
├── Image for illustration.png
├── symptoms-checker/
│   ├── knowledge_base.py       ← rules & medical facts
│   ├── inference_engine.py     ← weighted forward-chaining
│   ├── app.py                  ← Streamlit UI
│   ├── requirements.txt
│   └── README.md
└── career-advisor/
    ├── knowledge_base.py       ← career rules & roadmaps
    ├── inference_engine.py     ← weighted trait matching
    ├── app.py                  ← Streamlit UI
    ├── requirements.txt
    └── README.md
```

## Requirements

- Python 3.10+
- Streamlit 1.32+

Each system has its own `requirements.txt`. There are no shared dependencies beyond the Python standard library.

## Further Reading

- Negnevitsky, M. — *Artificial Intelligence: A Guide to Intelligent Systems* (3rd ed.)
- Russell, S. & Norvig, P. — *Artificial Intelligence: A Modern Approach* (4th ed.)
- [Streamlit Documentation](https://docs.streamlit.io)

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).
