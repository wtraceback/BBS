from flask import current_app


def allowed_file(filename):
    suffix = filename.split('.')[-1].lower()
    allowed_image_extensions = current_app.config['ALLOWED_IMAGE_EXTENSIONS']
    return suffix in allowed_image_extensions
