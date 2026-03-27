from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gov/home.html')

@app.route('/gov/category')
def category():
    return render_template('gov/category.html')

@app.route('/gov/department')
def department():
    return render_template('gov/department.html')

if __name__ == "__main__":
    app.run(debug=True)