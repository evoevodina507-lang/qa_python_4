import pytest
from main import BooksCollector




@pytest.mark.parametrize('book_name', [
    'Книга',
    'Длинное название до сорока символов',  # 37 символов
    'А' * 40,  # 40 символов (граница)
    'А' * 1,   # 1 символ (граница)
])
def test_add_new_book_valid(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert book_name in collector.books_genre
    assert collector.books_genre[book_name] == ''


@pytest.mark.parametrize('book_name', [
    '',          # пустая строка
    'А' * 41,    # 41 символ (больше допустимого)
])
def test_add_new_book_invalid_length(book_name):
    collector = BooksCollector()
    collector.add_new_book(book_name)
    assert len(collector.books_genre) == 0


def test_add_new_book_duplicate():
    collector = BooksCollector()
    collector.add_new_book('Дюна')
    collector.add_new_book('Дюна')
    assert len(collector.books_genre) == 1




@pytest.mark.parametrize('genre', [
    'Фантастика', 
    'Ужасы', 
    'Детективы', 
    'Мультфильмы', 
    'Комедии'
])
def test_set_book_genre_valid(genre):
    collector = BooksCollector()
    collector.add_new_book('Тестовая книга')
    collector.set_book_genre('Тестовая книга', genre)
    assert collector.books_genre['Тестовая книга'] == genre


def test_set_book_genre_invalid():
    collector = BooksCollector()
    collector.add_new_book('Книга')
    collector.set_book_genre('Книга', 'Романтика')
    assert collector.books_genre['Книга'] == ''




def test_get_book_genre_with_genre():
    """Тест: получение жанра для книги с установленным жанром"""
    collector = BooksCollector()
    book_name = 'Гарри Поттер'
    expected_genre = 'Фантастика'
    
    collector.add_new_book(book_name)
    collector.set_book_genre(book_name, expected_genre)
    
    assert collector.get_book_genre(book_name) == expected_genre


def test_get_book_genre_without_genre():
    """Тест: получение жанра для книги без жанра"""
    collector = BooksCollector()
    book_name = 'Колобок'
    
    collector.add_new_book(book_name)
    
    assert collector.get_book_genre(book_name) == ''




def test_get_books_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Комедии')
    collector.add_new_book('Книга 2')
    
    expected_dict = {'Книга 1': 'Комедии', 'Книга 2': ''}
    assert collector.get_books_genre() == expected_dict




def test_get_books_with_specific_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 2', 'Фантастика')
    collector.add_new_book('Книга 3')
    collector.set_book_genre('Книга 3', 'Ужасы')
    
    assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1', 'Книга 2']


def test_get_books_with_specific_genre_empty():
    """Тест: запрос жанра, которого нет в книгах"""
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Фантастика')
    
    assert collector.get_books_with_specific_genre('Комедии') == []




def test_get_books_for_children_with_children_books():
    """Тест: получение книг для детей, когда есть подходящие книги"""
    collector = BooksCollector()
    collector.add_new_book('Сказка')
    collector.set_book_genre('Сказка', 'Мультфильмы')
    collector.add_new_book('Смешарики')
    collector.set_book_genre('Смешарики', 'Мультфильмы')
    
    result = collector.get_books_for_children()
    
    assert result == ['Сказка', 'Смешарики']


def test_get_books_for_children_no_children_books():
    """Тест: получение книг для детей, когда нет подходящих книг"""
    collector = BooksCollector()
    collector.add_new_book('Фильм ужасов')
    collector.set_book_genre('Фильм ужасов', 'Ужасы')
    collector.add_new_book('Детектив')
    collector.set_book_genre('Детектив', 'Детективы')
    
    result = collector.get_books_for_children()
    
    assert result == []


def test_get_books_for_children_mixed_genres():
    """Тест: получение книг для детей, когда есть и подходящие, и неподходящие книги"""
    collector = BooksCollector()
    collector.add_new_book('Сказка')
    collector.set_book_genre('Сказка', 'Мультфильмы')
    collector.add_new_book('Фильм ужасов')
    collector.set_book_genre('Фильм ужасов', 'Ужасы')
    collector.add_new_book('Детектив')
    collector.set_book_genre('Детектив', 'Детективы')
    collector.add_new_book('Книга без жанра')
    
    result = collector.get_books_for_children()
    
    assert result == ['Сказка']


def test_get_books_for_children_empty_library():
    """Тест: получение книг для детей из пустой библиотеки"""
    collector = BooksCollector()
    
    result = collector.get_books_for_children()
    
    assert result == []




def test_add_book_to_favorites():
    """Тест: добавление книги в избранное"""
    collector = BooksCollector()
    collector.add_new_book('Избранная книга')
    
    collector.add_book_in_favorites('Избранная книга')
    
    assert collector.get_list_of_favorites_books() == ['Избранная книга']


def test_add_duplicate_book_to_favorites():
    """Тест: повторное добавление уже избранной книги не создает дубли"""
    collector = BooksCollector()
    collector.add_new_book('Избранная книга')
    collector.add_book_in_favorites('Избранная книга')
    
    collector.add_book_in_favorites('Избранная книга')
    
    assert len(collector.get_list_of_favorites_books()) == 1


def test_add_nonexistent_book_to_favorites():
    """Тест: добавление несуществующей книги в избранное игнорируется"""
    collector = BooksCollector()
    collector.add_new_book('Существующая книга')
    collector.add_book_in_favorites('Существующая книга')
    
    collector.add_book_in_favorites('Несуществующая книга')
    
    assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites():
    """Тест: удаление книги из избранного"""
    collector = BooksCollector()
    collector.add_new_book('Избранная книга')
    collector.add_new_book('Еще одна книга')
    collector.add_book_in_favorites('Избранная книга')
    collector.add_book_in_favorites('Еще одна книга')
    
    collector.delete_book_from_favorites('Избранная книга')
    
    assert collector.get_list_of_favorites_books() == ['Еще одна книга']


def test_delete_nonexistent_book_from_favorites():
    """Тест: удаление несуществующей книги из избранного не вызывает ошибку"""
    collector = BooksCollector()
    collector.add_new_book('Избранная книга')
    collector.add_book_in_favorites('Избранная книга')
    
    collector.delete_book_from_favorites('Несуществующая книга')
    
    assert collector.get_list_of_favorites_books() == ['Избранная книга']


def test_delete_last_book_from_favorites():
    """Тест: удаление последней книги из избранного"""
    collector = BooksCollector()
    collector.add_new_book('Единственная книга')
    collector.add_book_in_favorites('Единственная книга')
    
    collector.delete_book_from_favorites('Единственная книга')
    
    assert collector.get_list_of_favorites_books() == []


def test_get_favorites_empty():
    """Тест: получение списка избранного, когда он пуст"""
    collector = BooksCollector()
    
    result = collector.get_list_of_favorites_books()
    
    assert result == []