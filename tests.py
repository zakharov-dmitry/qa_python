from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_init_create_new_instance_books_rating_dict_exists_and_empty(self):
        collector = BooksCollector()
        assert type(collector.books_rating).__name__ == 'dict' and len(collector.books_rating) == 0

    def test_init_create_new_instance_favorites_list_exists_and_empty(self):
        collector = BooksCollector()
        assert type(collector.favorites).__name__ == 'list' and len(collector.favorites) == 0

    def test_add_new_book_add_one_books_default_rating_is_1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    def test_set_book_rating_change_rating_on_10_new_rating_is_10(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        new_rating = 10
        collector.set_book_rating('Гордость и предубеждение и зомби', new_rating)
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 10

    def test_get_book_rating_rating_is_returned(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_rating('Гордость и предубеждение и зомби') == 1

    def test_get_books_with_specific_rating_existing_rating_books_are_returned(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        result = collector.get_books_with_specific_rating(1)
        assert len(result) == 2 \
               and 'Гордость и предубеждение и зомби' in result \
               and 'Что делать, если ваш кот хочет вас убить' in result

    def test_get_books_with_specific_rating_not_existing_rating_empty_list(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_rating(1)
        assert type(result).__name__ == 'list' and len(result) == 0

    def test_get_books_rating_dict_with_all_books_returned(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        result = collector.get_books_rating()
        assert type(result).__name__ == 'dict' \
               and 'Гордость и предубеждение и зомби' in result \
               and 'Что делать, если ваш кот хочет вас убить' in result

    def test_add_book_in_favorites_existing_book_book_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

    def test_delete_book_from_favorites_delete_existing_book_book_is_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' not in collector.favorites

    def test_get_list_of_favorites_books_list_is_returned(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        result = collector.get_list_of_favorites_books()
        assert type(result).__name__ == 'list' and len(result) == 1 and 'Гордость и предубеждение и зомби' in result
