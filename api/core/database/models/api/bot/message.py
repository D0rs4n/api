from sqlalchemy import ARRAY, BigInteger, Column, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from api.core.database import Base


class Message(Base):
    """A message, sent somewhere on the Discord server."""

    __tablename__ = 'api_message'

    id = Column(BigInteger, primary_key=True)
    channel_id = Column(BigInteger, nullable=False)
    content = Column(String(4000), nullable=False)
    embeds = Column(ARRAY(JSONB(astext_type=Text())), nullable=False)
    author_id = Column(ForeignKey('api_user.id', deferrable=True, initially='DEFERRED'), nullable=False, index=True)
    attachments = Column(ARRAY(String(length=512)), nullable=False)

    author = relationship('ApiUser')
