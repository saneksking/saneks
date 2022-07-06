

def printInstructions(instructions):
    print(instructions)


def getUserScore(userName):
    try:
        inputs = open('userScore.txt', 'r')
        for line in inputs:
            content = line.split(', ')
            if content[0] == userName:
                inputs.close()
                return content[1]
            inputs.close()
        return '-1'
    except IOError:
        print("File not found. A new file will be created.")
        inputs = open('userScore.txt', 'w')
        inputs.close()
        return '-1'


def updateUserScore(newUser, userName='Anon', score='0'):
    if newUser:
        wrt = open('userScore.txt', 'a')
        wrt.write(userName + ', ' + score + '\n')
        wrt.close()
    else:
        temp = open('userScores.txt', 'w')
        wrt = open('userScore.txt', 'r')
        for line in wrt:
            content = line.split(', ')
            if content[0] == userName:
                temp.write(userName + ', ' + score + '\n')
            else:
                temp.write(line)
        wrt.close()
        temp.close()
