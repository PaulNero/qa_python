import pytest
from main import BooksCollector


@pytest.fixture
def add_new_books_for_test():
    collector = BooksCollector()
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    return collector

@pytest.fixture
def init_empty_BookColletor():
    return BooksCollector()

@pytest.fixture
def book_list():
    zombie = 'Гордость и предубеждение и зомби'
    cat = 'Что делать, если ваш кот хочет вас убить'
    wrong = 'Гордости и предубеждение и зомби'
    return [zombie, cat, wrong]