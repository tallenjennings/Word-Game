"""This is to help me learn"""

#introduction to question game
print('welcome to my program')

#collect persons info func
def collect():
    print('hi, what is your name?')
    global name
    name = input()
    print('how old are you?')
    global age
    age = int(input())
    print('what month were you born?')
    global birthmonth
    birthmonth = input()
    print('what day were you born?')
    global birthday
    birthday = int(input())
    print('how much do you weigh?')
    global weight
    weight = input()
    print('where are you from?')
    global location
    location = input()


#run function
collect()

#number game func
def game():
    print('pick a number!')
    num = int(input())
    agex = age + num
    print(name + ', you will be ' + str(agex) + ' in ' + str(num) + ' years!')
    birthyear = 2019 - age
    print('you were born within 1 year of ' + str(birthyear))
    print('i will print ' + birthmonth + ' ' + str(num) + ' times')
    print(birthmonth * num)
    numcomp = num > birthday
    if numcomp is True:
        print (str(num) + ' is larger than your birthday')
    else:
        print (str(num) + ' is smaller than your birthday')
    print('you weigh less than an elephant!')
    print('you live in a place with ' + str(len(location)) + ' characters in its name!')

# call game func
game()
