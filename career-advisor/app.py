"""
Career Path Advisor — Streamlit User Interface

Architecture layer: User Interface (app.py)
  Collects user trait profile → delegates to InferenceEngine → displays ranked career matches.

Run with:
    streamlit run app.py
"""

import streamlit as st
from inference_engine import InferenceEngine
from knowledge_base import TRAIT_OPTIONS

# ── Page configuration ──────────────────────────────────────────────────────

st.set_page_config(
    page_title="Career Path Advisor | Expert System",
    page_icon="🎯",
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
            color: #0f9d58;
            margin-bottom: 0;
        }
        .sub-header {
            font-size: 1rem;
            color: #5f6368;
            margin-bottom: 1.5rem;
        }
        .career-card {
            background: #f8f9fa;
            border-left: 5px solid #0f9d58;
            border-radius: 6px;
            padding: 1rem 1.25rem;
            margin-bottom: 1.2rem;
        }
        .career-card.perfect {
            border-left-color: #0f9d58;
        }
        .career-card.strong {
            border-left-color: #1a73e8;
        }
        .career-card.partial {
            border-left-color: #f29900;
        }
        .tag {
            display: inline-block;
            background: #e8f5e9;
            color: #1b5e20;
            border-radius: 12px;
            padding: 2px 10px;
            font-size: 0.8rem;
            margin: 2px;
        }
        .info-box {
            background: #e8f0fe;
            border: 1px solid #1a73e8;
            border-radius: 6px;
            padding: 0.75rem 1rem;
            font-size: 0.9rem;
            color: #174ea6;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Header ───────────────────────────────────────────────────────────────────

st.markdown('<p class="main-header">🎯 Career Path Advisor</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">An expert system that matches your interests, skills, and values to ideal career paths.</p>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="info-box">ℹ️ Answer the five questions in the sidebar to describe yourself, '
    "then click <strong>Find My Path</strong> to receive personalised career recommendations.</div>",
    unsafe_allow_html=True,
)

st.divider()

# ── Sidebar — trait selection ─────────────────────────────────────────────────

with st.sidebar:
    st.header("Your Profile")
    st.caption("Select the option that best describes you in each category.")

    user_profile: dict[str, str] = {}

    trait_icons = {
        "Primary Interest": "🌟",
        "Strongest Skill": "💪",
        "Core Value": "❤️",
        "Personality Type": "🧠",
        "Education Background": "🎓",
    }

    for trait, options in TRAIT_OPTIONS.items():
        icon = trait_icons.get(trait, "")
        st.subheader(f"{icon} {trait}")
        choice = st.selectbox(
            label=trait,
            options=["— Select —"] + options,
            key=f"trait_{trait}",
            label_visibility="collapsed",
        )
        if choice != "— Select —":
            user_profile[trait] = choice

    st.divider()
    confidence_threshold = st.slider(
        "Minimum match threshold (%)",
        min_value=20,
        max_value=80,
        value=40,
        step=10,
        help="Only show careers with a match score at or above this level.",
    )

    st.divider()
    profile_complete = len(user_profile) == len(TRAIT_OPTIONS)
    if profile_complete:
        st.success("✅ Profile complete — ready to analyse!")
    else:
        remaining = len(TRAIT_OPTIONS) - len(user_profile)
        st.warning(f"⚠️ {remaining} question(s) remaining.")

# ── Main panel ────────────────────────────────────────────────────────────────

summary_col, btn_col = st.columns([3, 1])

with summary_col:
    if user_profile:
        st.subheader("Your Selections")
        cols = st.columns(len(user_profile))
        for col, (trait, value) in zip(cols, user_profile.items()):
            with col:
                st.metric(label=trait, value=value)
    else:
        st.info("👈 Fill in your profile in the sidebar to get started.")

with btn_col:
    find_btn = st.button("🔍 Find My Path", type="primary", use_container_width=True)
    clear_btn = st.button("🗑️ Reset Profile", use_container_width=True)
    if clear_btn:
        st.rerun()

st.divider()

# ── Results ───────────────────────────────────────────────────────────────────

if find_btn:
    if len(user_profile) < 3:
        st.warning("Please answer at least 3 of the 5 questions for a meaningful recommendation.")
    else:
        engine = InferenceEngine(threshold=float(confidence_threshold))
        results = engine.evaluate(user_profile)

        if not results:
            st.error(
                "No careers matched your profile above the confidence threshold. "
                "Try lowering the threshold or adjusting your selections."
            )
        else:
            st.subheader(f"Career Recommendations — {len(results)} match(es) found")

            for i, rec in enumerate(results):
                confidence = rec.confidence

                if confidence >= 80:
                    level = "perfect"
                    badge = "🟢 Excellent Match"
                elif confidence >= 60:
                    level = "strong"
                    badge = "🔵 Strong Match"
                else:
                    level = "partial"
                    badge = "🟡 Partial Match"

                with st.container():
                    st.markdown(f'<div class="career-card {level}">', unsafe_allow_html=True)

                    rank_col, title_col, badge_col = st.columns([0.5, 4, 1.5])
                    with rank_col:
                        st.markdown(f"### #{i + 1}")
                    with title_col:
                        st.markdown(f"### {rec.career}")
                        st.caption(f"Field: **{rec.field}**")
                    with badge_col:
                        st.markdown(f"**{badge}**")

                    st.progress(
                        int(confidence) / 100,
                        text=f"Match Score: {confidence}%  ({rec.matched_traits}/{rec.total_traits} traits aligned)",
                    )

                    st.markdown(f"*{rec.description}*")

                    with st.expander("📋 Career Roadmap & Skills to Develop"):
                        st.markdown("**Step-by-Step Roadmap:**")
                        for line in rec.roadmap.strip().split("\n"):
                            st.markdown(line)

                        st.markdown("**Key Skills to Build:**")
                        skills_html = " ".join(
                            f'<span class="tag">{skill}</span>'
                            for skill in rec.skills_to_develop
                        )
                        st.markdown(skills_html, unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)
