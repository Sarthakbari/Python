file = open('youtube.txt', 'w')

try:
    file.write('Hey!')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Hey python...')