# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 00:15:26 2017

@author: OMNISLO
"""
monthlyInterestRate = annualInterestRate/12.0
lowerBound = balance/12
upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0

def remainingBalance (balance, monthlyPayment, monthlyInterestRate, months):
    if months == 0:
        return balance
    else:
        balance = remainingBalance(balance, monthlyPayment, monthlyInterestRate, months-1)
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        return balance
    
monthlyPayment = lowerBound
balanceAfterOneYear = remainingBalance(balance, monthlyPayment, monthlyInterestRate, 12)
while abs(0 - balanceAfterOneYear) > 0.001:
    if balanceAfterOneYear > 0:
        lowerBound = monthlyPayment
        monthlyPayment = (monthlyPayment + upperBound) / 2
        balanceAfterOneYear = remainingBalance(balance, monthlyPayment, monthlyInterestRate, 12)
    if balanceAfterOneYear < 0:
        upperBound = monthlyPayment
        monthlyPayment = (monthlyPayment + lowerBound) / 2
        balanceAfterOneYear = remainingBalance(balance, monthlyPayment, monthlyInterestRate, 12)
        
print("Lowest payment: " + str(round(monthlyPayment, 2)))