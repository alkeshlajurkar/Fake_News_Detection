from flask import Flask, escape, request, render_template
import pickle


# initialize a Tfidfvectorizer
vector = pickle.load(open("vectorizer.pk1", 'rb'))
model = pickle.load(open("finalized_model.pk1", 'rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("prediction.html")

@app.route('/prediction', methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        news = str(request.form['news'])
        print(news)
        predict = model.predict(vector.transform([news]))[0]
        print(predict)
        
        return render_template("prediction.html", prediction_text="News Headline is {}".format(predict))
    
    else:
        return render_template("prediction.html")

if __name__ == '__main__':
    app.run()

