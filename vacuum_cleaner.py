def what_to_do(sta, loc):
    global agent1, agent2
    if sta == 'clean':
        print('Location ' + loc + ' is clean! \nNow move to next location!')
        agent2 -= 1
    else:
        print('Cleaning the location ' + loc)
        agent1 += 1
        agent2 += 1

agent1 = 0
agent2 = 0
while True:
    print('1 - Top left   \t  2 - Top right')
    print('3 - Middle right \t 4 - Below')
    print('5 - Middle left \t 6 - Middle')
    location = input('\nEnter the vacuum cleaner current location: ')
    status = input('Is it clean or dirty: ')
    what_to_do(status, location)
    print('Agent1 point: ' + str(agent1))
    print('Agent2 point: ' + str(agent2))

    check = input('Do you want to do it again(y/n): ')
    if check == 'n':
        break
