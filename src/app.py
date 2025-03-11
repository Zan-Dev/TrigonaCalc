import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    angle = 0
    unit = "degrees"
    error = None
    
    if request.method == "POST":
        try:
            angle = float(request.form["angle"])
            unit = request.form["unit"]
            
            if unit == "degrees":
                angle_rad = np.radians(angle)
            else:
                angle_rad = angle
            
            result = {
                "sin": round(np.sin(angle_rad), 3),
                "cos": round(np.cos(angle_rad), 3),
                "tan": "Undefined" if np.isclose(np.cos(angle_rad), 0, atol=1e-9) else round(np.tan(angle_rad), 3),
                "sinh": round(np.sinh(angle_rad), 3),
                "cosh": round(np.cosh(angle_rad), 3),
                "tanh": round(np.tanh(angle_rad), 3),
                "csc": "Undefined" if np.isclose(np.sin(angle_rad), 0, atol=1e-9) else round(1 / np.sin(angle_rad), 3),
                "sec": "Undefined" if np.isclose(np.cos(angle_rad), 0, atol=1e-9) else round(1 / np.cos(angle_rad), 3),
                "cot": "Undefined" if np.isclose(np.tan(angle_rad), 0, atol=1e-9) else round(1 / np.tan(angle_rad), 3),                
            }

        except ValueError:
            error = "Masukkan angka yang valid!"
    
    return render_template("index.html", result=result, angle=angle, unit=unit, error=error)
