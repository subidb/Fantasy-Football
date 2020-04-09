import random


def randomize_list(listx):
    total = 0
    for x in range(3):
        x = random.randrange(1, 10)*5
        total += x
        listx.append(x)

    listx.append(total)
    return listx


def tuplelize(listx):
    return tuple(listx)


list1, list2, list3, list4, list5, list6 = ([i] for i in range(20, 26))
list_list = [list1, list2, list3, list4, list5, list6]

for li in list_list:
    randomize_list(li)


tuple1, tuple2, tuple3, tuple4, tuple5, tuple6 = \
    tuple(list1), tuple(list2), tuple(list3), tuple(list4), tuple(list5), tuple(list6)


tuples_list = [tuple1, tuple2, tuple3, tuple4, tuple5, tuple6]

# ratinglist = [v for i, v in enumerate(ratinglist) if i % 2 == 0]


