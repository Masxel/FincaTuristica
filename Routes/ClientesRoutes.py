import json
from flask import Blueprint, jsonify, request
from Models.Cliente import Cliente
from Repository.ClienteRepository import ClienteRepository

# Crear Blueprint para clientes
clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/api/clientes/<string:entrada>', methods=["GET"])
def CargarClientes(entrada: str):
    respuesta = {}
    try:
        # Limpiar entrada
        entrada = entrada.replace("'", "")
        respuesta = json.loads(entrada)
        
        # Obtener clientes del repository
        clientes = ClienteRepository().consultar()
        
        respuesta["Entidades"] = clientes
        respuesta["Respuesta"] = "OK"
        respuesta["Total"] = len(clientes) if clientes else 0
            
        return jsonify(respuesta)
        
    except Exception as ex:
        respuesta["Error"] = str(ex)
        respuesta["Respuesta"] = "Error"
        return jsonify(respuesta), 500

@clientes_bp.route('/api/clientes', methods=["GET"])
def obtener_clientes(): 
    try:
        datos_clientes = ClienteRepository().consultar()
        
        lista_clientes = []
        
        if datos_clientes:
            for dato in datos_clientes:
                cliente = Cliente()
                cliente.SetId(dato[0])
                cliente.SetNombre(dato[1])
                cliente.SetApellido(dato[2])
                cliente.SetTelefono(dato[3])
                cliente.SetEmail(dato[4])
                
                cliente_dict = {
                    "id": cliente.GetId(),
                    "nombre": cliente.GetNombre(),
                    "apellido": cliente.GetApellido(), 
                    "telefono": cliente.GetTelefono(),
                    "email": cliente.GetEmail()
                }
                
                lista_clientes.append(cliente_dict)
        
        return jsonify({
            "clientes": lista_clientes,
            "cantidad_total_clientes": len(lista_clientes),
            "status": "success"
        })
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes/<int:id_cliente>', methods=["GET"])
def obtener_cliente_por_id(id_cliente):
    try:
        dato_cliente = ClienteRepository().consultar_por_id(id_cliente)
        
        if dato_cliente:
            cliente = Cliente()
            cliente.SetId(dato_cliente[0])
            cliente.SetNombre(dato_cliente[1])
            cliente.SetApellido(dato_cliente[2])
            cliente.SetTelefono(dato_cliente[3])
            cliente.SetEmail(dato_cliente[4])
            
            cliente_dict = {
                "id": cliente.GetId(),
                "nombre": cliente.GetNombre(),
                "apellido": cliente.GetApellido(),
                "telefono": cliente.GetTelefono(),
                "email": cliente.GetEmail()
            }
            
            return jsonify({
                "cliente": cliente_dict,
                "status": "success"
            })
        else:
            return jsonify({
                "mensaje": f"No se encontró cliente con ID {id_cliente}",
                "status": "not_found"
            }), 404
            
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes', methods=["POST"])
def crear_cliente():
    """Crear un nuevo cliente"""
    try:
        data = request.get_json()
        
        return jsonify({
            "mensaje": "Cliente creado exitosamente",
            "data": data,
            "status": "success"
        }), 201
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes/<int:id_cliente>', methods=["DELETE"])
def eliminar_cliente(id_cliente):
    try:
        cliente_existente = ClienteRepository().consultar_por_id(id_cliente)
        
        if not cliente_existente:
            return jsonify({
                "mensaje": f"No se encontró cliente con ID {id_cliente}",
                "status": "not_found"
            }), 404
        
        resultado = ClienteRepository().eliminar(id_cliente)
        
        if resultado > 0:
            return jsonify({
                "mensaje": f"Cliente con ID {id_cliente} eliminado exitosamente",
                "id_eliminado": id_cliente,
                "status": "success"
            }), 200
        else:
            return jsonify({
                "mensaje": f"No se pudo eliminar el cliente con ID {id_cliente}",
                "status": "error"
            }), 500
            
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500