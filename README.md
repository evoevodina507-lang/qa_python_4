# BooksCollector - Юнит-тесты

## Описание
Проект по тестированию приложения BooksCollector (Яндекс Практикум)

## Реализованные тесты

### Метод add_new_book:
- test_add_new_book_valid - добавление книг с валидными названиями (параметризованный)
- test_add_new_book_invalid_length - проверка длины названия книги (параметризованный)
- test_add_new_book_duplicate - запрет дубликатов

### Метод set_book_genre:
- test_set_book_genre_valid - установка жанра (параметризованный)
- test_set_book_genre_invalid - проверка несуществующего жанра

### Метод get_book_genre:
- test_get_book_genre - получение жанра книги (параметризованный)

### Метод get_books_genre:
- test_get_books_genre - получение всего словаря книг

### Метод get_books_with_specific_genre:
- test_get_books_with_specific_genre - фильтрация книг по жанру

### Метод get_books_for_children:
- test_get_books_for_children - получение книг без возрастного рейтинга

### Методы favorites:
- test_favorites_operations - комплексный тест работы с избранным

## Запуск тестов
pytest -v tests.py
