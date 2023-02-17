from typing import Union

from passlib.context import CryptContext

from cookingplanner.utils.singleton import SingletonMeta


class PasswordManager(metaclass=SingletonMeta):
    """Password Manager Class."""
    
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: Union[str, bytes], hashed_password: Union[str, bytes]) -> bool:
        """Verify that the given password mathes the hashed password.

        Args:
            plain_password (Union[str, bytes]): Plain password to verified.
            hashed_password (Union[str, bytes]): Hashed password to compare.

        Returns:
            bool: True if the password matches the hashed password.
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: Union[str, bytes]) -> str:
        """Get the password hash of the given password.

        Args:
            password (Union[str, bytes]): Password to hash.

        Returns:
            str: The hash of the password.
        """        
        return self.pwd_context.hash(password)
