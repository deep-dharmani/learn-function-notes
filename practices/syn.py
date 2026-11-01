def square(num):
    return (num**2)
# square_=square(5)
# print(square_)

def func(*name,age):
    return name, age
info=func("deep","dharamani",age="25")
print(info)