from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError



def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png']
    print(ext)
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def file_size(value):
        limit = 100 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 100KB.')

name_regex = RegexValidator(regex=r'^[a-zA-Z\s]*$', message='Name should only contain characters')
phone_regex = RegexValidator(regex=r'^[789]\d{9}$', message='Invalid Phone Number')
register_regex = RegexValidator(regex=r'^1(RV|rv)\d{2}[a-zA-Z]{2}\d{3}$', message='Register Number is Invalid')