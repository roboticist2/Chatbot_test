from flask import Flask, request, , render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        response = "안녕하세요"
        return render_template('index.html', user_input=user_input, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    
