#Create a program that will take user input about dinner guests they are inviting, add names to a list, and print out invitations for each dinner guest.

#function to add names to list
def add_guests(guest: str, number: int):
    while True:
        invited=[]
        counter=0
        if counter<number:
            invited.append(guest)
            counter+=1
        else:
            break
        return invited
    
#function to print out invitations


#ask the user if they want to change a guest


#ask the user how many guests they want to invite
