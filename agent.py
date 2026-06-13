from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)
def analyze_severity(timeline):

    timeline = timeline.lower()

    critical_words = [
        "outage",
        "down",
        "unavailable",
        "failure",
        "critical"
    ]

    high_words = [
        "degraded",
        "latency",
        "slow",
        "performance"
    ]

    critical_score = sum(
        1 for word in critical_words
        if word in timeline
    )

    high_score = sum(
        1 for word in high_words
        if word in timeline
    )

    if critical_score >= 1:
        return "Critical"

    if high_score >= 1:
        return "High"

    return "Medium"

    return "Medium"


def build_prompt(timeline, severity, tone):

    return f"""
You are a production support communication specialist.

Business Rules:
- Avoid technical jargon completely
- Never mention databases, failovers, servers, clusters, root cause analysis, infrastructure, or engineering details
- Use customer-friendly language
- Professional wording
- Focus on service impact and restoration progress
- Keep updates concise and reassuring
- Use clear business communication style
- Do not expose internal technical details
- Tone must be {tone}
- Severity level is {severity}

Generate:

Generate exactly in this format:

INITIAL UPDATE:
(2-3 sentences)

===

IN PROGRESS UPDATE:
(2-3 sentences)

===

RESOLVED UPDATE:
(2-3 sentences)


Timeline:
{timeline}
"""


def generate_outage_updates(timeline, severity, tone):

    detected_severity = analyze_severity(timeline)

    prompt = build_prompt(
    timeline,
    detected_severity,
    tone
)
    

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text