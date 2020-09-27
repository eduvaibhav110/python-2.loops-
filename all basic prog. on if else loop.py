                            //conditions and loops

//checking no. is positive / negative /zero

num = float(input("Enter a number: "))  
  
if num > 0:  
 print("{0} is a positive number".format(num))  
elif num == 0:  
   print("{0} is zero".format(num))   
else:  
   print("{0} is negative number".format(num))   





//Check if a Number is Odd or Even

num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))  



//Check Leap Year

year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  






//Check Prime Number

num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  






//to Print all Prime Numbers between an Interval

#Take the input from the user:   
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
