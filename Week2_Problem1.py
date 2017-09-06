# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:31:06 2017

@author: OMNISLO
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0

def remainingBalance (balance, monthlyPaymentRate, monthlyInterestRate, months):
    if months == 0:
        return balance
    else:
        balance = remainingBalance(balance, monthlyPaymentRate, monthlyInterestRate, months-1)
        monthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - monthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
        return balance

balanceAfterOneYear = remainingBalance(balance, monthlyPaymentRate, monthlyInterestRate, 12)

print("Remaining balance: " + str(round(balanceAfterOneYear, 2)))