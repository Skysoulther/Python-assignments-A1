from Viewer1 import *
from Viewer2 import *
'''
Created on Oct 22 2016

@author: Dragos
'''

"""

A math teacher needs a program that will help students test different properties of complex numbers,
provided in the a+bi form (assume a, b integers for simplicity).

There are two UIs that can be used:
   1. menu-based UI
   2. command-based UI

More Info about the program can be found in the Viewers modules

"""
def optionMenu():
   '''
   prints the main menu for choosing an UI
   '''
   printMenuTypes()
   while True:
      try:
         option=input("Command: ")
         if option.upper()=='MENU':
            print('-'*50)
            mainMenu2()
            break
         elif option.upper()=='COMMAND':
            print('-'*50)
            mainMenu1()
            break
         elif option.upper()=='EXIT':
            print("-"*50+"\nThanks for using the app! Have a nice day!\n"+"-"*50)
            break
         else:
            raise ValueError
      except ValueError:
         print("-"*50+"\nPlease enter a valid option!\n"+"-"*50)
      input("Press any key to continue...")


def printMenuTypes():
   '''
   Prints a menu with two options
   '''
   print("\nWrite the command 'menu' if you want to use a menu-based UI and 'command' if you want to use a command-based UI")
   print("NOTE: You can use the command 'exit' to close the app if you don't want to choose any UI")

optionMenu()
