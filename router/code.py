from flask import Blueprint, request
from service import code

service = code.Code
code_route = Blueprint("code", __name__, url_prefix="/code")

@code_route.route("/<uuid>", methods=["GET"])
def searchCode():
    return service.searchCode()

@code_route.route("/", methods=["POST"])
def registCode():
    return service.registCode()
