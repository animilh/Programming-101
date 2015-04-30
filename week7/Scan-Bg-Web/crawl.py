import requests
from bs4 import BeautifulSoup


r = requests.get("http://register.start.bg")
html = r.text
soup = BeautifulSoup(html)
chrome_header = {
 "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}
links = []
upd_links = []
servers = []

for link in soup.find_all("a"):
    if link.get('href') != None and len(link.get('href')) > 0 \
        and not link.get('href').startswith('/') and link.get('href') \
            != '#top':
        links.append(link.get('href'))

for link in links:
    if link[0:12]=='link.php?id=':
        link = 'http://register.start.bg/' + link
        upd_links.append(link)
    else:
        upd_links.append(link)

f = open('upd_links.txt', 'w')

for link in upd_links:
    if link[0:7]!='http://':
        upd_links.remove(link)

for link in upd_links:
    f.write(link)
    f.write('\n')

f.close()

for link in upd_links:
    try:
        r = requests.head(link, allow_redirects=True, headers=chrome_header, timeout=8)
        servers.append(r.headers["Server"])
    except:
        pass

fs = open('servers.txt', 'w')

for name in servers:
    index = name.find('/')
    if index == -1:
        fs.write(name)
        fs.write('\n')
    else:
        fs.write(name[:index])
        fs.write('\n')

fs.close()
