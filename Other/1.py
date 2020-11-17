from decimal import Decimal

Probabilities = [Decimal("0.11"), Decimal("0.08"), Decimal("0.08"), Decimal("0.14"), Decimal("0.08"),Decimal("0.11"), Decimal("0.08"), Decimal("0.07"), Decimal("0.14"),Decimal("0.11")]
indexes = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
Probabilities1 = [Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0454545"), Decimal("0.0909091"), Decimal("0.0909091"), Decimal("0.0909091"), Decimal("0.0909091"), Decimal("0.0454545"), Decimal("0.136364"), Decimal("0.0909091")]
indexes1 = {'Ж': 0, 'у': 1, 'к': 2,
'я': 3, 'П': 4, 'е': 5,
'р': 6, 'в': 7, 'і': 8, 'т': 9,
'с': 10, 'н': 11, 'А': 12, 'а':13,
' ': 14}
def code(sequence):
    low_old = Decimal("0")
    high_old = Decimal("1")
    for word in sequence:
        index = indexes[word]
        low_new, high_new = sum(Probabilities[:index]), sum(Probabilities[:index + 1])
        low, high = low_old + (high_old - low_old) * low_new, low_old + (high_old -         low_old) * high_new
        print("Coding: ", low, high)
        low_old, high_old = low, high
    rounded = set_precision(low, high).normalize()
    print(rounded)
    print(format(int(str(rounded)[2:]), 'b'))
    return rounded

def decode(value):
    result = ''
    i = 0
    while value > 0.001 and i < 22:
        index = find(value)
        high, low = sum(Probabilities[:index + 1]), sum(Probabilities[:index])
        print("Code: ", value, " Borders: [" + str(low) + ", " + str(high) + ")")
        value = (value - low) / (high - low)
        result += str(key(index) + ' ')
        i += 1
    return result

def set_precision(low, high):
    down, up = str(low)[2:], str(high)[2:]
    n = min(len(down), len(up))
    for i in range(n):
        if down[i] is not up[i]:
            down = down[:i] + str(int(down[i])+1)
            break
    return Decimal("0." + down)

def find(key):
    for i in range(len(Probabilities)):
        if key < sum(Probabilities[:i + 1]):
            return i
def key(val):
    for keys, value in indexes.items():
        if val == value:
            return keys
print(decode(code(str(input()).split())))