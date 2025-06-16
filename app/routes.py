from flask import render_template, jsonify
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/info")
def info():
    return jsonify(
        name="DevOps Lab Environment",
        version="1.0.0",
        authors="Everton Vasconcelos"
    )

@app.route("/metrics")
def metrics():
    return jsonify(
        cpu_usage="15%",
        memory_usage="45%",
        status="running"
    )

