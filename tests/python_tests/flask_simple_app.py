from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app , supports_credentials=True)

@app.route('/')
@cross_origin()
def index():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True)
