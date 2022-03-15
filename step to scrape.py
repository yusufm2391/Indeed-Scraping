
#step 2 import library
import requests
from bs4 import BeautifulSoup

#step 1 create new variable
url = 'https://id.indeed.com/jobs'

#step 5 create variable params
params = {
    'q':'pyhton developer',
    'l':'new york'
}
#step 7 membuat variable baru untuk user agent
headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}

#step 3 create variable res (mean "requests)
#step 6 masukan parameter ke variabel res
res = requests.get(url, params = params, headers = headers)

#step 7 menggunakan beautifulsoup
soup=BeautifulSoup(res.text, 'html.parser')

print(soup.prettify())

#step 4 check status.code sudah selesai
#print(res.status_code)
