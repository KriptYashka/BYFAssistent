import enum

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ENUM

from src.db.repository.tables.base import Base, CRUDMixin


class StatusRequest(enum.Enum):
    CONSIDERATION = "На рассмотрении"
    ACCEPT = "Подтвержден"
    DECLINE = "Отклонен"
    CANCEL = "Отменен"


class SubscriptionRequest(Base, CRUDMixin):
    __tablename__ = 'subscription_requests'
    id = Column(Integer, primary_key=True)
    price_id = Column(Integer, ForeignKey('prices.id'))
    user_id = Column(Integer, ForeignKey('users.tg_id'))
    status = Column(
        ENUM(StatusRequest, name="sub_request_status_enum", create_type=True),
        default=StatusRequest.CONSIDERATION)
    response_message = Column(String(1000), nullable=True)
