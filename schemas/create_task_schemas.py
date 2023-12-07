from marshmallow import fields, validates, ValidationError

class CreateTaskSchema:
    name = fields.String(required=True)
    description = fields.String(required=False)
    color = fields.String(required=True)

    @validates('title')
    def validate_name(self, value):
        if len(value) < 120:
            raise ValidationError('Name must be at leat 120 characters long.')
        
    @validates('description')
    def validate_author(self, value):
        if len(value) < 300:
            raise ValidationError('Description must be at leat 300 characters long.')
    
    @validates('color')
    def validate_color(self, value):
        if len(value) < 7:
            raise ValidationError('Color must be at leat 7 characters long.')
        
    