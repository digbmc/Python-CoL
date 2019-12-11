#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# this is a comment

"""
Created on Thu Nov 14 10:11:03 2019

Notes and code from python community of learning session 1

https://automatetheboringstuff.com/chapter1/

@author: amcgrath1
"""

# This program says hello and asks for my name

print('Hello world!') # displays string 'Hello world'

print('What is your name?') # asks for user input

myName = input() # Creates a new variable called myName and assigns it to user input (string)

print ('The length of your name is: ')

print(len(myName)) # returns the length of the string myName

print('What is your age?')

myAge = input() 

print('you will be ' + str(int(myAge) + 1) + ' in a year.') 
# turns the string myAge into an integer and adds 1 to it

"""
here is another comment

"""        