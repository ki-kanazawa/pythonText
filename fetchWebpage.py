import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    respose = requests.get(url)
    if respose.status_code==200:
        return respose.text
    else :
        print('アクセスできません')
        return None
    
def extract_links(html):
    soup = BeautifulSoup(html,'html.parser')
    title = soup.title.string
    links = [a['href'] for a in soup.find_all('a' , href=True)]
    return title , links

url = input('URLを入力してください：')
html_content = fetch_webpage(url)
if html_content:
    tilte , links= extract_links(html_content)
    print(f'タイトル：{tilte}')
    print(f'リンク：')
    for link in links:
        print(link)