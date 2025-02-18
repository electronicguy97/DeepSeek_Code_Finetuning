from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained("./deepseek-code-search")
tokenizer = AutoTokenizer.from_pretrained("./deepseek-code-search")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = tokenizer(data['text'], return_tensors='pt')
    outputs = model.generate(**inputs)
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)