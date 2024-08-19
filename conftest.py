from testin_oop_homework import Library



def library_creation_of_list_of_books() -> dict:
    list_of_books_con = {"list_of_book": [], "name": "Kharkiv national Library", "amount_of_books": 0}
    return list_of_books_con

def library() -> Library:
    library = Library(list_of_book=[] , name="Kharkiv national Library", amount_of_books=0)
    return library




