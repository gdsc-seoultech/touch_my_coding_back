from flask import Blueprint, jsonify
from service import first

service = first.First
first_route = Blueprint("first", __name__, url_prefix="/first")

@first_route.route("/", methods=["GET"])
def main():
    return service.main()

@first_route.route("/test", methods=["GET"])
def test():
    return service.test()
