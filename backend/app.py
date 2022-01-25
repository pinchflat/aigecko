import os
from flask import Flask
from flask_cors import CORS
from api.image import image_route

app = Flask(__name__)
app.register_blueprint(image_route)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "NOT_A_SECRET_KEY")
app.debug = os.getenv("DEBUG", False)

CORS(app)

if __name__ == "__main__":    
    port = int(os.getenv("PORT", 5000))
    app.run(os.getenv("LISTEN", "0.0.0.0"), port=port)