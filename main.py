from flask import Flask
from rutas.video import routes_video

app = Flask(__name__)
app.register_blueprint(routes_video)

if __name__ == '__main__':
    app.run(debug=True, port="5000", host="0.0.0.0")