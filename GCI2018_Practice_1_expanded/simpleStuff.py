'''
Created on Nov 5, 2018

@author: justin
'''

def printGCI():    
    for x in range(1,11):
        print("GCI is great")
    
def userInput():
    print("Enter your name")
    name = input()
    print("Hello {}, please to meet you!".format(name))
    print("Hello {}, please to meet you! Did you know that your name backwards is {}?".format(name, name[::-1]))
    
printGCI()
userInput()