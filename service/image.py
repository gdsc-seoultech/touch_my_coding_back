from ast import keyword
from email import header
import requests
import json
import os # .env 값에서 API_KEY 가져오기 
from dotenv import load_dotenv # 가상 환경에서 환경변수 

class Image:
    def searchImage(query, page):
        image_url_list = []

        requset_url = 'https://unsplash.com/napi/search' # 웹 요청 
        params = {
            'query': query,
            'per_page': 10,
            'page': page
        }
        
        url_response = requests.get(requset_url, params=params).json()["photos"]
    
        total_pages = url_response["total_pages"]
        results = url_response["results"]
        
        if (total_pages >= int(page)): # 정상    
            for i in results:
                urls = i["urls"]["raw"]
                image_url_list.append(urls)
            
        server_response = {
            "success": True,
            "total_pages": total_pages,
            "result": image_url_list 
        }    
        
        return server_response

    def getLabel(uri):
        load_dotenv()
        label = {
            "requests": [
                {
                "image": {
                    "source": {
                    "imageUri": uri
                    }
                },
                "features": [
                    {
                    "type": "LABEL_DETECTION",
                    "maxResults": 5
                    }
                ]
                }
            ]
        }

        json_data = json.dumps(label)
        API_KEY = os.environ.get("API_KEY")

        response = requests.post(f'https://vision.googleapis.com/v1/images:annotate?key={API_KEY}', data=json_data) 
        r = response.json() # json으로 변환 
        labels = r['responses'][0]['labelAnnotations']

        for label in labels:
            print(label['description']) # keyword만 출력 

Image.getLabel('https://images.unsplash.com/photo-1499988921418-b7df40ff03f9?ixlib=rb-1.2.1\u0026q=80\u0026fm=jpg\u0026crop=entropy\u0026cs=tinysrgb\u0026w=400\u0026fit=max')
# img url은 small로 추천 드립니다. raw를 쓰니 용량이 초과한다고 뜨네용