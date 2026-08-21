import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.mark.parametrize('book_name', [
    'Книга',

    'Длинное название до сорока символов',  # 37 символов

    'А'
])
def test_add_new_book_valid(collector, book_name):
    collector.add_new_book(book_name)
    assert book_name in collector.books_genre
    assert collector.books_genre[book_name] == ''

@pytest.mark.parametrize('book_name', [
    '',
    'А' * 41
])
def test_add_new_book_invalid_length(collector, book_name):
    collector.add_new_book(book_name)
    assert len(collector.books_genre) == 0

def test_add_new_book_duplicate(collector):
    collector.add_new_book('Дюна')
    collector.add_new_book('Дюна')
    assert len(collector.books_genre) == 1

@pytest.mark.parametrize('genre', [
    'Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'
])
def test_set_book_genre_valid(collector, genre):
    collector.add_new_book('Тестовая книга')
    collector.set_book_genre('Тестовая книга', genre)
    assert collector.books_genre['Тестовая книга'] == genre

def test_set_book_genre_invalid(collector):
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Романтика')
    assert collector.books_genre['Книга'] == ''

@pytest.mark.parametrize('book_name, expected_genre', [
    ('Гарри Поттер', 'Фантастика'),
    ('Сияние', 'Ужасы'),
    ('Колобок', '')
])
def test_get_book_genre(collector, book_name, expected_genre):
    collector.add_new_book(book_name)
    if expected_genre:
        collector.set_book_genre(book_name, expected_genre)
    assert collector.get_book_genre(book_name) == expected_genre

def test_get_books_genre(collector):
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Комедии')
    collector.add_new_book('Книга 2')
    expected_dict = {'Книга 1': 'Комедии', 'Книга 2': ''}
    assert collector.get_books_genre() == expected_dict

def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 2', 'Фантастика')
    collector.add_new_book('Книга 3')
    collector.set_book_genre('Книга 3', 'Ужасы')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 2']
    assert collector.get_books_with_specific_genre('Ужасы') == ['Книга 3']

def test_get_books_for_children(collector):
    collector.add_new_book('Сказка')
    collector.set_book_genre('Сказка', 'Мультфильмы')
    collector.add_new_book('Фильм ужасов')
    collector.set_book_genre('Фильм ужасов', 'Ужасы')
    collector.add_new_book('Детектив')
    collector.set_book_genre('Детектив', 'Детективы')
    collector.add_new_book('Книга без жанра')
    assert collector.get_books_for_children() == ['Сказка']

def test_favorites_operations(collector):
    collector.add_new_book('Избранная книга')
    collector.add_new_book('Еще одна книга')
    collector.add_book_in_favorites('Избранная книга')
    collector.add_book_in_favorites('Еще одна книга')
    assert collector.get_list_of_favorites_books() == ['Избранная книга', 'Еще одна книга']
    collector.add_book_in_favorites('Избранная книга')
    assert len(collector.get_list_of_favorites_books()) == 2
    collector.add_book_in_favorites('Несуществующая книга')
    assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()
    collector.delete_book_from_favorites('Избранная книга')
<<<<<<< HEAD
    assert collector.get_list_of_favorites_books() == ['Еще одна книга']
=======
    assert collector.get_list_of_favorites_books() == ['Еще одна книга']
>>>>>>> 435d972ac4fe3ddb39fd2305eb9e0dfad0f8ef98
