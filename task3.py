def gh(a,b,n):
  d=str(a*b)
  if n[-2:]==d:
    print("True")
  else:
    print("Folse")
  return a
a=int(input("напишите любой день месяца "))
b=int(input("напишите число месяца "))
n=input("напишите любой год ")
s=gh(a,b,n)