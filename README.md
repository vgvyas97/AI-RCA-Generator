# 📟 AI-Driven Root Cause Analysis (RCA) Generator

An automated, AIOps-focused web application designed to significantly reduce Mean Time to Repair (MTTR) and eliminate manual post-mortem overhead. This tool ingests raw cloud metrics, system events, and application logs, utilizing Large Language Models (LLMs) to instantly synthesize production-grade Root Cause Analysis (RCA) reports.

## 🚀 The Operational Problem Solved
During a high-severity production outage, engineering teams waste critical cycles manually digging through fragmented data across logging platforms and metrics dashboards. Post-incident reporting often takes hours of manual synthesis. 

**This solution automates the triage and documentation phase**, transforming chaotic infrastructure telemetry into an actionable, structured SRE incident report within seconds.

---

## 🛠️ Architecture & Tech Stack

* **Frontend Framework:** Streamlit (Python-native UI)
* **AI Orchestration:** OpenAI API (GPT-4o-mini engine)
* **Data Format:** Markdown-optimized incident documentation

---

## ⚙️ Core Features
* **Raw Telemetry Ingestion:** Accepts unstructured, messy multi-line logs, CPU/Memory metrics, and API gateway response traces.
* **Deterministic Prompt Engineering:** Uses system-level guardrails to force the LLM to act as a Principal Site Reliability Engineer, avoiding AI hallucinations and ensuring technical accuracy.
* **Production-Ready Document Output:** Auto-generates high-quality Markdown sheets including Executive Summaries, Incident Timelines, Root Cause Determinations, and Action Items.

---

## 💻 Local Setup & Execution

### Prerequisites
* Python 3.9 or higher installed
* An OpenAI API Key

### Installation Steps
1. Clone this repository to your machine:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-rca-generator.git](https://github.com/YOUR_GITHUB_USERNAME/ai-rca-generator.git)
   cd ai-rca-generator
