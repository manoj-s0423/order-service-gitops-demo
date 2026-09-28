from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "order-service",
        "version": "1.0.0",
        "status": "healthy"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/orders/<order_id>")
def get_order(order_id):
    return jsonify({
        "order_id": order_id,
        "status": "CONFIRMED"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
