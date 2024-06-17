from pywebio.input import input_group,slider, textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw
from pywebio.output import put_success, put_error, put_warning, put_html,put_table, put_image
from pywebio.session import run_js
from pywebio import start_server

creds = {
    "login": "admin",
    "password": "123",
}


def main():
    put_html("<h1>weather of monitoring of weather</h1>")
    login_form = input_group(
        "Enter your creds",
        [
            input_pw("Login", placeholder="Login here", name="login"),
            input_pw("Password", type=PASSWORD, placeholder="Input password here", name="password")
        ]

    )
    if login_form == creds:
        put_success("Welcome")
    else:
        put_warning("Go away")
        run_js("setTimeout(function(){location.reload();}, 5000)")
        return
    weather_data = input_group(
        "Enter weather params",
        [
            input_pw("temperature",name="temperature", required=True),
            slider("",  name="humidity", max_value=100,min_value=0,required=True),
        ]

    )
    obseving_data.append(weather_data)
    weather_acunulated_data = [["temperature", "humidity"]]

    run_js("setTimeout(function(){location.reload();}, 5000)")

if __name__ == "__main__":
    start_server(main, port=10000)