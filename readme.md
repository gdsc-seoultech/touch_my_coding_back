# Touch my coding 백엔드 서버입니다.

### 개발 환경

- conda말고 pipfile 추천드려요
- python 3.8
- 라이브러리 requirements.txt 참고<br/><br/>

### Code formatter

향후 논의 해봐요
<br/><br/>

### 가상환경 구성

```
# 가상환경 만들기
virtualenv env --python=python3.8
```

<br/><br/>

### freeze 활용법

```
# freeze 생성
pip freeze > requirements.txt

# freeze 라이브러라 다운로드
pip install -r requirements.txt
```

<br/><br/>

### db migrate 활용

https://blogger.pe.kr/887

```
# 첫 설정
flask db init

# 생성
flask db migrate

# 업데이트
flask db upgrade
```
