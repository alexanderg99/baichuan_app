from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Define the route to serve the webpage
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle form submission
@app.route('/submit_text/', methods=['POST'])
def submit_text():
    
    input_text = request.form.get('inputText')
    print(f"Submitted Text {input_text}")
    # Send a request to FastAPI route
    response = requests.post('http://0.0.0.0:8000/infer', json={'inputText': input_text})

    if response.status_code == 200:
        result = response.json()['result']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Error processing text'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)