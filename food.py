from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory list
foods = []

# -------------------------
# CREATE - Add food
# -------------------------
@app.route('/foods', methods=['POST'])
def create_food():
    data = request.json
    food = {
        "id": len(foods) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    foods.append(food)
    return jsonify({"message": "Food added!", "food": food}), 201


# -------------------------
# READ - Get all foods
# -------------------------
@app.route('/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)


# -------------------------
# UPDATE - Edit food
# -------------------------
@app.route('/foods/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    for food in foods:
        if food["id"] == food_id:
            data = request.json
            food["name"] = data.get("name", food["name"])
            food["price"] = data.get("price", food["price"])
            return jsonify({"message": "Food updated!", "food": food})
    return jsonify({"message": "Food not found"}), 404


# -------------------------
# DELETE - Remove food
# -------------------------
@app.route('/foods/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    global foods
    foods = [food for food in foods if food["id"] != food_id]
    return jsonify({"message": "Food deleted!"})


if __name__ == "__main__":
    app.run(debug=True)