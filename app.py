# from distutils.log import debug
import os
import model_load
from flask import Flask, render_template, request



app = Flask(__name__)           


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])  
def submission():  
    if request.method == 'POST':
        f = request.form.get('text_box')
        f_path = f
        p = model_load.predict_label(f_path)
        return render_template("success.html", prediction = p, f_path=f_path)
    else: 
        return 'Something went wrong'    


if __name__ == "__main__":
    app.run(debug=True)

