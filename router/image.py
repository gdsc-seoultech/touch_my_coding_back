from flask import Blueprint, jsonify # 모듈을 나누는 친구 
from service import image

service = image.Image
image_route = Blueprint("image", __name__, url_prefix="/image")

@image_route.route("/test", methods=["GET"])
def main():
    return service.test()
