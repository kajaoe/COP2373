# Set the constants for the ticket sales.
TOTAL_TICKETS = 10
MAX_TICKETS_PER_BUYER = 4

# Track the inventory of tickets.
def get_tickets(available_tickets):
    try:
        # Prompt user on how many tickets they want and inform of the limit.
        requested_tickets = int(input('Howdy! Want to buy a ticket?\n'
                                      f'We can only sell {MAX_TICKETS_PER_BUYER} tickets per person!\n'
                                      '\n'))
        # Set a limit on amount of tickets to be purchased.
        if requested_tickets > MAX_TICKETS_PER_BUYER:
            print(f'Sorry, you cannot purchase {requested_tickets} tickets.\n'
                  'Only 4 tickets can be purchased per buyer.\n')
            return 0

        # Prevent user from buying what is not available in inventory.
        elif requested_tickets > available_tickets:
            print(f'Sorry, we are in high demand! Only {available_tickets} tickets are left.\n')
            return 0

        # Prevent user from entering zero or negative amount.
        elif requested_tickets <= 0:
            print('Please enter a number greater than zero.')
            return 0

        else:
            return requested_tickets

    except ValueError:
        print('Please enter a valid whole number.\n')
        return 0

def main():
    available_tickets = TOTAL_TICKETS
    total_buyers = 0

    # Prompt the user until inventory is clear.
    while available_tickets > 0:
        print(f'There are {available_tickets} tickets available during pre-sale.')

        # Call the input function to get the purchase amount.
        purchased_tickets = get_tickets(available_tickets)

        # Tally each transaction.
        if purchased_tickets > 0:
            available_tickets -= purchased_tickets
            total_buyers += 1
            print('Thank you for your purchase!\n'
                  f'There are still {available_tickets} tickets left.\n')

    # Announce when inventory is clear.
    print('\nPre-sale has ended!')
    print(f'{total_buyers} buyers have purchased all available tickets.')

# Execute main.
if __name__ == '__main__':
    main()