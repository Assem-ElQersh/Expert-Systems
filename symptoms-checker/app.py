"""
Symptoms Checker — Streamlit User Interface

Architecture layer: User Interface (app.py)
  Accepts symptom input from the user → delegates to InferenceEngine → displays results.

Run with:
    streamlit run app.py
"""

import streamlit as st
from inference_engine import InferenceEngine
from knowledge_base import ALL_SYMPTOMS

# ── Page configuration ──────────────────────────────────────────────────────

st.set_page_config(
    page_title="Symptoms Checker | Expert System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────────────────────

st.markdown(
    """
    <style>
        .main-header {
            font-size: 2.4rem;
            font-weight: 700;
            color: #1a73e8;
            margin-bottom: 0;
        }
        .sub-header {
            font-size: 1rem;
            color: #5f6368;
            margin-bottom: 1.5rem;
        }
        .result-card {
            background: #f8f9fa;
            border-left: 5px solid #1a73e8;
            border-radius: 6px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        }
        .result-card.high {
            border-left-color: #d93025;
        }
        .result-card.medium {
            border-left-color: #f29900;
        }
        .result-card.low {
            border-left-color: #188038;
        }
        .disclaimer {
            background: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 6px;
            padding: 0.75rem 1rem;
            font-size: 0.85rem;
            color: #856404;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Header ───────────────────────────────────────────────────────────────────

st.markdown('<p class="main-header">🩺 Symptoms Checker</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">An expert system that analyses your symptoms and suggests possible conditions.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="disclaimer">⚠️ <strong>Medical Disclaimer:</strong> This tool is for educational purposes only '
    "and does <strong>not</strong> constitute medical advice. Always consult a qualified healthcare "
    "professional for diagnosis and treatment.</div>",
    unsafe_allow_html=True,
)

st.divider()

# ── Sidebar — symptom selection ───────────────────────────────────────────────

with st.sidebar:
    st.header("Select Your Symptoms")
    st.caption("Check all symptoms that apply to you right now.")

    selected_symptoms: set[str] = set()

    symptom_groups = {
        "General": [
            "Fever",
            "High Fever (>39°C)",
            "Fatigue",
            "Chills",
            "Muscle Aches",
        ],
        "Respiratory": [
            "Cough",
            "Dry Cough",
            "Productive Cough",
            "Shortness of Breath",
            "Chest Tightness",
            "Nasal Congestion",
            "Runny Nose",
            "Sneezing",
        ],
        "Head & Throat": [
            "Headache",
            "Sore Throat",
            "Loss of Taste/Smell",
        ],
        "Digestive": [
            "Nausea / Vomiting",
            "Diarrhea",
        ],
        "Skin & Eyes": [
            "Skin Rash",
            "Itchy / Watery Eyes",
        ],
    }

    for group_name, symptoms in symptom_groups.items():
        st.subheader(group_name)
        for symptom in symptoms:
            if symptom in ALL_SYMPTOMS and st.checkbox(symptom, key=f"sym_{symptom}"):
                selected_symptoms.add(symptom)

    st.divider()
    confidence_threshold = st.slider(
        "Minimum confidence threshold (%)",
        min_value=10,
        max_value=80,
        value=30,
        step=5,
        help="Only show diagnoses with confidence at or above this level.",
    )

# ── Main panel ────────────────────────────────────────────────────────────────

col_left, col_right = st.columns([2, 1])

with col_left:
    if selected_symptoms:
        st.subheader(f"Selected Symptoms ({len(selected_symptoms)})")
        st.write(", ".join(sorted(selected_symptoms)))
    else:
        st.info("👈 Select your symptoms in the sidebar, then click **Analyse**.")

with col_right:
    analyse_btn = st.button("🔍 Analyse Symptoms", type="primary", use_container_width=True)
    clear_btn = st.button("🗑️ Clear All", use_container_width=True)

    if clear_btn:
        st.rerun()

st.divider()

# ── Results ───────────────────────────────────────────────────────────────────

if analyse_btn:
    if not selected_symptoms:
        st.warning("Please select at least one symptom before running the analysis.")
    else:
        engine = InferenceEngine(threshold=float(confidence_threshold))
        results = engine.evaluate(selected_symptoms)

        if not results:
            st.error(
                "No conditions matched your symptom profile above the confidence threshold. "
                "Try lowering the threshold or consult a doctor directly."
            )
        else:
            st.subheader(f"Analysis Results — {len(results)} possible condition(s) found")

            for i, result in enumerate(results):
                confidence = result.confidence

                if confidence >= 80:
                    level = "high"
                    badge = "🔴 High Match"
                elif confidence >= 55:
                    level = "medium"
                    badge = "🟡 Moderate Match"
                else:
                    level = "low"
                    badge = "🟢 Low Match"

                with st.container():
                    st.markdown(
                        f'<div class="result-card {level}">',
                        unsafe_allow_html=True,
                    )

                    rank_col, title_col, badge_col = st.columns([0.5, 4, 1.5])
                    with rank_col:
                        st.markdown(f"### #{i + 1}")
                    with title_col:
                        st.markdown(f"### {result.conclusion}")
                    with badge_col:
                        st.markdown(f"**{badge}**")

                    st.progress(int(confidence) / 100, text=f"Confidence: {confidence}%")

                    st.caption(
                        f"Matched {result.matched_conditions} of {result.total_conditions} rule criteria"
                    )

                    with st.expander("More details & advice"):
                        st.markdown(f"**About this condition:**  \n{result.description}")
                        st.markdown(f"**Recommended action:**  \n{result.advice}")

                    st.markdown("</div>", unsafe_allow_html=True)

            st.divider()
            st.markdown(
                '<div class="disclaimer">⚠️ These results are generated by a rule-based expert system and '
                "are <strong>not</strong> a substitute for professional medical diagnosis. "
                "Please see a qualified doctor for any health concerns.</div>",
                unsafe_allow_html=True,
            )
