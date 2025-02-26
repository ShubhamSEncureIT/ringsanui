from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    try:
        # Get webhook data
        data = request.json  
        timestamp = datetime.utcnow().isoformat() + "Z"

        # Log received data
        print(f"✅ Webhook received at {timestamp}")
        print("Received Data:", json.dumps(data, indent=2))

        # Save to a local JSON file (simulating database storage)
        with open("webhook_data.json", "a") as file:
            json.dump({"timestamp": timestamp, "data": data}, file)
            file.write("\n")

        # Send API response with received data
        return jsonify({
            "message": "Webhook received successfully",
            "timestamp": timestamp,
            "received_data": data
        }), 200

    except Exception as e:
        print("❌ Error:", str(e))
        return jsonify({"error": "Failed to process webhook"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
