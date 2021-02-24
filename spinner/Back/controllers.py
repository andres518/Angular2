
from flask.views import MethodView
from flask import jsonify, request
import time



class LoginUserControllers(MethodView):
    """
        Example Login
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
       

         
        return jsonify({"login ok": True}), 200
    

    def get():
        pass
    
    
    def put():
        pass


class LoginUserControllers2(MethodView):
    """
        Example Login
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        email = content.get("Correo")
        password = content.get("Contraseña")
        name = content.get("Nombre")
        

        return jsonify({"login ok": True, "Nombre": name, "Correo": email}), 200
    



class RegisterUserControllers(MethodView):
    """
        Example register
    """
    def post(self):
        #simulacion de espera en el back con 1.5 segundos
        time.sleep(3)
        content = request.get_json()
        Correo = content.get("Correo")
        Contraseña = content.get("Contraseña")
        Nombre = content.get("Nombre")
    

        return jsonify({"register ok": True, "Nombre": Nombre, "Correo": Correo,"Contraseña": Contraseña}), 200
    
    def get():
        pass
    
    def put():
        pass
     
