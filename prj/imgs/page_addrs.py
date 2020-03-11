import urllib.request
import pickle
from lxml import etree
    
def get_page(url):

    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    htmlx = etree.HTML(html)
	
    try:
        page_addr = htmlx.xpath('//*[@title="Older Comments"]/@href')[0]
        page_url = 'http:' + page_addr
        addrs.append(page_url)
        return get_page(page_url)
		
    except IndexError:
        with open('page_addrs.pkl','wb') as f:
            pickle.dump(addrs, f)
            f.close()

if __name__ == '__main__':
    url='http://jandan.net/ooxx'
    addrs=['http://jandan.net/ooxx']
    get_page(url)
