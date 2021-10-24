from flask import Flask, Response,render_template,jsonify
from flask_cors import CORS
import json
import logging

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.UsersResource.user_service import UserResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/imdb/artists/<prefix>')
def get_artists_by_prefix(prefix):
    res = IMDBArtistResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/users')
def get_users():
    res = UserResource.get_by_template(None)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/usersinfo')

def get_users_1():
    #fake_user=[{"userID":"1","userName":"Wenqing Zhong","email":"wz2557@columbia.edu"},{"userID":"2","userName":"Xiyuan Zhao","email":"xz2994@columbia.edu"}]
    res = UserResource.get_by_template(None)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    #print("This is the return type", type(rsp))
    return rsp

@app.route('/restaurant_info')
def get_r():
    fake_rest=[{"RID":1, "name":"ELysian Fields Cafe","owner":"Manson Wudy","type":"Pizza","location":"10029"},
               {"RID":1, "name":"Massawa","owner":"Wooden Wuddy","type":"Seafood","location":"10027"},
               {"RID":1, "name":"Szechuan Garden","owner":"Stephen Wang","type":"Chinese","location":"10025"}]
    return render_template('restaurant_info.html',restaurants=fake_rest)

@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
