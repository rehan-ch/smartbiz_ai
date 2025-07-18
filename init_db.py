from app.db.session import engine
from app.db.base import Base
from app.models.product import Product
from app.models.category import Category


def init_db():
    print("📦 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully")


if __name__ == "__main__":
    init_db()
