from transformers import BertTokenizer, BertForSequenceClassification
import pickle

# Load the pre-trained model and tokenizer
model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Save the model and tokenizer to .pkl files
with open('bert_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

print("Model and tokenizer saved successfully!")
