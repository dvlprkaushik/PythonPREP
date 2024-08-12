# Define the spam keywords
spam_keyword_1 = "Make a lot of money"
spam_keyword_2 = "buy now"
spam_keyword_3 = "subscribe this"
spam_keyword_4 = "click this"

# Input from the user
# Convert input to lowercase for case-insensitive comparison
user_comment = input('Enter your comment: ').lower()

# Check if the comment contains any spam keywords
if spam_keyword_1.lower() in user_comment or \
   spam_keyword_2.lower() in user_comment or \
   spam_keyword_3.lower() in user_comment or \
   spam_keyword_4.lower() in user_comment:
    print("This comment is spam.")
else:
    print("This comment is not spam.")
