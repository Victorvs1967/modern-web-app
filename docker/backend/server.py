import os.path

from flask import Flask
import flask-cors


class ModernWebApp(Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        flask_cors.CORS(self)

app = ModernWebApp('modern-web-app')

env = os.environ.get('APP_ENV', 'dev')
print(f'Starting application in {env} mode')
app.config.from_object(f'backend.{env}_settings')
