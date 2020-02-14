#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
from time import time
from random import randint


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for i,w in enumerate(weights):
        hash_table_insert(ht,w,i)
    
    for i,w in enumerate(weights):
        # value = limit - prev_w   v = limit - w
        w2 = (limit - w)
        # print('w1', w)
        # print('w2', w2)
        print('possible addition', w,w2)
        j = hash_table_retrieve(ht,w2)
        # print('i',i)
        if j:
            print('j', j, f'{weights[j]} + {w}')
        if not j:
            continue
        else: return (i,j) if i > j else (j,i)
    return None


# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")


if __name__ == '__main__':
    start = time()

    arr = [randint(1,100) for i in range(500)]

    iw = get_indices_of_item_weights(arr,len(arr),150)
    print(iw)

    end = time()

    print('processing time: ', end - start)
