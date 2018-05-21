#!c:\Python27\python.exe
'''
programmer name: Jared Schuller
Program name: hw01.py

Program: Calculates amount student has to pay at college

'''
import os

STANDARD_COST = 14000
EXTRA_CLASS_COST = 800
REM_CLASS_COST = 30.1
FLAT_FEE = 100.01
STANDARD_CREDITS = 20

def getUserInfo():
    '''
    receives input from user
    '''
    
    lastName = raw_input("Enter your last name: ")
    firstName = raw_input("Enter your first name: ")
    credit = int(raw_input("Enter the number of credits you are taking: "))
    remClasses = int(raw_input("Enter the number of remedial courses that you are taking: "))

    return lastName, firstName, credit, remClasses

def calcUserInfo(credit, remClasses):

    '''
    calculates tuition and cost info
    '''

    extraClasses = credit - STANDARD_CREDITS
    totalTuition = (extraClasses * EXTRA_CLASS_COST) + STANDARD_COST
    totalFees = (remClasses * REM_CLASS_COST) + FLAT_FEE
    totalCost = totalTuition + totalFees

    return totalTuition, totalFees, totalCost

def outputUserInfo(lastName, firstName, totalTuition, totalFees, totalCost):

    '''
    outputs calculated info on screen
    '''

    print firstName, lastName
    print "Your tuition is: $%.2i" %(totalTuition)
    print "Your fees are: $%.2i" %(totalFees)
    print "You owe: $%.2i" %(totalCost)

def main():

    lastName, firstName, credit, remClasses = getUserInfo()
    totalTuition, totalFees, totalCost = calcUserInfo(credit, remClasses)
    outputUserInfo(lastName, firstName, totalTuition, totalFees, totalCost)
    
    os.system("pause")

if __name__ == '__main__':
    main()
    
