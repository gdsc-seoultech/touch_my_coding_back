from flask import jsonify

class Second:
    def main():
        response = {
            "success": True,
            "data": {
                "test": "hello",
                "my": "world",
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