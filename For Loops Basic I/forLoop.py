#name: Tala khaled
#email : talakh1798@gmail.com
#description : for loop practice 


#1 Basic - Print all integers from 0 to 150.
for i in range(0,151,1):
    print(i)

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001,5):
    print(x)

#3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,101,1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding ")    

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for y in range (0 ,500001):
    if y % 2 == 1:
        sum+=y
print(sum)

#5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours
for v in range (2018,0,-4):
    print(v)


#6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
    
lowNum=2
highNum=15
mult=3 

for r in range (lowNum,highNum+1):
    if r % mult == 0 :
        print (r)
       
