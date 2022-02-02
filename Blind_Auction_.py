
from os import system
bidderInfo=[]
def addBiddingInfo(name, price):
    bidderInfo_new={}
    bidderInfo_new["name"]=name
    bidderInfo_new["price"]=price
    bidderInfo.append(bidderInfo_new)

print("logo............................")
continuloop=True
while(continuloop):
    name=input("Enter the bidder name ")
    price=int(input("enetr the price"))
    addBiddingInfo(name=name,price=price)
    otherUser=input("type 'yes' if some one wants to also bid, else type 'no' ")
    continuloop=True if(otherUser=='yes') else False

#add to dictonary

def getWinner():
   for i in range len:
       for c in user:
          print(user[c])


if not continuloop:
    getWinner()

print(bidderInfo)



#ask if anyon else
#########if ys clear screen if no find highest bid and show

# system("clear")