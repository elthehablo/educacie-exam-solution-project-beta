import numpy as np
import matplotlib.pyplot as plt



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

def coins(wallet, amount):
    """
    function that determines what coins need to be used from wallet wallet to pay for the amount that is needed
    returns: two things are returned: the indexes in an array of coins that need to be used and a negative amount that displays the change you get back
    """

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


print(coins(wallet, 9.4))


