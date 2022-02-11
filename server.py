from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=7)


@app.route('/success')
def success():
    return "success"

if __name__=="__main__":
    app.run(debug=True)

