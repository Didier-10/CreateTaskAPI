from marshmallow import fields, validates, ValidationError

class CreateTaskSchema:
    name = fields.String(required=True)
    description = fields.String(required=False)
    color = fields.String(required=True)

    @validates('name')
    def validate_name(self, value):
        if len(value) > 120:
            raise ValidationError('The name must have a maximum of 120 characters.')
        
    @validates('description')
    def validate_description(self, value):
        if len(value) > 300:
            raise ValidationError('The Description must have a maximum of 300 characters.')
    
    @validates('color')
    def validate_color(self, value):
        if len(value) > 7:
            raise ValidationError('The Color must have a maximum of 7 characters.')
        
    