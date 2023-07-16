from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def chatbot():
    user_input = request.form.get('user_input')  # 사용자의 입력 받기
    response = "안녕하세요"  # 답변으로 "안녕하세요" 설정
    return response

if __name__ == '__main__':
    app.run()
    
