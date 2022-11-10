#Задание
# доделать задачу про солнце с урока,
# пропорции "06:00"- 0, "12:00"- 90, "18:00"-180

class Downedit(Exception):
    pass

while True:
   try:
     time = input("Give me time! ")
     ttime = [int(i) for i in time.split(":")]
   except(ValueError):
       print("Error!")
   else:
       break
if ttime[0] >= 18 and ttime[0] <= 24 or ttime[0] >= 0 and ttime[0] < 6:
    raise Downedit("Sun in dark!")
else:
    print(((ttime[0] - 6) * 15) + ttime[1] * 0.25)
