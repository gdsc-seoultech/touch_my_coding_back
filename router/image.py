from flask import Blueprint, jsonify, request # 모듈을 나누는 친구 
from service import image

service = image.Image
image_route = Blueprint("image", __name__, url_prefix="/image")

@image_route.route("/", methods=["GET"])
def searchImage():
    query = request.args.get("query")
    per_page = request.args.get("per_page")
    page = request.args.get("page")

    return service.searchImage(query, per_page, page)