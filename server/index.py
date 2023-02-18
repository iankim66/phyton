from flask import Flask ## flask 안 library 에서 Flask 를 가져오겠다. 
## Flask 클래스 생성 
## __name__ : 파일의 이름 
app = Flask(__name__)

@app.route('/')
## @ : 네비게이터 : 바로 아래에 있는 함수를 실행하겠다.
## route (주소) : 주소에 요청을 하면 아래의 함수를 실행 
## @app.route('/') : 127.0.0.1:5000/ 요청 하는 경우 아래의 함수를 실행 
def index():
    return 'Hello World'
app.run
## cmd 창에서 ..server directory 로 커서를 옮긴후 
## set FLASK_APP=index 를 입력
## 그리고 flask run 을 입력 
## 그리고, 기존의 explor 엡애서 주소창에 http://127.0.0.1:5000/ 입력하면 "Hellow world"출력 
