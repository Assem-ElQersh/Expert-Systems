"""
Knowledge Base for the Career Path Advisor Expert System.

Each Rule encodes a career recommendation with:
  - conditions  : dict mapping trait category → expected string value
  - career      : the recommended career title
  - field        : broad professional field
  - description : what this career involves
  - roadmap     : step-by-step guide to entering the career
  - skills_to_develop : list of key skills to build
  - weight      : confidence weight used by the inference engine

Trait categories and their valid values are defined in TRAIT_OPTIONS below.
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class CareerRule:
    conditions: Dict[str, str]    # {trait_category: expected_value}
    career: str
    field: str
    description: str
    roadmap: str
    skills_to_develop: List[str]
    weight: float


# ── Valid trait options (drives the UI dropdowns) ────────────────────────────

TRAIT_OPTIONS: Dict[str, List[str]] = {
    "Primary Interest": [
        "Technology & Computing",
        "Science & Research",
        "Art & Creativity",
        "Business & Finance",
        "Healthcare & Medicine",
        "Education & Teaching",
        "Law & Justice",
        "Engineering & Building",
        "Social Impact & Community",
        "Media & Communication",
    ],
    "Strongest Skill": [
        "Analytical & Problem-Solving",
        "Communication & Writing",
        "Leadership & Management",
        "Technical & Engineering",
        "Creative & Design",
        "Empathy & People Skills",
        "Research & Investigation",
        "Organisation & Planning",
        "Coding & Software",
        "Sales & Persuasion",
    ],
    "Core Value": [
        "Innovation & Discovery",
        "Helping Others",
        "Financial Stability",
        "Creative Freedom",
        "Challenge & Growth",
        "Work-Life Balance",
        "Social Impact",
        "Recognition & Status",
        "Autonomy",
        "Security & Stability",
    ],
    "Personality Type": [
        "Logical & Analytical",
        "Creative & Artistic",
        "Empathetic & Caring",
        "Strategic & Visionary",
        "Detail-Oriented & Precise",
        "Entrepreneurial & Risk-Taking",
        "Communicative & Persuasive",
        "Practical & Hands-On",
        "Curious & Investigative",
        "Leadership & Decisive",
    ],
    "Education Background": [
        "Computer Science / IT",
        "Business / Management",
        "Fine Arts / Design",
        "Biology / Life Sciences",
        "Engineering",
        "Social Sciences",
        "Law / Political Science",
        "Medicine / Nursing",
        "Education / Humanities",
        "Mathematics / Statistics",
    ],
}

CAREER_RULES: List[CareerRule] = [
    CareerRule(
        conditions={
            "Primary Interest": "Technology & Computing",
            "Strongest Skill": "Coding & Software",
            "Core Value": "Innovation & Discovery",
            "Personality Type": "Logical & Analytical",
            "Education Background": "Computer Science / IT",
        },
        career="Software Engineer",
        field="Technology",
        description=(
            "Software engineers design, develop, and maintain software systems. "
            "They work across web, mobile, systems, and cloud platforms."
        ),
        roadmap=(
            "1. Earn a Bachelor's degree in Computer Science or a related field.\n"
            "2. Master at least one programming language deeply (Python, Java, or C++).\n"
            "3. Build a portfolio of personal or open-source projects on GitHub.\n"
            "4. Complete internships to gain industry experience.\n"
            "5. Pursue cloud certifications (AWS, Azure, GCP) to stand out.\n"
            "6. Target mid-level roles after 2–3 years; aim for senior/staff levels with 5+."
        ),
        skills_to_develop=[
            "Data structures & algorithms",
            "System design",
            "Version control (Git)",
            "CI/CD pipelines",
            "Cloud platforms",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Technology & Computing",
            "Strongest Skill": "Analytical & Problem-Solving",
            "Core Value": "Innovation & Discovery",
            "Personality Type": "Curious & Investigative",
            "Education Background": "Mathematics / Statistics",
        },
        career="Data Scientist",
        field="Technology / Data",
        description=(
            "Data scientists extract insights from large datasets using statistical "
            "analysis, machine learning, and data visualisation to drive decisions."
        ),
        roadmap=(
            "1. Build a strong foundation in statistics, linear algebra, and probability.\n"
            "2. Learn Python (NumPy, Pandas, Scikit-learn) and SQL.\n"
            "3. Complete end-to-end ML projects and publish them on Kaggle or GitHub.\n"
            "4. Earn a specialisation certificate (e.g., Google Data Analytics, DeepLearning.AI).\n"
            "5. Build domain knowledge in a vertical (finance, healthcare, NLP).\n"
            "6. Aim for roles at data-driven companies or research labs."
        ),
        skills_to_develop=[
            "Machine learning & deep learning",
            "Python & R programming",
            "Data visualisation (Matplotlib, Tableau)",
            "SQL & big data tools",
            "Statistical modelling",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Art & Creativity",
            "Strongest Skill": "Creative & Design",
            "Core Value": "Creative Freedom",
            "Personality Type": "Creative & Artistic",
            "Education Background": "Fine Arts / Design",
        },
        career="UX/UI Designer",
        field="Design & Technology",
        description=(
            "UX/UI designers create intuitive, visually appealing digital experiences. "
            "They bridge user research and visual design to build products people love."
        ),
        roadmap=(
            "1. Study fundamentals of design thinking, colour theory, and typography.\n"
            "2. Master design tools: Figma, Adobe XD, or Sketch.\n"
            "3. Build a portfolio of case studies showing problem → research → solution.\n"
            "4. Learn basic HTML/CSS to collaborate effectively with developers.\n"
            "5. Conduct user research and usability testing on your projects.\n"
            "6. Apply for junior designer roles or freelance on platforms like Dribbble."
        ),
        skills_to_develop=[
            "User research & interviews",
            "Wireframing & prototyping",
            "Visual hierarchy & layout",
            "Figma / Adobe XD",
            "Accessibility standards (WCAG)",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Business & Finance",
            "Strongest Skill": "Leadership & Management",
            "Core Value": "Financial Stability",
            "Personality Type": "Strategic & Visionary",
            "Education Background": "Business / Management",
        },
        career="Business Analyst",
        field="Business & Strategy",
        description=(
            "Business analysts identify organisational needs and recommend solutions. "
            "They bridge the gap between IT and business stakeholders."
        ),
        roadmap=(
            "1. Earn a degree in Business, Economics, or a related field.\n"
            "2. Develop strong skills in data analysis, Excel, and SQL.\n"
            "3. Obtain a CBAP or PMI-PBA certification.\n"
            "4. Learn Agile and Scrum methodologies.\n"
            "5. Build experience through internships in consulting or corporate strategy.\n"
            "6. Progress toward senior analyst or product manager roles."
        ),
        skills_to_develop=[
            "Requirements gathering",
            "Process modelling (BPMN)",
            "Data analysis & Excel",
            "Stakeholder communication",
            "Agile / Scrum",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Healthcare & Medicine",
            "Strongest Skill": "Empathy & People Skills",
            "Core Value": "Helping Others",
            "Personality Type": "Empathetic & Caring",
            "Education Background": "Medicine / Nursing",
        },
        career="Clinical Nurse / Healthcare Professional",
        field="Healthcare",
        description=(
            "Nurses and healthcare professionals provide direct patient care, administer "
            "treatments, and support physicians in hospitals, clinics, and communities."
        ),
        roadmap=(
            "1. Complete a nursing degree (BSN) or relevant healthcare programme.\n"
            "2. Pass licensure exams (NCLEX-RN for nursing).\n"
            "3. Gain clinical experience in a hospital or community health setting.\n"
            "4. Choose a specialisation: paediatrics, oncology, ICU, mental health, etc.\n"
            "5. Pursue advanced practice roles (NP, CRNA) with a master's degree.\n"
            "6. Consider healthcare management or policy for a leadership track."
        ),
        skills_to_develop=[
            "Patient assessment & monitoring",
            "Clinical decision-making",
            "Medication administration",
            "Communication & empathy",
            "Emergency response",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Science & Research",
            "Strongest Skill": "Research & Investigation",
            "Core Value": "Challenge & Growth",
            "Personality Type": "Curious & Investigative",
            "Education Background": "Biology / Life Sciences",
        },
        career="Biomedical Researcher",
        field="Science & Research",
        description=(
            "Biomedical researchers conduct experiments to understand diseases and develop "
            "new treatments, vaccines, and medical technologies."
        ),
        roadmap=(
            "1. Earn a BSc in Biology, Biochemistry, or a related life science.\n"
            "2. Pursue a Master's or PhD in a specialised biomedical field.\n"
            "3. Work in academic or industry labs during your studies.\n"
            "4. Publish research in peer-reviewed journals to build your profile.\n"
            "5. Apply for postdoctoral positions at research institutions or biotech firms.\n"
            "6. Aim for principal investigator or R&D director roles long-term."
        ),
        skills_to_develop=[
            "Laboratory techniques (PCR, ELISA, cell culture)",
            "Statistical analysis (R, SPSS)",
            "Scientific writing",
            "Grant writing",
            "Data interpretation",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Social Impact & Community",
            "Strongest Skill": "Communication & Writing",
            "Core Value": "Social Impact",
            "Personality Type": "Communicative & Persuasive",
            "Education Background": "Social Sciences",
        },
        career="Social Worker / Community Developer",
        field="Social Services",
        description=(
            "Social workers help individuals and families navigate challenges such as "
            "poverty, mental health, and abuse. Community developers build local programmes."
        ),
        roadmap=(
            "1. Earn a BSW (Bachelor of Social Work) or related social science degree.\n"
            "2. Complete supervised field placements during your studies.\n"
            "3. Obtain licensure (LCSW in the US or equivalent).\n"
            "4. Gain experience in a specific sector: child welfare, mental health, housing.\n"
            "5. Pursue an MSW for advanced clinical or administrative roles.\n"
            "6. Build expertise in grant writing to fund community programmes."
        ),
        skills_to_develop=[
            "Active listening & counselling",
            "Case management",
            "Crisis intervention",
            "Community outreach",
            "Report writing",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Engineering & Building",
            "Strongest Skill": "Technical & Engineering",
            "Core Value": "Challenge & Growth",
            "Personality Type": "Practical & Hands-On",
            "Education Background": "Engineering",
        },
        career="Civil / Mechanical Engineer",
        field="Engineering",
        description=(
            "Engineers design, build, and maintain physical systems and infrastructure — "
            "from bridges and buildings to engines and manufacturing lines."
        ),
        roadmap=(
            "1. Earn a BEng or BSc in Civil, Mechanical, or Structural Engineering.\n"
            "2. Complete graduate engineering internships or co-op placements.\n"
            "3. Obtain professional engineer (PE/CEng) licensure.\n"
            "4. Specialise in a sub-discipline: structural, environmental, automotive, etc.\n"
            "5. Build project management skills (PMP certification is valuable).\n"
            "6. Progress from junior engineer → project engineer → engineering manager."
        ),
        skills_to_develop=[
            "CAD software (AutoCAD, SolidWorks)",
            "Structural analysis",
            "Project management",
            "Technical drawing & specifications",
            "Regulatory standards & safety",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Law & Justice",
            "Strongest Skill": "Analytical & Problem-Solving",
            "Core Value": "Social Impact",
            "Personality Type": "Detail-Oriented & Precise",
            "Education Background": "Law / Political Science",
        },
        career="Lawyer / Legal Counsel",
        field="Law",
        description=(
            "Lawyers advise clients, draft legal documents, and represent individuals or "
            "organisations in disputes. Specialisations include corporate, criminal, and family law."
        ),
        roadmap=(
            "1. Complete an undergraduate degree (any major, though pre-law is common).\n"
            "2. Take the LSAT and gain admission to an accredited law school.\n"
            "3. Earn your Juris Doctor (JD) — 3 years of intensive legal study.\n"
            "4. Pass the Bar Exam in your jurisdiction.\n"
            "5. Join a law firm, public defender's office, or corporate legal team.\n"
            "6. Choose a specialisation and build your client reputation over 5–10 years."
        ),
        skills_to_develop=[
            "Legal research & writing",
            "Critical analysis",
            "Oral argumentation",
            "Negotiation",
            "Attention to detail",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Education & Teaching",
            "Strongest Skill": "Communication & Writing",
            "Core Value": "Helping Others",
            "Personality Type": "Empathetic & Caring",
            "Education Background": "Education / Humanities",
        },
        career="Teacher / Educator",
        field="Education",
        description=(
            "Teachers inspire and educate students at primary, secondary, or tertiary levels. "
            "They design curricula, assess learning, and foster intellectual growth."
        ),
        roadmap=(
            "1. Earn a Bachelor's in Education (BEd) or a subject-specific degree + PGCE.\n"
            "2. Complete teaching practice placements in schools.\n"
            "3. Obtain QTS (Qualified Teacher Status) or equivalent certification.\n"
            "4. Begin teaching at a junior level; build classroom management skills.\n"
            "5. Pursue CPD (continuing professional development) and specialisations.\n"
            "6. Progress to head of department, deputy head, or educational leadership."
        ),
        skills_to_develop=[
            "Curriculum design",
            "Classroom management",
            "Assessment & feedback",
            "Inclusive teaching practices",
            "Communication & patience",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Media & Communication",
            "Strongest Skill": "Communication & Writing",
            "Core Value": "Creative Freedom",
            "Personality Type": "Creative & Artistic",
            "Education Background": "Education / Humanities",
        },
        career="Journalist / Content Strategist",
        field="Media & Communications",
        description=(
            "Journalists investigate and report on events and issues for the public. "
            "Content strategists plan and produce digital content for brands and organisations."
        ),
        roadmap=(
            "1. Earn a degree in Journalism, Communications, or English.\n"
            "2. Write for your university newspaper or start a blog to build a portfolio.\n"
            "3. Complete internships at news outlets, magazines, or digital agencies.\n"
            "4. Develop multimedia skills: video, podcasting, and social media.\n"
            "5. Build a personal brand and social media presence.\n"
            "6. Specialise in a beat (tech, politics, science) or transition to content strategy."
        ),
        skills_to_develop=[
            "Investigative research",
            "Writing & editing",
            "SEO & digital marketing",
            "Video & audio production",
            "Social media strategy",
        ],
        weight=5,
    ),
    CareerRule(
        conditions={
            "Primary Interest": "Business & Finance",
            "Strongest Skill": "Analytical & Problem-Solving",
            "Core Value": "Financial Stability",
            "Personality Type": "Detail-Oriented & Precise",
            "Education Background": "Mathematics / Statistics",
        },
        career="Financial Analyst / Actuary",
        field="Finance",
        description=(
            "Financial analysts evaluate investment opportunities, model financial risks, "
            "and provide data-driven recommendations to businesses and investors."
        ),
        roadmap=(
            "1. Earn a degree in Finance, Economics, Mathematics, or Statistics.\n"
            "2. Learn financial modelling with Excel and Python.\n"
            "3. Pursue the CFA (Chartered Financial Analyst) designation.\n"
            "4. Gain experience in investment banking, consulting, or corporate finance.\n"
            "5. Build expertise in a niche: equity research, risk, FP&A, or actuary.\n"
            "6. Progress to VP or Director of Finance with 7–10 years of experience."
        ),
        skills_to_develop=[
            "Financial modelling (Excel, Python)",
            "Valuation methods (DCF, comparable)",
            "Risk analysis",
            "Data visualisation",
            "Regulatory knowledge",
        ],
        weight=5,
    ),
]
