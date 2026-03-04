from flask import Flask, request, jsonify

app = Flask(__name__)

foods = {}

@app.route('/foods', methods=['POST'])
def add_food():
    data = request.json
    food_id = len(foods) + 1
    foods[food_id] = data['name']
    return jsonify({"message": "Food added"}), 201

@app.route('/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

@app.route('/foods/<int:id>', methods=['PUT'])
def update_food(id):
    if id in foods:
        foods[id] = request.json['name']
        return jsonify({"message": "Food updated"})
    return jsonify({"error": "Food not found"}), 404

@app.route('/foods/<int:id>', methods=['DELETE'])
def delete_food(id):
    if id in foods:
        del foods[id]
        return jsonify({"message": "Food deleted"})
    return jsonify({"error": "Food not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)