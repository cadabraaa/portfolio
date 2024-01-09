from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs.15,00,000'
}, {
    'id': 2,
    'title': 'Data Scienctist',
    'location': 'Delhi, India',
    'salary': 'Rs.15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs.12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Franscisco, USA',
    'salary': '$.120,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/nav')
def nav():
  return render_template('nav.html')


@app.route('/footer')
def footer():
  return render_template('footer.html')


@app.route('/portfolio1')
def portfolio1():
  return render_template('portfolio1.html')


@app.route('/QuickSight')
def QuickSight():
  return render_template('QuickSight.html')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
