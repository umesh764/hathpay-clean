from app import create_app
from modules.models import db

print("🚀 Creating database...")
app = create_app()
with app.app_context():
    db.create_all()
    print("✅ Database created successfully!")