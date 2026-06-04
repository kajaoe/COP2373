# Set the constants for the ticket sales.
TOTAL_TICKETS = 20
MAX_TICKETS_PER_BUYER = 4

# Track the inventory of tickets.
def get_tickets(remaining_tickets):
    try:
        # Prompt user on how many tickets they want and inform of the limit.
        requested_tickets = int(input('How many tickets would you like to purchase?\n'
                                      f'Maximum of {MAX_TICKETS_PER_BUYER} tickets per person.\n'
                                      '\n'))
        # Set a limit on amount of tickets to be purchased.
        if requested_tickets > MAX_TICKETS_PER_BUYER:
            print(f'Sorry, you cannot purchase {requested_tickets} tickets.\n'
                  'Only 4 tickets can be purchased per buyer.\n')
            return 0

        # Prevent user from buying what is not available in inventory.
        elif requested_tickets > remaining_tickets:
            print(f'Sorry, we are in high demand! Only {remaining_tickets} tickets are left.')
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
    remaining_tickets = TOTAL_TICKETS
    total_buyers = 0

    # Prompt the user until inventory is clear.
    while remaining_tickets > 0:
        print(f'There are {remaining_tickets} tickets available during pre-sale.')

        # Call the input function to get the purchase amount.
        purchased_tickets = get_tickets(remaining_tickets)

        # Tally each transaction.
        if purchased_tickets > 0:
            remaining_tickets -= purchased_tickets
            total_buyers += 1
            print('Thank you for your purchase!\n'
                  f'There are still {remaining_tickets} tickets left.\n')

    # Announce when inventory is clear.
    print('\nPre-sale has ended!')
    print(f'{total_buyers} buyers have purchased all available tickets.')

# Execute main.
if __name__ == '__main__':
    main()