import time


class VideoStore:

    def __init__(self, filename):
        self.__filename = filename

    def frontOfStore(self):
         
        #display the initial choice selection menu                   
        print("Welcome to the front of the Video Store! Options are listed below: \n")
        print("Enter '1' to view a list of videos and prices \nEnter '2' to view your cart")
        print("Enter '3' to add a video to your cart\nEnter '4' to remove from cart\nEnter '5' to checkout (which will exit program after displaying totals)")

        #exception handling and input validation for choice of 'list', 'cart', 'add', 'remove', and 'checkout
        while True:
            try:
                choice = int(input("\nCHOICE: "))
                while choice>5 or choice <1:
                    choice = int(input("Please enter a number between 1 and 5 \nCHOICE: "))
                break
            except:
                print("Error: Please attempt another input as an integer")
                
        return choice
            
    def displayStoreProducts(self):
        #display the movies, type, and price, as read from the file
        MoviesinFile = open(self.__filename, 'r')
        for line in MoviesinFile:
            print(line)
        MoviesinFile.close()
        return 0

    def addProducts(self, choice):
        movie_chosen = str(' ')
        #input validation and exception handling per choice, returning movie_chosen and number
        if choice == 1:
            while True:
                    try:
                        number = int(input("How many copies of 'Bourne Identity' would you like to add? :"))
                        while number <1:
                            number = int(input("Please enter a number greater than 1 to add: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
            movie_chosen = 'The Bourne Identity'
            
        elif choice == 2:
                while True:
                    try:
                        number = int(input("How many copies of 'Harry Potter' would you like to add? :"))
                        while number <1:
                            number = int(input("Please enter a number greater than 1 to add: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
                movie_chosen = 'Harry Potter'
                
        elif choice == 3:
                while True:
                    try:
                        number = int(input("How many copies of 'The Holy Grail' would you like to add? :"))
                        while number <1:
                            number = int(input("Please enter a number greater than 1 to add: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
                movie_chosen = 'The Holy Grail'
                
        elif choice == 4:
                while True:
                    try:
                        number = int(input("How many copies of 'Arrival' would you like to add? :"))
                        while number <1:
                            number = int(input("Please enter a number greater than 1 to add: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
                movie_chosen = 'Arrival'
                
        elif choice == 5:
                while True:
                    try:
                        number = int(input("How many copies of 'Hidden Figures' would you like to add? :"))
                        while number <1:
                            number = int(input("Please enter a number greater than 1 to add: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
                movie_chosen = 'Hidden Figures'
                
        print("Adding copies of '"+ movie_chosen+"' to cart. . .")
        #pause screen for viewer accessibility
        time.sleep(2)
        return number, movie_chosen

    def viewCart(self, numMovies1, numMovies2, numMovies3, numMovies4, numMovies5):
        #print the numbers associated with the number of copies per movie
        print("The Bourne Identity: ", numMovies1)
        print("Harry Potter:        ", numMovies2)
        print("The Holy Grail:      ", numMovies3)
        print("Arrival:             ", numMovies4)
        print("Hidden Figures:      ", numMovies5)
        return 0
    
    def removeProducts(self, remove_number, cart_num):
        print("Removing products from cart . . .")
        #pause screen for viewer accessibility
        time.sleep(2)
        #return value of the previous num in cart minus the number being removed
        return int(cart_num - remove_number)

    def selfCheckout(self, numMovies1 = 9.99, numMovies2 = 15.99, numMovies3 = 4.75, numMovies4 = 24.99, numMovies5 = 29.98):
        totalMovies1 = numMovies1 
        totalMovies2 = numMovies2
        totalMovies3 = numMovies3
        totalMovies4 = numMovies4
        totalMovies5 = numMovies5
        total = totalMovies1 + totalMovies2 + totalMovies3 + totalMovies4 + totalMovies5
        #format the print functions per movie, and total
        print("The Bourne Identity: ", "$ %.2f" % totalMovies1)
        print("Harry Potter       : ", "$ %.2f" % totalMovies2)
        print("The Holy Grail     : ", "$ %.2f" % totalMovies3)
        print("Arrival            : ", "$ %.2f" % totalMovies4)
        print("Hidden Figures     : ", "$ %.2f" % totalMovies5)
        print("----------------------------------------------")
        print("Total(Tax Included): ", "$%.2f"  % total)
        return 0

    def movieOptions(self, num):
        #define each movie option, returning string of movie titles
        if num == 1:
            return("The Bourne Identity")
        elif num ==2:
            return("Harry Potter")
        elif num == 3:
            return("The Holy Grail")
        elif num == 4:
            return("Arrival")
        elif num == 5:
            return("Hidden Figures")
        
    

def main():

    ProductsFile = open("products.csv", 'r')
    
    ProductsList = []
    aVideoStore = VideoStore("products.csv")

    #load the data into a list
    for line in ProductsFile:
        stringList = []
        stringLine = str(line)
        stringLine.rstrip()
        stringList = stringLine.split(",")
        ProductsList.append(stringList[0])
        ProductsList.append(stringList[1])

    #initialize a dictionary of each movie title, with corresponding amounts of each movie assigned (currently 0 for all)
    ProductsDictionary = {"The Bourne Identity" : 0, "Harry Potter" : 0, "The Holy Grail" : 0, "Arrival" : 0, "Hidden Figures" : 0}
    ProductsFile.close()

    
    fchoice = aVideoStore.frontOfStore()

    #loop to infinitely come back to base screen, until break statement within checkout
    while fchoice >=1 or fchoice <=5:
        
        if fchoice == 1:
            print("Displaying store options. . . \n-----------------------------------\n")
            print("Listed as 'Movie', '(type)', 'price (USD)'\n")
            aVideoStore.displayStoreProducts()
            print("Returning to main menu in 6 seconds. . .")
            time.sleep(6)
            fchoice = aVideoStore.frontOfStore()
        elif fchoice == 2:
            print("Displaying your cart. . . \n---------------------------------\n")
            aVideoStore.viewCart(ProductsDictionary["The Bourne Identity"],ProductsDictionary["Harry Potter"],ProductsDictionary["The Holy Grail"],ProductsDictionary["Arrival"],ProductsDictionary["Hidden Figures"])
            print("Returning to main menu in 10 seconds. . .")
            time.sleep(10)
            fchoice = aVideoStore.frontOfStore()
        elif fchoice == 3:
            print("Enter '1' for ", ProductsList[0], "for $"+ProductsList[1])
            print("Enter '2' for ", ProductsList[2], "for $"+ProductsList[3])
            print("Enter '3' for ", ProductsList[4], "for $"+ProductsList[5])
            print("Enter '4' for ", ProductsList[6], "for $"+ProductsList[7])
            print("Enter '5' for ", ProductsList[8], "for $"+ProductsList[9])
            while True:
                    try:
                        choice = int(input("Which product would you like to add to your cart? :"))
                        while choice <1 or choice >5:
                            choice = int(input("Please enter a number between 1 and 5: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
            mov_num_added, mov_choice = aVideoStore.addProducts(choice)
            ProductsDictionary[mov_choice] = mov_num_added
            fchoice = aVideoStore.frontOfStore()
        elif fchoice == 4:
            print("Displaying items currently in cart")
            aVideoStore.viewCart(ProductsDictionary["The Bourne Identity"],ProductsDictionary["Harry Potter"],ProductsDictionary["The Holy Grail"],ProductsDictionary["Arrival"],ProductsDictionary["Hidden Figures"])
            while True:
                    try:
                        remove_choice = int(input("Which movie are you wanting to remove? (Numbers 1 -5): "))
                        while remove_choice <1 or remove_choice >5:
                            remove_choice = int(input("Please enter a number between 1 and 5: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
            movie_choice = aVideoStore.movieOptions(remove_choice)
            while True:
                    try:
                        remove_num = int(input("How many copies would you like to remove?: "))
                        while(remove_num > ProductsDictionary[movie_choice]):
                            remove_num = int(input("Please enter a number less than or equal to the number in cart: "))
                        break
                    except:
                        print("Error: Please attempt another input as an integer \n")
            ProductsDictionary[movie_choice] = aVideoStore.removeProducts(remove_num, ProductsDictionary[movie_choice])
            fchoice = aVideoStore.frontOfStore()
        elif fchoice == 5:
            print("Here's your taxed total, based off your purchases made today")
            fchoice = aVideoStore.selfCheckout(ProductsDictionary["The Bourne Identity"] * 10.69,ProductsDictionary["Harry Potter"] * 17.11,ProductsDictionary["The Holy Grail"] * 5.08,ProductsDictionary["Arrival"] * 26.74,ProductsDictionary["Hidden Figures"] * 32.10)
            return 0
        
        
main()
