#step 9 membuat direktori dengan mengimport lib os
import os

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
#soup=BeautifulSoup(res.text, 'html.parser') dicut dipindahkan ke step 10




#step 8 membuat fungsi total page yang isinya params dict
#dihapus aja print(soup.prettify())

def get_total_pages():
    params = {
        'q': 'pyhton developer',
        'l': 'new york'
    }
    res = requests.get(url, params = params, headers = headers)

# step 9 lanjutan membuat directory mkdir
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
#step 10 mengextract raw material
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

#scraping step
    soup = BeautifulSoup(res.text, 'html.parser')
    print(soup.prettify())

if __name__ == '__main__':
    get_total_pages()

#step 4 check status.code sudah selesai
#print(res.status_code)
