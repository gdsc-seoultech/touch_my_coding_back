from flask import jsonify
from model import models

class First:
    def main():
        # formating 필요
        my_value = models.Test.query.all() 
        for i in my_value:
            print(i.__dict__)
        response = {
            "success": True,
            "data": {
                "test": [
                    {
                        "a":"b"
                    }
                ],
                "router": "second",
            }
        }
        return jsonify(response)

    def test(name):
        response = {
            "success": True,
            "data": {
                "name": name
            }
        }

        return jsonify(response)