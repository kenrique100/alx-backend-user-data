#!/usr/bin/env python3

from sqlalchemy import Column, String
from .base import Base

class UserSession(Base):
    __tablename__ = 'user_sessions'

    id = Column(String, primary_key=True)
    user_id = Column(String, nullable=False)
    session_id = Column(String, nullable=False)

    def __init__(self, *args, **kwargs):
        super(UserSession, self).__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
