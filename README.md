# spring2026-genai
genai 
# 👨‍🍳 Intelligent AI Chef

**Intelligent AI Chef** -> High-precision recipe recommendations powered by Gemini 1.5 Flash.  
It utilizes advanced prompt engineering (CoT + ReAct) to transform your available ingredients, tools, and time constraints into a logical cooking plan with integrated YouTube guides.

---

## 🏗️ Architecture

```plaintext
User Input (Ingredients, Time, Tools)
        |
        v
Streamlit Frontend (Python)
        |
        +-- POST /api/generate_content (Google Gemini API)
        |      |
        |      +-- [Reasoning Layer]
        |      |     |-- Analogical Prompting: Contextualizes the chef's persona.
        |      |     |-- Chain-of-Thought (CoT): Logical breakdown of cooking steps.
        |      |     +-- ReAct Pattern: Generates search actions for external resources.
        |      |
        |      +-- [Output Generation]
        |            |-- Structured Recipe (Markdown)
        |            +-- Dynamic YouTube Search Query
        |
        v
YouTube Results Link
```

---

## 🛠️ Tech Stack

| Layer        | Technology |
|-------------|------------|
| Frontend    | Streamlit (Python-based Web Framework) |
| AI Engine   | Google Gemini 1.5 Flash |
| Language    | Python 3.10+ |
| Reasoning   | Chain-of-Thought (CoT), ReAct, Analogical Prompting |
| Integration | URI Encoding for Dynamic YouTube Linking |
| Security    | OS Environment Variable Management |

---

## ✨ Features Implemented

- **Guest-First Logic**: Immediate recipe generation without complex authentication.  
- **Constraint-Aware Reasoning**: AI strictly respects your time limit (e.g., 10 mins) and available tools (e.g., Air Fryer only).  
- **Explainable Cooking**: Uses Chain-of-Thought to explain why certain steps are prioritized for efficiency.  
- **ReAct Integration**: Automatically extracts a "YouTube Search Query" from the AI's reasoning to provide a 1-click video guide.  
- **Multimodal Ready**: Architecture designed to support future image-based ingredient recognition.  

---

## 📂 Project Structure

```plaintext
Intelligent-AI-Chef/
├── app.py              # Main application (UI + Reasoning Logic)
├── check.py            # Model availability & API diagnostic tool
├── .env                # API Key storage (Environment variables)
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## 🚀 Setup & Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/intelligent-ai-chef.git
cd intelligent-ai-chef
```

### Install dependencies:

```bash
pip install streamlit google-generativeai
```

### Configure API Key:

Get your API Key from Google AI Studio.  
Set it in your environment or directly in `app.py`.

### Run the App:

```bash
streamlit run app.py
```

---

## 📝 Reasoning Logic (CoT + ReAct)

Unlike standard LLM wrappers, this system enforces a structured thinking process:

- **Analogical**: The AI identifies a similar "base recipe" as a mental template.  
- **CoT (Chain-of-Thought)**: The AI calculates the cooking sequence.  
  Example:  
  > "Since the user only has 15 minutes, we must parboil the potatoes before frying."  
- **ReAct**: The AI concludes the reasoning by generating an "Action" — a specific search string for YouTube to validate the recipe visually.  

---

## 📑 Notes

- **Model Resilience**: Currently optimized for `gemini-1.5-flash` to ensure high rate limits and stability for free-tier users.  
- **Safety**: Prompt includes constraints to avoid dangerous ingredient combinations or hazardous tool usage.
