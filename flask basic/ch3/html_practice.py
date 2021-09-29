from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('practice.html') # 템플릿 폴더가 필요하다.(경로설정)

if __name__=='__main__':
    app.run()