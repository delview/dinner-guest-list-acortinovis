#Create a program that will take user input about dinner guests they are inviting, add names to a list, and print out invitations for each dinner guest.

#function to add names to list
def add_guests(guest: str, number: int):
    while True:
        invited=[]
        counter=0
        if counter<number: #we want to make sure that thenumber of guests is no more than he one chosen by the guest
            invited.append(guest)
            counter+=1
        else:
            break
        return invited
    
#function to print out invitations
def invitations(invited:list):
    for guest in invited:
        print(f'dear{guest}, you are invited to my birthday dinner this Sunday')
        
#ask the user if they want to change a guest


#ask the user how many guests they want to invite
