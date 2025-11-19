from flask  import Flask ,render_template,request,send_file
import pandas as pd
import joblib

app=Flask(__name__)

model=joblib.load('spam_model.pkl')
vectorizer=joblib.load('tfidf.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    score = None

    if request.method == 'POST':
        message = request.form.get('message', '')

        vec = vectorizer.transform([message])

        prediction = model.predict(vec)[0]

        # Some models may not implement decision_function; guard against that
        try:
            score = model.decision_function(vec)[0]
        except Exception:
            score = None

        result = 'Spam' if prediction == 1 else 'Not Spam'

    return render_template('index.html', result=result, score=score)


if __name__=='__main__':
    app.run(debug=True,port=5001)
    
