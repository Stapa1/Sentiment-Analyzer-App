from flask import Flask, request, jsonify, render_template
import pickle
import torch
from transformers import BertTokenizer, BertForSequenceClassification

app = Flask(__name__)

# Load the pre-trained BERT model and tokenizer
with open('bert_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review_text = data['text']
    
    # Tokenize the input review text
    inputs = tokenizer(review_text, return_tensors='pt', truncation=True, padding=True, max_length=512)

    # Perform the prediction
    with torch.no_grad():
        logits = model(**inputs).logits

    # Get sentiment label and score
    predicted_class = torch.argmax(logits, dim=-1).item()
    sentiment = {0: "Very Negative", 1: "Negative", 2: "Neutral", 3: "Positive", 4: "Very Positive"}
    score = torch.nn.functional.softmax(logits, dim=-1).max().item()

    return jsonify({'label': sentiment[predicted_class], 'score': score})

if __name__ == '__main__':
    app.run(debug=True)
