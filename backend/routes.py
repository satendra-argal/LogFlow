from flask import Blueprint, request, jsonify
from models import ActivityLog
from schemas import ActivityLogSchema
from sqlalchemy import func
from marshmallow import ValidationError
from app import db

blueprint = Blueprint('routes', __name__)
activity_log_schema = ActivityLogSchema()

@blueprint.route('/logs', methods=['POST'])
def add_log():
    try:
        data = activity_log_schema.load(request.json)
        new_log = ActivityLog(**data)
        db.session.add(new_log)
        db.session.commit()
        return jsonify({"message": "Log added successfully"}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@blueprint.route('/logs/<user_id>', methods=['GET'])
def get_logs(user_id):
    start = request.args.get('start')
    end = request.args.get('end')
    activity = request.args.get('activity')

    query = ActivityLog.query.filter_by(user_id=user_id)
    if start and end:
        query = query.filter(ActivityLog.timestamp.between(start, end))
    if activity:
        query = query.filter_by(activity=activity)

    logs = query.all()
    return jsonify([{
        "user_id": log.user_id,
        "activity": log.activity,
        "timestamp": log.timestamp.isoformat(),
        "metadata": log.custom_metadata
    } for log in logs])

@blueprint.route('/logs/stats', methods=['GET'])
def get_stats():
    start = request.args.get('start')
    end = request.args.get('end')

    user_activity_count = db.session.query(
        ActivityLog.user_id,
        func.count(ActivityLog.id)
    ).filter(
        ActivityLog.timestamp.between(start, end)
    ).group_by(ActivityLog.user_id).all()

    most_frequent_activity = db.session.query(
        ActivityLog.activity,
        func.count(ActivityLog.activity)
    ).group_by(ActivityLog.activity).order_by(func.count(ActivityLog.activity).desc()).first()

    return jsonify({
        "user_activity_count": {user: count for user, count in user_activity_count},
        "most_frequent_activity": most_frequent_activity[0] if most_frequent_activity else None
    })
