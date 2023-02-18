from flask import Flask, render_template
## flask 안 library 에서 Flask 를 가져오겠다. 
## Flask 클래스 생성 
## __name__ : 파일의 이름 
app = Flask(__name__)

@app.route('/')
## @ : 네비게이터 : 바로 아래에 있는 함수를 실행하겠다.
## route (주소) : 주소에 요청을 하면 아래의 함수를 실행 
## @app.route('/') : 127.0.0.1:5000/ 요청 하는 경우 아래의 함수를 실행 
def index():
    return 'Hello World'
## cmd 창에서 ..server directory 로 커서를 옮긴후 
## set FLASK_APP=index 를 입력
## 그리고 flask run 을 입력 
## 그리고, 기존의 explor 엡애서 주소창에 http://127.0.0.1:5000/ 입력하면 "Hellow world"출력 
@app.route('/main')
def main():
    return render_template('main.html')
##127.0.0.1:5000/main 이라는 주소로 요청을 하는경우 위의 함수를 실행 
## 127.0.0.1 : localhost 
app.run(port="8080")
## 또 다른 방법으로 index.py 를 실행 시키는 방법
## 위에서 run 을 시키면 아래에 출력물이 실행됨 