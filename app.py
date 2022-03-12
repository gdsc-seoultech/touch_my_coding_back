from flask import Flask
from flask_cors import CORS

from database import db, migrate
from config import Config
from router import image
from model.models import User, Test 

# app 시작
app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db.init_app(app)
migrate.init_app(app, db)

# 라우터 등록
app.register_blueprint(image.image_route) # img 라우터 등록



# http method 분기처리
# @app.route("/test", methods=["GET", "POST"])
# def check():
#     if request.method == "POST":
#         return "POST method"
#     else:
#         return "??"

# path parameter 사용법
# @app.route("/my/<name>")
# def checck(name):
#     return f'myname {name}'

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='127.0.0.1',port=5000, debug=True) #외부 접속 허용시