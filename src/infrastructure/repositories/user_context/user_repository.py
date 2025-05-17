from advanced_alchemy import repository
from sqlalchemy import select

from src.domain.user_context.entities.user import UserEntity
from src.domain.user_context.value_objects import UserId
from src.infrastructure.database.models import UserModel


class UserRepository(repository.SQLAlchemyAsyncRepository[UserModel]):
    """Repository for User model operations.

    Provides methods to query and persist user data, converting between domain entities and database models.

    Attributes:
        model_type: The type of the database model.

    """

    model_type: type[UserModel] = UserModel

    async def get_by_email(self, email: str) -> UserEntity | None:
        """Get a user by email address.

        Args:
            email: The email address of the user.

        Returns:
            UserEntity | None: The user entity if found, otherwise None.

        """
        statement = select(UserModel).where(UserModel.email == email)
        user_model: UserModel = await self.session.scalar(statement)

        if not user_model:
            return None

        return self._to_entity(user_model)

    async def save(self, user_entity: UserEntity) -> UserEntity:
        """Save or update a user entity in the database.

        Args:
            user_entity: The user entity to save or update.

        Returns:
            UserEntity: The saved or updated user entity.

        """
        statement = select(UserModel).where(UserModel.id == user_entity.user_id.value)
        existing_user: UserModel = await self.session.scalar(statement)

        if existing_user:
            existing_user.email = user_entity.email
            existing_user.hashed_password = user_entity.hashed_password
            existing_user.is_active = user_entity.is_active
        else:
            new_user = self.model_type(
                id=user_entity.user_id.value,
                email=user_entity.email,
                hashed_password=user_entity.hashed_password,
                is_active=user_entity.is_active,
            )
            self.session.add(new_user)

        await self.session.commit()
        return user_entity

    async def block_user(self, email: str, reason: str) -> None:
        """Block a user by email address.

        Args:
            email: The email address of the user.
            reason: Reason for blocking

        """
        statement = select(UserModel).where(UserModel.email == email)
        user: UserModel = await self.session.scalar(statement)
        user.blocked = True
        user.reason_for_blocking = reason

    def _to_entity(self, model: UserModel) -> UserEntity:
        """Convert a UserModel to a UserEntity.

        Args:
            model: The database model to convert.

        Returns:
            UserEntity: The corresponding user entity.

        """
        return UserEntity(
            user_id=UserId(model.id),
            email=model.email,
            hashed_password=model.hashed_password,
            is_active=model.is_active,
        )

    def _to_model(self, entity: UserEntity) -> UserModel:
        """Convert a UserEntity to a UserModel.

        Args:
            entity: The user entity to convert.

        Returns:
            UserModel: The corresponding database model.

        """
        return UserModel(
            id=entity.user_id.value,
            email=entity.email,
            hashed_password=entity.hashed_password,
            is_active=entity.is_active,
        )
