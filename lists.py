import requests
import decider as dec
from bs4 import BeautifulSoup
import re

'''
File that holds the bulk of the cool code. used for actually scraping EBAY and returning lists of names, shipping, and prices of
three different criteria. Use requests for grabbing the html, bs4 for the scraping, and re for sifting through the data and getting
what is needed
'''

#These two functions utilize requessts and bs4 for actually getting the ebay data. They take in the item name for searching
#and the first function also takes in buy now or auction. Sold items is the same for either, and has a different url,
#so had a seperate function.
def getsoup(item, bnorauc):
    ebayUrl = "https://www.ebay.com/sch/i.html?_nkw="+item+"&_sacat=0&LH_"+bnorauc+"=1&LH_ItemCondition=3000&LH_PrefLoc=2"
    r= requests.get(ebayUrl)
    return BeautifulSoup(r.text, features="html.parser")
def getsoupsold(item):
    ebayUrl = "https://www.ebay.com/sch/i.html?_nkw="+item+"&_sacat=0&LH_Complete=1&LH_Sold=1&LH_auction=1&LH_ItemCondition=3000"
    r= requests.get(ebayUrl)
    return BeautifulSoup(r.text, features="html.parser")

#make list of name for item in buy now. Created a list for all the item titles, and returned a list
#of them minus the first one because that's usually some ebay mumbojumbo
def createnamelistbnact(item):
    listings = getsoup(item, 'BIN').find_all('div', attrs={'class': 's-item__title'})
    retlist = []
    for name in listings:
        retlist.append(name.get_text())
    return retlist[1:]

#make list of price for item in buy now. Create a list of the strings in the item price class,
#removed the commas, and then extracted the number as a float. As some prices are ranged,
#made it so retlist was given the average of whatever was found.
def createpricelistbnact(item):
    listings = getsoup(item, 'BIN').find_all('span', attrs={'class': 's-item__price'})
    retlist = []
    for price in listings:
        price = re.sub(',','',price.get_text())
        if 'to' in price:
            strli = re.findall(r"\$(\d*.\d*).*?", price)
            retlist.append((float(strli[0])+float(strli[1]))/2)
            continue
        retlist.append(float(price[1:]))
    return retlist[1:]

#make list of shippinh for item in buy now. Create a list of the strings in the item shippinh class,
#for each item, added float of shipping cost to retlist if there was one, otherwise put in 0 if free
def createshippinglistbnact(item):
    listings = getsoup(item, 'BIN').find_all('span', attrs={'class': 's-item__shipping'})
    retlist = []
    for price in listings:
        curp = re.match(r"\+\$(\d*\.\d*)", price.get_text())
        if curp:
            retlist.append(float(curp.group()[2:]))
        else:
            retlist.append(0)
    return retlist


#These are the same as the three above, but for auctions and not buy now.
def createnamelistacact(item):
    listings = getsoup(item, 'Auction').find_all('div', attrs={'class': 's-item__title'})
    retlist = []
    for name in listings:
        retlist.append(name.get_text())
    return retlist[1:]
def createpricelistacact(item):
    listings = getsoup(item, 'Auction').find_all('span', attrs={'class': 's-item__price'})
    retlist = []
    for price in listings:
        price = re.sub(',','',price.get_text())
        if 'to' in price:
            strli = re.findall(r"\$(\d*.\d*).*?", price)
            retlist.append((float(strli[0])+float(strli[1]))/2)
            continue
        retlist.append(float(price[1:]))
    return retlist[1:]
def createshippinglistacact(item):
    listings = getsoup(item, 'Auction').find_all('span', attrs={'class': 's-item__shipping'})
    retlist = []
    for price in listings:
        curp = re.match(r"\+\$(\d*\.\d*)", price.get_text())
        if curp:
            retlist.append(float(curp.group()[2:]))
        else:
            retlist.append(0)
    return retlist


#These are the same as the six above, but for sold items.
def createnamelistacsold(item):
    listings = getsoupsold(item).find_all('div', attrs={'class': 's-item__title'})
    retlist = []
    for name in listings:
        retlist.append(name.get_text())
    return retlist[1:]
def createpricelistacsold(item):
    listings = getsoupsold(item).find_all('span', attrs={'class': 's-item__price'})
    retlist = []
    for price in listings:
        price = re.sub(',','',price.get_text())
        retlist.append(dec.getavg(list(map(float, re.findall(r"\$(\d*.\d*).*?", price)))))
    return retlist[1:]
def createshippinglistacsold(item):
    listings = getsoupsold(item).find_all('span', attrs={'class': 's-item__shipping'})
    retlist = []
    for price in listings:
        curp = re.match(r"\+\$(\d*\.\d*)", price.get_text())
        if curp:
            retlist.append(float(curp.group()[2:]))
        else:
            retlist.append(0)
    return retlist




