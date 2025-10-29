import json
from flask import Blueprint, jsonify, request
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
    """Obtener todos los clientes"""
    try:
        clientes = ClienteRepository().consultar()
        
        return jsonify({
            "clientes": clientes,
            "total": len(clientes) if clientes else 0,
            "status": "success"
        })
        
    except Exception as ex:
        return jsonify({
            "error": str(ex),
            "status": "error"
        }), 500

@clientes_bp.route('/api/clientes', methods=["POST"])
def crear_cliente():
    """Crear un nuevo cliente"""
    try:
        # Obtener datos JSON del request
        data = request.get_json()
        
        # Aquí integrarías con ClienteService para crear el cliente
        # Por ahora solo retorno confirmación
        
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