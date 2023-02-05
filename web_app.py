from flask import Flask

app = Flask('__main__')


@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
