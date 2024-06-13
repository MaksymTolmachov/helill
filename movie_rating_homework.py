from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw, slider
from pywebio.output import put_success, put_error, put_warning, put_html, put_image, put_text
from pywebio.session import run_js
from pywebio import start_server

movie_type_options = ["Horror", "Comedy", "Action", "Western", "Science fiction", "Fiction"]
movie_emotion_options = ["Sad", "Happy", "Disappointed", "Confused"]
reviews_info = []

def main():
    user_name = input_pw("What is your name?").title()
    name_of_the_movie = input_pw("What is the name of the movie? ").title()
    movie_type_select = select("What type of movie is that?", options=movie_type_options)
    text_about_the_movie = input_pw("Write down short text about your opinion on this movie.")
    movie_rating = slider("How will you rate this movie?", min_value=1, max_value=10)
    if movie_rating == 8 or 9 or 10:
#I put html to make it nicer to look at
        put_html("<h1>I think it's a good movie already.</h1>")
    emotion_after_watching_movie = select("What emotion this movie left after it?", options=movie_emotion_options)
    good_or_bad_movie = radio("Will you recommend this movie?", options=["Yes", "No"])







    reviews_info.append([user_name, name_of_the_movie, movie_type_select, text_about_the_movie, movie_rating, emotion_after_watching_movie, good_or_bad_movie])
    run_js("setTimeout(function(){location.reload();}, 2000)")

if __name__ == "__main__":
    start_server(main, part=14000)



