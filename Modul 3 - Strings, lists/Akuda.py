# Два списки цілих заповнюються випадковими числами.
# Сформуйте третій список, який містить:
# ■ елементи обох списків;
# ■ елементи обох списків без повторень;
# ■ елементи, спільні для двох списків;
# ■ тільки унікальні елементи кожного зі списків;
# ■ тільки мінімальне та максимальне значення кожного зі
# списків.

from random import randint
number = int(input("Take first diap - "))
number2 = int(input("Take second diap - "))
number3 = int(input("Take cost numbers - "))
list = [randint(number, number2) for i in range(number3)]
list2 = [randint(number, number2) for j in range(number3)]
emptylist, mx, dup = [], [], []
sum1, sum2, sum3 = [], [], []
for i in list+list2:
       if i not in emptylist:
           emptylist.append(i)
       else:
           dup.append(i)

mx.append(min(list))
mx.append(min(list2))
mx.append(max(list))
mx.append(max(list2))

# dup = [x for i, x in enumerate(list) if i != list.index(x)]
print("List #1 : ", list)
print("List #2 : ", list2)
print("List #3 : ", list+list2)
print("Elements of both list : ", dup)
print("Elements without repe : ", emptylist)
print("El common to two list : ", emptylist)
print("Min, max number : ", mx)
