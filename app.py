import io
from flask import Flask, render_template, request
import pathlib
import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from tensorflow.keras.preprocessing import image
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'
db = SQLAlchemy(app)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    guide = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return '<Food %r>' % self.id

CUR_PATH = pathlib.Path().resolve()
MODEL_PATH = os.path.join(CUR_PATH, 'Models\\ResNet152V2\\fine_tune_model_best.keras')
IMAGE_SIZE = (256, 256)

model = load_model(MODEL_PATH)

esp32cam_ip = '10.254.5.180'

def preprocess(mImg):
    img = mImg.copy()
    img.resize(IMAGE_SIZE)
    img = image.img_to_array(img) / 255
    img = np.expand_dims(img, axis=0)
    return img

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', esp_ip=esp32cam_ip)

@app.route('/guide', methods=['POST'])
def result():
    img = request.files['img'].read()
    img = Image.open(io.BytesIO(img))
    mImg = preprocess(img)
    pred_probs = model.predict(mImg)[0]
    index = np.argmax(pred_probs)
    food = Food.query.filter_by(id=int(index+1)).first()
    return render_template('result.html', food=food)

if __name__ == '__main__':
    app.run(debug=True)