#Create a program that will take user input about dinner guests they are inviting, add names to a list, and print out invitations for each dinner guest.

#function to add names to list
def add_guests(invited:list):
    while True:
        guest=input ("please enter the guest's name ").title().strip()
        invited.append(guest)
        return invited
            
    
#function to print out invitations
def invitations(invited:list):
    for guest in invited:
        print(f'dear {guest}, you are invited to my birthday dinner this Sunday ')

def replace(invited:list, new_guest: int,cancelled:int):
    if cancelled in invited:
        index=invited.index(cancelled)
        invited[index]=new_guest
        return invited
    else:
        print('make sure the user you want to remove is part of the list')

#ask the user how many guests they want to invite and who
number=int(input('how many guests would you like to invite? '))
guest_list=[]
counter=0
while True:
    if counter<number: #we want to make sure that thenumber of guests is no more than he one chosen by the guest
        guest_list=add_guests(guest_list)
        counter+=1
        continue
    else:
        break
print(invitations(guest_list))

while True:
    answer=input('do you want to edit your list? (y/n) ')
    if answer=='y':
        cancelled=(input(f'who is the guest you would like to replace? ')).title().strip()
        new_guest=(input('who is the guest you would like to add? ')).title().strip()
        guest_list=replace(guest_list,new_guest,cancelled)
        print (guest_list)

#ask the user if they want to change a guest