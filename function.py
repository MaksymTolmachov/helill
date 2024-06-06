# user_name = input("Enter your name")
# normalized_user_text = user_name.strip().title()
# print(normalized_user_text)
#
#
# user_surname = input("Enter your surname")
# normalized_user_text = user_surname.strip().title()
# print(normalized_user_text)


# def get_normalized_print(message):
#     user_name = input(message)
#     normalized_user_text = user_name.strip().title()
#     print(normalized_user_text)
#
#
# get_normalized_print("Enter your name")
# get_normalized_print("Enter your surname")

def add_two_numbers(number_1, number_2):
    """number_1 must not be zero"""
    result = number_1 + number_2
    return result

result = add_two_numbers(2,6)

print(result)

def can_you_swim(answer):
    positive_part = "yes"
    result = positive_part in answer.lower()
    return result


can_you_swim("yes")






