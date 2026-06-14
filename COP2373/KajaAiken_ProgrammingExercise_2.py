# This program will use functions to create a spam detector using keywords.
# It will simultaneously keep a spam score and track the likelihood of a message being spam
# based off of the spam score.

# A function that will scan the email for keywords and phrases.
def track_spam_score(email, keywords):
    # Set the constants.
    score = 0
    spam_detected = []

    # Convert lowercase wording for case-sensitive detection.
    email_lower = email.lower()

    for word in keywords:
        # Track the number detections of keywords and phrases.
        count = email_lower.count(word.lower())
        if count > 0:
            score += count
            # Track the detected keywords and phrases.
            spam_detected.append(f'{word} was found {count} times.')

    return score, spam_detected

# A function that will track the likelihood of a message being spam based off the spam score.
def track_spam_likelihood(score):
    if score == 0:
        return 'Not spam.'
    elif 1 <= score <= 2:
        return 'Not likely spam.'
    elif 3 <= score <= 5:
        return 'Maybe spam. Tread lightly.'
    else:
        return 'Most likely spam.'

# A function that holds a list of 30 common spam keywords and phrases.
def main():
    keywords = ['buy now', 'free', 'earn money', 'act now', 'limited time', 'click here', 'guaranteed', 'no catch', 'winner',
                     'congratulations', 'urgent', 'risk free', '100% satisifed', 'double your income', 'save big', 'order now',
                     'as seen on', 'cancel at any time', 'make $', 'pure profit', 'hidden fees', 'invest now', 'lowest price',
                     'lose weight', 'meet singles', 'pre-approved', 'social security number', 'verify your account', 'bitcoin',
                     'jackpot']
    print('=' * 50)
    print('      ---!!!--- Spam Detector ---!!!--- ')
    print('=' * 50)
    print('Paste your email message for spam detection. Please press enter TWICE to continue.')

    # Ensure multiple lines pass input.
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)
    email = '\n'.join(lines)

    if not email.strip():
        print('Please enter a valid email address.')
        return

    # Process the user's email input.
    score, spam_detected = track_spam_score(email, keywords)
    likelihood = track_spam_likelihood(score)

    # Display the results of the spam score.
    print('-' * 50)
    print('           --- Scanning Results... --- ')
    print('-' * 50)
    print(f'Total spam detected: {score}')
    print(f'Total spam likelihood: {likelihood}')
    print('-' * 50)

    if spam_detected:
        print('Here are the spam keywords and phrases detected:')
        for spam in spam_detected:
            print(f'- {spam}')

    else:
        print('Here are the spam keywords and phrases not detected:')
        for spam in spam_detected:
            print(f'- {spam}')

if __name__ == '__main__':
    main()

