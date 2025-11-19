from flask  import Flask ,render_template,request,send_file
import pandas as pd
import joblib

app=Flask(__name__)

model=joblib.load('model.pkl')
vectorizer=joblib.load('vectorizer.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    resullt=None
    score=None
    
    if request.method=='Post':
        message=request.form['message']
        
        vec=vectorizer.transform([message])
        
        prediction=model.predict(vec)[0]
        
        score=model.decision_function(vec)[0]
        
        result='Spam' if prediction==1 else 'Not Spam'
        
    return render_template('index.html', result=result, score=score)    


if __name__=='__main__':
    app.run(debug=True,port=5001)
    
