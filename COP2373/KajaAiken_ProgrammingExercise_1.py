# Set the constants for the ticket sales.
TOTAL_TICKETS = 20
MAX_TICKETS_PER_BUYER = 4

# Track the inventory of tickets.
remaining_tickets = TOTAL_TICKETS
total_buyers = 0

# Prompt the user until inventory is clear.
while remaining_tickets > 0:
    print(f'There are {remaining_tickets} tickets available during pre-sale')

    try:
        # Prompt user on how many tickets they want and inform of the limit.
        requested_tickets = int(input('How many tickets would you like to purchase?\n'
                                      f'Maximum of {MAX_TICKETS_PER_BUYER} tickets per person.'))

        # Set a limit on amount of tickets to be purchased.
        if requested_tickets > MAX_TICKETS_PER_BUYER:
            print(f'Sorry, you cannot purchase {requested_tickets} tickets.')

        # Prevent user from buying what is not available in inventory.
        elif requested_tickets > remaining_tickets:
            print(f'Sorry, we are in high demand! Only {remaining_tickets} tickets are left.')

        # Prevent user from entering zero or negative amount.
        elif requested_tickets <= 0:
            print('Please enter a number greater than zero.')

        # Tally each transaction and inform user of remaining tickets.
        else:
            remaining_tickets -= requested_tickets
            total_buyers += 1
            print('Thank you for your purchase!\n'
                  f'There are still {remaining_tickets} tickets left.')

    # Prevent user from entering an input that is not a number.
    except ValueError:
        print('Please enter a valid whole number.')

# Announce when the inventory is cleared.
print('Pre-sale has ended!\n'
      f'{total_buyers} buyers have purchased all available tickets.')