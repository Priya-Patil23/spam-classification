from flask import Flask , render_template , request
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow.keras.models import load_model
import re
from nltk.stem import WordNetLemmatizer
w = WordNetLemmatizer()
from nltk.corpus import stopwords
import numpy as np


def clean2(x):
    new = []
    for i in x.split(" "):
        if len(i) >= 2 and i not in stopwords.words('english'):
            new.append(w.lemmatize(i))

    return " ".join(new)


def clean(x):
    return re.sub('[^a-zA-Z0-9]' , " " , x).lower()

model = load_model('spam.h5')
tokenize = pickle.load(open('tokenizer.pkl' , 'rb'))
maxlength = 442

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict" , methods = ['POST'])
def predict():
    input = request.form.get("email")
    first = clean(input)
    second = clean2(first)
    a = model.predict(pad_sequences(tokenize.texts_to_sequences([second]) , maxlen = 442 , padding = 'post'))
    ans = np.round(a[0][0])
    if ans == 0.0:
        result = "Ham"
    else:
        result = "Spam"
    return render_template("index.html", result=result)



if "__main__" == __name__:
    app.run(debug = True)