MSG_INPUT_FIRST_NAME = "Enter your name"
MSG_INPUT_LAST_NAME = "Enter your surname "

user_first_name = input(MSG_INPUT_FIRST_NAME).title().strip()
# user_first_name = user_first_name.title()
# user_first_name = user_first_name.strip()
user_second_name = input(MSG_INPUT_LAST_NAME).title().strip()

# welcome_text = "very glad to you "
# mark = "!"
# result = welcome_text+user_first_name+user_second_name+mark
# max two pluses

template = "Very glad to you {user_first_name} {user_second_name}!"
result = template.format(user_first_name=user_first_name, user_second_name=user_second_name)
# result = f"Very glad to you {user_first_name} {user_second_name}!"
print(result)
print("thanks")
