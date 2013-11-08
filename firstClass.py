# For python hith than 3.0.0
import re
import urllib.request
from prettytable import PrettyTable

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
        t = PrettyTable(['Tag name', 'Count of tag'])
        for tag, count in hash_map.items():
               t.add_row([tag, count])
        print(t)

page = FirstClass.linkHandler('http://vk.com')
list_of_tags = FirstClass.reHandler('(?<=</).*?(?=>)',page)
FirstClass.tableGenerationFunc(list_of_tags)



"""
#For python under than 3.0.0

import urllib2

def linkHandler(link):
    response = urllib2.urlopen(link)
    txt = response.read()
    return txt
"""