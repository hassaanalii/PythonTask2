import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#Task 1 Factorial of a number using recursion

def factorial(number):
    if number==1:
        return 1
    else:
        return number * factorial(number-1)
    
# number = int(input("Enter a number to find its factorial: "))
# print(factorial(number))


#Task 2 Fibonacci Series upto a certain number

def fib(number):
    f0 = 0
    f1 = 1
    sum = 0
    arr = [f0,f1]
    for i in range(2,number):
        sum = (f0+f1)
        f0 = f1
        f1 = sum
        arr.append(sum)
    return arr

# ans = fib(int(input("Enter a number:")))
# for i in ans:
#     print(i)


#Task 3

# SELECTION SORT

def selection_sort(arr):

    for i in range(0,len(arr)):
        min = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
            else:
                continue
    
        index = arr.index(min)
        temp = arr[index]
        arr[index] = arr[i]
        arr[i] = temp
    return arr

# my_lst = selection_sort([10,60,30,5,7])
# for i in my_lst:
#     print(i)


# Bubble Sort 

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                continue
    return arr
    
    # my_lst = bubble_sort([10,60,30,5,7])
    # for i in my_lst:
    #     print(i)


#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return
    else:
        mid = len(arr) // 2
        left_list = arr[:mid]
        right_list = arr[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        merge_two_sorted_lsts(left_list,right_list, arr)


def merge_two_sorted_lsts(l1,l2,arr):
    i=j=k=0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            arr[k] = l1[i]
            k+=1
            i+=1
        else:
            arr[k] = l2[j]
            k+=1
            j+=1
    while i < len(l1):
        arr[k] = l1[i]
        k+=1
        i+=1
    while j < len(l2):
        arr[k] = l2[j]
        k+=1
        j+=1

# arr = [31,41,22,33,2]
# merge_sort(arr)
# print(arr)

#Task 4
#CSV File manipulation

def csv_manipulation():

    df = pd.read_csv('sample.csv')
    sub1_list = df['Subject1'].tolist()

    sum = 0
    for i in sub1_list:
        sum+=i
    mean = sum/len(sub1_list)
    print(f"The mean of subject 1 is: {mean}")

    if len(sub1_list) % 2 == 0:
        ans = even_median(sub1_list)
        print("The median of subject1 is : " ,  ans)
    else:
        median = (len(sub1_list)) //2
        print(f"The median of subject 1 is: {sub1_list[median]}")
        
def even_median(l):
    return (l[len(l)//2] + l[len(l)//2 -1])/2

# csv_manipulation()



#TASK 5 Seaborn

def seaborn_usage():
    # print(sns.get_dataset_names())
    tips = sns.load_dataset("tips")
    # print(tips)
    print(sns.scatterplot(x="tip",y="total_bill", data=tips, hue="day"))
    plt.show()
    
# seaborn_usage()

#TASK 6 Error Handling

def error_handling():
    try:
        numerator= 5
        denominator = 0
        ans = numerator/denominator

        
        return ans
    except ZeroDivisionError:
        print("Denominator cannot be zero")
    except IndexError:
        print("There is no 9th index")    
    finally:

        print("Remaining Code!")
        try:
            lst = [1,2,3,4]
            return lst[9]
        except IndexError:
            print("Index out of bound")

error_handling()

