"""
skill_analyzer.py — Skill Gap Analyzer Module
Compares student skills against role requirements and visualizes gaps.
"""

import plotly.graph_objects as go

ROLE_SKILLS = {
    "Software Development Engineer (SDE)": {
        "DSA & Algorithms": 95,
        "OOP Concepts": 90,
        "System Design": 80,
        "Database (SQL/NoSQL)": 75,
        "Problem Solving (CP)": 85,
        "Git & Version Control": 70,
        "Operating Systems": 70,
        "Computer Networks": 65,
    },
    "Data Scientist": {
        "Machine Learning": 95,
        "Python / R": 90,
        "Statistics & Probability": 85,
        "Data Visualization": 80,
        "Deep Learning": 75,
        "SQL & Data Wrangling": 80,
        "Feature Engineering": 75,
        "Big Data Tools": 60,
    },
    "Full Stack Developer": {
        "HTML / CSS / JS": 95,
        "React / Vue / Angular": 85,
        "Node.js / Django / Flask": 80,
        "REST APIs": 85,
        "Database (SQL/NoSQL)": 75,
        "Git & Version Control": 80,
        "Docker / Cloud Basics": 65,
        "UI/UX Principles": 60,
    },
    "ML Engineer": {
        "Machine Learning": 95,
        "Deep Learning / PyTorch": 90,
        "Python (NumPy, Pandas)": 90,
        "MLOps / Model Deployment": 80,
        "Cloud (AWS/GCP/Azure)": 75,
        "Feature Engineering": 80,
        "Computer Vision / NLP": 70,
        "Docker / Kubernetes": 65,
    },
    "DevOps / Cloud Engineer": {
        "Linux & Shell Scripting": 90,
        "Docker & Kubernetes": 90,
        "CI/CD Pipelines": 85,
        "Cloud (AWS/GCP/Azure)": 90,
        "Monitoring & Logging": 75,
        "Infrastructure as Code": 70,
        "Networking Fundamentals": 80,
        "Git & Version Control": 75,
    },
    "Cybersecurity Analyst": {
        "Networking & Protocols": 90,
        "Linux & Shell Scripting": 85,
        "Ethical Hacking Tools": 80,
        "Cryptography Basics": 75,
        "OWASP / Web Security": 85,
        "SIEM Tools": 70,
        "Incident Response": 70,
        "Risk Assessment": 65,
    },
}


def get_roles():
    return list(ROLE_SKILLS.keys())


def analyze_gap(role: str, student_skills: dict) -> dict:
    """
    Compare student skill levels (0-100) against role requirements.
    Returns a dict with skill, required, student, and gap.
    """
    required = ROLE_SKILLS.get(role, {})
    result = []
    for skill, req_level in required.items():
        student_level = student_skills.get(skill, 0)
        gap = max(0, req_level - student_level)
        result.append({
            "skill": skill,
            "required": req_level,
            "yours": student_level,
            "gap": gap,
        })
    return result


def make_gap_chart(analysis: list) -> go.Figure:
    """Return a Plotly horizontal bar chart showing required vs student skills."""
    skills = [r["skill"] for r in analysis]
    required = [r["required"] for r in analysis]
    yours = [r["yours"] for r in analysis]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Required",
        y=skills,
        x=required,
        orientation='h',
        marker_color='rgba(130, 80, 255, 0.5)',
        marker_line_color='rgba(130, 80, 255, 1)',
        marker_line_width=1.5,
    ))
    fig.add_trace(go.Bar(
        name="Your Level",
        y=skills,
        x=yours,
        orientation='h',
        marker_color='rgba(0, 212, 170, 0.8)',
    ))
    fig.update_layout(
        barmode='overlay',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Inter', size=13),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, font=dict(color='white')),
        xaxis=dict(range=[0, 100], gridcolor='rgba(255,255,255,0.08)', tickfont=dict(color='white')),
        yaxis=dict(gridcolor='rgba(255,255,255,0.05)', tickfont=dict(color='white')),
        margin=dict(l=10, r=20, t=40, b=20),
        height=380,
    )
    return fig
