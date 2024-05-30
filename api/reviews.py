import numpy as np
import urllib.request
import bs4 as bs
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# load the nlp model and tfidf vectorizer from disk
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
vectorizer = pickle.load(open('tranform.pkl', 'rb'))

@app.route("/reviews", methods=["POST"])
def reviews():
    imdb_id = request.form['imdb_id']
    sauce = urllib.request.urlopen('https://www.imdb.com/title/{}/reviews?ref_=tt_ov_rt'.format(imdb_id)).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    soup_result = soup.find_all("div", {"class": "text show-more__control"})

    reviews_list = []  # reviews
    reviews_status = []  # comments (good or bad)
    for reviews in soup_result:
        if reviews.string:
            reviews_list.append(reviews.string)
            # passing the review
            movie_review_list = np.array([reviews.string])
            movie_vector = vectorizer.transform(movie_review_list)
            pred = clf.predict(movie_vector)
            reviews_status.append('Good' if pred else 'Bad')

    # combining reviews and comments
    movie_reviews = {reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))}

    return render_template('reviews.html', reviews=movie_reviews)

if __name__ == "__main__":
    app.run()
