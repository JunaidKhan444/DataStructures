def smart_divide (func):
    print("Inside Smart Divide")
    def inner(a,b):
        if b==0:
            print("b Cant be Zero")
        else:
            
            print("{} divided by {} equals {}".format(a,b,func(a,b)))
        

    return inner



@smart_divide
def divide(a,b):
    return a/b

divide(4,1)
        