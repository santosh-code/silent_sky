from app.db.session import engine, Base
from app.models import emotions_models  # ✅ This is enough to load User, EmotionEntry, CoreProblem

# Recreate tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("✅ All tables dropped (if any) and recreated successfully.")