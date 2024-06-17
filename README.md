def max_sum(array,number):
    narray=len(array)
    '''if number>narray:
        return 'subarray of size greater than the array isnot possible'''
    max_sum=float('-inf')
    for i in range(narray-number+1):
        current_sum=0
        for j in range(number):
            current_sum+=(i+j)*array[i+j]
            max_sum=max(max_sum,current_sum)
    return max_sum


array1=[4,3,2,7,1,9]
number=3
print(max_sum(array1,number))
