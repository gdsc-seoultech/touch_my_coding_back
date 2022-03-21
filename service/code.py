from flask import Response
from model.models import User
from sqlalchemy import select
from database import db

class Code:
    def searchCode(uuid):

        select_query = db.session.query(User).where(User.uuid == uuid).first()
        
        if not select_query: 
            return Response (
                "not valid data",
                status = 400
            )

        code = select_query.code

        response = {
            "success": True,
            "code": code  
        }

        return response
    
    def registCode(data):
        
        uuid = data["uuid"]
        code = str(data["code"])

        select_query = select(User).where(User.uuid == uuid)
        prev_code = db.session.execute(statement = select_query).scalars().all()
 
        # 이전 정보가 있으면 수정, 아닐 시 생성
        if len(prev_code) == 1:
            db.session.query(User).filter(User.uuid == uuid).update({"code": code})
            db.session.commit()

        elif len(prev_code) == 0:
            new_code = User(uuid = uuid, code = code)
            db.session.add(new_code)
            db.session.commit()
        
        else:
            return Response (
                "bad reqeust",
                status = 400
            )

        response = {
            "success": True
        }

        return response