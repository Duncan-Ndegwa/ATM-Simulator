




'''
        OBJECTIVES
Should be able to:
        1. Check their balance
        2. Deposit money -After deposit update balance and show
        3. Withdraw money - only if they have enough balance
        4. Exit the system


- Users start with initial of $1000 
- Show a constant menu that presents ppl with options on whether to deposit,check balance, withdraw or exit 
  

            BONUS OBJECTIVES
1. Put a PIN system where user has to enter their PIN before access
2. Add a feature to keep track of all transactions [Deposits and Withdrawals] and let users view transaction history
    

'''

import time

# The initial balance that the user starts with.
balance = 1000

# Creating the transaction file which will be used to check transaction history
file = open('transactions.txt', 'w')

# Function for the variety of services the ATM handles.
def choices():
    time.sleep(1)
    print()
    print("Welcome to the ATM!")
    print()
    print('1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Transaction History')
    print('5. Exit')
    print()

# Function to help users deposit money into their accounts. 
def deposits():
      try:
        global balance
        deposit = float(input('Please enster the amount to be deposited: '))
        print()
        if deposit < 0:
               print('The number to be entered must be a positive number!')
               deposits()
        else:
            print ("Confirming.")
            time.sleep(1)
            print('Confirmed.') 
            print(f'Successfully deposited ${deposit}.')
            print()
            balance = balance + deposit
            print(f"Your balance is now ${balance}.")
            print()
            file = open("transactions.txt", "a")
            file.write(f"${deposit} successfuly deposited.\n")
            file.close()
            choices()
      except ValueError:
            print()
            print('Kindly enter numbers [numerical values] only.')
            print()
            choices()
     

      
# Function to help users withdraw money from their accounts 
def withdraws():
       try:
            global balance
            withdraw = float(input('Please enter the amount you would like to withdraw: '))
        
            if withdraw > balance:
                print()
                print('You have insufficient balance.')
                choices()
            elif withdraw < 0:
                print("The number to be entered must be a positive number!")
            else:
                balance = balance - withdraw
                print()
                print('Confirming.')
                time.sleep(1)
                print("Confirmed.") 
                print(f"Your new balance: ${balance}")
                print()
                file = open("transactions.txt", "a")
                file.write(f"${withdraw} successfuly withdrawn.\n")
                file.close()
                choices()
       except ValueError:
            print()
            print('Kindly enter numbers [numerical values] only.')
            print()
            choices()



# Function run when used chooses option '1' which will show them how much money they have in their accounts. 
def check_balance():
    global balance
    print()
    print('Checking.')
    time.sleep(1)
    print(f"Your balance is: ${balance}")
    print()
    choices()


# Function that would run when user chooses option '4' which will show them the services they used and the amount specified in each service.
def transaction_history():
    print()
    myfile = open("transactions.txt","r")
    contents = myfile.read()
    print(contents)
    choices()
  

# Function that helps the PIN run so that only authorised people can access the account.

def pin():
  
  # Your assigned pin and number of attempts.
  pin = '1234'
  attempts = 3
  
   
  while attempts > 0:
         user_pin = input("Please enter your PIN (or press 'q' to exit): ")
         if user_pin == pin:
            print('PIN Confirmed.')
            time.sleep(1)
            atm()
         elif user_pin == 'q':
              break
         else: 
            attempts -= 1
            print()
            print(f'Incorrect PIN! Please try again. You have {attempts} attempts left.')
            print()
  else:
         print("You have exceeded the number of attempts.")  
     


  # The main function of the progect designed for user interactions [how the ATM and the user interact].
def atm():
 
  print()
  print("Welcome to the ATM!")

  print()
     
 # The various services the ATM has to offer.
  print('1. Check Balance')
  print('2. Deposit')
  print('3. Withdraw')
  print('4. Transaction History')
  print('5. Exit')

    # The actions that will take place as a result of the choices that the user will pick.
  while True:

       
      choice = input("Please choose an option:")
    
      if choice == '5':
            print()
            print('Exiting.')
            time.sleep(1)
            print("Thank you for your service.")
            print()
            break
      elif choice not in (['1', '2', '3', '4', '5']):
            print()
            print('Invalid choice! Please try again.')
            choices()
# Calling the deposit function
      elif choice == '2':
           deposits()
# Calling the withdraws function
      elif choice == '3':
          withdraws()
# Calling the check_balance function
      elif choice == '1':
           check_balance()
# Calling the transaction_history function
      elif choice == '4':
            transaction_history()
             


# Calling the function.
pin()
    
