from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World! 成都信息工程大学20级毕业设计、21、22级工程实践王伟组的同学们，元旦节快乐！'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
