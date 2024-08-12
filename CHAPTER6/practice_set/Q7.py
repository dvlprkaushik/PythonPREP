sentence = "Kaushik Das is working on some exciting new projects in web development.".lower()
substring = input('Enter the word : ').lower()

if substring in sentence:
    print('The post is talking about you')
else:
    print('the post is not talking about you')