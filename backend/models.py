from app import db
from sqlalchemy.dialects.postgresql import JSON

class ActivityLog(db.Model):
    __tablename__ = 'activity_log'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String, nullable=False)
    activity = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    custom_metadata = db.Column(JSON, nullable=True)
