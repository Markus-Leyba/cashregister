#testing calling a function that is defined before the 'purchase function'.
def quantityFunction():
    try:
        quantity = int(input("Please enter quantity [enter a positive integer only, e.g 1, 3, 5]:\n"))
        if quantity <= 0:
            quantityFunction()
        
        else:
            pass
                 
    except ValueError:
        quantityFunction()
        
    quantity = quantity #attempting to make variable globally accessible. 
        

def purchase ():
     
     #LISTS
     
    customerList = ['Fred', 'Tom Brady', 'Julie Luck', 'Pope John Paul IV', 'Pikachu Nakamoto']

    memberList = ['Fred', 'Tom Brady', 'Julie Luck']

    productDict = {'bread': {3.00}, 'shampoo': {5.50}, 'conditioner': {5.60},}
    #orderHistory = {'Fred':[['bread', 4, 3.00, 12.00] ['shampoo', 3, 5:50, 16.50]], }

    #VARIABLES

    customerName = input("Please enter the name of the customer name [e.g Fred]:\n")
   
   
    productName = input("Please enter product name [enter a valid product only e.g bread, shampoo]:\n")
    if productName in productDict: #checks if productName exists in productDict, WORKS.
        pass
    else:
        input("That product does not exist. Please enter a product.:\n")
            
        
    #Quantity
    quantity = quantityFunction()
    quantity = int
        
        
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
        
    # unitPrice does not deal with exceptions
    unitPrice = float(input("We'll scan later, for now fucking type the price:\n"))
    
    # doesn't account for 5% discount
    # currently quantity is undefined. 
    total = float(unitPrice*quantity)
    
   
    # RECEIPT ELEMENTS OF PURCHASE
    # spacing and formatting need to be fixed
    
    print(f'{customerName:10} purchases {quantity:4}x {productName:>30}')
    print(f'Unit Price (AUD) {unitPrice:>30}')
    if membership == 'Y': 
            print(customerName,"gets a discount of 5%")
    elif membership == 'y':   
            print(customerName,"gets a discount of 5%")
    else:
            pass
    print(f'Total Price (AUD) {total:30}')
    customerList.append(customerName)
    print(customerList,'checking if it adds new customer,') #adds new customer
    
      
        
purchase()