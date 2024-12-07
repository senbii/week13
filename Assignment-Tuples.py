def swap(a, b):
    a, b = b, a
    return a, b


def assignment():
    hours = {}
    with open('mbox.txt', 'r') as file:
        for line in file:
            if line.startswith('From '):
                words = line.strip().split()
                if len(words) > 5:
                    time_part = words[5]
                    hour = time_part.split(':')[0]
                    hours[hour] = hours.get(hour, 0) + 1

    hours = dict(sorted(hours.items()))

    return hours


def tuple():
    number = int(input('enter a number: '))
    word = input('enter a word: ')
    symbol = input('enter a symbol: ')
    return (number, word, symbol)

def oddTuples(t):
    newT = ()
    for i in range(len(t)):
        if not i % 2:
            newT += (t[i], )
    
    return newT

def main():
    hours = assignment()
    for hour, count in hours.items():
        print(f'{hour} {count}')
    
    print(tuple())
    
    print(oddTuples(('I','am','a','test','tuple.')))


if __name__ == '__main__':
    main()
