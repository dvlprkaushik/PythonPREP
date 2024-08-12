favLang = {}

name = input('Enter name : ')  # Say you enter "John"
lang = input('Enter language : ')  # Enter "Python"
favLang[name] = lang  # favLang now is {"John": "Python"}

name = input('Enter name : ')  # Enter "John" again
lang = input('Enter language : ')  # Enter "Java"
favLang[name] = lang  # favLang now becomes {"John": "Java"}, "Python" is overwritten

print(favLang)
