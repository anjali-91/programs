original_array = [1,2,3,4,5,6,7,8,9]
size = 3

subarray = [original_array[i:i+size]
            for i in range (0,len(original_array),size)]

print(subarray)