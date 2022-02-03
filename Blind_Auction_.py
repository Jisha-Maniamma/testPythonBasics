from os import system

bidderInfo = []

bidderInfo1 ={}
def addBiddingInfo(name, price):
    bidderInfo_new = {}
    bidderInfo_new["name"] = name
    bidderInfo_new["price"] = price
    # bidderInfo_new = {"name": name, "price": price}
    bidderInfo.append(bidderInfo_new)
    bidderInfo1[name]=price;


print("logo............................")
continuloop = True
while continuloop:
    name = input("Enter the bidder name ")
    price = int(input("what is your bid? $"))
    addBiddingInfo(name=name, price=price)
    otherUser = input("type 'yes' if some one wants to also bid, else type 'no' ")
    continuloop = True if (otherUser == 'yes') else False


# add to dictonary

def getWinner():
    greatest = 0
    winnername = ""
    for i in range(len(bidderInfo)):
        if bidderInfo[i]["price"] > greatest:
            greatest = bidderInfo[i]["price"]
            winnername = bidderInfo[i]["name"]
    print(f"{greatest} {winnername}")


if not continuloop:
    getWinner()

print(bidderInfo)
print(bidderInfo1)

# ask if anyon else
#########if ys clear screen if no find highest bid and show

# system("clear")
