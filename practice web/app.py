"""
🚀 Anti-Gravity AI Career Mentor
A Streamlit app for student placement preparation.

Python's antigravity Easter egg: `import antigravity`
We take that spirit — defy gravity, reach for the stars! 🌌
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from modules.predictor import predict_placement, make_radar_chart
from modules.skill_analyzer import get_roles, analyze_gap, make_gap_chart, ROLE_SKILLS
from modules.resume_analyzer import analyze_resume
from modules.project_suggester import filter_projects, get_domains, get_difficulties
from modules.chatbot import get_response

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Anti-Gravity AI Career Mentor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
# CUSTOM CSS — Dark Glassmorphism Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Global Reset */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0a0015 0%, #0d001f 40%, #000d2e 100%);
    color: #e8e0ff;
}

/* Hide Streamlit branding */
#MainMenu, footer, header { visibility: hidden; }

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #110025 0%, #0a001a 100%) !important;
    border-right: 1px solid rgba(130, 80, 255, 0.2);
}
[data-testid="stSidebar"] * { color: #e0d0ff !important; }

/* Card container */
.ag-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(130, 80, 255, 0.25);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
    backdrop-filter: blur(12px);
    transition: border-color 0.3s ease, transform 0.2s ease;
}
.ag-card:hover {
    border-color: rgba(130, 80, 255, 0.6);
    transform: translateY(-2px);
}

/* Hero banner */
.ag-hero {
    background: linear-gradient(135deg, rgba(130, 80, 255, 0.18) 0%, rgba(0, 180, 220, 0.10) 100%);
    border: 1px solid rgba(130, 80, 255, 0.3);
    border-radius: 20px;
    padding: 2.5rem 2rem;
    text-align: center;
    margin-bottom: 2rem;
}
.ag-hero h1 {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #b085ff, #00cfff, #b085ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.ag-hero p { color: #a090cc; font-size: 1.1rem; margin-top: 0.5rem; }

/* Score badge */
.ag-score {
    text-align: center;
    padding: 1.5rem;
    border-radius: 16px;
    font-size: 3.5rem;
    font-weight: 800;
}
.ag-score-high {
    background: linear-gradient(135deg, rgba(0, 212, 130, 0.15), rgba(0, 212, 130, 0.05));
    border: 2px solid rgba(0, 212, 130, 0.4);
    color: #00d482;
}
.ag-score-low {
    background: linear-gradient(135deg, rgba(255, 100, 80, 0.15), rgba(255, 100, 80, 0.05));
    border: 2px solid rgba(255, 100, 80, 0.4);
    color: #ff6450;
}

/* Stat pill */
.ag-pill {
    display: inline-block;
    background: rgba(130, 80, 255, 0.15);
    border: 1px solid rgba(130, 80, 255, 0.3);
    border-radius: 50px;
    padding: 0.3rem 1rem;
    font-size: 0.85rem;
    margin: 0.2rem;
    color: #c0a0ff;
}

/* Project card */
.proj-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(130, 80, 255, 0.2);
    border-radius: 14px;
    padding: 1.2rem;
    margin-bottom: 1rem;
    transition: all 0.25s ease;
    height: 100%;
}
.proj-card:hover {
    border-color: rgba(130, 80, 255, 0.6);
    background: rgba(130, 80, 255, 0.08);
    transform: translateY(-3px);
}
.proj-title { font-size: 1.05rem; font-weight: 700; color: #c8aaff; margin-bottom: 0.4rem; }
.proj-desc { font-size: 0.88rem; color: #9080b0; line-height: 1.5; }
.proj-tech { margin-top: 0.6rem; }
.diff-beginner { color: #00d482; font-size: 0.8rem; font-weight: 600; }
.diff-intermediate { color: #ffb347; font-size: 0.8rem; font-weight: 600; }
.diff-advanced { color: #ff6450; font-size: 0.8rem; font-weight: 600; }

/* Chat UI */
.chat-user {
    background: linear-gradient(135deg, rgba(130, 80, 255, 0.25), rgba(130, 80, 255, 0.1));
    border: 1px solid rgba(130, 80, 255, 0.3);
    border-radius: 16px 16px 4px 16px;
    padding: 0.8rem 1.1rem;
    margin: 0.5rem 0;
    margin-left: 20%;
    color: #e0d0ff;
    font-size: 0.93rem;
}
.chat-bot {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px 16px 16px 4px;
    padding: 0.8rem 1.1rem;
    margin: 0.5rem 0;
    margin-right: 20%;
    color: #c8b8f8;
    font-size: 0.93rem;
    line-height: 1.6;
}

/* Streamlit widgets override */
.stSlider [data-baseweb="slider"] { margin-top: 0.2rem; }
div[data-testid="stMetricValue"] { font-size: 2rem !important; color: #b085ff !important; }
.stSelectbox > div > div { background: rgba(255,255,255,0.05) !important; border-color: rgba(130,80,255,0.3) !important; }
.stTextArea textarea { background: rgba(255,255,255,0.04) !important; border-color: rgba(130,80,255,0.3) !important; color: #e0d0ff !important; }
.stTextInput input { background: rgba(255,255,255,0.04) !important; border-color: rgba(130,80,255,0.3) !important; color: #e0d0ff !important; }
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #3b82f6) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover { opacity: 0.85; transform: translateY(-1px); }
.stTabs [data-baseweb="tab-list"] { background: rgba(255,255,255,0.03); border-radius: 12px; border: 1px solid rgba(130,80,255,0.15); }
.stTabs [data-baseweb="tab"] { color: #9080b0 !important; font-weight: 500; }
.stTabs [aria-selected="true"] { color: #c0a0ff !important; background: rgba(130,80,255,0.15) !important; border-radius: 10px; }
[data-testid="stRadio"] label { color: #c0a0ff !important; }
.stMarkdown h3 { color: #c0a0ff; }
.stMarkdown h2 { color: #d0b0ff; }
hr { border-color: rgba(130,80,255,0.15) !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1rem 0;'>
        <div style='font-size:3rem'>🚀</div>
        <div style='font-size:1.2rem; font-weight:800; color:#c0a0ff;'>Anti-Gravity</div>
        <div style='font-size:0.85rem; color:#7060a0;'>AI Career Mentor</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    st.markdown("**📌 Quick Tips**")
    st.info("💡 Use the **Predictor** tab first to see your placement readiness score.")
    st.success("🎯 Then check **Skill Gap** to know exactly what to learn next.")
    st.warning("📄 Paste your resume in **Resume Analyzer** for instant feedback.")

    st.divider()
    st.markdown("""
    <div style='font-size:0.78rem; color:#504060; text-align:center;'>
        🐍 Inspired by Python's <code>import antigravity</code><br>
        Defy limits. Build the impossible. 🌌
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# MAIN TABS
# ─────────────────────────────────────────────
tabs = st.tabs([
    "🏠 Home",
    "📄 Resume Analyzer",
    "🧠 Placement Predictor",
    "📊 Skill Gap",
    "💡 Projects",
    "🤖 Chatbot",
])

# ══════════════════════════════════════════════
# TAB 0 — HOME
# ══════════════════════════════════════════════
with tabs[0]:
    st.markdown("""
    <div class='ag-hero'>
        <h1>🚀 Anti-Gravity AI Career Mentor</h1>
        <p>Your personal AI-powered placement preparation assistant</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class='ag-card' style='text-align:center'>
            <div style='font-size:2.5rem'>🧠</div>
            <div style='font-weight:700;color:#c0a0ff;font-size:1.05rem;margin:0.5rem 0'>Placement Predictor</div>
            <div style='color:#7060a0;font-size:0.88rem'>ML model predicts your placement readiness with a probability score and skill radar chart.</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class='ag-card' style='text-align:center'>
            <div style='font-size:2.5rem'>📊</div>
            <div style='font-weight:700;color:#c0a0ff;font-size:1.05rem;margin:0.5rem 0'>Skill Gap Analyzer</div>
            <div style='color:#7060a0;font-size:0.88rem'>Pick your dream role and instantly see which skills you're missing vs industry requirements.</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class='ag-card' style='text-align:center'>
            <div style='font-size:2.5rem'>📄</div>
            <div style='font-weight:700;color:#c0a0ff;font-size:1.05rem;margin:0.5rem 0'>Resume Analyzer</div>
            <div style='color:#7060a0;font-size:0.88rem'>Paste your resume and get instant skill extraction, section detection, and improvement tips.</div>
        </div>""", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown("""<div class='ag-card' style='text-align:center'>
            <div style='font-size:2.5rem'>💡</div>
            <div style='font-weight:700;color:#c0a0ff;font-size:1.05rem;margin:0.5rem 0'>Project Suggester</div>
            <div style='color:#7060a0;font-size:0.88rem'>15+ unique AI/ML project ideas that will make your resume stand out in interviews.</div>
        </div>""", unsafe_allow_html=True)
    with col5:
        st.markdown("""<div class='ag-card' style='text-align:center'>
            <div style='font-size:2.5rem'>🤖</div>
            <div style='font-weight:700;color:#c0a0ff;font-size:1.05rem;margin:0.5rem 0'>Career Chatbot</div>
            <div style='color:#7060a0;font-size:0.88rem'>Ask anything about DSA, ML, resume tips, salary, LinkedIn, or interview prep.</div>
        </div>""", unsafe_allow_html=True)
    with col6:
        st.markdown("""<div class='ag-card' style='text-align:center'>
            <div style='font-size:2.5rem'>🌌</div>
            <div style='font-weight:700;color:#c0a0ff;font-size:1.05rem;margin:0.5rem 0'>Anti-Gravity Spirit</div>
            <div style='color:#7060a0;font-size:0.88rem'>Like <code>import antigravity</code> — this tool helps you defy the odds and soar above the competition.</div>
        </div>""", unsafe_allow_html=True)

    st.divider()
    st.markdown("""
    <div class='ag-card'>
        <h3 style='color:#c0a0ff;margin-top:0'>🐍 The Antigravity Connection</h3>
        <p style='color:#9080b0;line-height:1.7;'>
        In Python, typing <code style='color:#b085ff'>import antigravity</code> opens the legendary XKCD comic #353 — 
        where a programmer literally flies by learning Python. This project embodies that same spirit: 
        with the right AI tools and knowledge, <strong style='color:#c0a0ff'>you can defy gravity</strong> in your career journey. 
        Every skill you learn, every project you build, every interview you ace — it all adds lift. 
        This mentor is your launchpad. 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 1 — RESUME ANALYZER
# ══════════════════════════════════════════════
with tabs[1]:
    st.markdown("## 📄 Resume Analyzer")
    st.markdown("<p style='color:#7060a0'>Paste your resume text below. We'll extract skills, detect sections, and give improvement suggestions.</p>", unsafe_allow_html=True)

    SAMPLE_RESUME = """John Doe | john.doe@gmail.com | +91 9876543210
https://github.com/johndoe | https://linkedin.com/in/johndoe

EDUCATION
B.Tech Computer Science | XYZ University | CGPA: 8.2 | 2021-2025

SKILLS
Python, Java, C++, Machine Learning, Deep Learning, TensorFlow, Pandas, NumPy
SQL, MySQL, MongoDB, Git, GitHub, REST API, HTML, CSS, React

PROJECTS
1. AI Resume Screener - Built NLP-based resume screening tool using scikit-learn
2. Stock Predictor - LSTM model for stock price prediction using TensorFlow

INTERNSHIP
ML Intern at TechCorp (June 2024 - Aug 2024) - Developed image classification pipeline

CERTIFICATIONS
Machine Learning by Andrew Ng - Coursera (2023)
AWS Cloud Practitioner (2024)

ACHIEVEMENTS
Winner - National Hackathon 2024
Rank 450 in LeetCode India"""

    use_sample = st.checkbox("📋 Use sample resume for demo", value=False)
    resume_text = st.text_area(
        "Paste your resume here",
        value=SAMPLE_RESUME if use_sample else "",
        height=280,
        placeholder="Paste your full resume text here...",
    )

    if st.button("🔍 Analyze Resume", key="analyze_btn"):
        if not resume_text.strip():
            st.warning("Please paste your resume text or check the sample box.")
        else:
            result = analyze_resume(resume_text)

            st.divider()
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("📊 Total Skills Found", result["total_skills"])
            c2.metric("📋 Sections Detected", len(result["sections"]))
            c3.metric("✉️ Email", "✅ Found" if result["email"] else "❌ Missing")
            c4.metric("📱 Phone", "✅ Found" if result["phone"] else "❌ Missing")

            st.markdown("---")
            col_l, col_r = st.columns([1, 1])

            with col_l:
                st.markdown("### 🛠️ Skills Extracted")
                if result["skills"]:
                    for category, skills in result["skills"].items():
                        with st.expander(f"**{category}** ({len(skills)} skills)", expanded=True):
                            st.markdown(" ".join([f"<span class='ag-pill'>{s}</span>" for s in skills]), unsafe_allow_html=True)
                else:
                    st.warning("No recognizable skills found. Add more technical keywords.")

            with col_r:
                st.markdown("### 📋 Sections Detected")
                for section in result["sections"]:
                    st.success(f"✅ {section}")
                missing_sections = {"Education", "Experience / Internship", "Projects", "Certifications", "Achievements"} - set(result["sections"])
                for ms in missing_sections:
                    st.error(f"❌ {ms} — Missing!")

                if result["links"]:
                    st.markdown("### 🔗 Links Found")
                    for link in result["links"]:
                        st.markdown(f"<span class='ag-pill'>🔗 {link[:50]}{'...' if len(link)>50 else ''}</span>", unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("### 💡 Improvement Suggestions")
            for suggestion in result["suggestions"]:
                st.info(suggestion)

# ══════════════════════════════════════════════
# TAB 2 — PLACEMENT PREDICTOR
# ══════════════════════════════════════════════
with tabs[2]:
    st.markdown("## 🧠 Placement Predictor")
    st.markdown("<p style='color:#7060a0'>Fill in your profile details. Our ML model will predict your placement probability.</p>", unsafe_allow_html=True)

    with st.form("predictor_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🧩 Technical Skills**")
            dsa = st.radio("DSA & Algorithms", options=[0, 1], format_func=lambda x: "✅ Yes" if x else "❌ No", horizontal=True, key="dsa")
            ml = st.radio("Machine Learning knowledge", options=[0, 1], format_func=lambda x: "✅ Yes" if x else "❌ No", horizontal=True, key="ml")
            competitive = st.radio("Competitive Programming (LeetCode/CF)", options=[0, 1], format_func=lambda x: "✅ Yes" if x else "❌ No", horizontal=True, key="cp")
            communication = st.radio("Good Communication Skills", options=[0, 1], format_func=lambda x: "✅ Yes" if x else "❌ No", horizontal=True, key="comm")

        with col2:
            st.markdown("**🏆 Experience & Academics**")
            projects = st.radio("Built real projects?", options=[0, 1], format_func=lambda x: "✅ Yes" if x else "❌ No", horizontal=True, key="proj")
            internship = st.radio("Completed an Internship?", options=[0, 1], format_func=lambda x: "✅ Yes" if x else "❌ No", horizontal=True, key="intern")
            cgpa = st.slider("CGPA (out of 10)", min_value=4.0, max_value=10.0, value=7.5, step=0.1)

        submitted = st.form_submit_button("🚀 Predict My Placement Score", use_container_width=True)

    if submitted:
        cgpa_norm = (cgpa - 4.0) / 6.0  # normalize for radar chart
        score, verdict = predict_placement(dsa, ml, projects, internship, cgpa, competitive, communication)

        st.divider()
        c1, c2 = st.columns([1, 1])
        with c1:
            score_class = "ag-score-high" if score >= 60 else "ag-score-low"
            st.markdown(f"""
            <div class='ag-score {score_class}'>
                {score}%
            </div>
            <div style='text-align:center;margin-top:1rem;font-size:1.2rem;font-weight:600;color:#c0a0ff'>{verdict}</div>
            """, unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("**🎯 Personalized Tips:**")
            if dsa == 0: st.warning("📌 Start practicing DSA on LeetCode — aim for 150+ problems")
            if ml == 0: st.info("📌 Learn ML basics: Andrew Ng's course on Coursera is free to audit")
            if projects == 0: st.info("📌 Build 2–3 real-world projects and deploy them online")
            if internship == 0: st.warning("📌 Apply for internships on LinkedIn, Internshala, and AngelList")
            if cgpa < 7.0: st.warning("📌 A CGPA above 7.0 helps pass shortlisting filters at top companies")
            if competitive == 0: st.info("📌 Practice competitive programming — even 50 problems makes a difference")

        with c2:
            fig = make_radar_chart(dsa, ml, projects, internship, cgpa_norm, competitive, communication)
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ══════════════════════════════════════════════
# TAB 3 — SKILL GAP ANALYZER
# ══════════════════════════════════════════════
with tabs[3]:
    st.markdown("## 📊 Skill Gap Analyzer")
    st.markdown("<p style='color:#7060a0'>Select your target role and rate your current skill levels. We'll show exactly where you need to improve.</p>", unsafe_allow_html=True)

    role = st.selectbox("🎯 Target Role", get_roles())

    required_skills = list(ROLE_SKILLS[role].keys())
    st.markdown(f"**Rate your current level in {role} skills (0 = None, 100 = Expert):**")

    student_skills = {}
    num_skills = len(required_skills)
    cols_per_row = 2
    skill_pairs = [required_skills[i:i+cols_per_row] for i in range(0, num_skills, cols_per_row)]

    for pair in skill_pairs:
        row_cols = st.columns(cols_per_row)
        for idx, skill in enumerate(pair):
            with row_cols[idx]:
                student_skills[skill] = st.slider(skill, 0, 100, 40, key=f"skill_{skill}")

    if st.button("📊 Analyze My Skill Gap", key="gap_btn"):
        analysis = analyze_gap(role, student_skills)
        fig = make_gap_chart(analysis)

        st.markdown("---")
        st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

        st.markdown("### 🔍 Detailed Breakdown")
        for item in analysis:
            gap = item["gap"]
            bar_color = "#00d482" if gap == 0 else ("#ffb347" if gap < 30 else "#ff6450")
            pct = int((item["yours"] / item["required"]) * 100) if item["required"] > 0 else 0
            status = "✅ On track" if gap == 0 else (f"⚠️ {gap}% gap" if gap < 30 else f"🔴 {gap}% gap")
            st.markdown(f"""
            <div class='ag-card' style='padding:1rem;margin-bottom:0.6rem'>
                <div style='display:flex;justify-content:space-between;margin-bottom:0.4rem'>
                    <span style='font-weight:600;color:#c0a0ff'>{item['skill']}</span>
                    <span style='font-size:0.85rem;color:{bar_color}'>{status}</span>
                </div>
                <div style='background:rgba(255,255,255,0.05);border-radius:8px;height:8px;overflow:hidden'>
                    <div style='width:{pct}%;background:linear-gradient(90deg,{"#00d482" if gap==0 else "#7c3aed"},{"#00cfff" if gap==0 else "#b085ff"});height:100%;border-radius:8px;transition:width 0.5s'></div>
                </div>
                <div style='display:flex;justify-content:space-between;margin-top:0.3rem;font-size:0.8rem;color:#604080'>
                    <span>Your level: {item['yours']}/100</span><span>Required: {item['required']}/100</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 4 — PROJECT SUGGESTER
# ══════════════════════════════════════════════
with tabs[4]:
    st.markdown("## 💡 Project Suggester")
    st.markdown("<p style='color:#7060a0'>Discover unique AI/ML projects that make your resume stand out. Filter by domain and difficulty.</p>", unsafe_allow_html=True)

    fc1, fc2 = st.columns(2)
    with fc1:
        domain_filter = st.selectbox("🏷️ Domain", get_domains())
    with fc2:
        diff_filter = st.selectbox("📊 Difficulty", get_difficulties())

    projects = filter_projects(domain_filter, diff_filter)
    st.markdown(f"<p style='color:#7060a0'>Showing <strong style='color:#c0a0ff'>{len(projects)}</strong> projects</p>", unsafe_allow_html=True)
    st.markdown("---")

    for i in range(0, len(projects), 3):
        row_projects = projects[i:i+3]
        cols = st.columns(3)
        for col, proj in zip(cols, row_projects):
            diff_class = f"diff-{proj['difficulty'].lower()}"
            tech_pills = "".join([f"<span class='ag-pill'>{t}</span>" for t in proj['tech']])
            with col:
                st.markdown(f"""
                <div class='proj-card'>
                    <div style='display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.5rem'>
                        <span class='ag-pill'>{proj['tag']}</span>
                        <span class='{diff_class}'>{proj['difficulty']}</span>
                    </div>
                    <div class='proj-title'>{proj['title']}</div>
                    <div class='proj-desc'>{proj['description']}</div>
                    <div class='proj-tech'><div style='font-size:0.75rem;color:#504060;margin-bottom:0.3rem'>TECH STACK</div>{tech_pills}</div>
                    <div style='margin-top:0.6rem;font-size:0.82rem;color:#6040a0'>Impact: {proj['impact']}</div>
                </div>
                """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
# TAB 5 — CHATBOT
# ══════════════════════════════════════════════
with tabs[5]:
    st.markdown("## 🤖 Career Mentor Chatbot")
    st.markdown("<p style='color:#7060a0'>Ask me anything about placements, skills, resume, interviews, or your career path!</p>", unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "bot", "content": "👋 Hey! I'm your **Anti-Gravity Career Mentor AI**. Ask me about:\n\n• DSA & Algorithms\n• Machine Learning\n• Resume tips\n• Interview prep\n• Placement strategy\n• Project ideas\n• Internships & salary\n\nWhat would you like to know? 🚀"}
        ]

    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div class='chat-user'>🧑‍💻 {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-bot'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    suggestion_topics = ["Interview tips 🎯", "Resume advice 📄", "DSA roadmap 🧩", "ML learning path 🤖", "Salary info 💰", "Internship tips 💼"]
    st.markdown("**💬 Quick questions:**")
    sug_cols = st.columns(len(suggestion_topics))
    for i, topic in enumerate(suggestion_topics):
        if sug_cols[i].button(topic, key=f"sug_{i}"):
            response = get_response(topic)
            st.session_state.messages.append({"role": "user", "content": topic})
            st.session_state.messages.append({"role": "bot", "content": response})
            st.rerun()

    with st.form("chat_form", clear_on_submit=True):
        col_inp, col_btn = st.columns([5, 1])
        with col_inp:
            user_input = st.text_input("", placeholder="Ask me about DSA, ML, resume, interviews, salary...", label_visibility="collapsed")
        with col_btn:
            send = st.form_submit_button("Send 🚀", use_container_width=True)

    if send and user_input.strip():
        response = get_response(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "bot", "content": response})
        st.rerun()

    if len(st.session_state.messages) > 1:
        if st.button("🗑️ Clear Chat", key="clear_chat"):
            st.session_state.messages = [st.session_state.messages[0]]
            st.rerun()
