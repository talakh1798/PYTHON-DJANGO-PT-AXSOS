#name: Tala khaled
#email : talakh1798@gmail.com
#description : practice functions

# Countdown
def Countdown(n):
    list=[]
    for i in range(n,-1,-1):
        list.append(i)
    return list

print(Countdown(5))    

# Print and Return 
def print_and_return(num):
    print(num[0])
    return num[1]

x=print_and_return([1,2])
print(x)

# First Plus Length
def First_Plus_Length(list1):
    return list1[0] + len(list1)

z= First_Plus_Length([1,2,3,4,5])
print(z)


# Values Greater than Second 
def values_greater_than_second(list2):
    if len(list2) < 2 :
        return False
    
    sec_value=list2[1]
    new_list=[]
    for i in list2:
        if i > sec_value:
            new_list.append(i)
    print(len(new_list))
    return new_list
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))        
print(values_greater_than_second([3]))

# This Length, That Value
def length_and_value(size,value):
    return [value] * size
print(length_and_value(4, 7))
print(length_and_value(6, 2))
    



