def even_numbers(num):
    for i in range(1,num+1):
        even=0
        if i%2==0:
            even+=1
    if even==0:
        return "no any Even numbers in your range"
    else:
        return f"There are {even} even numbers in the range of {num}"
range_=int(input("Enter your range of even numbers: "))
even_=even_numbers(range_)
print(even_)