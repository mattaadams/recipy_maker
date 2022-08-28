import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def file_size(value): 
    limit = 10485760 # 10 MB
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 10 MB.')