Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> revolution={}
for i in range(2019, 2022):
  print("year "+ str(i))
  year=i
  u1=int(input("Enter the number of 2nd year UG students "))
  u2=int(input("Enter the number of 3rd year UG students "))
  u3=int(input("Enter the number of 4th year UG students "))                
  p1=int(input("Enter the number of 1st year PG students "))
  p2=int(input("Enter the number of 2st year PG students "))
  F=int(input("Total Number of faculty Members in the department "))
  S=u1+u2+u3+p1+p2
  SFR=S/F
  revolution[i]=float(SFR)
  revolution["u1"]=u1
  revolution["u2"]=u2
  revolution["u3"]=u3
  revolution["p1"]=p1
  revolution["p2"]=p2
  revolution["F"]=F
  print("No of students in the department= " +str(S))
  print("Student faculty ratio= " +str(SFR))
  print(revolution)
  print(" ")
Avg_SFR=(revolution[2019] + revolution[2020] + revolution[2021])/3
print("average SFR= " +str(Avg_SFR))
if Avg_SFR<=15:
  score=20
elif Avg_SFR<=17:
  score=18
elif Avg_SFR<=19:
  score=16
elif Avg_SFR<=21:
  score=14
elif Avg_SFR<=23:
  score=12
elif Avg_SFR<=25:
  score=10
elif Avg_SFR>25:
  score=0
print("marks=" +str(score))