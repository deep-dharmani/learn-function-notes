Arguements and parameters:
                           parameters and arguements are given inside the parenthesis 
of our functions but both are different things parameters are used when we buit a func
and give a name to that arguement we use that prameter name inside the defination of
function for their work and arguements are those which we pass in parenthesis of our 
function when we call that in our program we have to pass that arguement according to 
how many parameters it contains in the def of that function
simple conclusion: arguements are passed when we call a function and parameters are passed
when we define a function , means parameter are just placeholders which are working in a function 
at the place of arguements but arguements are actual values of that placeholders.

return and print:
             when we use a print in def of function it will just display our print statement
and if we want to store that in a variable it will not because it only print something in our 
output and return will give acctual result of our function and we  easily store that value inside
any variable and we use that variable at any time it will directly shows that returned value.

default arguements:
     when we call a function and  pass nothing in parenthesis as arguement then it will give eror
but if we add a default arguement when we def a function and in parenthesis of function 
parameter = that default arguement and now if pass nothing  at the place of that parameter then  
it will take that default value.

keyword arguement:
     we can write our arguement at any place when we call our function but we have to write that 
parameter name = That value of arguement and we can write in any arangement and one important thing
if we write it for one arguement then for others also we have to do same at it will automatically 
takes that arguement in the form of dictionary.

*args:
    if user of function can pass many values as arguements as our that  parameter and this 
is possible if we add * before name of  our that parameter, but if you have two or more parameters
then we have to user key word arguement for identification of other arguement but not for our *args
because keyword arguement only takes one value of arguement.

**kwargs:
    if we write ** before a parameter then it only takes values of arguement in  keyword arguement 
form and it will takes values as dictionary type.

simple conclusion: keyword arguement only takes one arguement for one parameter in dictionary form,
*args takes unlimited arguement but not in dictionary form and **kwargs takes unlimited and also
in dictionary form.

>> Main points on functions.
>Functions didn't automatically run when we call them then it will works.
>parameters and arguement both are different things.
>return and print both are different things.
>we have to use return when need our value back inside a variable.
>functions are not use to write a syntax like we are writing loops which are run only one time
in our program but we use functions when we need that just call that function many times which
we want in clean code.
>it will aviod the repetation in our code means if we want to do same programing in our project
aviod to copy that code just make a function of that work and call where we need through this our
code will become clean.
