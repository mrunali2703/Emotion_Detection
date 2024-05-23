from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)
CORS(app)

model = joblib.load('Random_forest_train.pkl')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    if isinstance(text, str):
        text = text.lower()
    else:
        text = str(text).lower()

    text = ' '.join([word for word in text.split() if word not in stop_words])
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

@app.route('/detect_emotions', methods=['POST'])
def detect_emotions_route():
    data = request.json
    text = data.get('text', '')
    processed_text = preprocess_text(text)
    prediction = model.predict([processed_text])
    return jsonify({'emotions': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
