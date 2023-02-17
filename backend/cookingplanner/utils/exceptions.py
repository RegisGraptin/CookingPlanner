
from fastapi import HTTPException, status

EmailAlreadyExistsException = HTTPException(
    status_code = status.HTTP_409_CONFLICT,
    detail      = "Email already exists.",
    headers     = {"WWW-Authenticate": "Bearer"}
)
