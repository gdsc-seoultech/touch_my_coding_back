from flask import Blueprint, json, request # 모듈을 나누는 친구 
from service import image

service = image.Image
image_route = Blueprint("image", __name__, url_prefix="/api/image")

@image_route.route("/", methods=["GET"])
def searchImage():
    query = request.args.get("query")
    page = request.args.get("page")

    return service.searchImage(query, page)

@image_route.route("/label", methods=["POST"])
def getLabel():
    data = json.loads(request.data)

    return service.getLabel(data["url"])