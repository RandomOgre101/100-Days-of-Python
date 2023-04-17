# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap(year):
#         return 29
#     return month_days[month-1]
    

  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)



def perfect(num):
    count=0
    for i in range(1,num):
        if num%i==0:
            count+=i

    if count==num:
        return True
    else:
        return False
        
        

for num in range(1,10000001):
    if perfect(num) is True:
        print(num)

