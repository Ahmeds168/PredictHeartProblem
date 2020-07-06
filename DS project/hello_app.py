from flask import request
from flask import jsonify
from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_cors import cross_origin

app= Flask(__name__)


@app.route('/')
def home():
	return render_template('hello.html')


@app.route('/ahmed', methods=[ 'post'])
def hello():


    message=request.get_json(force=True)
    age=float(message['age'])
    gender=float(message['gender'])
    cp=float(message['cp'])
    restbp=float(message['restbp'])
    chol=float(message['chol'])
    fbs=float(message['fbs'])
    restecg=float(message['restecg'])
    thalach=float(message['thalach'])
    exang=float(message['exang'])
    oldpeak=message['oldpeak']
    slope=float(message['slope'])
    ca=float(message['ca'])
    thal=float(message['thal'])


    import pandas as pd # load and manipulate data and for One-Hot Encoding
    import numpy as np # calculate the mean and standard deviation
    import matplotlib.pyplot as plt # drawing graphs
    from sklearn.tree import DecisionTreeClassifier # a classification tree
    from sklearn import tree
    from sklearn.model_selection import train_test_split # split  data into training and testing sets
    from sklearn.model_selection import cross_val_score # cross validation
    from sklearn.metrics.classification import confusion_matrix # creates a confusion matrix

    df = pd.read_csv('processed.cleveland.data',header=None)
    df.columns = ['age', 
                'sex', 
                'cp', 
                'restbp', 
                'chol', 
                'fbs', 
                'restecg', 
                'thalach', 
                'exang', 
                'oldpeak', 
                'slope', 
                'ca', 
                'thal', 
                'hd']

    df_no_misssing= df.loc[(df['ca']!='?')&(df['thal']!='?')]
    X = df_no_misssing.drop('hd',axis=1).copy()
    y = df_no_misssing['hd'].copy()
    pd.get_dummies(X,columns=['cp']).head()
    X_encoded = pd.get_dummies(X,columns=['cp','restecg','slope','thal'])
    y_not_zero_index=y>0
    y[y_not_zero_index]=1
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
    clf_dt = DecisionTreeClassifier(random_state=42)
    clf_dt = clf_dt.fit(X_train, y_train)

    import pandas as pd
    dict={'age':age, 'sex':gender,'cp':cp,'restbp':restbp,'chol':chol,'fbs':fbs,'restecg':restecg,'thalach':thalach,'exang':exang,'oldpeak':oldpeak,'slope':slope,'ca':ca,'thal':thal}
    dataframe = pd.DataFrame.from_dict(dict, orient='index').T
    if clf_dt.predict(dataframe)[0]==0:
        status="no heart disease"
    else:
        status="heart disease"




    response={
    'greeting':'Patient has  '+status + '!'

    }
    return jsonify(response)  
    


if __name__ == "__main__":
    app.run(debug=True) 





        
            