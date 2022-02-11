from flask import Flask, json, render_template, request
import random

saturation = 95
luminance = 50

app = Flask(__name__)

def rosify(palabra):
  mybytes = palabra.lower().encode('utf-8')
  myint = int.from_bytes(mybytes, 'little')
  random.seed(myint)
  hue = random.randint(290, 340)
  color = 'hsl(%d, %d%%, %d%%)' % (hue, saturation, luminance)
  return(color)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def uploadFilesPB():
    # get the uploaded file
    name = request.form['name']
    color = rosify(name)
    return render_template("index.html", color=color)

if __name__ == "__main__":
    app.run()