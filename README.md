# CineSenseAI

CineSenseAI is an AI-based movie recommendation system that leverages machine learning and data from The Movie Database (TMDb) to provide personalized movie recommendations based on user preferences.

## Technologies Used

- Flask
- gunicorn
- numpy
- scikit-learn
- pandas
- beautifulsoup4
- requests

## About

CineSenseAI uses a Flask backend to handle requests and responses, while gunicorn is used as the WSGI HTTP server to serve the Flask application.

For data manipulation and machine learning tasks, numpy, scikit-learn, and pandas are used. These libraries help in processing and analyzing data, as well as building machine learning models for movie recommendations.

Web scraping of movie data from external sources is done using beautifulsoup4, a Python library for pulling data out of HTML and XML files.

Requests library is utilized for making HTTP requests to the TMDb API, which provides access to a large database of movies, TV shows, and actors.

The web app is built using AJAX (Asynchronous JavaScript and XML) technology, allowing seamless interaction between the user interface and the backend server without the need for page reloads.

## Usage

To run the CineSenseAI web application:

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Set up your TMDb API key by following the instructions on the TMDb website.
3. Start the Flask application with gunicorn by running `gunicorn -w 4 -b 127.0.0.1:5000 app:app`.
4. Access the web application in your browser at `http://localhost:5000`.

## License

This project is licensed under the [MIT License](LICENSE).
