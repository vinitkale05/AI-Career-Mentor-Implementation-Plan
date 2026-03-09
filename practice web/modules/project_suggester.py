"""
project_suggester.py — AI Project Idea Suggester
Curated unique project ideas with tech stacks and difficulty levels.
"""

PROJECTS = [
    {
        "title": "AI Resume Screener",
        "domain": "AI/ML",
        "description": "Automatically screen resumes for job fitness using NLP and cosine similarity. Rank candidates and explain decisions.",
        "tech": ["Python", "spaCy / NLTK", "Scikit-learn", "Streamlit"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "🏆 Placement Gold",
    },
    {
        "title": "Smart Interview Trainer",
        "domain": "AI/ML",
        "description": "Generate role-specific mock interview questions, evaluate answers via NLP, and give confidence score feedback.",
        "tech": ["Python", "Transformers (Hugging Face)", "Streamlit", "SpeechRecognition"],
        "difficulty": "Advanced",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "🔥 Trending",
    },
    {
        "title": "Fake News Detector",
        "domain": "NLP",
        "description": "Classify news articles as real or fake using TF-IDF + LSTM. Deploy as a web extension.",
        "tech": ["Python", "Scikit-learn", "TensorFlow/Keras", "Flask"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐",
        "tag": "📰 Social Impact",
    },
    {
        "title": "Stock Price Predictor",
        "domain": "Data Science",
        "description": "Predict next-day stock prices using LSTM on historical data. Include live chart dashboard.",
        "tech": ["Python", "yFinance", "TensorFlow/Keras", "Plotly Dash"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐",
        "tag": "📈 Finance AI",
    },
    {
        "title": "AI Handwriting to Text",
        "domain": "Computer Vision",
        "description": "Convert handwritten notes from images to digital text using CNN + CTC loss (OCR pipeline).",
        "tech": ["Python", "OpenCV", "TensorFlow", "Tesseract OCR"],
        "difficulty": "Advanced",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "🖊️ CV Project",
    },
    {
        "title": "Mental Health Chatbot",
        "domain": "NLP",
        "description": "An empathetic chatbot that detects stress/anxiety from text and suggests coping strategies. Uses sentiment analysis.",
        "tech": ["Python", "Transformers", "Streamlit", "VADER Sentiment"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "💚 Social Good",
    },
    {
        "title": "Real-Time Object Detection App",
        "domain": "Computer Vision",
        "description": "Live webcam object detection using YOLOv8. Deploy on a Streamlit web app with class labels and confidence.",
        "tech": ["Python", "YOLOv8 (Ultralytics)", "OpenCV", "Streamlit"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐",
        "tag": "📷 Vision AI",
    },
    {
        "title": "Code Bug Fixer AI",
        "domain": "AI/ML",
        "description": "Paste buggy code and get explanations + fixes using a fine-tuned LLM or CodeLlama API.",
        "tech": ["Python", "OpenAI API / Ollama", "Streamlit", "LangChain"],
        "difficulty": "Advanced",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "🤖 GenAI",
    },
    {
        "title": "Crop Disease Detector",
        "domain": "Computer Vision",
        "description": "Upload a photo of a crop leaf and detect diseases using a CNN trained on PlantVillage dataset.",
        "tech": ["Python", "TensorFlow/Keras", "Streamlit", "PIL"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐",
        "tag": "🌾 AgriTech",
    },
    {
        "title": "AI Music Mood Classifier",
        "domain": "Data Science",
        "description": "Analyze Spotify audio features to classify song mood (happy, sad, energetic). Suggest playlists.",
        "tech": ["Python", "Spotipy API", "Scikit-learn", "Plotly"],
        "difficulty": "Beginner",
        "impact": "⭐⭐⭐",
        "tag": "🎵 Fun & Creative",
    },
    {
        "title": "E-commerce Recommendation Engine",
        "domain": "Data Science",
        "description": "Build a collaborative filtering recommendation system for products. Include a live demo UI.",
        "tech": ["Python", "Scikit-learn", "Pandas", "Streamlit / Flask"],
        "difficulty": "Intermediate",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "🛒 Industry Use",
    },
    {
        "title": "Sign Language Translator",
        "domain": "Computer Vision",
        "description": "Translate hand gestures (ASL) to text/speech in real-time using MediaPipe + CNN.",
        "tech": ["Python", "MediaPipe", "TensorFlow", "OpenCV", "pyttsx3"],
        "difficulty": "Advanced",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "♿ Accessibility",
    },
    {
        "title": "Traffic Violation Detector",
        "domain": "Computer Vision",
        "description": "Detect red-light jumping and helmetless riders in traffic video using YOLO + tracking.",
        "tech": ["Python", "YOLOv8", "OpenCV", "DeepSort"],
        "difficulty": "Advanced",
        "impact": "⭐⭐⭐⭐",
        "tag": "🚦 Smart City",
    },
    {
        "title": "AI Study Planner",
        "domain": "AI/ML",
        "description": "Input exam syllabus and time left. AI generates an optimized daily study schedule using constraint satisfaction.",
        "tech": ["Python", "Streamlit", "Pandas", "OpenAI API"],
        "difficulty": "Beginner",
        "impact": "⭐⭐⭐⭐",
        "tag": "📚 EdTech",
    },
    {
        "title": "Deepfake Face Detector",
        "domain": "Computer Vision",
        "description": "Detect AI-generated/deepfake faces in images using a CNN trained on real vs fake datasets.",
        "tech": ["Python", "TensorFlow/Keras", "OpenCV", "Streamlit"],
        "difficulty": "Advanced",
        "impact": "⭐⭐⭐⭐⭐",
        "tag": "🔒 Cybersecurity AI",
    },
]


def get_domains():
    return ["All"] + sorted(set(p["domain"] for p in PROJECTS))


def get_difficulties():
    return ["All", "Beginner", "Intermediate", "Advanced"]


def filter_projects(domain="All", difficulty="All"):
    result = PROJECTS
    if domain != "All":
        result = [p for p in result if p["domain"] == domain]
    if difficulty != "All":
        result = [p for p in result if p["difficulty"] == difficulty]
    return result
