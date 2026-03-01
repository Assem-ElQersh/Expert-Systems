# Career Path Advisor — Expert System

A rule-based career guidance expert system that matches a user's interests, skills, values, and personality to personalised career recommendations with detailed roadmaps.

## Architecture

| File | Role |
|---|---|
| `knowledge_base.py` | Domain knowledge — 12 career rules spanning technology, healthcare, law, education, and more |
| `inference_engine.py` | Rules Engine — weighted forward-chaining that scores each career rule against the user's trait profile |
| `app.py` | User Interface — Streamlit web application |

## How It Works

1. The user selects one option per trait category (5 dropdowns) in the sidebar.
2. The **Inference Engine** evaluates all rules in the **Knowledge Base** by counting how many trait conditions match.
3. Confidence is computed as `(matched_traits / total_traits) × 100%`.
4. Results above the configurable threshold are displayed ranked by match score, with expandable roadmaps and skill lists.

## Running the App

```bash
# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

## Trait Categories

| Category | Examples |
|---|---|
| Primary Interest | Technology, Healthcare, Art, Business, Law... |
| Strongest Skill | Analytical, Communication, Leadership, Coding... |
| Core Value | Innovation, Helping Others, Financial Stability... |
| Personality Type | Logical, Creative, Empathetic, Strategic... |
| Education Background | Computer Science, Medicine, Engineering, Law... |

## Career Coverage

| Career | Field |
|---|---|
| Software Engineer | Technology |
| Data Scientist | Technology / Data |
| UX/UI Designer | Design & Technology |
| Business Analyst | Business & Strategy |
| Clinical Nurse / Healthcare Professional | Healthcare |
| Biomedical Researcher | Science & Research |
| Social Worker / Community Developer | Social Services |
| Civil / Mechanical Engineer | Engineering |
| Lawyer / Legal Counsel | Law |
| Teacher / Educator | Education |
| Journalist / Content Strategist | Media & Communications |
| Financial Analyst / Actuary | Finance |
