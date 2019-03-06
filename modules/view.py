import json
from flask import Response
import config

class View(object):
    @staticmethod
    def ok(**kwargs):
        data = {
            'ok': True,
            'msg': None
        }
        set_cookie = None
        for key, val in kwargs.items():
            if key == 'msg':
                data['msg'] = val
            if key == 'set_cookie':
                set_cookie = val
        res = Response(json.dumps(data), mimetype='application/json')
        if set_cookie != None:
            res.set_cookie(config.app.get('cookie_key'), set_cookie)
        return res
    @staticmethod
    def data(data):
        res = {
            'ok': True,
            'data': data
        }
        return Response(json.dumps(res), mimetype='application/json')
    @staticmethod
    def error(ex):
        res = {
            'ok': False,
            'msg': str(ex)
        }
        return Response(json.dumps(res), mimetype='application/json')
