from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
import openai
import os
import json
import uuid
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['GENERATED_FOLDER'] = 'generated/'
app.secret_key = os.getenv('FLASK_SECRET_KEY')  
openai.api_key = os.getenv('OPENAI_API_KEY')

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['GENERATED_FOLDER']):
    os.makedirs(app.config['GENERATED_FOLDER'])

def generate_threats_for_component(component_name, component_type):
    # Prepare the prompt for ChatGPT
    prompt = (
        f"Identify STRIDE threats for a component named '{component_name}' of type '{component_type}'. "
        "Provide each threat with the following details: title, description, type (Spoofing, Tampering, etc.), status, severity, mitigation, and modelType as 'STRIDE'."
        "Format the output as a JSON array."
    )
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a security expert specializing in threat modeling using STRIDE methodology."},
                      {"role": "user", "content": prompt}]
        )
        
        # Parse the response
        threats_data = json.loads(response['choices'][0]['message']['content'])
        
        # Ensure each threat has a unique ID
        for threat in threats_data:
            threat["id"] = str(uuid.uuid4())  # Generate a unique ID for each threat
            threat["modelType"] = "STRIDE"    # Specify the model type

        return threats_data

    except Exception as e:
        print("Error generating threats:", e)
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.json'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            with open(file_path, 'r') as f:
                json_data = json.load(f)

            # Iterate through each component in the JSON to generate threats
            for diagram in json_data.get("detail", {}).get("diagrams", []):
                for cell in diagram.get("cells", []):
                    component_name = cell["data"].get("name", "Unknown Component")
                    component_type = cell["data"].get("type", "Unknown Type")
                    
                    # Generate STRIDE threats for each component
                    threats = generate_threats_for_component(component_name, component_type)
                    
                    # Update the component's "threats" field with generated data
                    cell["data"]["threats"] = threats

            # Save the updated JSON to a new file for download
            output_filename = f"threat_model_{uuid.uuid4()}.json"
            output_path = os.path.join(app.config['GENERATED_FOLDER'], output_filename)
            with open(output_path, 'w') as f:
                json.dump(json_data, f, indent=4)

            # Pass the updated JSON and download URL to the template
            return render_template('results.html', updated_json=json_data, download_url=output_filename)

    return render_template('index.html')

# Endpoint to test ChatGPT API connectivity
@app.route('/test-chatgpt')
def test_chatgpt():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Hello, can you confirm API connectivity?"}]
        )
        return jsonify({"status": "success", "response": response['choices'][0]['message']['content']})
    except Exception as e:
        return jsonify({"status": "failure", "error": str(e)})

# Endpoint for downloading the generated JSON file
@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(app.config['GENERATED_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)