#Create a program that will take user input about dinner guests they are inviting, add names to a list, and print out invitations for each dinner guest.

#function to add names to the guest list
def add_guests(invited:list):
    while True:
        guest=input ("please enter the guest's name ").title().strip()
        invited.append(guest)
        return invited
            
#function to print out invitations
def invitations(invited:list):
    for guest in invited:
        print(f'dear {guest}, you are invited to my birthday dinner this Sunday ')

#function to replace a guest
def replace(invited:list, new_guest: int,cancelled:int):
        index=invited.index(cancelled) #I want to find which position the guest to replace is in
        invited[index]=new_guest #replace the guest with the new one
        return invited

#ask the user how many guests they want to invite
number=int(input('how many guests would you like to invite? '))
guest_list=[]
counter=0
while True:
    if counter<number: #we want to make sure that the number of guests is no more than the one chosen by the guest
        guest_list=add_guests(guest_list) #call the function to add guests to the list
        counter+=1
        continue
    else:
        break
print('')
print("here's your first guest list: ")
invitations(guest_list)
counter_edit=1 #this counter allow the user to see which version/number of their list  they are looking at
#ask the user if they want to change a guest
while True:
    print('')
    answer=input('do you want to edit your list? (y/n) ')
    if answer=='y':
        cancelled=(input(f'who is the guest you would like to replace? ')).title().strip()
        if cancelled in guest_list: #we want to make sure the guest is part of the list
            new_guest=(input('who is the guest you would like to add? ')).title().strip()
            guest_list=replace(guest_list,new_guest,cancelled)
            counter_edit+=1 #everytime you edit the list, this counter it's gonna increase and let you know the number of the list
            print('')
            print(f'here is your {counter_edit} list: ') 
            invitations(guest_list) #print the new inivitations
        else:
            print('make sure the guest you want to remove is part of the list')
            pass
    else:
        print('goodbye! ')
        break

