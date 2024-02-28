from flask import Flask, render_template
app = Flask(__name__)

@app.route ('/')
def home_page ():
    return render_template ("index.html")


@app.route ('/play')
def level_1 ():
    return render_template("index.html", num = 3, color = "#ADD8E6")

@app.route ('/play/<int:num>')
def level_2 (num):
    return render_template("index.html", num = num, color = "#ADD8E6")


@app.route ('/play/<int:num>/<string:color>')
def level_3 (num, color):
    return render_template("index.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug = True)