from flask import Flask, jsonify

# Creates the app
app = Flask(__name__)

# Defines an endpoint with hello_world as the path 
@app.route("/hello_world", methods=["GET"])

# Returns the JSON response for the simple API with a 200 status code saying it was successful
def hello_world():
    return jsonify({"hello": "world"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)