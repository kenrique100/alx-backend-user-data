#!/usr/bin/env python3
from datetime import datetime, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from models import storage

class SessionDBAuth(SessionExpAuth):
    def create_session(self, user_id=None):
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        
        user_session = UserSession(user_id=user_id, session_id=session_id)
        storage.new(user_session)
        storage.save()
        
        return session_id

    def user_id_for_session_id(self, session_id=None):
        if session_id is None:
            return None
        
        sessions = storage.all(UserSession)
        for session in sessions.values():
            if session.session_id == session_id:
                if self.session_duration <= 0:
                    return session.user_id
                if session.created_at is None:
                    return None
                if datetime.now() > session.created_at + timedelta(seconds=self.session_duration):
                    return None
                return session.user_id
        return None

    def destroy_session(self, request=None):
        if request is None:
            return False
        
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        
        sessions = storage.all(UserSession)
        for session in sessions.values():
            if session.session_id == session_id:
                storage.delete(session)
                storage.save()
                return True
        return False
