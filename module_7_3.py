class WordsFinder: # класс поиска слов в тексте из файлов

    def __init__(self, *file_names): # объект этого класса должен принимать неограниченного количество названий файлов
        self.file_names = file_names

    def get_all_words(self): # добавляет в словарь, название файла и его содержание(в нижнем регистре,
        # без знаков препинания)
        all_words = {}
        for file_name in self.file_names: # перебор файлов
            with open(file_name, encoding='utf-8') as file: # открытие файла
                words = [] # временный список для добавления слов из файла
                for line in file: # перебор строк файла
                    line = line.lower() # перевод в нижний регистр
                    punctuation_marks = [',', '.', '=', '!', '?', ';', ':'] # список знаков препинаний
                    for sign in punctuation_marks: # перебор знаков препинаний
                        line = line.replace(sign, "") # удаление знаков препинаний
                    line = line.replace(' - ', " ")  # знак тире(обособлен пробелами) заменяется пробелом
                    words.extend(line.split())  # разбивка строк на слова и добавление их в список
                    all_words[file_name] = words # почти аналогично all_words.update({file_name: words}) -
                    # добавление в словарь названия файла(ключ) и списка слов из него(значение)
        return all_words

    def find(self, word): # метод, где word - искомое слово
        result_found = {}
        for name, words in self.get_all_words().items(): # перебор списка слов(значений) в словаре
            if word.lower() in words: # если искомое слово есть в списке слов
                number = words.index(word.lower()) # позиция первого такого слова в списке слов
                result_found[name] = number + 1 # создаём словарь, ключ(название файла),
                # значение(позиция первого такого слова в списке слов этого файла)
                return result_found # если найдено выводим словарь
            else: # если не найдено искомое слово, ищем в следующем файле(ключе)
                continue
        return

    def count(self, word): # метод, где word - искомое слово
        counter = {}
        for name, words in self.get_all_words().items(): # перебор списка слов(значений) в словаре
            counter.update({name: words.count(word.lower())}) # добавление в словарь - ключ(название файла),
            # значение(количество искомого слова в списке слов этого файла)
        return counter

# Пример выполнения программы:
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего