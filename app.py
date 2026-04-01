from flask import Flask, jsonify

# Creates the app
app = Flask(__name__)

# Defines an endpoint with hello_world as the path 
@app.route("/hello_world", methods=["GET"])

def hello_world():
    return jsonify({"hello": "world"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)