from litestar import Controller, post

from src.application.user_context.services.auth_service import AuthService
from src.infrastructure.database.base import BaseModel
from src.infrastructure.dependencies.user_context.auth_dependencies import user_dependencies


class LoginData(BaseModel):
    email: str
    password: str


class AuthController(Controller):
    """Basic auth controller."""

    dependencies = user_dependencies

    @post("/register")
    async def login(self, auth_service: AuthService, data: LoginData) -> dict[str, str]:
        """Login endpoint."""
        user = await auth_service.register_user(data.email, data.password)
        return {"user_id": str(user.user_id)}
