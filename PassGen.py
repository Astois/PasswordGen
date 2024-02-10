def main():
    import random
    while True:
        PassOO = input("Do you want to generate a pass? (yes/no): ")
        if  PassOO.lower() == "yes":

            with open("char.txt", "r") as file: #opens the text file in read mode
                CharList = list(file.read()) #reads the text file and turns it into a list
            
            CharNum = 16  #sets the number of characters for the password
            CharSelect = random.sample(CharList, CharNum)  #selects randomly from the list without replacement

            random_string = "".join(CharSelect) # joins the random selected char into a string
            print("Your New Pass is...", random_string)
        elif PassOO.lower() == "no":
            break
main()        