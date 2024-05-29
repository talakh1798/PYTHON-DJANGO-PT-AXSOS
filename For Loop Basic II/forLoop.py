# name: Tala khaled
# email: Talakh1798@gmail.com
# Description: for loop practice

# Biggie Size
def Biggie_Size(list):
    for i in range(len(list)):
        if list[i]>0:
            list[i]="big"
    return list
print(Biggie_Size([-1, 3, 5, -5])) 

# Count Positives
def count_positives(list1):
    count=0
    for num in list1:
        if num > 0 :
            count +=1
    list1[-1]=count
    return list1
print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# Sum Total
def sum_total(list2):
    sum=0
    for i in list2:
        sum+=i
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2])) 

# Average
def average(list3):
    sum=0
    for num in list3:
        sum+=num
        average=sum/len(list3)
    return average
print(average([1,2,3,4]))   

# Length 
def length(list4):
    length=len(list4)
    return length

print(length([37,2,1,-9]) )
print(length([]))

# minimum
def minimum(list5):
    if len(list5)==0:
        return False
    
    min_number=list5[0]
    for num in list5:
        if num < min_number:
            min_number=num
    return min_number        
    

print( minimum([37,2,1,-9]))
print(minimum([]))

# Maximum
def maximum(list_max):
    if len(list_max)==0:
        return False
    max_num=list_max[0]
    for num in list_max:
        if num > max_num:
            max_num=num
    return max_num
print( maximum([37,2,1,-9])) 
print(([]))      

# ultimate_analysis
def ultimate_analysis(lst):
    sumTotal=sum(lst)
    average=sum(lst)/len(lst)
    min_num=min(lst)
    max_num=max(lst)

    dirctory={'sumTotal':sumTotal, 'average':average , 'minimum':min_num , 'maximum':max_num , 'length':len(lst)}
    return dirctory
print(ultimate_analysis([37, 2, 1, -9])) 


# Reverse List
def reverse_list(lst1):
    reverse_lst=[]
    for i in range(len(lst1)-1 , -1 , -1 ):
        reverse_lst.append(lst1[i])
    return reverse_lst    

print(reverse_list([37,2,1,-9]) )        











    
    





