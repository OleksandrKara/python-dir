"""
Короче дивись. Напиши прогу яка працює з командної стрічки.
На вхід першим аргументом отримує URL веб сторінки (ніяких дурних питань типу введіть адресу сторінки і так далі),
далі скачує цю сторінку, аналізує її і виводить список HTML тегів що зустрічаються на цій сторінці
так напроти кожного тега число що відображає скільки раз цей тег був використаний на сторінці.
Теги вважаються однаковими навіть якщо в них різні атрибути.
вивід інформації має йти на екран ( в консоль).
Також вивід має бути форматованим у вигляді таблиці (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables)
(головне щоб було читабельно зовні виглядало як таблиця). Ніякого граф інтерфейсу.
Також повинні бути тести. Як самий простий варіант - можеш написати окремо скріпт який буде тестувати функції твоєї основної програми.
Код не повинен бути монолітним, тоєсть він повинен бути розділеним на логічні блоки, функції.
Для роботи на д прогою - створюєш свій аккаунт на гітлабі і коли доробиш кожен кусок коду вигружаєш туди комітами.

Тепер план:
1.  Прога яка може просто скачувати з нету будь-яку веб сторінку і виводити її вміст в консоль.
    На даному єтапі в коді уже мають бути виділені функції (як мінімум одна, яка буде виконувати всю роботу)
    також скріпт повинен мати можливість бути імпортованим. Тут перший комміт. Подивись на коду по urllib, urllib2 або якщо це пітон 3+ то на аналогічно бубліотеку.
2.  Реалізувати пошук ХТМЛ тегів. Подивись на модуль re.
    Тут прогам має просто вивести всі ХТМЛ теги які використовуються. тоже комміт.
3. Прога повинна вміти порахувати кількість зустрічей тега. Тоже комміт.

Приблизно так. План можеш міняти як тобі зручно.
В подальшому можна буде зробити базу і павучків, які будуть лазити по нету і збирати статистику по популярності тегів, але то уже якщо буде цікаво.
"""


# For python hith then 3.0.0

import re
import urllib.request
# dictionaries

class FirstClass:
    def linkHandler(link):
        url = urllib.request.urlopen(link)
        txt = url.read()
        return txt

    def reHandler(regExp,html):
        r = re.compile(regExp)
        result = r.findall(str(html))
        return result

    def tableGenerationFunc(result):
        hash_map = {}
        for element in result:
            sub_item = element
            element = result
            counter = 0
            for item in element:
                if sub_item==item:
                    counter = counter + 1
            hash_map[sub_item] = counter
        print(hash_map)


        """ I tryed to make a string that contsins all tags and after it posible to parse each tags with function str.count()
        for element in result:
            elements = element + elements
        print(elements)
        print(result[2])
        print(str.count(elements,result[2]))
        """

page = FirstClass.linkHandler('http://vk.com')
list_of_tags = FirstClass.reHandler('(?<=</).*?(?=>)',page)
FirstClass.tableGenerationFunc(list_of_tags)



"""
#For python under then 3.0.0

import urllib2

def linkHandler(link):
    response = urllib2.urlopen(link)
    txt = response.read()
    return txt
"""