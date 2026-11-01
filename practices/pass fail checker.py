def pass_fail(marks):
    if 100 >= marks >= 40 :
        return "passed"
    elif 0 <= marks < 40:
        return "failed"
    else:
        return f"{marks} is invalid no of marks"
marks_= int(input("Enter marks:"))
pass_fail_= pass_fail(marks_)
print(pass_fail_)