path = [('s', 'a'), ('s', 'b'), ('b', 'g')]

def func(startState, finalState, path):
    curr = path.pop()[0]
    finalPath = [finalState, curr]
    while curr != startState:
        for i in path:
            if i[1] == curr:
                curr = i[0]
                finalPath.append(curr)
                break
    return finalPath

print(func('s', 'g', path))

