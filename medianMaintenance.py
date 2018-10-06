from DataStructures.MinHeap import MinHeap
from DataStructures.MaxHeap import MaxHeap
Hlow = MaxHeap()
Hhigh = MinHeap()
numbers = open("./Median.txt", "r")
median_sum = 0
for number in numbers:
    x = int(number)
    maxHlow = Hlow.peekMax()
    if maxHlow is None:
        Hlow.insert(x)
        median_sum += x
        continue
    if x < maxHlow:
        Hlow.insert(x)
    else:
        Hhigh.insert(x)
    if Hlow.size > Hhigh.size + 1:
        Hhigh.insert(Hlow.extractMax())
    elif Hhigh.size > Hlow.size + 1:
        Hlow.insert(Hhigh.extractMin())
    if Hlow.size >= Hhigh.size:
        print("median when ", x, Hlow.peekMax())
        median_sum += Hlow.peekMax()
    else:
        print("median when ", x, Hhigh.peekMin())
        median_sum += Hhigh.peekMin()
print(median_sum%10000)