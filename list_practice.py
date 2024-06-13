from pywebio.input import textarea, select, checkbox, radio, FLOAT, DATE, PASSWORD, DATETIME, input as input_pw
from pywebio.output import put_success, put_error, put_warning, put_html, put_image
from pywebio.session import run_js
admin_one_login = "aaa"
admin_one_password = "123"

good_weather = ["Sunny", "Snowy"]
bad_weather = ["Cloudy", "Rainy"]
weather_options = bad_weather + good_weather

monitoring_info = []
def main():
    put_html("<h1> program for monitoring of weather</h1>")
    login = input_pw("Enter your login", required=True)
    password = input_pw("Enter your password", type=PASSWORD, required=True )

    if login != admin_one_login or admin_one_password != admin_one_password:
        put_error("Wrong password or login")
        run_js("setTimeout{function(){location.reload();}, 6000)")
        return

    monitoring_date = input_pw("Enter date of monitoring", type=DATE)
    weather = select("what weather is today?", options=weather_options)
    if weather in good_weather:
        put_success("Very good that you went on a walk")

        print(monitoring_info)
