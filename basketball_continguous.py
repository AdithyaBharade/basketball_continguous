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

'''You are competing in a basketball contest. In this contest the score for each 
successful shot depends on both the distance from the basket and the player's 
position. The ball is shot N times, successfully. You are given an array A containing the 
distance of a player from basket for N shots. The index of array represents 
the position of the player. Score is calculated by multiplying the position with the 
distance from the basket.
Your task is to find and return an integer value, representing the maximum possible 
score you can achieve by choosing a contiguous subarray of size K from the given 
array.
Given: 
K=3
A=[4,3,2,7,1,9]'''