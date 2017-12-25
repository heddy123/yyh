from urllib.request import urlopen
from urllib.request import FancyURLopener

url  = "http://www.seriouseats.com/2015/02/how-to-make-chinese-hot-pot-at-home-guide.html"



def get_webpage(url):

	class AppURLopener(FancyURLopener):
	    version = "Mozilla/5.0"

	opener = AppURLopener()
	response = opener.open(url)

	data = response.read()
	text = data.decode("utf-8")
	return text

text = get_webpage(url)


with open('html_text.txt', 'w') as f:
    f.write(text)