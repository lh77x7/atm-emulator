#!/usr/bin/python3
import os
import string
import getpass
import time

#create list of users, their PINs and bank statements
#here - version of 5 users list, but ATMs connects with database and then
#users are autorizied

users = ['krzysiek', 'denis', 'tomek', 'peter', 'lukas']
pin_code = ['1111', '2222', '3333', '4444', '5555']
amount = [500, 1000, 1500, 2000, 2500]
count = 0
inner_counter = 0

#check if user exists
while True:
        user = input('\nENTER USER NAME: ')
        user = user.lower()
        if user in users:
            if user == users[0]:
                n = 0
            elif user == users[1]:
                n = 1
            elif user == users[2]:
                n = 2
            elif user == users[3]:
                n = 3
            else:
                n = 4
            break
        else:
            #first attempts == 0
            if inner_counter < 4:
                print('-----------------------')
                print('WRONG USERNAME')
                print('-----------------------')
                inner_counter = inner_counter + 1
            else:
                print('------------------')
                print('5 TIMES WRONG USERNAME')
                print('AFTER 5 SECONDS YOUR CARD WILL BE REMOVED')
                time.sleep(5)
                exit()
#check users pins - 3 attempts
while count < 3:
    print('--------------------')
    pin = str(getpass.getpass('ENTER YOUR PIN: '))
    print('--------------------')
    if pin.isdigit():
        if user == 'krzysiek':
            if pin == pin_code[0]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'denis':
            if pin == pin_code[1]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'tomek':
            if pin == pin_code[2]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'peter':
            if pin == pin_code[3]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

        if user == 'lukas':
            if pin == pin_code[4]:
                break
            else:
                count = count + 1
                print('-------------------')
                print('WRONG PIN')
                print('-------------------')
                print()

    else:
        print('----------------------')
        print('PIN CODE HAS ONLY DIGITS')
        print('----------------------')
        count = count + 1

#while user has 3 false attempts
while count == 3:
        print('----------------------')
        print('YOUR CARD IS LOCKED')
        print('3 FALSE ATTEMPTS')
        print('----------------------')
        exit()

print('-------------------')
print('WELCOME TO YOUR ACCOUNT ', str.capitalize(users[n]))
print('-------------------')

while True:
    print('-----------------------')
    options = input('SELECT OPTION:\nStatement-(S), Withdraw-(W) \n'
    'Cash-In-(C), Change PIN-(P) \nQuit-(Q) \n').lower()
    print('-----------------------')
    valid_options = ['s', 'w', 'c', 'p', 'q']
    options = options.lower()
    if options == 's':
       print('-------------------')
       print(str.capitalize(users[n]), ', MONEY STATUS: ', amount[n], 'EURO. ')
       print('-------------------')
    elif options == 'w':
      print('--------------------')
      cash_out = int(input('ENTER AMOUNT: '))
      print('--------------------')
      if cash_out%5 != 0:
          print('--------------------------')
          print('AMOUNT NEED TO BE MATCH 5 EURO NOTES')
          print('--------------------------')
      elif cash_out > amount[n]:
          print('--------------------------')
          print('YOU DON\'T HAVE ENAUGH MONEY')
          print('--------------------------')
      else:
          amount[n] = amount[n] - cash_out
          print('--------------------------')
          print('ACTUAL BALANCE IS: ', amount[n], 'EURO')
          print('--------------------------')
    elif options == 'c':
      print('--------------------')
      cash_in = int(input('ENTER AMOUNT YOU CASH IN: '))
      print('--------------------')
      print()
      if cash_in%5 != 0:
          print('--------------------')
          print('CASH IN AMOUNT MUST MATCH 5 EURO NOTES')
          print('--------------------')
      else:
          amount[n] = amount[n] + cash_in
          print('--------------------')
          print('NEW BALANCE: ', amount[n], 'EURO')
          print('--------------------')
    elif options == 'p':
      print('--------------------')
      new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
      print('--------------------')
      if new_pin.isdigit() and new_pin != pin_code[n] and len(new_pin) == 4:
          print('-----------------')
          new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
          print('-----------------')
          if new_ppin != new_pin:
              print('-------------------')
              print('PIN DOESN\'T MATCH')
              print('-------------------')
          else:
              pin_code[n] = new_pin
              print('---------------')
              print('NEW PIN CODE SAVED')
              print('---------------')
      else:
          print('----------------------')
          print('NEW PIN CODE MUST HAVE 4 DIGITS\n'
          'AND NEED TO BE DIFFERENT FROM OLD PIN CODE')
          print('----------------------')
    elif options == 'q':
        exit()
    else:
        print('------------------')
        print('OPTIONS NOT VALID')
        print('------------------')
