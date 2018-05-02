import bs4, requests, pyperclip

def getAmazonPrice(url):
    res= requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elems=soup.select('#priceblock_ourprice')
    return elems[0].text.strip()

def productname(url):
    res= requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    elems=soup.select('#productTitle')
    return elems[0].text.strip()
   

url= pyperclip.paste()
price = getAmazonPrice(url)
name= productname(url)
print("The price of {} is {}" .format(name ,price))
