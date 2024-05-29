#!/usr/bin/env python3
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from models.user import User
from os import getenv
from datetime import datetime, timedelta

class SessionDBAuth(SessionExpAuth):
    def create_session(self, user_id=None):
        session_id = super().create_session(user_id)
        new_session = UserSession(user_id=user_id, session_id=session_id)
        self._session.add(new_session)
        self._session.commit()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        user_session = self._session.query(UserSession).filter_by(session_id=session_id).first()
        if user_session:
            return user_session.user_id
        return None

    def destroy_session(self, request=None):
        session_id = self.session_cookie(request)
        if session_id:
            user_session = self._session.query(UserSession).filter_by(session_id=session_id).first()
            if user_session:
                self._session.delete(user_session)
                self._session.commit()
