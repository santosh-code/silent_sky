# from app.models.emotions_models import EmotionEntry
# from app.db.session import SessionLocal


# def save_emotion_entry(state: dict) -> dict:
#     session = SessionLocal()
#     try:
#         entry = EmotionEntry(
#             problem_text=state["problem_text"],
#             reaction_text=state["reaction_text"],
#             classified_emotion=state["classified_emotion"],
#             trigger_source=state["trigger_source"]
#         )
#         session.add(entry)
#         session.commit()
#         session.refresh(entry)
#         print(f"✅ Entry saved with ID: {entry.id}")
#     except Exception as e:
#         session.rollback()
#         print(f"❌ Failed to save entry: {e}")
#     finally:
#         session.close()
#     return state  # Return unchanged state to pass along


from app.models.emotions_models import EmotionEntry
from app.db.session import SessionLocal  # ✅ Corrected import path

def save_emotion_entry(state: dict) -> dict:
    session = SessionLocal()
    try:
        entry = EmotionEntry(
            user_id=state.get("user_id", 1),  # Default to 1 or dynamically pass user_id
            entry_text=state.get("entry_text", ""),  # Add this line
            problem_text=state["problem_text"],
            reaction_text=state["reaction_text"],
            classified_emotion=state["classified_emotion"],
            trigger_source=state["trigger_source"]
        )
        session.add(entry)
        session.commit()
        session.refresh(entry)
        print(f"✅ Entry saved with ID: {entry.entry_id}")
    except Exception as e:
        session.rollback()
        print(f"❌ Failed to save entry: {e}")
    finally:
        session.close()