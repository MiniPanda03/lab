import timeit

data = [4,10,11,5,73,5,1]
def heap_sort(tab):
    for start in range(int((len(tab) - 2) / 2), -1, -1):
        shiftdown(tab, start, len(tab) - 1)
    for end in range(len(tab) - 1, 0, -1):
        tab[end], tab[0] = tab[0], tab[end]
        shiftdown(tab, 0, end - 1)
    return tab

def shiftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break

def quicksort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return array
plik=open("time.txt","w")
start = timeit.default_timer()
quicksort(data)
stop = timeit.default_timer()
czas = stop - start
plik.write("Czas quicksort: "+str(czas)+"\n")
start = timeit.default_timer()
heap_sort(data)
stop = timeit.default_timer()
czas = stop - start
plik.write("Czas heap: "+str(czas)+"\n")