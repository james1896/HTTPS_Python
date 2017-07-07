# -*- coding:utf-8 -*-
from flask import Flask
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/test',methods=['GET','POST'])
def test():
    return jsonify({"a":"b"})


if __name__ == '__main__':
    # app.run('0.0.0.0', debug=True, port=8100)
    # 使用  pysslOpen自带的证书
    # app.run('0.0.0.0', debug=True, port=8100, ssl_context='adhoc')

    # 使用自签名证书
    app.run('0.0.0.0', debug=True, port=8100, ssl_context=('/Users/moses/Desktop/https/server.crt',
                                                           '/Users/moses/Desktop/https/server.key'))
