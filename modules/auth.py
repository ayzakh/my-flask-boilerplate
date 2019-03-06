import hashlib
import config

class Auth(object):
    @staticmethod
    def _get_user_if_exists(cookie_value):
        # вот это взять из БД или из кэша
        users_database = [
            { "login": "login1", "password": "password1", "phone": "78887888888" },
            { "login": "login2", "password": "password2", "phone": "79998999999" },
            { "login": "login3", "password": "password3", "phone": "77777777777" },
            { "login": "login4", "password": "password4", "phone": "76666666666" },
            { "login": "login5", "password": "password5", "phone": "75555555555" },
            { "login": "login6", "password": "password6", "phone": "74444444444" },
            { "login": "login7", "password": "password7", "phone": "73333333333" }
        ]
        for user in users_database:
            if cookie_value == Auth._user_to_cookie(user.get('login'), user.get('password')):
                return user
        raise Exception('Incorrect login or password')
    @staticmethod
    def _validate_user(login, password):
        if login == None or login == '':
            raise Exception('Empty login')
        if password == None or password == '':
            raise Exception('Empty password')
    @staticmethod
    def _validate_cookie_value(cookie_value):
        if cookie_value == None or cookie_value == '':
            raise Exception('Unauthorized')
    @staticmethod
    def _user_to_cookie(login, password):
        hl = hashlib.sha256()
        data = login + ':' + password
        hl.update(data.encode('utf-8'))
        data = hl.hexdigest()
        return data
    @staticmethod
    def authorize(request):
        login = request.form['login']
        password = request.form['password']
        Auth._validate_user(login, password)
        cookie_value_equivalent = Auth._user_to_cookie(login, password)
        Auth._get_user_if_exists(cookie_value_equivalent)
        return cookie_value_equivalent
    @staticmethod
    def check(request, **kwargs):
        cookie_value = request.cookies.get(config.app.get('cookie_key'))
        Auth._validate_cookie_value(cookie_value)
        user = Auth._get_user_if_exists(cookie_value)
        return user
