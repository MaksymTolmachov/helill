
from pywebio.input import input as input_pw
from pywebio.output import put_html, put_text, put_image


#header
put_html("<h1>Its finally summer🎉!!!</h1>")
put_html("<h2> Сонце гріє </2h> ")
summer_poem = """Сонце гріє, вітер віє
З поля на долину,
Над водою гне з вербою
Червону калину;
На калині одиноке
Гніздечко гойдає, -
А де ж дівся соловейко?
Не питай, не знає. """
put_text(summer_poem)
question_what_plans_for_your_summer = input_pw("What plans do you have for this summer?")
# I don't know how to count symbols. I spend about an hour to find th answer aaaaaaaaaa!
# I don't know how to count symbols. I spend about an hour to find th answer aaaaaaaaaa!
# I don't know how to count symbols. I spend about an hour to find th answer aaaaaaaaaa!
symbols_in_my_summer_plans = len(question_what_plans_for_your_summer)
put_text(symbols_in_my_summer_plans)
img = open("Summer-1170x650-1.jpg", "rb").read()
put_image(img, width="650px")





