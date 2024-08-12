def counter(string, substring, flag):
    count = 0
    if flag:  #Overlapping allowed
        for i in range(len(string) - len(substring) + 1):
            if string[i:i + len(substring)] == substring:
                count += 1
    else:
        print(' ')

    return count


print(counter('Sgggs', 'gg', True))
