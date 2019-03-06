import config
from flask import Flask, request, send_from_directory
from flask_cors import cross_origin
from modules.view import View
from modules.auth import Auth

app = Flask(__name__, static_url_path='', static_folder=config.app.get('static_folder'))

@cross_origin(origins=config.app.get('frontend_origin'), supports_credentials=True)
@app.route("/")
def index():
    return send_from_directory(config.app.get('static_folder'), 'index.html')

@cross_origin(origins=config.app.get('frontend_origin'), supports_credentials=True)
@app.route('/auth', methods=['POST'])
def auth():
    try:
        cookie = Auth.authorize(request)
        return View.ok(set_cookie=cookie)
    except Exception as e:
        return View.error(e)

@cross_origin(origins=config.app.get('frontend_origin'), supports_credentials=True)
@app.route('/whoami')
def whoami():
    try:
        credentials = Auth.check(request)
        return View.data(credentials)
    except Exception as e:
        return View.error(e)

if __name__ == '__main__':
    app.run(
        config.app.get('serve').get('host'),
        config.app.get('serve').get('port')
    )
