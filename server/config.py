# import logging
# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

#     # Define the base directory
#     base_dir = os.path.abspath(os.path.dirname(__file__))
#     db_path = os.path.join(base_dir, 'instance', 'app.db')

#     # Ensure the directory for the database exists
#     os.makedirs(os.path.dirname(db_path), exist_ok=True)

#     # Set the SQLAlchemy database URI
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f'sqlite:///{db_path}'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_key'
#     LOG_LEVEL = logging.DEBUG

#     @staticmethod
#     def init_app(app):
#         handler = logging.StreamHandler()
#         handler.setLevel(Config.LOG_LEVEL)
#         formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)
#         app.logger.addHandler(handler)

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///instance/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your_jwt_secret_key')
