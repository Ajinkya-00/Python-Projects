def num_guessing(num):

    while True:
        guess = int(input("Enter the number to guess: "))

        if guess < secret:
            print("To Low 😒")
        elif guess > secret:
            print("To High 😯")
        else:
            print("🥳 Correct ! the number was",secret)

secret = int(input("Enter the secret number: "))

num_guessing(secret)        