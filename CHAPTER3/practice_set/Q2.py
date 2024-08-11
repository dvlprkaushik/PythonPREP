from datetime import date
currDate = date.today()
name = input('Enter Your Name : ')
letter = '''
Dear name, You are selected! Date 
'''
print(letter.replace("name", name).replace("Date", str(currDate)))
