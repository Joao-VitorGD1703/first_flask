from flask import Flask
from controller.item_controller import item_blueprint

app = Flask(__name__)

# Registrando o blueprint
app.register_blueprint(item_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
