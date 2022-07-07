''' 
 
 THIS IS A CASH REGISTER PROJECT. IT USES A MENU INTERFACE VIA THE MAIN MENU FUNCTION. 
 
 !!!PARAMETERS -
 
 - NO imports allowed except for SYS. 
 - MUST FUNCTION FROM A SINGLE FILE. 
 
 
 !!!BUGS - (Thursday 8:50pm 14/4) -
 
 
 - In MAINMENU OPTION 2 > 
 
 1**** the newUpdatedProducts and newPrices input variables do not take commas. 
 It only works if it doesn't add commas. This is a bug because project parameter dictate
 that prices and items be entered as lists where elements are separated by commas. 
 
 2**** to add list of itmes, I've used a method where the user needs to enter the amount of items or prices
 that they will enter. 
 
 3*** the two functions are able to output 2 lists (addUpdateOutput, newPricesOutput). However,
 I have not been able to use these two lists to update the membersDict variable which is global. 
 
 
 - In MAINMENU OPTION 1 > 
 
 4*** I tried creating multiple orders by embedding certain parts of the placeOrder() function into
 a subPlaceOrder() function. But this did not work. How can I strucutre it so that it can do multuple orders? 
 
 5**** In regards to adding the customerName to customerList, it works. I know this because I print the value
 of memberList, so the program adds but it does not change the list on the actual code. 
 is this normal? 
 
 6*** Any hints on an easy way to create a 'reveal the most valuable customer' option would be appreciated. 
 
 
 
 
 
 !!!ISSUES TO BE UPDATED - (Thursday 8:50pm 14/4) -

 - 5% discount has not been adjusted to appropriate decimal places.  
 - receipt elements still need to be formatted. (need to figure out column width)
 - PART 3 of assignment 25% done
 
 
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
            
            #PRODUCT NAME - 
            productName = '' #Q3
            while True: #Q3
                productName = input("Please enter product name [enter a valid product only e.g bread, shampoo]:\n")
                if productName in productDict: #checks if productName exists in productDict, WORKS.
                    break #Q3
                else:
                    input("That product does not exist. Please enter a product.:\n")
                    break
                
                
            #QUANTITY
            def quantityFunction():
                try:
                    internal_quantity = int(input("Please enter quantity [enter a positive integer only, e.g 1, 3, 5]:\n"))
                    if internal_quantity <= 0:
                        return quantityFunction() #Q1
                         
                    else:
                       return internal_quantity
                       
                except TypeError:
                    return quantityFunction() #Q1
                    
                except ValueError:
                    return quantityFunction() #Q1
            
            quantity = quantityFunction()
            print(quantity, 'this is quantity') #result as inputed
            print(type(quantity)) #int
                
            #MEMBERSHIP
            membership = '' #Q2
            while True: #Q2
                membership = input("The customer is not a member. Do they want to join? [press N if yes/press N if no]:\n")
                if membership == 'y':
                    print("customer is now a member.")
                    memberList.append(customerName)
                    print('This is the member list',memberList) #adds member to memberList BUT doesn't show in file list
                    break #Q2
                elif membership == 'Y':
                    print("customer is now a member.")
                    memberList.append(customerName)
                    print('This is the member list', memberList) #adds member to memberList BUT doesn't show in file list
                    break #Q2
                elif membership == 'n':
                    print("membership declined.")
                    break #Q2
                elif membership == 'N':
                    print("membership declined.")
                    break #Q2
                else:
                    input("Invalid input. Please enter y or n (e.g y for yes).")
                
            #UNIT PRICE
            unitPrice = float(input("We'll scan later, for now type the price:\n"))
            print(unitPrice)
            print(type(unitPrice))
            # unitPrice does not deal with exceptions


            #TOTAL
            total = float(unitPrice * quantity)   
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
        
        def addUpdateFunc():
            productArray = []
            priceArray = []
            try:
                numberOfProducts = int(input('enter number of products.'))
    #THE PROBLEM SEEMS TO BE HERE. IF I ENTER number without COMMAS it works.
                newUpdateProducts = list(map(str,input('\nlist all products then press enter :').strip().split()))[:(numberOfProducts)]
                print('List of products to add or update.')
                print('With number of products to update.')
                print(newUpdateProducts)
                print(numberOfProducts)
                return numberOfProducts, newUpdateProducts
                    
               
            except TypeError:
                if numberOfProducts != int:
                    print('Quantity of products was not an integer. Start again.')
                    return addUpdateFunc()
                else: 
                    print('Invalid input. Start again.')
                    return addUpdateFunc()
                    
            except:
                print('Invalid input. Start again.')
                return addUpdateFunc()
         
        #new var 
        addUpdateOutput = addUpdateFunc() 
        print(addUpdateOutput, 'addUpdateOutput')
        
        #new var
        newOrUpdatedProducts = addUpdateOutput[1]
        print(newOrUpdatedProducts)
        
        
###########BUG1        
        def priceFunc():
            try:
                numberOfnewPrices = int(input('enter number of new prices (e.g 5).'))
######THE PROBLEM SEEMS TO BE HERE. IF I ENTER number without COMMAS it works.
## BUT PROJECT REQUIRES COMMAS.  
                newPrices = list(map(float,input('\nlist all new prices with a space and NO COMMA inbetween \n (e.g 3.00 2.50 10.80)\n make sure prices and products are in the same order. \n then press enter :').strip().split()))[:numberOfnewPrices]
                print('List of prices')
                print('with number of prices to update')
                print(newPrices)
                print(numberOfnewPrices)
                return numberOfnewPrices, newPrices
            
            except TypeError:
                
                if numberOfnewPrices != int:
                    print('Number of products to be priced - invalid input\n Please enter an integer (e.g 8).')
                    return priceFunc()
                else: 

                    for price in newPrices: 
                        print(price)
                        if price != float:
                            price = 0
                            print(price)
        
        #new variable                    
        priceFuncOutput = priceFunc() # data looks like (numberOfnewPrices, [newPrices])
        print (priceFuncOutput, 'priceFuncOutput')  
        
        #new variable 
        newPricesOutput = priceFuncOutput[1] 
        print(newPricesOutput, 'newPricesOutput')
        
        #var that updates dictionary
        tempDict = dict(zip(addUpdateOutput, newPricesOutput))
       
        print(tempDict, 'tempDict')   
        
        productDict.update(tempDict)   
        
                  
         
                
            #Finally: 
            #CODE BLOCK TO loop through dict to change blank prices to 0. 
            
        
   
    
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

