from pywebio.output import put_html, put_text , put_image
from pywebio.input import input as input_pw
from pywebio.input import NUMBER, FLOAT
from pywebio.session import run_js
from pywebio import start_server

name = str(input_pw(f"What is your name?")).title()


total_score = 0


def ask_a_quation_number_1(quation_1) -> int:
    input_pw(quation_1)
    return

def get_amount_of_points_round_1_correct(quation_1):
    if quation_1 == "8":
        total_score + 1
        return put_text(f"{name},your score is{total_score}")

def ask_a_quation_number_2(quation_2) -> int:
        input_pw(quation_2)
        return


def get_amount_of_points_round_2_correct(quation_2):
    if quation_2 == 9:
        total_score + 1
        return put_text(f"{name},your score is{total_score}")

def ask_a_quation_number_3(quation_3) -> float:
        input_pw(quation_3)
        return

def get_amount_of_points_round_3_correct(quation_3):
    if quation_3 == 4.5:
        total_score + 1
        return put_text(f"{name},your score is{total_score}")

def ask_a_quation_number_4(quation_4) -> float:
        input_pw(quation_4)
        return


def get_amount_of_points_round_4_correct(quation_4):
    if quation_4 == 84:
        total_score + 1
        return put_text(f"{name},your score is{total_score}")

def ask_a_quation_number_5(quation_5) -> float:
        input_pw(quation_5)
        return


def get_amount_of_points_round_5_correct(quation_5):
    if quation_5 == 224:
        total_score + 1
        return put_text(f"{name},your score is{total_score}")

def put_image_of_stars(total_score):
    if not  total_score == 5:
        return put_text(f"{name},your score is{total_score}")

def put_image_of_stars(total_score):
    if total_score == 5:
        img = open('five_stars.jpeg', 'rb').read()
        put_image(img, width='500px')





ask_a_quation_number_1("How much is 5 + 3")
ask_a_quation_number_2("How much is 54 ∻ 6")
ask_a_quation_number_3("How much is 9 ∻ 2")
ask_a_quation_number_4("How much is 50 + 34")
ask_a_quation_number_5("How much is 134 + 90")
