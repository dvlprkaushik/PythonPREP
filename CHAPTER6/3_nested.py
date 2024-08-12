candies = 6  # You have 6 candies
like_candies = True  # You like the candies

if candies > 5:
    if like_candies:
        print("Yay! You eat the candies!")  # This runs if you have more than 5 candies and you like them
    else:
        print("You give the candies to a friend.")  # This runs if you have more than 5 candies but don't like them
else:
    if like_candies:
        print("You save the candies for later.")  # This runs if you have 5 or fewer candies and you like them
    else:
        print("You give the candies to someone else.")  # This runs if you have 5 or fewer candies but don't like them
