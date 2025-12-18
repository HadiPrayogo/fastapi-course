from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, models, database
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

# 1. SECRET_KEY
# 2. Algroithm
# 3. Time
SECRET_KEY = f"{settings.secret_key}"
ALGORITHM = f"{settings.algorithm}"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expires_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credential_exception
        
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credential_exception

    return token_data

# def get_current_active_user(
#     current_user: Annotated[User, Depends(get_current_user)],):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credential_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user