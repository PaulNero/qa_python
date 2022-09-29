# qa_python
## Финальный проект 2 спринта "Тестирование веб-приложений на Python"

### В проекте используется несколько фикстур вот их описание:

def add_new_books_for_test(): 
> Инициализирует класс и создаёт несколько книг для тестов.

def init_empty_BookColletor():
> Инициализирует пустой класс.

def book_list(): 
> Содержит список книг используемых в тесте для сокращения количества копипасты.

### Описание разработанных тестов: 

def test_add_new_book_add_two_books(self):
> Пример теста от Яндекс.Практикума

def test_add_new_book_with_right_name_and_rating_1(self, init_empty_BookColletor, book_list):
> Тест создаёт новую книгу и проверяет её название и назначенный по-умолчанию рейтинг.

def test_add_new_book_twice_impossible_books_list_len_2(self, add_new_books_for_test, book_list):
> Тест создаёт две книги и проверяет, что нельзя создать ещё одну книгу с таким же названием.\
    По окончанию теста, должно остаться 2 элемента.

def test_set_book_rating_impossible_for_book_is_not_in_list_None(self, add_new_books_for_test, book_list):
> Тест создаёт две книги и проверяет, что если в названии книги может возникнуть ошибка. \
    Книги не будет в списке и ей нельзя изменить значение рейтинга.

def test_set_book_rating_impossible_less_that_1(self, add_new_books_for_test, book_list):
> Тест проверяет, что книге нельзя назначить значения рейтинга равные 0 и отрицательным значениям.\
    Но книге можно назначить рейтинг больше значения по умолчанию.

def test_set_book_rating_impossible_more_that_10(self, add_new_books_for_test, book_list):
> Тест проверяет, что книге можно назначить значения рейтинга равные 9 и 10.\
    Но книге нельзя назначить рейтинг больше 10.

def test_get_books_with_specific_rating_2_books_more_5_and_1_book_equal_5(self, add_new_books_for_test, book_list):
> Тест проверяет фильтрацию по рейстингу, для этого созданы три книги со значениями рейтинга 5, 7 и 9.\
    Первая часть теста выводит список из двух книг со значением рейтинга больше 5.\
    Вторая часть теста выводит книгу с рейтингом равным 5.

def test_set_book_rating_impossible_for_book_is_not_in_list_none(self, add_new_books_for_test, book_list):
> Тест проверяет, что нельзя назначить рейтинг книге, которой нет в списке добавленных книг.

def test_add_book_in_favorites_1_book_in_favorite(self, add_new_books_for_test, book_list):
> Тест проверяет, что книгу можно добавить в избранные.

def test_add_book_in_favorites_if_book_not_in_list_no_books_in_favorites(self, add_new_books_for_test, book_list):
> Тест проверяет, что в избранные нельзя добавить книгу, которой нет в списке добавленных книг.

def test_delete_book_from_favorites_2_book_add_1_book_left(self, add_new_books_for_test, book_list):
> Тест проверяет удаление книги из избранного путём добавления в избранное двух книг 
    с промежуточным контролем состояния списка избранных.\
    Затем удаляет одну из книг и проверяет, что размер списка отличается от промежуточного контроля.