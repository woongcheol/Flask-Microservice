# PyPI(python Package Index) : 파이썬 패키지를 설치하는 프로그램(주로 커맨드 창이나 쉘에서 사용)  
# 명령어는 pip

from flask import Flask

app = Flask(__name__) # app이라는 이름으로 flask 객체(인스턴스) 생성

@app.route("/hello/<user>") # 데코레이터(@) 및 라우터(경로) 생성(보안에 좋다)
def hello(user): #hello World!! 출력 함수 
	return "hello World!!" + user

if __name__=="__main__": # app을 실행시켜준다
	app.run()