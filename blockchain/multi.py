import multiprocessing
from random import randint

def add(a,b,return_dict):
    # print(a+b)
    sum = a + b
    return_dict[str(a) + '+' + str(b)] = sum


manager = multiprocessing.Manager()
return_dict = manager.dict()


p1 = multiprocessing.Process(target=add, args=(randint(1,100), randint(1,100),return_dict))
p2 = multiprocessing.Process(target=add, args=(randint(1,100), randint(1,100),return_dict))
p3 = multiprocessing.Process(target=add, args=(randint(1,100), randint(1,100),return_dict))
p4 = multiprocessing.Process(target=add, args=(randint(1,100), randint(1,100),return_dict))



p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()


print(return_dict)

