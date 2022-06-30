

def printInstructions(instructions):
    print(instructions)


def getUserScore(userName):
    name = open('userScores', 'r')
    for i in name:
        print(i, end='')
        content = []
        i.join(content).split(' ,')
        if content != name:
            name.close()
            return content
    name.close()
    return '-1'







