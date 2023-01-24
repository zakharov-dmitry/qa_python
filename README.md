class BooksCollector:

def __init__(self):
Possible testcases for the method:
    1. after creation of the clas instance, the books_rating dictionary is created and empty
        --> COVERED with test_init_create_new_instance_books_rating_dict_exists_and_empty
    2. after creation of the clas instance, the list of favorites is created and empty
        --> COVERED with test_init_create_new_instance_favorites_list_exists_and_empty

def add_new_book(self, name):
Possible test cases for the method:
    1. after adding the book(s), it is existing in the dictionary books_rating
        --> COVERED with test_add_new_book_add_two_books
    2. after adding the new book its default rating in the favorites list is set on 1
        --> COVERED test_add_new_book_add_one_books_default_rating_is_1
    3. not possible to add the same book twice, the book will be presented only once in the books_rating
    4. [OPTIONAL] check the behavior with same name of the book but with capitalized letter

def set_book_rating(self, name, rating):
Possible test cases for the method:
    1. it is possible to change the rating of the book that exists in books_rating
        --> COVERED with test_set_book_rating_change_rating_on_10_new_rating_is_10
    2. if the book doesn't exist in books_rating nothing will happen by attempt to chance its rating
    3. it is possible to set the rating on 10 for the existing book
        --> COVERED with test_set_book_rating_change_rating_on_10_new_rating_is_10
    4. it is NOT possible to set the rating on 0 for the existing book, rating remain the same
    5. it is NOT possible to set the rating on 11 for the existing book, rating remain the same
    6. [OPTIONAL] check the behavior of the method by giving invalid values for the rating [1.0,"@"," ","a1"]

def get_book_rating(self, name):
Possible test cases for the method:
    1. by providing the existing book name the correct value of its rating will be returned
        ---> COVERED with test_get_book_rating_rating_is_returned
    2. by providing NOT existing book name the method will return nothing (None)

def get_books_with_specific_rating(self, rating):
Possible test cases for the method:
    1. by providing the rating that exists in books_rating ALL books with this rating are returned
        --> COVERED with test_get_books_with_specific_rating_existing_rating_books_are_returned
    2. by providing the NOT existing rating an empty list is returned
        --> COVERED with est_get_books_with_specific_rating_not_existing_rating_empty_list

def get_books_rating(self):
    Possible test cases for the method:
    1. the dictionary books_rating is shown successfully
        --> COVERED with test_get_books_rating_dict_with_all_books_returned

def add_book_in_favorites(self, name):
    Possible test cases for the method:
    1. the book exists in books_rating and can be successfully added to the favorites list
        --> COVERED with test_add_book_in_favorites_existing_book_book_is_added
    2. the book exists in books_rating and after 2 times adding this book to favorites it will be presented only once
    3. the book that NOT exists in books_rating can not be added to the favorites list

def delete_book_from_favorites(self, name):
    Possible test cases for the method:
    1. the book that exists in the list favorites can be successfully deleted from the list
        ---> COVERED with test_delete_book_from_favorites_delete_existing_book_book_is_deleted
    2. if the book not exists in favorites, by trying to delete it the favorite list will remain unchanged

def get_list_of_favorites_books(self):
    Possible test cases for the method:
    1. the list favorites is shown successfully
        --> COVERED with test_get_list_of_favorites_books_list_is_returned
