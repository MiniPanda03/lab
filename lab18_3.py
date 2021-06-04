from queue import Queue
from queue import LifoQueue
import timeit
f = open("wyniki.txt", "w")
start = timeit.default_timer()
q = Queue(maxsize = 100)
for i in range(100):
    q.put(i)
stack = LifoQueue(maxsize = 100)
while(not q.empty()):
    stack.put(q.get())
stop = timeit.default_timer()
czas=stop-start
f.write("Czas z liczbami w programie="+str(czas)+"\n")
print('Czas z liczbami w programie: ', czas)  

start = timeit.default_timer()

f2= open("liczby.txt")
q2= Queue(maxsize = 100)
for x in f2:
  q2.put(x)
f2.close()
stack2 = LifoQueue(maxsize = 100)
while(not q2.empty()):
    stack2.put(q2.get())
stop = timeit.default_timer()
czas = stop - start
f.write("Czas z odczytem z pliku="+str(czas)+"\n")
print('Czas z odczytem z pliku: ', stop - start)
f.close()
