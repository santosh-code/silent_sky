from app.db.session import SessionLocal
from app.models.emotions_models import User, EmotionEntry
from datetime import time, datetime

def test_insert_user_and_entry():
    db = SessionLocal()

    # 1. Create test user
    user = User(
        name="Test User",
        email="test@silentsky.app",
        sleep_time=time(22, 30)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    # 2. Add test emotion entry
    entry = EmotionEntry(
        user_id=user.user_id,
        entry_text="My manager shouted at me in the morning.",
        problem_text="Manager shouting in front of team",
        reaction_text="Stayed silent, felt ashamed",
        classified_emotion="Anger",
        trigger_source="Manager",
        timestamp=datetime.utcnow()
    )
    db.add(entry)
    db.commit()

    print("✅ Test user and entry inserted successfully.")

if __name__ == "__main__":
    test_insert_user_and_entry()
