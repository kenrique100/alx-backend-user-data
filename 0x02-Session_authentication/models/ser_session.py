import uuid
from datetime import datetime
from models.base import Base

class UserSession(Base):
    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id', "")
        self.session_id = kwargs.get('session_id', str(uuid.uuid4()))

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'session_id': self.session_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
