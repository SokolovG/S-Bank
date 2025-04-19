from litestar import Router

from src.interfaces.api.user_context.controllers import AuthController, UserController

auth_router = Router(path="auth", route_handlers=[AuthController])
user_router = Router(path="user", route_handlers=[UserController])
