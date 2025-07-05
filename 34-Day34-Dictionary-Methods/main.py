ep1 = {122: 45, 123: 89, 567: 69, 670: 69}     # dictionary is ordered
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)      #updates ep1 by adding keys values of ep2 in ep1
# ep1.clear()     #empty dictionary
# ep1.pop(122)      #remove the key value pair of 122
ep1.popitem()     #remove last key value pair form ep1
del ep1[122]       #delete the key value pair of 122
print(ep1) 
