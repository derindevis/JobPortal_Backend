import sys
from database import SessionLocal
from models.user import User
from utils.hashing import hash_password

def create_admin(username, password):
    db = SessionLocal()
    try:
        existing = db.query(User).filter(User.username == username).first()
        if existing:
            print(f"User '{username}' already exists. Updating role to admin...")
            existing.role = "admin"
            existing.hashed_password = hash_password(password)
        else:
            print(f"Creating new admin user '{username}'...")
            new_admin = User(
                username=username,
                hashed_password=hash_password(password),
                role="admin"
            )
            db.add(new_admin)
        
        db.commit()
        print("Admin user setup successful!")
    except Exception as e:
        print(f"Error creating admin: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_admin.py <username> <password>")
        sys.exit(1)
    
    admin_username = sys.argv[1]
    admin_password = sys.argv[2]
    create_admin(admin_username, admin_password)
