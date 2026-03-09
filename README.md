🚀 Anti-Gravity AI Career Mentor — Implementation Plan
A Streamlit-based AI web app that acts as a personal placement mentor for students. It predicts placement readiness, analyzes skills, suggests projects, and chats with students like a mentor.

Proposed Changes
Project Structure
practice web/
├── app.py                  # Main Streamlit app (entry point)
├── requirements.txt        # All Python dependencies
├── modules/
│   ├── __init__.py
│   ├── predictor.py        # Placement Prediction (ML - DecisionTree)
│   ├── skill_analyzer.py   # Skill Gap Analyzer
│   ├── resume_analyzer.py  # Resume text parser (NLP)
│   ├── project_suggester.py# Project recommendation engine
│   └── chatbot.py          # Rule-based career mentor chatbot
└── assets/
    └── style.css           # Custom dark-mode premium CSS theme
Core Modules
[NEW] app.py — Main Streamlit App
Multi-tab layout with animated sidebar
Tabs: 🏠 Home | 📄 Resume | 🧠 Predictor | 📊 Skill Gap | 💡 Projects | 🤖 Chatbot
Python antigravity Easter egg on launch
Gorgeous dark glassmorphism theme
[NEW] modules/predictor.py — Placement Predictor
DecisionTreeClassifier trained on synthetic student data (10+ features)
Input form: DSA, ML, Projects, Internship, CGPA, Competitive Programming, etc.
Outputs: probability score, verdict, and radar chart visualization
[NEW] modules/skill_analyzer.py — Skill Gap Analyzer
Student picks a target role (SDE, Data Scientist, Full Stack, ML Engineer, etc.)
App compares their skills vs. required skills for that role
Shows a visual gap chart (progress bars / bar chart)
[NEW] modules/resume_analyzer.py — Resume Analyzer
Accepts raw text paste of resume
Extracts: skills, keywords, email, phone, education
Shows extracted entities and improvement suggestions
Uses re (regex) + keyword matching (no heavy NLP dependency for simplicity)
[NEW] modules/project_suggester.py — Project Suggester
Shows 15+ curated unique AI/ML project ideas students rarely build
Filters by domain (Web, AI/ML, Data, Full Stack, NLP, CV)
Each project card has: title, description, tech stack, difficulty level, GitHub link format
[NEW] modules/chatbot.py — Career Mentor Chatbot
Rule-based chatbot with 30+ predefined intents
Topics: interview tips, resume advice, which language to learn, placements, salary, etc.
Styled as a real chat UI with bubbles
[NEW] requirements.txt
streamlit
pandas
scikit-learn
plotly
[NEW] assets/style.css
Dark gradient theme (purple-blue-black palette)
Glassmorphism card UI
Smooth animations for tabs and cards
Verification Plan
Manual Testing (Streamlit Local Server)
From the project directory, run:
streamlit run app.py
The browser should open automatically at http://localhost:8501
Test each tab:
Home: Verify welcome screen and antigravity Easter egg reference
Resume Analyzer: Paste sample resume text → verify skill extraction shows
Placement Predictor: Fill out form → verify prediction score and chart renders
Skill Gap: Select a target role → verify skill comparison bars appear
Project Suggester: Filter by domain → verify project cards show
Chatbot: Type "hello" / "resume tips" → verify bot replies
