pattern = 'abacaaba'


def makeTable(pattern):
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 or pattern[i] != pattern[j - 1]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


print(makeTable(pattern))
