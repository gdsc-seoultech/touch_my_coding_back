from flask import jsonify
from model import image

class Image:
    def main():
        # formating 필요
        print("반응 완료")
        my_value = image.Image.query.all() 
        for i in my_value:
            print(i.__dict__)
        response = {
            "success": True,
            "data": {
                "test": [
                    {
                        "url":"성공"
                    }
                ]
            }
        }
        return jsonify(response)

    def test():
        with open("../img_url.txt", "w") as file:
            return file.readline()
    
    def searchCode():
        return True
    
    def registCode():
        return True