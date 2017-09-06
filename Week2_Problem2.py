# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 00:40:53 2017

@author: OMNISLO
"""

balance = 484
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0


def remainingBalance (balance, monthlyPayment, monthlyInterestRate, months):
    if months == 0:
        return balance
    else:
        balance = remainingBalance(balance, monthlyPayment, monthlyInterestRate, months-1)
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        return balance

monthlyPayment = 10
balanceAfterOneYear = remainingBalance(balance, monthlyPayment, monthlyInterestRate, 12)
#print (monthlyPayment, balanceAfterOneYear)
while balanceAfterOneYear > 0:
    monthlyPayment += 10
    balanceAfterOneYear = remainingBalance(balance, monthlyPayment, monthlyInterestRate, 12)
    #print (monthlyPayment, balanceAfterOneYear)

print("Lowest payment: " + str(monthlyPayment))