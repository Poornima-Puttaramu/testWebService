from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample identity data
identities = [
    {"id": "E001", "firstName": "John", "lastName": "Doe", "email": "john.doe@example.com"},
    {"id": "E002", "firstName": "Jane", "lastName": "Smith", "email": "jane.smith@example.com"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(identities)

@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = next((u for u in identities if u["id"] == id), None)
    return jsonify(user or {})

@app.route("/users", methods=["POST"])
def add_user():
    user = request.json
    identities.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(debug=True)
