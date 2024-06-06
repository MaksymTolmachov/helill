from pywebio.output import put_html, put_text
from pywebio.input import input as input_pw
from pywebio.input import NUMBER, FLOAT
from pywebio.session import run_js
from pywebio import start_server


def get_triangle_area(catet1: int | float, catet2: int | float) -> int | float:
    result = (catet1 * catet2) / 2
    return result


def get_formatted_html_h2(message: str) -> str:
    result_h2 = f"<h2>{message}</h2>"
    return result_h2


def convert_string_to_number(string_like_number: str) -> float | int:
    if string_like_number.isdigit():
        result = int(string_like_number)

        is_only_one_dot_in_strings = string_like_number.count(".") == 1

        if string_like_number.count(".") == 1 and string_like_number.replace(".", "").isdigit():
            result
    return result


def main():
    catet_1 = input_pw("Enter length of first catet", type=NUMBER)
    catet_2 = input_pw("Enter length of second catet")
    catet_2 = float(catet_2)
    triangle_area = get_triangle_area(catet_1, catet_2)
    put_text(triangle_area)


    run_js("setTimeout(function(){location.reload();}, 5000)")

if __name__ == "__main__":
    start_server(main, port=10000)
