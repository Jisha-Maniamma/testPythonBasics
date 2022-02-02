
from os import system


print("logo............................")
name=input("Enter the bidder name ")
price=int(input("enetr the price"))
#add to dictonary
bidderInfo=[]
def addBiddingInfo(name, price):
    bidderInfo_new={}
    bidderInfo_new["name"]=name
    bidderInfo_new["price"]=price
    bidderInfo.append(bidderInfo_new)

otherUser=input("type 'yes' if some one wants to alo bid")

addBiddingInfo(name=name,price=price)

print(bidderInfo)



#ask if anyon else
#########if ys clear screen if no find highest bid and show

# system("clear")