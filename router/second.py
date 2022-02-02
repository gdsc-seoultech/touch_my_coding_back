from flask import Blueprint
from service import second

service = second.Second
second_route = Blueprint("second", __name__, url_prefix="/second")

@second_route.route("/", methods=["GET"])
def main():
    return service.main()

@second_route.route("/test", methods=["GET"])
def test():
    return service.test("touch")