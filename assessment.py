from flask import Flask , request,jsonify

import requests

app=Flask(__name__)

API_KEY="AIzaSyDNo8R_ZvJAQQdUlXdPWUg9gUdMSoLDQ44"
GEMINI_URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route("/api/generate",methods=["POST"])
def generate():
    try: 
        data=request.get_json()
        prompt=data.get("prompt","")

        payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
         
        headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }
        
        response = requests.post(GEMINI_URL, json=payload, headers=headers)
        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)