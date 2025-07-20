import os

from settings import Settings

def get_image_placeholder():
    path = os.path.join(Settings.BASE_DIR, "resources", "placeholder", "unknown.jpg")
    return open(path, "rb").read()
