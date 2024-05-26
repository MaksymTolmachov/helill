head = "~" * 50
beauty_for_name = "*" * 10
print(head)

MSG_INPUT_FOOD_NAME = "Enter your dish name"
MSG_INPUT_FOOD_RECIPE = "Enter recipe of your dish "
food_name = input(MSG_INPUT_FOOD_NAME).upper().strip()
food_recipe = input(MSG_INPUT_FOOD_RECIPE).lower().strip()
result_name = f"{beauty_for_name}{food_name}{beauty_for_name}"
result_recipe = f"{food_recipe} 🍖"
number_of_words = "result_recipe".lower().count("м'ясо")
result_count = f"The word м'ясо was used {number_of_words} times"
print(result_name)
print(result_recipe)
print(result_count)
print(head)

