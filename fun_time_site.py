from pywebio.input import input as input_pw
from pywebio.input import NUMBER
from pywebio.output import put_text, put_html

pizza_cost = 250
cola_cost = 60



#header
put_html("<h1>Helo my name is Marin</h1> ")
put_html("<h2>Helo my name is Marin🍕</h2> ")

#inpute section
name = str(input_pw("what is your name?"))


formatted_order_cola = f" good evening, {name}. how much pizzas want to order? "
put_text(formatted_order_cola)
pizza_count_order = input_pw("Enter wanted amount", type=NUMBER,)
pizza_order_cost = pizza_count_order * pizza_cost
put_text(formatted_order_cola * 2)
formatted_order_cola = f"{name} also you may want to buy a coke with price {cola_cost} for bottle "
put_text(formatted_order_cola)
cola_count_cost = input_pw("Enter amount", type=NUMBER)
cola_order_cost = ""









