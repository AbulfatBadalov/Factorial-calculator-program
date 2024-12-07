#Faktorial hesablayan
a=int(input("Reqem daxil edin: "))
b=1
#burda a ve b deyisenlerini yaratdim
if a<0:
   print("Menfi ededlerin faktoriali olmur.")
   #burda if sert operatorundan istifade ederek sert qoydum
elif a==0:
     print("Cavab: 1")
else:
#asagida range ve fordan ibaret faktorialin riyazi ifadesidir
  for i in range(1,a+1):
     b=b*i
  print(f"Cavab: {b}")