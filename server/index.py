from flask import Flask, render_template ,request, redirect
import random
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
## 새로운 api 생성 
## 또 다른 방법으로 index.py 를 실행 시키는 방법
## 위에서 run 을 시키면 아래에 출력물이 실행됨 
# 127.0.0.1 = localhost
# 127.0.0.1:5000/main 이라는 주소로 요청을 하는 경우 아래의 함수를 실행

## localhost:5000/login 주소로 생성 
@app.route("/login")
def login():
    ## main.html 에서 데이터를 보내는 형식
    ## {id : xxxx, pass : xxxx}
    _id = request.args.get("id")
    _pass = request.args.get("pass")
    print(_id , _pass)
    if (_id == 'test') & (_pass == '1234'):
        return render_template("second.html")
    else:
        # 로그인 실패시 localhost : 5000 /main 으로 이동
        return redirect("/main")
    #return _id, _pass
    # localhost : 5000/data api 생성
    # post 형태로 요청시 
@ app.route('/data',methods = ['post'])
def data():
    _use = request.form['use']
    _list = ['바위','가위','보']
    choice_list = random.choice(_list)
    # 무승부 인 경우 
    if _use == choice_list:
        result = '무승부'
    elif _use == '바위':
        if choice_list == '가위':
            result = '승'
        else : 
            result = '패'
    elif _use == '가위':
        if choice_list == '보':
            result = '승'
        else:
            result = '패'
    else:
        if choice_list == '바위':
            result = '승'
        else :
            resutl = '패'
    return render_template('result.html', res = result)

app.run(port="8080")

