from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
from config import DB_PATH,DB_TYPES
# SQLAlchemy 2.0 ga mos ravishda deklarativ bazani yaratish
Base = declarative_base()

class UserSettings(Base):
    __tablename__ = 'user_settings'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True, nullable=False)
    language = Column(String, nullable=True)

# SQLite ma'lumotlar bazasining manzili 
DATABASE_URL = f'{DB_TYPES}{DB_PATH}'
engine = create_engine(DATABASE_URL, echo=False)

# Jadvalni yaratish
def db_init():
    Base.metadata.create_all(engine)


db_init()
# Sessiya ishlab chiqaruvchisini yaratish
SessionLocal = sessionmaker(bind=engine)

def add_user_settings(user_id, language):
    """Foydalanuvchi sozlamalarini qo'shish"""
    with SessionLocal() as session:
        user_settings = UserSettings(user_id=user_id, language=language)
        try:
            session.add(user_settings)
            session.commit()
        except IntegrityError:
            session.rollback()
            print(f"User ID {user_id} already exists.")

def get_user_settings(user_id):
    """Foydalanuvchi sozlamalarini olish"""
    with SessionLocal() as session:
        return session.query(UserSettings).filter_by(user_id=user_id).first()

def update_user_settings(user_id, language):
    """Foydalanuvchi sozlamalarini yangilash"""
    with SessionLocal() as session:
        settings = session.query(UserSettings).filter_by(user_id=user_id).first()
        if settings:
            settings.language = language
            session.commit()
        else:
            print(f"No settings found for user ID {user_id}")

def get_all_user_ids():
    """Barcha foydalanuvchilarning user_id larini olish"""
    with SessionLocal() as session:
        user_ids = session.query(UserSettings.user_id).all()
        return [user_id[0] for user_id in user_ids]  # [(6061010090,), (12345678,)] -> [6061010090, 12345678]

# # Test qilish
# user_id = 6061010090

# # Foydalanuvchi sozlamalarini qo'shish
# add_user_settings(user_id, 'uz')
# add_user_settings(12345678, 'ru')  # Yangi foydalanuvchi qo‘shish

# # Foydalanuvchi sozlamalarini olish
# settings = get_user_settings(user_id)
# print(f"User settings: {settings.language}" if settings else "No settings found")

# # Foydalanuvchi sozlamalarini yangilash
# update_user_settings(user_id, 'en')

# # Yangilangan sozlamalarni olish
# updated_settings = get_user_settings(user_id)
# print(f"Updated user settings: {updated_settings.language}" if updated_settings else "No settings found")

# Barcha user_id larni olish
# all_user_ids = get_all_user_ids()
# invite_link=""
# for id in all_user_ids:
#     invite_link += f"[{id}](tg://user?id={id})\n"
# print(invite_link)
# all_user_cout=len(all_user_ids)
# print(f"All User IDs: {all_user_ids}")
# print(f"Barcha foydalanuvchilar soni: {all_user_cout}")
