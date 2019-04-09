from urllib import request

url = "106.14.116.1"

data = request.urlopen(url)
html = data.read()
print(html)
file = open("106.html", 'w')
file.close()
