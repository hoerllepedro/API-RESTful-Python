from flask import Flask, request, jsonify

app = Flask(__name__)

class Material:
    def __init__(self, id, name, qtde):
        self.id = id
        self.name = name
        self.qtde = qtde

    @staticmethod
    def buscar_material_por_id(id):
        for material in materiais:
            if material.id == id:
                return material
        return None


materiais = []
material_id_counter = 0


@app.route('/materials', methods=['GET'])
def listar_materiais():
    response = []
    for i, material in enumerate(materiais):
        data = {
            'id': material.id,
            'name': material.name,
            'qtde': material.qtde
        }
        response.append(data)
    
    return jsonify(response), 200

@app.route('/materials', methods=['POST'])
def criar_material():
    data = request.get_json()
    nome = data['material']['name']
    qtde = data['material']['qtde']
    
    global material_id_counter
    material_id_counter += 1
    material = Material(material_id_counter, nome, qtde)
    materiais.append(material)
    
    response = {'message': 'Material criado com sucesso!'}
    return jsonify(response), 201

@app.route('/materials/<int:id>', methods=['GET'])
def buscar_material(id):
    material = Material.buscar_material_por_id(id)
    if material:
        response = {'material': {
            'id': material.id,
            'name': material.name,
            'qtde': material.qtde
        }}
        return jsonify(response), 200
    else:
        return jsonify({'message': 'Material não encontrado'}), 404

 
@app.route('/materials/<int:id>', methods=['PUT'])
def alterar_material(id):
    data = request.get_json()
    nome = data['material']['name']
    qtde = data['material']['qtde']
    
    material = Material.buscar_material_por_id(id)
    if material:
        material.name = nome
        material.qtde = qtde
        
        response = {
            'material': {
                'id': material.id,
                'name': material.name,
                'qtde': material.qtde
            }
        }
        return jsonify(response), 200
    else:
        return jsonify({'message': 'Material não encontrado'}), 404

@app.route('/materials/<int:id>', methods=['DELETE'])
def remover_material(id):
    material = Material.buscar_material_por_id(id)
    if material:
        materiais.remove(material)
        response = []
        for i, material in enumerate(materiais):
            data = {
                'id': material.id,
                'name': material.name,
                'qtde': material.qtde
            }
            response.append(data)
        return jsonify(response), 200
    else:
        return jsonify({'message': 'Material não encontrado'}), 404



if __name__ == '__main__':
    app.run()
