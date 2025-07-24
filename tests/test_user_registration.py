from app.db.session import SessionLocal
from app.models.emotions_models import User
from datetime import datetime, time

db = SessionLocal()

new_user = User(
    name="Aarav",
    age=27,
    occupation="Engineer",
    email="aarav@example.com",
    sleep_time=time(22, 0),  # 10:00 PM
    reflection_window_minutes=30,
    preferred_scripture="Gita",
    wants_affirmations=True,
    wants_notifications=True,
    sees_therapist=False,
    crisis_support_opt_in=True,
    primary_goal="Understand myself better",
    is_spiritual=True,
    language="English"
)

db.add(new_user)
db.commit()
db.refresh(new_user)
print(f"✅ Registered user with ID: {new_user.user_id}")
db.close()
