#zadanie z tablicy
# q = int(input())
# p = int(input())
# if (q < 1.3*p):
#   print ("TAK")
# else:
#   print("NIE")

# #zad1
 # n = int(input())
 # for i in range(n):
 #   print(i**3+3, end)

# print(list(range(10)))
# print(list(range(5)))
# print(list(range(2,10)))
# print(list(range(12,10)))
# print(list(range(12,10, -1)))

#print(list(range(9, 1, -2)))

# for i in range(0,10,2):
#   print(i, end=" ")

#L = [0,1,2,3,4,5,6]
#print(L[:4:-3])
#       ^^^ 
#range musi mieć podane liczby
#list nie musi
#range(start,stop,step)

#pętla liczb dwucyfrowych od 10 do 21
#for i in range(10,22): print (i, end=" ")
#pętla liczb dwucyfrowych nieparzystych od 15 do 31
#for i in range(15,32,2): print (i,end=" ")
#pętla liczb dwucyfrowych malejąco (step ujemny)
#for i in range(99,9,-1): print (i, end=" ")
#pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100,981,20): print (i, end=" ")
#zad2
#for i in range(105,999,15): print(i, end=" ")

#zad3
a = int(input())
for i in range(1,a+1):
 if (a % i == 0) :
   print(i)