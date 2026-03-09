"""
resume_analyzer.py — Resume Text Analyzer Module
Extracts skills, entities, and gives improvement suggestions.
"""

import re

SKILL_KEYWORDS = {
    "Programming Languages": [
        "python", "java", "c++", "c#", "javascript", "typescript", "go", "rust",
        "kotlin", "swift", "scala", "r", "matlab", "perl", "ruby",
    ],
    "Web Technologies": [
        "html", "css", "react", "angular", "vue", "node.js", "express", "django",
        "flask", "fastapi", "bootstrap", "tailwind", "next.js", "graphql",
    ],
    "Data & AI": [
        "machine learning", "deep learning", "nlp", "computer vision", "tensorflow",
        "pytorch", "keras", "scikit-learn", "pandas", "numpy", "matplotlib",
        "seaborn", "plotly", "opencv", "hugging face", "transformers", "llm",
    ],
    "Databases": [
        "sql", "mysql", "postgresql", "mongodb", "redis", "cassandra",
        "elasticsearch", "sqlite", "oracle", "firebase",
    ],
    "Cloud & DevOps": [
        "aws", "azure", "gcp", "docker", "kubernetes", "terraform", "ci/cd",
        "jenkins", "github actions", "linux", "bash", "ansible",
    ],
    "Tools & Practices": [
        "git", "github", "jira", "agile", "scrum", "rest api", "microservices",
        "system design", "data structures", "algorithms", "leetcode",
    ],
}

SECTION_KEYWORDS = {
    "Education": ["education", "university", "college", "degree", "b.tech", "b.e", "m.tech", "bsc", "msc", "gpa", "cgpa"],
    "Experience / Internship": ["internship", "intern", "experience", "worked at", "company", "role"],
    "Projects": ["project", "developed", "built", "implemented", "created", "designed"],
    "Certifications": ["certified", "certification", "coursera", "udemy", "nptel", "aws certified"],
    "Achievements": ["winner", "hackathon", "rank", "awarded", "scholarship", "medal"],
}


def extract_email(text: str):
    match = re.search(r'[\w.\-+]+@[\w.\-]+\.[a-zA-Z]{2,}', text)
    return match.group(0) if match else None


def extract_phone(text: str):
    match = re.search(r'(\+91[\-\s]?)?[6-9]\d{9}', text)
    return match.group(0) if match else None


def extract_links(text: str):
    links = re.findall(r'https?://[^\s]+', text)
    return links


def extract_skills(text: str):
    text_lower = text.lower()
    found = {}
    for category, skills in SKILL_KEYWORDS.items():
        matched = [s for s in skills if re.search(r'\b' + re.escape(s) + r'\b', text_lower)]
        if matched:
            found[category] = matched
    return found


def detect_sections(text: str):
    text_lower = text.lower()
    detected = []
    for section, keywords in SECTION_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            detected.append(section)
    return detected


def generate_suggestions(skills_found: dict, sections: list, email, phone) -> list:
    suggestions = []
    total_skills = sum(len(v) for v in skills_found.values())

    if total_skills < 5:
        suggestions.append("📌 Add more technical skills (aim for 10–20 keywords relevant to your target role).")
    if "Projects" not in sections:
        suggestions.append("📌 Add a dedicated Projects section with 2–3 impactful projects.")
    if "Experience / Internship" not in sections:
        suggestions.append("📌 Include any internship or work experience, even if it's a small project.")
    if "Achievements" not in sections:
        suggestions.append("📌 Mention achievements: hackathons, competitive programming ranks, scholarships.")
    if "Certifications" not in sections:
        suggestions.append("📌 Add certifications (Coursera, AWS, NPTEL, etc.) to boost credibility.")
    if not email:
        suggestions.append("📌 Include a professional email address.")
    if not phone:
        suggestions.append("📌 Include a phone number for recruiter contact.")
    if "Data & AI" not in skills_found and "Programming Languages" not in skills_found:
        suggestions.append("📌 Add core programming skills and any AI/ML experience you have.")

    if not suggestions:
        suggestions.append("✅ Your resume looks well-structured! Focus on quantifying your impact (use numbers).")
    return suggestions


def analyze_resume(text: str) -> dict:
    """Full pipeline: extract everything and generate suggestions."""
    email = extract_email(text)
    phone = extract_phone(text)
    links = extract_links(text)
    skills = extract_skills(text)
    sections = detect_sections(text)
    suggestions = generate_suggestions(skills, sections, email, phone)
    word_count = len(text.split())

    return {
        "email": email,
        "phone": phone,
        "links": links,
        "skills": skills,
        "sections": sections,
        "suggestions": suggestions,
        "word_count": word_count,
        "total_skills": sum(len(v) for v in skills.values()),
    }
