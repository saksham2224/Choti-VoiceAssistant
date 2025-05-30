from flask import Flask, request, jsonify
from flask_cors import CORS
from assistant import process_query

app = Flask(__name__)
CORS(app)  # To allow frontend access

@app.route('/process', methods=['POST'])
def process():
    print("Received request at /process")  # Debug
    data = request.json
    query = data.get('query', '')
    print("User query:", query)  # Debug
    response_text = process_query(query)
    print("Response generated:", response_text)  # Debug
    return jsonify({"response": response_text})

if __name__ == '__main__':
    print("🚀 Starting Flask backend server on http://127.0.0.1:5000")
    app.run(debug=True)
