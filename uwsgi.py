from app import app
from werkzeug.debug import DebuggedApplication
import config

if __name__ == "__main__":
    # app.debug = True
    if config.app.get('debug_mode', False):
        app = DebuggedApplication(app, evalex=True)
    app.run()

# gunicorn -b :5000 uwsgi:app
