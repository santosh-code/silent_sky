import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# Initialize Groq LLM (LLaMA3 or Mixtral)
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192"
)

def classify_with_groq(problem_text: str, reaction_text: str) -> dict:
    system_prompt = """You are a helpful emotion analysis assistant.
Given a user's problem and their reaction, classify the emotion they felt and the source of the trigger.

Respond ONLY in valid JSON format like this:
{
  "classified_emotion": "...",
  "trigger_source": "..."
} 
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Problem: {problem_text}\nReaction: {reaction_text}")
    ]

    result = llm.invoke(messages)

    try:
        parsed = json.loads(result.content)
        return {
            "classified_emotion": parsed.get("classified_emotion", "Unknown"),
            "trigger_source": parsed.get("trigger_source", "Unknown")
        }
    except json.JSONDecodeError:
        return {
            "classified_emotion": "Unknown",
            "trigger_source": "Unknown"
        }
