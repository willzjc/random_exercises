dictionary={
    1:2, 2:1, -3:-1 , 4: -10, 5: 100
}

print("Unsorted dictionary")
print(dictionary.items(),'\n')
print("Sorted dictionary based on keys")
print (list((k,v) for k,v in sorted(dictionary.items(), key= lambda x : x[0]) ),'\n')
print("Sorted dictionary based on values")
print (list((k,v) for k,v in sorted(dictionary.items(), key= lambda x : x[1]) ),'\n')
