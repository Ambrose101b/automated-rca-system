from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    # This endpoint tells our future monitoring system that the app is OK
    return jsonify({"status": "healthy", "message": "Service is running normally"}), 200

if __name__ == '__main__':
    # Running on port 5000, accessible from any IP (0.0.0.0)
    app.run(host='0.0.0.0', port=5000)