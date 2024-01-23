# 2. Build a Flask app with static HTML pages and navigate between them.


from flask import Flask

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/galaxy')
def galaxy():
    return app.send_static_file('galaxy.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000)
