from flask import Flask
from APIs.performance_api import performance_api
from APIs.play_api import play_api
from APIs.theatre_api import theatre_api
from APIs.user_api import user_api

app = Flask(__name__)

app.register_blueprint(performance_api)
app.register_blueprint(play_api)
app.register_blueprint(theatre_api)
app.register_blueprint(user_api)

if __name__ == "__main__":
    app.run(debug=True)
