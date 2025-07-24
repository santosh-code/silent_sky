from app.db.session import SessionLocal
from app.models.emotions_models import UserProfile
from datetime import time

def test_add_user():
    db = SessionLocal()

    user = UserProfile(
        name="Aarav",
        age=27,
        sleeping_time=time(22, 0),
        reflection_window_minutes=30,
        preferred_scripture="Gita",
        wants_affirmations=True,
        wants_notifications=True,
        occupation="Software Engineer",
        sees_therapist=False,
        crisis_support_opt_in=True,
        primary_goal="Understand triggers and feel better",
        is_spiritual=True,
        language="English"
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"✅ User added with ID: {user.user_id}")
    db.close()

if __name__ == "__main__":
    test_add_user()
