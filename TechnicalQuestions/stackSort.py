def stackSort(sort):
    helperStack = []
    orderedPos = 0
    while orderedPos < len(sort):
        smallest = sort.pop()
        for i in range(orderedPos, len(sort)):
            element = sort.pop()
            if element < smallest:
                element, smallest = smallest, element
            helperStack.append(element)
        sort.append(smallest)
        for j in range(len(helperStack)):
            sort.append(helperStack.pop())
        orderedPos+=1
stack1 = [10,9,8,7,4,3,99,1,2,10,20]
stackSort(stack1)
print(stack1)