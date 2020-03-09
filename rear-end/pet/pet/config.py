import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET KEY') or 'XinTT SB'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'petHospital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    # CV_UPLOAD_DIR = os.path.join(basedir, 'uploaded_CV')
    # IMG_UPLOAD_DIR = os.path.join(basedir, 'profile_images')


# line 1-8 code from lecture 15 config.py, I change the secret_key