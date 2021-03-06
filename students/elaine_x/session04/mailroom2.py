'''
##########################
#Python 210
#Session 04 - Mailroom Part 2
#Elaine Xu
#Feb 5,2019
###########################
'''
import sys
import datetime
import operator

def send_a_thankyou():
    '''send a thankyou note to donor'''
    # creating a list of donors - lower case
    donor_list = []
    for donor in donor_db:
        donor_list.append(donor.lower())
    #print(donor_list) #for testing
    #prompt for a full name
    while True:
        fullname = input("Enter full name of the donor (type 'list' to show all donor names): ")
        if fullname.lower() == 'list':
            for donor in donor_db:
                print(donor)
        elif fullname.lower() not in donor_list:
            print(f'{fullname} does not exist in current donor data, '
                  f'adding {fullname} to the donor data.')
            #prompt for a donation amount
            donation_amount = float(input("Enter the donation amount: "))
            donor_db[fullname] = [donation_amount, 1]
            print(f"{donation_amount} has been added to {fullname}'s donation history.")
            #print(donor_db) #for testing
            break
        elif fullname.lower() in donor_list:
            #prompt for a donation amount
            donation_amount = float(input("Enter the donation amount: "))
            donor_db[fullname][0] = donor_db[fullname][0] + donation_amount
            donor_db[fullname][1] = donor_db[fullname][1] + 1
            print(f"{donation_amount} has been added to {fullname}'s donation history.")
            #print(donor_db) #for testing
            break
    #send thankyou note
    print("Composing Thank You email:")
    print(f'Thank you {fullname} for your generous donation of {donation_amount:^10.2f}!')
    print()

def create_a_report():
    '''create a report in tabular and return to original prompt'''
    sorted_donor_db = sorted(donor_db.items(), key=operator.itemgetter(1), reverse=True)
    print("Printing report:")
    title = ('Donor Name', 'Total Given', "Num Gifts", 'Average Gift')
    print("{:<24} | {:^13} | {:^11} | {:^11}".format(*title))
    print("-"*70)
    for k, v in sorted_donor_db:
        print("{:<25} ${:>13.2f} {:>13}  ${:>12.2f}"
              .format(k, v[0], v[1],
                      v[0]/v[1]))
    print()

def sort_total_donation(number):
    '''sort donors by total historical donation amount'''
    return number[1][0]

def send_letters_to_all_donors():
    '''generate thankyou letter to all donors'''
    for key in donor_db:
        with open(key+"_"+str(datetime.date.today())+".txt", 'w') as f:
            f.write("Dear {name},\n"
                    "\n"
                    "        Thank you for your very kind donation of ${amount:10.2f}.\n"
                    "\n"
                    "        It will be put to very good use.\n"
                    "\n"
                    "                       Sincerely\n"
                    "                          -The Team".format(name=key, amount=donor_db[key][0]))
    print("Thank you letters to all donors have been generated in the local disk.\n")

def exit_program():
    '''exit program'''
    print("Exiting the program")
    sys.exit()

def main():
    '''main operation of the program'''
    choice = ''
    while True:
        choice = int(input(PROMPT))
        if choice in DIC_MENU:
            DIC_MENU[choice]()
        else:
            print("Not a valid option, try again.\n")


DIC_MENU = {1: send_a_thankyou,
            2: create_a_report,
            3: send_letters_to_all_donors,
            4: exit_program
            }

PROMPT = ('Menu\n'
          'Please choose from below options:\n'
          '1 - Send a Thank You\n'
          '2 - Create a Report\n'
          '3 - Send letters to all donors\n'
          '4 - Quit\n'
          'Enter your selection: ')

#############################################################
if __name__ == "__main__":

    donor_db = {"William Gates, III": [653772.32, 2],
                "Jeff Bezos": [877.33, 1],
                "Paul Allen": [663.23, 3],
                "Mark Zuckerberg": [1663.23, 3],
                "Bob Smith": [500.00, 1],
                }

    main()
