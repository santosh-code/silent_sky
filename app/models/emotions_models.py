from sqlalchemy import Column, Integer, String, Text, Time, DateTime, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from app.db.session import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    occupation = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    sleep_time = Column(Time, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Optional Personalization Fields
    reflection_window_minutes = Column(Integer, default=30)
    preferred_scripture = Column(String(50), default="All")  # Gita, Bible, Quran, All
    wants_affirmations = Column(Boolean, default=True)
    wants_notifications = Column(Boolean, default=True)
    sees_therapist = Column(Boolean, default=False)
    crisis_support_opt_in = Column(Boolean, default=False)
    primary_goal = Column(String(200))
    is_spiritual = Column(Boolean, default=True)
    language = Column(String(50), default="English")


class CoreProblem(Base):
    __tablename__ = "core_problems"

    core_problem_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    summary = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


class EmotionEntry(Base):
    __tablename__ = "emotion_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    entry_text = Column(Text)
    problem_text = Column(Text)
    reaction_text = Column(Text)
    classified_emotion = Column(String(100))
    trigger_source = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    core_problem_id = Column(Integer, ForeignKey("core_problems.core_problem_id"))


class SpiritualResponse(Base):
    __tablename__ = "spiritual_responses"

    response_id = Column(Integer, primary_key=True, index=True)
    core_problem_id = Column(Integer, ForeignKey("core_problems.core_problem_id"))
    source = Column(String(50))  # Gita, Bible, Quran
    insight = Column(Text)
    affirmation = Column(Text)
    strategy = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
