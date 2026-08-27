from typing import List, Optional

class User:
    """
    Represents a system user. Designed to fulfill Angkor University
    Python Programming II (Lesson 1) Homework requirements.
    """

    def __init__(
        self, 
        user_id: int, 
        username: str, 
        email: str, 
        roles: Optional[List[str]] = None
    ) -> None:
        """
        Initialize a new User instance.
        
        Args:
            user_id: Unique integer identifier for the user.
            username: The username string.
            email: The email address string.
            roles: An optional list of security roles. Defaults to ["user"].
        """
        self.user_id: int = user_id
        self.username: str = username
        self.email: str = email
        # If no roles are provided, default to a list containing ["user"] [1]
        self.roles: List[str] = roles if roles is not None else ["user"]

    def get_profile_summary(self) -> str:
        """
        Returns a formatted, human-readable summary of the user's profile [1].
        """
        roles_str: str = ", ".join(self.roles)
        return (
            f"User: {self.username} (ID: {self.user_id}) | "
            f"Email: {self.email} | "
            f"Roles: {roles_str}"
        )

    def has_role(self, role: str) -> bool:
        """
        Checks if the user has a specific permission role.
        """
        return role in self.roles

    def add_role(self, role: str) -> None:
        """
        Safely adds a new role to the user's active role list.
        """
        if role not in self.roles:
            self.roles.append(role)