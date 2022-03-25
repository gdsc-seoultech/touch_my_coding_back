from ast import keyword
import requests
import json
from google.cloud import vision # Imports the Google Cloud client library


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
        label_list = []
       # Instantiates a client
        client = vision.ImageAnnotatorClient()

        image = vision.Image()
        image.source.image_uri = uri 

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations 

        for label in labels:
            label_list.append(label.description) # 키워드만 출력
        
        server_response = {
            "success": True,
            "label": label_list
        }

        return server_response