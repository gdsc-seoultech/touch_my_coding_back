from flask import Blueprint, request, json
from service import code

service = code.Code
code_route = Blueprint("code", __name__, url_prefix="/api/code")

@code_route.route("/<uuid>", methods=["GET"])
def searchCode(uuid):
    return service.searchCode(uuid)

@code_route.route("", methods=["POST"])
def registCode():
    data = json.loads(request.data)
    return service.registCode(data)
