from typing import TypedDict
from app.services.llm_handler import classify_with_groq
from app.services.db_handler import save_emotion_entry
from langgraph.graph import StateGraph, END, START
from langchain_core.runnables import RunnableLambda

# Updated EmotionState schema
class EmotionState(TypedDict):
    problem_text: str
    reaction_text: str
    classified_emotion: str
    trigger_source: str

# Updated classify function: sends both inputs to LLM
def classify_entry(state: EmotionState) -> EmotionState:
    result = classify_with_groq(state["problem_text"], state["reaction_text"])
    return {**state, **result}

def build_emotion_graph():
    builder = StateGraph(EmotionState)
    builder.add_node("classify", RunnableLambda(classify_entry))
    builder.add_node("save_to_db", RunnableLambda(save_emotion_entry))
    builder.set_entry_point("classify")
    builder.add_edge("classify", "save_to_db")
    builder.set_finish_point("save_to_db")
    return builder.compile()
