#I dom.t know if it needs to be on a site or on terminal (but i guees its needs to be on site because of put_html)
import pprint

from pywebio.output import put_html, put_text
from pywebio.input import input as input_pw


user_surname = input_pw("Enter your surname")


def get_user_name(message):
    user_name = input_pw(message)
    put_text(user_name)
    return user_name

put_html(f"<h1> Вітаємо тебе, шановний {user_surname}</h1>")





def get_area_of_rectangle(side_number_1, side_number_2):
    area_of_rectangle = side_number_1 * side_number_2
    return area_of_rectangle


get_area_of_rectangle(2, 5)




