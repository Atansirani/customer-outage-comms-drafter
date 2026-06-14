#  Customer Outage Communications Drafter

## Overview

Customer Outage Communications Drafter is an AI-powered web application that helps Production Support and Site Reliability Engineering (SRE) teams generate professional customer-facing outage communications from technical incident timelines.

During production incidents, engineers often communicate using highly technical terminology that may be difficult for customers to understand. This solution automatically transforms technical outage details into clear, concise, and customer-friendly status updates.

The application leverages Google's Gemini AI model along with an AI-agent workflow to generate communication drafts in multiple stages of an incident lifecycle.

---

## Problem Statement

During service outages:

* Engineers focus primarily on troubleshooting and recovery.
* Customer communications are often delayed.
* Technical updates may contain jargon unsuitable for customers.
* Communication quality varies across teams.

These challenges can lead to:

* Reduced customer trust
* Increased support tickets
* Poor incident communication experience
* Inconsistent messaging

This project addresses these challenges by automatically generating customer-ready communications in seconds.

---

## Solution

The application accepts:

* Technical outage timeline
* Incident severity
* Desired communication tone

and automatically generates:

### 📢 Initial Update

First communication informing customers about the incident.

### 🔄 In Progress Update

Status update communicating investigation and recovery progress.

### ✅ Resolved Update

Final communication confirming restoration of services.

---

## Key Features

### AI-Powered Communication Generation

Uses Google's Gemini AI model to convert technical events into customer-friendly language.

### Tone Customization

Supports multiple communication styles:

* Calm
* Empathetic
* Concise

### Severity-Aware Processing

The AI Agent analyzes outage details and considers severity while generating communications.

### Professional Web Interface

Interactive Streamlit-based UI enabling rapid communication generation.

### AI Agent Workflow

The solution implements an agent-based workflow:

1. Timeline Analysis
2. Severity Detection
3. Prompt Construction
4. AI Content Generation
5. Response Delivery

### Secure Configuration

API keys are managed using environment variables and excluded from version control.

---

## System Architecture

```text
Engineer Input
      │
      ▼
Technical Timeline
      │
      ▼
AI Agent Analysis
      │
      ├── Severity Detection
      ├── Prompt Engineering
      └── Context Preparation
      │
      ▼
Gemini AI Model
      │
      ▼
Generated Communications
      │
      ▼
Streamlit User Interface
```

---

## Technology Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| Frontend        | Streamlit               |
| Backend         | Python                  |
| AI Model        | Google Gemini 2.5 Flash |
| Configuration   | python-dotenv           |
| Version Control | Git & GitHub            |

---

## Project Structure

```text
Customer-Outage-Comms-Drafter/
│
├── app.py
├── agent.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── docs/
│   ├── AI_Usage_Note.md
│   ├── Architecture.md
│   └── prompts.md
│
├── sample_data/
│   ├── sample_input.txt
│   └── sample_output.txt
│
├── tests/
│   └── test_agent.py
│
├── resumes/
│   ├── Arnipalli_Tansi_Rani_Resume.pdf
│   ├── Yadagiri_Charishma_Resume.pdf
│   ├── Rohit_Sharma_Resume.pdf
│   └── Chukkala_Lavanya_Siri_Resume.pdf
```

---

## Testing

Basic test cases have been implemented to validate core agent functionality.

Run tests using:

```bash
python -m pytest tests/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Atansirani/customer-outage-comms-drafter.git
cd customer-outage-comms-drafter
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
python -m streamlit run app.py
```

---

## Sample Input

```text
10:05 Database cluster unavailable
10:12 Root cause identified
10:30 Failover initiated
10:45 Recovery in progress
11:00 Service restored
```

---

## Sample Output

### Initial Update

We are currently experiencing an unexpected service interruption affecting some users. Our teams are actively investigating and working to restore normal service.

### In Progress Update

The underlying issue has been identified and recovery activities are underway. Our teams continue to work diligently toward full restoration.

### Resolved Update

The issue has been fully resolved and all services have been restored. We sincerely apologize for the inconvenience and appreciate your patience.

---

## Assumptions

* User provides a valid outage timeline.
* Internet connectivity is available.
* Gemini API services are accessible.

---

## Limitations

* Severity analysis currently uses rule-based keyword detection.
* Generated content may require human approval before external communication.
* Depends on external AI service availability.

---

## AI Capability Demonstrated

This prototype demonstrates an AI Agent workflow:

1. Accept technical outage timeline input.
2. Analyze outage severity.
3. Construct contextual prompts.
4. Invoke Gemini 2.5 Flash for communication generation.
5. Validate and display structured customer updates.
6. Export generated communications.

The system demonstrates:

* LLM-powered content generation
* Prompt engineering
* Agent-based decision flow
* Structured communication output

---

## Future Enhancements

* Multi-language support
* Automatic severity classification using AI
* Incident summary generation
* Email integration
* Slack / Microsoft Teams integration
* Historical incident analytics
* PDF communication reports

---

## AI Usage

This project was developed using AI-assisted software development practices.

AI was used for:

* Code generation assistance
* Prompt engineering
* UI prototyping
* Documentation assistance
* Testing support

All generated code was reviewed, tested, and validated by the development team.

---

## Demo Video

Demo Video Link:

https://drive.google.com/file/d/1RFvqpkAbMqpwySXnjClI5boM1HY1YgKL/view?usp=sharing

---

## Team Members (Team No 3)

| Name                    | Role                                          |
| --------------------    | --------------------------------------------- |
| Arnipalli Tansi Rani    | UI Development, AI Integration, Documentation |
| Yadagiri Charishma      | Backend Logic & Processing                    |
| Rohit Sharma            | Testing & Validation                          |
| Chukkala Lavanya Siri   | Documentation & Demo Video                    |

---

## Team Documents

The resumes of all team members are available in the `resumes/` directory.


