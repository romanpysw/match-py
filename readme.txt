Скрипт match-py-v2.py выполняет процедуру матчинга 2х одинаковых по полям .csv файлов
Также, в директории будет создано 2 .csv файла для вывода записей, которые совпали по матчингу и 
для записи не совпавших записей

Были использованы библиотеки:
Встроенная - re - для работы с регулярными выражениями
Встроенная - csv - для работы с .csv файлами
Внешняя - pytils - замена кириллицы латинницой
Внешняя - fuzzywuzzy - алгоритмы неточного сравнения текстовых строк
Внешняя - python-Levenshtein - ускорение работы fuzzywuzzy

Алгортим работы:
  Скрипт содержит 3 главных цикла:
    1) # if (НАИМЕНОВАНИЕ-ТОВАРА-1 И НАИМЕНОВАНИЕ-ТОВАРА-2 СОВПАДАЮТ БОЛЕЕ ЧЕМ НА 60%) and (ВСЕ ЦИФРЫ ИЗ НАИМЕНОВАНИЕ-ТОВАРА-1 И НАИМЕНОВАНИЕ-ТОВАРА-2 РАВНЫ)
       # if (ПРОИЗВОДЕТЕЛЬ-2 И ПРОИЗВОДИТЕЛЬ 1 СОВПАДАЮТ БОЛЕЕ ЧЕМ НА 40%)
       То записать как совпавшие

  2) # if (НАИМЕНОВАНИЕ-ТОВАРА-1 И НАИМЕНОВАНИЕ-ТОВАРА-ИЗ-СПИСКА-СОВПАВШИХ-ЗАПИСЕЙ РАВНЫ) and (ЦЕНА-ТОВАРА-1 И ЦЕНА-ТОВАРА-1-ИЗ-СПИСКА-СОВПАВШИХ-ЗАПИСЕЙ РАВНЫ)
       То пропустить, остальное - записать как не совпавшее

  3) # if (НАИМЕНОВАНИЕ-ТОВАРА-2 И НАИМЕНОВАНИЕ-ТОВАРА-ИЗ-СПИСКА-СОВПАВШИХ-ЗАПИСЕЙ РАВНЫ) and (ЦЕНА-ТОВАРА-2 И ЦЕНА-ТОВАРА-2-ИЗ-СПИСКА-СОВПАВШИХ-ЗАПИСЕЙ РАВНЫ)
       То пропустить, остальное - записать как не совпавшее

Достоверность матчинга - 93% в данном конкретном случае
НО - 6% списка совпавших ошибочны

