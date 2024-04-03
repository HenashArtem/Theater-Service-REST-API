from flask import Flask
from APIs.performance_api import performance_api

app = Flask(__name__)

app.register_blueprint(performance_api)


if __name__ == "__main__":
    app.run(debug=True)
