import lists

'''
This file holds all the seperate calculations for finding profitability, as well as getavg
'''

#simple average calculation
def getavg(list):
    if len(list) == 0:
        return 0
    return round(sum(list)/len(list), 2)

#returns string stating maximum price possible to buy ITEM and still make profit
def needforprofit(item):
    item = item.replace(' ', '_')
    return 'possible buy if less than: '+ str(round((getavg(lists.createpricelistacsold(item)))*.86 - getavg(lists.createshippinglistacsold(item)),2))+'\n(Items sold at a price range may scew this upwards)'

#simple calculation giving % of profit given sell price and buy price. Not currently used, but easy to have
def getprofper(buyprice, sellprice):
    return sellprice/buyprice

#these all adjusted for shipping and ebay taking about .14 of earnings. Somewhat simple equations to find needed sell/buyprice for percent or dollars desired, given counterpart.
def finddesiredprofper(buyprice, shipprice, perdes):
    return round(1.163*perdes*(buyprice+shipprice),2)

def finddesiredprofdol(buyprice, shipprice, doldes):
    return round(1.163*(buyprice+shipprice+doldes),2)
    
def buypricedesiredprofper(sellprice, shipprice, perdes):
    return round((sellprice*1000)/(1163*perdes)-shipprice, 2)

def buypricedesiredprofdol(sellprice, shipprice, doldes):
    return round(.86*sellprice-shipprice-doldes, 2)
