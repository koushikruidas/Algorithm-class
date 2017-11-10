import BST

class Car:
    def __init__(self, license):
        self.license = license


def key(obj):
    return obj.license


car1 = Car(5)
car2 = Car(6)
car3 = Car(5)


A = [car1, car2, car3]

print(key(A[0]))

k = 10
L = []
for x in range(k):
    L.append([])

print(L)

L[key(A[0])].append(A[0])
L[key(A[1])].append(A[1])
L[key(A[2])].append(A[2])

print(L)

output = []
for x in range(k):
    output.extend(L[x])

print(output)