tup = (1, 2, 76, 342, 32, "green", True).....tuples ko change nhi kr skte
# tup[0] = 90....throws error
print(type(tup), tup)
print(len(tup))....len of tuple i.e.,7
print(tup[0])
print(tup[-1])....7-1=6th true
print(tup[2])
# print(tup[34])....error

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]....slicing k baad naya tuple banta h
print(tup2)
....tuples are immutable strings are immutable lists are mutable
