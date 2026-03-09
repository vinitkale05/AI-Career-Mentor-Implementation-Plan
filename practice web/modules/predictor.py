"""
predictor.py — Placement Prediction Module
Uses a Decision Tree Classifier to predict student placement likelihood.
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
import plotly.graph_objects as go


def train_model():
    """Train a Decision Tree on synthetic student placement data."""
    data = {
        "DSA":              [1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0],
        "MachineLearning":  [1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0],
        "Projects":         [1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,0],
        "Internship":       [1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0],
        "CGPA":             [9,8,6,9,7,8,9,5,8,9,6,8,5,7,8,9,6,7,9,5],
        "CompetitiveProg":  [1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0],
        "Communication":    [1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0],
        "Placement":        [1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0],
    }
    df = pd.DataFrame(data)
    X = df.drop("Placement", axis=1)
    y = df["Placement"]
    model = DecisionTreeClassifier(max_depth=6, random_state=42)
    model.fit(X, y)
    return model


def predict_placement(dsa, ml, projects, internship, cgpa, competitive, communication):
    """Return placement probability (0-100) and verdict."""
    model = train_model()
    features = [[dsa, ml, projects, internship, cgpa, competitive, communication]]
    prob = model.predict_proba(features)[0]
    placed_prob = round(float(prob[1]) * 100 if len(prob) > 1 else float(prob[0]) * 100, 1)
    verdict = "🎉 High Placement Potential!" if placed_prob >= 60 else "⚠️ Needs Improvement"
    return placed_prob, verdict


def make_radar_chart(dsa, ml, projects, internship, cgpa_norm, competitive, communication):
    """Generate a Plotly radar chart of the student's skills."""
    categories = ["DSA", "ML", "Projects", "Internship", "CGPA", "Competitive", "Communication"]
    values = [dsa, ml, projects, internship, cgpa_norm, competitive, communication]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        name='Your Skills',
        line_color='rgba(130, 80, 255, 1)',
        fillcolor='rgba(130, 80, 255, 0.25)',
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 1], gridcolor='rgba(255,255,255,0.1)'),
            angularaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            bgcolor='rgba(0,0,0,0)',
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Inter'),
        margin=dict(t=30, b=30, l=30, r=30),
    )
    return fig
