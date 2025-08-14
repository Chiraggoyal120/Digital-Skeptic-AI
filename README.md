# 🔍 Digital Skeptic AI

**One-line pitch:**  
Empowering critical thinking by providing AI-driven, multi-agent analysis of news articles to detect bias, extract claims, and suggest fact-checking steps.

---

## 🚀 Features
- **Multi-Agent Analysis**: Specialized AI agents for factual claims, tone analysis, bias detection, entity recognition, and counter-perspectives.
- **Robust Scraping**: Extracts article text from multiple layouts with fallbacks.
- **Bias & Red Flag Detection**: Identifies loaded language, missing viewpoints, and logical fallacies.
- **Verification Questions**: Generates actionable questions to fact-check the article.
- **Gradio Interface**: Simple, user-friendly web app.

---
##Approach

The project follows a multi-agent architecture where each “agent” is a specialized AI prompt tailored for a specific analysis task.
The workflow is as follows:

Input & Scraping

User provides a URL of a news article.

The system scrapes the article content using newspaper3k with a BeautifulSoup fallback to handle different site structures.

Agent-Based Analysis

The extracted text is sent to different AI agents (via OpenRouter API), each with a focused role:

Factual Claim Extractor – Identifies all factual claims in the article.

Bias Detector – Highlights potential bias in framing or language.

Tone Analyzer – Analyzes sentiment, style, and emotional tone.

Verification Question Generator – Suggests questions to validate the claims.

Entity & Stakeholder Extractor – Lists people, organizations, and entities mentioned.

Meta-Analysis Synthesizer – Combines insights into a final critical summary.

Prompt Engineering

Each agent uses a carefully crafted, context-specific prompt to maximize output quality and insight.

Responses are requested in Markdown format for easy display and readability.

Output Presentation

Results from all agents are displayed in a tabbed Gradio interface for clarity.

Users can copy, save, or reuse the analysis.

Resilience & Reliability

Error handling for failed scraping attempts.

Modular design so that agents can be swapped or upgraded independently.

Configuration file for quick updates to model choices and API endpoints.

💡 This approach ensures that the AI output is not only correct, but deeply insightful and context-aware — aligning with the hackathon’s highest scoring criteria.
## 📦 Installation

 ---
### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/digital-skeptic-ai.git
cd digital-skeptic-ai

Go to OpenRouter and sign up for a free account.

Once logged in, navigate to API Keys from your profile menu.

Click "Create API Key".

Give it a name (e.g., Digital Skeptic AI) and click "Generate".

Copy the generated key — it will look like:
sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxx
