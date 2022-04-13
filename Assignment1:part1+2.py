''' 
 
 THIS IS A CASH REGISTER PROJECT. IT USES A MENU INTERFACE VIA THE MAIN MENU FUNCTION. 
 
 !!!PARAMETERS -
 
 - NO imports allowed except for SYS. 
 - MUST FUNCTION FROM A SINGLE FILE. 
 
 
 !!!BUGS - (wednesday 3:35pm 13/4) -
 
 - 'quantity' becomes a non-type when handling an exception or error.
 - 'membership' does not deal with more than 1 invalid input attempt (I can change it to the quantity function method, but I need to
 solve it first).
 - 'productName' displays value of incorrect product when incorrect product is entered. (this is printed in the receipt elements).
    same issue with memebership, does not deal infinitely with exceptions, so I will have to change it to a function. 
 
 
 !!!ISSUES TO BE UPDATED - (wednesday 3:35pm 13/4) -

 - 5% discount has not been adjusted to appropriate decimal places.  
 - add/update function has not been implemented. 
 - receipt elements still need to be formatted. (need to figure out column width)
 - PART 3 of assignment has not been implemented at all. 
 - 
 
'''
 
 
 
#DATA - LISTS & DICTIONARIES - GLOBAL
customerList = ['Fred', 'Tom Brady', 'Julie Luck', 'Pope John Paul IV', 'Pikachu Nakamoto']

memberList = ['Fred', 'Tom Brady', 'Julie Luck']

productDict = {'bread': 3.00, 'shampoo': 5.50, 'conditioner': 5.60,}
#orderHistory = {'Fred':[['bread', 4, 3.00, 12.00] ['shampoo', 3, 5:50, 16.50]], }

#MAIN MENU
def mainMenu ():
  print('Welcome to the RMIT retail management system.')
  print('1: Place an order')
  print('2: Add/update products and prices')
  print('3: Display existing customers')
  print('4: Display existing customers with membership')
  print('5: Display existing products')
  print('0: Exit the program')
  try: 
#MAINMENU OPTION 1 - PLACE ORDER
    selection=int(input("Choose an option by entering corresponding number (e.g press 1 for option 1)."))
    if selection==1:
        def placeOrder():

            #CUSTOMER NAME
            customerName = input("Please enter the name of the customer name [e.g Fred]:\n")
            
            #PRODUCT NAME
            productName = input("Please enter product name [enter a valid product only e.g bread, shampoo]:\n")
            if productName in productDict: #checks if productName exists in productDict, WORKS.
                pass
            else:
                input("That product does not exist. Please enter a product.:\n")
                    
            #QUANTITY
            def quantityFunction():
                try:
                    internal_quantity = int(input("Please enter quantity [enter a positive integer only, e.g 1, 3, 5]:\n"))
                    if internal_quantity <= 0:
                        quantityFunction()
                         
                    else:
                       return internal_quantity
                       
                except TypeError:
                    quantityFunction()
                    
                except ValueError:
                    quantityFunction()
            
            quantity = quantityFunction()
            print(quantity, 'this is quantity') #result as inputed
            print(type(quantity)) #int
                
            #MEMBERSHIP
            membership = input("The customer is not a member. Do they want to join? [press N if yes/press N if no]:\n")
            if membership == 'y':
                print("customer is now a member.")
                memberList.append(customerName)
                print('This is the member list',memberList) #adds member to memberList BUT doesn't show in file list
            elif membership == 'Y':
                print("customer is now a member.")
                memberList.append(customerName)
                print('This is the member list', memberList) #adds member to memberList BUT doesn't show in file list
            elif membership == 'n':
                print("membership declined.")
            elif membership == 'N':
                print("membership declined.")
            else:
                input("Invalid input. Please enter y or n (e.g y for yes).")
                
            #UNIT PRICE
            unitPrice = float(input("We'll scan later, for now fucking type the price:\n"))
            print(unitPrice)
            print(type(unitPrice))
            # unitPrice does not deal with exceptions


            #TOTAL
            total = float(unitPrice * quantity)   # doesn't account for 5% discount
            if membership == 'Y':
                endTotal = float((total/100)*95)
                
            elif membership == 'y':
                endTotal = float((total/100)*95)
            else: 
                endTotal = total
                return endTotal
            print(total, 'this is total')
            print(type(total))
            print(endTotal,'this is endTotal')
            print(type(endTotal))
            
            
            # RECEIPT ELEMENTS OF PURCHASE
            print(f'{customerName:10} purchases{quantity:4}x{productName:>15}')
            print(f'Unit Price $AUD {unitPrice}')
            if membership == 'Y': 
                    print(customerName,"gets a discount of 5%")
            elif membership == 'y':   
                    print(customerName,"gets a discount of 5%")
            else:
                    pass
            print(f'Total Price (AUD) {endTotal}')
            customerList.append(customerName)
            print(customerList,'checking if it adds new customer,') #adds new customer
    # spacing and formatting need to be fixed
            
            
        placeOrder()
    
    #MAINMENU OPTION 2 - ADD/UPDATE PRODUCTS & PRICES
    elif selection==2:
        
        def addUpdate():
            
            #step 1: message to add or update (divides here into separate steps)
            #step 2: add prices to new or updated product
            
        
         addUpdate()
    
    #MAINMENU OPTION - DISPLAY EXISTING CUSTOMERS
    elif selection==3:
        def displayCustomers():
        #FORMATTING COMPLETED.
            print('-CUSTOMER LIST-')
            for customer in customerList:
                print('{cus:20}'.format(cus=customer))
            
        
        
        displayCustomers()
    
    #MAINMENU OPTION 4 - DISPLAY EXISTING MEMBERS
    elif selection==4:
        def displayMembers():
         #FORMATTING COMPLETED.
            print('-MEMBER LIST-')
            for member in memberList:
                print ('{mem:20}'.format(mem=member))
            print(memberList)
        
        
        displayMembers ()
    
    #MAINMENU OPTION 5 - DISPLAY EXISTING PRODUCTS
    elif selection==5:
        def displayProducts():
        #FORMATTING COMPLETED
            print('-PRODUCT LIST-')
            for key, (product, price) in enumerate(productDict.items()):
                print(f'{product:15} $AUD{price}')
          
        
        displayProducts ()
        
    
    #MAINMENU OPTION 0 - EXIT
    elif selection==0:
        print('-EXITED PROGRAM. SEE YOU AGAIN-')
        exit
      
    else:
      print('Invalid choice: Enter 0-5')
      mainMenu()
      
  except ValueError:
    (print('Invalid choice: Enter 0-5')) 
    mainMenu()
       
#Starts mainMenu Function
mainMenu()


        


    