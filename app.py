from flask import Flask, render_template, request
import joblib
import threading
import webbrowser
import time

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('sentiment_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        comment = request.form['comment']
        data = vectorizer.transform([comment])
        prediction = model.predict(data)[0]
        return render_template('index.html', comment=comment, prediction=prediction)

def open_browser():
    time.sleep(1)  # Let the server start
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run(debug=False, use_reloader=False)
