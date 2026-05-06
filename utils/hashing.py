# utils/hashing.py
from passlib.context import CryptContext

# bcrypt is the hashing algorithm — industry standard for passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Converts plain text password to bcrypt hash."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Returns True if plain_password matches the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)

