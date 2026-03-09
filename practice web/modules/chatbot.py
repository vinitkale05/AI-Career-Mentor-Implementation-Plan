"""
chatbot.py — Rule-Based Career Mentor Chatbot Module
Responds to student queries with career, placement, and skill advice.
"""

import random

INTENTS = {
    # Greetings
    ("hello", "hi", "hey", "howdy", "sup"): [
        "👋 Hey there! I'm your Anti-Gravity Career Mentor. Ask me anything about placements, skills, or your career!",
        "Hi! Ready to supercharge your career? What would you like to know? 🚀",
    ],
    # Resume
    ("resume", "cv", "curriculum vitae"): [
        "📄 **Resume Tips:**\n- Keep it to 1 page (for freshers)\n- Use action verbs: Built, Designed, Implemented\n- Quantify impact: 'Improved accuracy by 15%'\n- Add GitHub/LinkedIn links\n- Tailor it for each job role",
        "📌 Your resume should highlight: Skills → Projects → Internship → Education. Always lead with your strongest section!",
    ],
    # Interview
    ("interview", "interview prep", "interview tips"): [
        "🎯 **Interview Prep Plan:**\n1. DSA: Practice 2 LeetCode problems/day\n2. CS Fundamentals: OS, DBMS, Networks\n3. Projects: Know your projects inside-out\n4. HR Round: Prepare STAR method stories\n5. Mock interviews: Use Pramp or Interviewbit",
        "💡 Top Interview Tips:\n- Think aloud while solving problems\n- Ask clarifying questions\n- Discuss time & space complexity\n- Research the company beforehand",
    ],
    # DSA / Algorithms
    ("dsa", "data structures", "algorithms", "leetcode", "competitive programming"): [
        "🧩 **DSA Roadmap:**\n1. Arrays & Strings\n2. Linked Lists\n3. Stacks & Queues\n4. Trees & Graphs\n5. Dynamic Programming\n6. Sorting & Searching\n\nPlatforms: LeetCode, Codeforces, HackerRank",
        "Start with easy LeetCode problems, then medium. Aim for 150+ problems before placements. Consistency beats intensity! 💪",
    ],
    # Machine Learning
    ("machine learning", "ml", "deep learning", "ai", "artificial intelligence"): [
        "🤖 **ML Learning Path:**\n1. Python (NumPy, Pandas, Matplotlib)\n2. Statistics & Probability\n3. Scikit-learn (classic ML)\n4. Deep Learning: TensorFlow / PyTorch\n5. Projects: Kaggle competitions\n\nCertification: Andrew Ng's ML Course on Coursera",
        "🔥 For AI/ML roles, a strong portfolio matters more than your grade. Build 2-3 end-to-end projects and deploy them!",
    ],
    # Python
    ("python", "learn python", "python tips"): [
        "🐍 Python is the #1 language for AI/Data roles. Focus on:\n- OOP Concepts\n- List comprehensions\n- File I/O\n- API calling with `requests`\n- Pandas & NumPy for data work",
    ],
    # Projects
    ("project", "projects", "project ideas", "build project"): [
        "💡 Go to the **Project Suggester** tab for 15+ unique project ideas! The best projects for placements are ones that solve real problems.",
        "🚀 Project tips:\n- Deploy your projects online (Streamlit Cloud / Heroku)\n- Add a README with demo GIFs\n- Link GitHub in your resume\n- Choose projects relevant to your target role",
    ],
    # Internship
    ("internship", "intern", "how to get internship"): [
        "💼 **Internship Hunt Tips:**\n1. LinkedIn: Apply with Easy Apply filter\n2. Internshala, AngelList, Wellfound\n3. Email cold-outreach to startups\n4. Contribute to Open Source (GitHub)\n5. Attend college hackathons — companies recruit there!",
    ],
    # CGPA / Grades
    ("cgpa", "gpa", "marks", "grades", "percentage"): [
        "📊 CGPA matters for shortlisting at big companies (usually 6.5+ cutoff). But a strong portfolio and DSA skills can override a low CGPA at startups and product companies!",
    ],
    # Salary
    ("salary", "package", "ctc", "pay"): [
        "💰 Average placement packages (India, 2024):\n- Service (TCS, Infosys): ₹3.5–7 LPA\n- Product Startups: ₹8–15 LPA\n- FAANG/Top MNCs: ₹20–50+ LPA\n\nFocus on skills → the package follows! 🎯",
    ],
    # LinkedIn
    ("linkedin", "profile", "networking"): [
        "🔗 **LinkedIn Profile Tips:**\n- Professional photo\n- Keyword-rich headline (e.g., 'ML Engineer | Python | Deep Learning')\n- 500+ connections\n- Post project updates — recruiters notice!\n- Recommendations from professors/managers",
    ],
    # Skills
    ("skills", "what to learn", "which skill"): [
        "🛠️ **In-demand skills 2024:**\n- AI/ML + Python\n- Full Stack (React + Node)\n- Cloud (AWS/Azure)\n- Cybersecurity\n- Data Engineering\n\nPick ONE domain, go deep, then expand.",
    ],
    # Placement
    ("placement", "campus placement", "on campus", "off campus"): [
        "🎓 **Placement Strategy:**\n1. Start DSA prep 6 months before\n2. Build 2 solid projects\n3. Apply off-campus too (don't rely only on college)\n4. Network on LinkedIn\n5. Practice mock interviews weekly",
    ],
    # Motivation
    ("motivate", "motivation", "depressed", "stressed", "give up", "sad"): [
        "💙 It's okay to feel overwhelmed. Every developer was a beginner once. Progress > perfection. Take one step today, no matter how small. You've got this! 🚀",
        "🌟 Remember: Most successful engineers faced rejection too. Keep building, keep applying. Your breakthrough is closer than you think!",
    ],
    # Thanks
    ("thanks", "thank you", "great", "awesome", "nice"): [
        "😊 You're welcome! Keep building and keep growing. Anything else I can help with?",
        "🚀 Happy to help! Keep the momentum going. You're going to do great things!",
    ],
    # Goodbye
    ("bye", "goodbye", "see you", "exit", "quit"): [
        "👋 Good luck with your placement journey! Remember: consistency is the key. See you at the top! 🏆",
    ],
}

DEFAULT_RESPONSES = [
    "🤔 I'm not sure about that specific query. Try asking about: resume, DSA, ML, internship, projects, or interview tips!",
    "💡 Great question! Could you rephrase it? I can help with topics like: skills, placement, salary, LinkedIn, Python, etc.",
]


def get_response(user_input: str) -> str:
    """Match user input to an intent and return a response."""
    text = user_input.lower().strip()
    for keywords, responses in INTENTS.items():
        if any(kw in text for kw in keywords):
            return random.choice(responses)
    return random.choice(DEFAULT_RESPONSES)
