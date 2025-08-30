from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError
from app.core.config import settings


def create_token(data: dict, expire_minutes = 30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(30)
    to_encode.update({'exp': expire})
    return jwt.encode(
        to_encode,
        settings.JWT_SECERT_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
    
def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECERT_KEY,
            algorithms=settings.JWT_ALGORITHM
        )
        return payload
    except JWTError:
        return None