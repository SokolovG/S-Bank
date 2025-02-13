from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from backend.app.infrastructure.database.base import Base
from backend.app.infrastructure.models.enums import ParticipantStatus


class EventRegistration(Base):
    __tablename__ = 'event_registrations'

    profile_id: Mapped[int] = mapped_column(
        ForeignKey('profiles.id', use_alter=True, ondelete='CASCADE'),
        primary_key=True
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey('events.id', use_alter=True, ondelete='CASCADE'),
        primary_key=True
    )
    status: Mapped['ParticipantStatus'] = mapped_column(
        default=ParticipantStatus.REGISTERED
    )


class EventOrganizers(Base):
    __tablename__ = 'event_organizers'
    organizer_id: Mapped[int] = mapped_column(
        ForeignKey('organizers.id', use_alter=True, ondelete='CASCADE'),
        primary_key=True
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey('events.id', use_alter=True, ondelete='CASCADE'),
        primary_key=True
    )
