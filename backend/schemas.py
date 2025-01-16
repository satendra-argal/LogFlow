from marshmallow import Schema, fields

class ActivityLogSchema(Schema):
    user_id = fields.Str(required=True)
    activity = fields.Str(required=True)
    timestamp = fields.DateTime(required=True)
    custom_metadata = fields.Dict(required=False)