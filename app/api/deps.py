import os
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.core.config import settings
from app.crud.crud_user import user as user_db
from app.logger import logger

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
            audience=None,
            issuer=None,
            options={
                "verify_aud": False,
                "verify_signature": True,
            },
        )
        id: int = payload.get("user_id")
        if id is None:
            logger.error(f"id not found = {payload}")
            raise credentials_exception
    except JWTError as e:
        logger.error(e, f"token = {token}")
        raise credentials_exception

    user = user_db.get(id)
    if user is None:
        raise credentials_exception
    return user
