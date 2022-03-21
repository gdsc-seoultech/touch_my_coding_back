import requests

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

    
