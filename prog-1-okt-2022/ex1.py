wallet = [0, 0, 3, 3, 2, 1, 6, 1] #1 EUcent, 2 cent, 5 cent, 10 cent, 20 cent, 50 cent, 1eu, 2eu

def findBiggestCoin(amount):
    """
    function goes through the wallet and determines what the highest amount of coin is that can be used to reduce the amount

    returns: index of wallet which coin is the biggest coin that can be used
    """
    wallettest = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
    for i in range(6):
        if amount < wallettest[i]:
            return i
    return 7

def walletdisplay(wallettest, array):
    """
    prints the amount of coins that exist for every sort of coin that is in the wallet
    """
    for i in range(len(array)):
        print("of a "+str(wallettest[i])+" coin we have "+str(array[i])+" left.")

def walletsum(wallet):
    """
    returns the value of money that is in the wallet
    """
    wallettest = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
    sum = 0
    for i in range(len(wallet)):
        sum += (wallet[i])*(wallettest[i])
    return sum


#the below function doesn't work as intended and is therefore defunct
"""
def coins(wallet, amount):
    if walletsum(wallet) < amount:
        raise Exception("the amount cannot be paid")
    wallettest = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
    emptywallet = [0, 0, 0, 0, 0, 0, 0, 0]
    while amount > 0:
        print("remaining amount to pay: "+str(amount))
        print("current wallet:")
        walletdisplay(wallettest, wallet)
        deductionIndex = findBiggestCoin(amount)
        print("deduction index: "+str(deductionIndex))
        if wallet[deductionIndex] > 0:
            amount -= wallettest[deductionIndex]
            emptywallet[deductionIndex] += 1
            wallet[deductionIndex] -= 1
        else:
            print("not sufficient adequate coins")
            j = deductionIndex - 1
            foundCoin = False
            while(j > -1 and foundCoin == False):
                if wallet[j] > 0:
                    amount -= wallettest[j]
                    emptywallet[j] += 1
                    wallet[j] -= 1
                    foundCoin = True
                j -= 1
    return emptywallet, amount

"""
#the right function sort of
def walletfunc(amount):
	wallet = [0, 0, 3, 3, 2, 1, 6, 1]
	walletlib = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
	cycler = 7
	walletused = [0, 0, 0, 0, 0, 0, 0, 0]

	if walletsum(wallet) < amount:
		raise Exception("the amount cannot be paid")
	while amount > 0:
		while wallet[cycler] > 0 and amount > 0:
			print(amount)
			walletused[cycler] += 1
			amount -= walletlib[cycler]
			wallet[cycler] -= 1
		cycler -= 1
	leftovermoney = -1*round(amount, 2)
	return walletused, leftovermoney

print(walletfunc(19.99))



#print(coins(wallet, 9.4))


