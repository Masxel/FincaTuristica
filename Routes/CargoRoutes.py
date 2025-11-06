import json
from flask import Blueprint, jsonify, request
from Models.Cargo import Cargo
from Repository.CargoRepository import CargoRepository


cargo_bp = Blueprint('cargo', __name__)

@cargo_bp.route('/api/cargos', methods=["GET"])
def obtener_cargos(): 
    try:
        datos_cargos = CargoRepository().consultar_todos_cargos()
        lista_cargos = []
        if datos_cargos:
            for dato in datos_cargos:
                cargo = Cargo()
                cargo.SetId(dato[0])
                cargo.SetDescripcion(dato[1])

                cargo_dict = {
                    "id": cargo.GetId(),
                    "descripcion": cargo.GetDescripcion()
                }

                lista_cargos.append(cargo_dict)

        return jsonify({
            "cargos": lista_cargos,
            "cantidad_total_cargos": len(lista_cargos),
            "status": "success"
        })
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500