from flask_app import app

#Importar mis controladores
from flask_app.controllers import users, messages

if __name__ == "__main__":
    app.run(debug=True)