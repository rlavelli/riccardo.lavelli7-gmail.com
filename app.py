import numpy as np
import re
from flask import Flask,render_template,url_for,request
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from collections import Counter

stop_words = set(stopwords.words('english'))

app = Flask(__name__)

# home page ---
@app.route('/')
def home():
	return render_template('home.html')

# sentiment page ---
@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')

# topic page ---
@app.route('/topic')
def topic():
    return render_template('topic.html')


# predict sentiment page ---
@app.route('/predict',methods=['POST'])
def predict():
	

	if request.method == 'POST':
		message = request.form['message']
		#data = [message]
		sentiment_obj = TextBlob(message)
		my_prediction = sentiment_obj.sentiment.polarity
	return render_template('result.html',prediction = my_prediction)

# predict topic page ---
@app.route('/topic_predict', methods=['POST'])
def topic_predict():

    if request.method == 'POST':
        message = request.form['message']
        message_clean = re.sub(r'[^\w\s]','', message)
        message_clean = word_tokenize(message_clean)
        new_sentence =[]
        for w in message_clean:
            if w not in stop_words: new_sentence.append(w)
        counts = Counter(new_sentence)
        counts_high = {x : counts[x] for x in counts if counts[x] >= 3}
        
    return render_template('result_topic.html', word_count=counts_high)


if __name__ == '__main__':
	app.run(debug=True)


# -- Example
#phrase = 'the weather is beautiful!'
#sentiment_objects = TextBlob(phrase)

#print(sentiment_objects.sentiment.polarity)
#print(phrase)
# --