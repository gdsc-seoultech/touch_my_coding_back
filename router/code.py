from flask import Blueprint, request
from service import code

service = code.Code
code_route = Blueprint("code", __name__, url_prefix="/code")

@code_route.route("/search", methods=["GET"])
def searchImage():
    query = request.args.get("query")
    per_page = request.args.get("per_page")
    page = request.args.get("page")

    return service.searchImage(query, per_page, page)