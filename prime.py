class PrimeNum:
  def primenum(self,lower,upper):
    for num in range(lower,upper + 1):
      if num > 1:
         for i in range(2,num):
         
             if (num % i) == 0:
               break
         else:
           print(num)  
             

p=PrimeNum()
a=int(input("Enter lower :"))
b=int(input("Enter upper :"))
p.primenum(a,b)
