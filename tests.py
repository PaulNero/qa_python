from main import BooksCollector
import pytest

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_with_right_name_and_rating_1(self, init_empty_BookColletor, book_list):
        init_empty_BookColletor.add_new_book(book_list[0])

        assert book_list[0] in init_empty_BookColletor.get_books_rating()
        assert init_empty_BookColletor.get_books_rating().get(book_list[0]) == 1

    def test_add_new_book_twice_impossible_books_list_len_2(self, add_new_books_for_test, book_list):
        add_new_books_for_test.add_new_book(book_list[0])

        assert len(add_new_books_for_test.get_books_rating()) == 2

    def test_set_book_rating_impossible_for_book_is_not_in_list_None(self, add_new_books_for_test, book_list):
        add_new_books_for_test.set_book_rating(name=book_list[2], rating=2)

        assert add_new_books_for_test.get_books_rating().get(book_list[2]) == None

    def test_set_book_rating_impossible_less_that_1(self, add_new_books_for_test, book_list):
        add_new_books_for_test.set_book_rating(name=book_list[0], rating=-1)
        assert add_new_books_for_test.get_books_rating().get(book_list[0]) == 1

        add_new_books_for_test.set_book_rating(name=book_list[0], rating=0)
        assert add_new_books_for_test.get_books_rating().get(book_list[0]) == 1

        add_new_books_for_test.set_book_rating(name=book_list[0], rating=2)
        assert add_new_books_for_test.get_books_rating().get(book_list[0]) == 2

    def test_set_book_rating_impossible_more_that_10(self, add_new_books_for_test, book_list):
        add_new_books_for_test.set_book_rating(name=book_list[0], rating=9)
        assert add_new_books_for_test.get_books_rating().get(book_list[0]) == 9

        add_new_books_for_test.set_book_rating(name=book_list[0], rating=10)
        assert add_new_books_for_test.get_books_rating().get(book_list[0]) == 10

        add_new_books_for_test.set_book_rating(name=book_list[0], rating=11)
        assert add_new_books_for_test.get_books_rating().get(book_list[0]) == 10

    def test_get_books_with_specific_rating_2_books_more_5_and_1_book_equal_5(self, add_new_books_for_test, book_list):
        add_new_books_for_test.set_book_rating(name=book_list[0], rating=5)
        add_new_books_for_test.set_book_rating(name=book_list[1], rating=7)

        add_new_books_for_test.add_new_book(book_list[2])
        add_new_books_for_test.set_book_rating(name=book_list[2], rating=9)

        rating_more_that_5 = []
        rating_equal_5 = []
        for i in add_new_books_for_test.get_books_rating():
            name = i
            rating = add_new_books_for_test.get_books_rating().get(i)
            if rating > 5:
                rating_more_that_5.append(name)
            else:
                rating_equal_5.append(name)

        assert len(rating_more_that_5) == 2
        assert rating_equal_5[0] == book_list[0]

    def test_set_book_rating_impossible_for_book_is_not_in_list_none(self, add_new_books_for_test, book_list):
        assert add_new_books_for_test.get_books_rating().get(book_list[2]) == None

    def test_add_book_in_favorites_1_book_in_favorite(self, add_new_books_for_test, book_list):
        add_new_books_for_test.add_book_in_favorites(book_list[0])

        assert book_list[0] in add_new_books_for_test.get_list_of_favorites_books()

    def test_add_book_in_favorites_if_book_not_in_list_no_books_in_favorites(self, add_new_books_for_test, book_list):
        add_new_books_for_test.add_book_in_favorites(book_list[2])

        assert book_list[2] not in add_new_books_for_test.get_list_of_favorites_books()

    def test_delete_book_from_favorites_2_book_add_1_book_left(self, add_new_books_for_test, book_list):
        add_new_books_for_test.add_book_in_favorites(book_list[0])
        add_new_books_for_test.add_book_in_favorites(book_list[1])

        assert book_list[0] in add_new_books_for_test.get_list_of_favorites_books()
        assert len(add_new_books_for_test.get_list_of_favorites_books()) == 2

        add_new_books_for_test.delete_book_from_favorites(book_list[0])

        assert book_list[0] not in add_new_books_for_test.get_list_of_favorites_books()
        assert len(add_new_books_for_test.get_list_of_favorites_books()) != 2
