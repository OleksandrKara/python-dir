import urllib.request

f = urllib.request.urlopen('http://vk.com')
print(f.read())
