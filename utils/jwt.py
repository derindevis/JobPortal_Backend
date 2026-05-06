# jwt is used to create and read the token; datetime handles the expiry
from jose import jwt
from datetime import datetime, timedelta, timezone

# SECRET_KEY is a unique string used to sign your tokens so they can't be faked
SECRET_KEY = ("SECRET_KEY", "your_secret_key_here")
# HS256 is the standard algorithm used to sign the JWT[cite: 4]
ALGORITHM = "HS256"
# This sets how long the user stays logged in (e.g., 60 minutes)[cite: 4]
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# This function creates the actual "ID card" string[cite: 4]
def create_access_token(username: str):
    # we copy the data we want to hide in the token (the username)[cite: 4]
    to_encode = {"sub": username}
    # calculate the time when the token should stop working[cite: 4]
    expire = datetime.now(datetime.timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # add that expiry time to our data[cite: 4]
    to_encode.update({"exp": expire})
    # create the final signed token string[cite: 4]
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# This function reads the token to see who the user is[cite: 4]
def verify_access_token(token: str):
    # decode looks at the token and checks if our SECRET_KEY signed it[cite: 4]
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    # if it's valid, it returns the username (sub) stored inside[cite: 4]
    return payload.get("sub")