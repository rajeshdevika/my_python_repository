class A:
       def __init__(self,num,num_len):
           self.number=num
           self.num_len=num_len

           print(f'the number lengtg is {num_len}')
           print(f'the given number is {self.number}')

       def prime(self):
           if(self.number<0):
               print("numer cannot be negative")
               return -1
           elif(self.num_len==1):
               print("the given digit has lengh of 1 so value is addition of itself to it")
               return  self.number+self.number
           elif(self.number>=0and self.num_len>1):
                self.lop=[]
                for self.i in str(self.number):
                   self.lop.append(self.i)
                return int(self.lop[0])+int(self.lop[-1])



inpt=int(input("enter the number"))
l=len(str(inpt))
k=A(inpt,l)
print(k.prime())
