from flask import Flask, jsonify, request

app = Flask(__name__)


dados=[
    {"id":1, "nome": "Item 1"},    
    {"id":2, "nome": "Item 2"}
]
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(dados)

@app.route('/api/items/', methods=['GET'])  # Rota para todos os itens

@app.route('/api/items/?<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in dados if item["id"] == item_id), None)
    if item is not None:
        return jsonify(item)
    else:
        return jsonify({"error": "Item não encontrado"}), 404

@app.route('/api/items', methods=['POST'])           
def create_item():
    novo_item = request.json
    novo_item['id'] = len(dados) +1
    dados.append(novo_item)
    return jsonify(novo_item), 201

if __name__ == '__main__':
    app.run(debug=True)    





