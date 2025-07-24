# from app.langgraph_flow.daily_tracker import build_emotion_graph

# graph = build_emotion_graph()

# output = graph.invoke({
#     "problem_text": "My boss ignored my input in a meeting.",
#     "reaction_text": "I stayed silent and felt disappointed."
# })

# print(output)
from app.langgraph_flow.daily_tracker import build_emotion_graph

graph = build_emotion_graph()

# Input state (this must include 'entry_text' and optionally 'user_id')
state = {
    "user_id": 1,  # Optional, but recommended
    "entry_text": "My boss ignored my input in a meeting. I stayed silent and felt disappointed.",
    "problem_text": "My boss ignored my input in a meeting.",
    "reaction_text": "I stayed silent and felt disappointed.",
    "classified_emotion": "",   # These will be filled by the LLM
    "trigger_source": ""
}

result = graph.invoke(state)
print(result)
