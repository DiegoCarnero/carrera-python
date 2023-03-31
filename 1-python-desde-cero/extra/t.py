x = 50


def func(num=3, a="a"):
    global x

    print(x)
    x = num
    print(a, x)


func(a="b", num=4)
func()
