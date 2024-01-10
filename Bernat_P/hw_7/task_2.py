class Fraction:
  def __init__(self, *args):
       if len(args) == 1:
            if isinstance(args[0], int):
                self.num = int(args[0])
                self.denum = 1
            elif isinstance(args[0], str):
                if '/' in args[0]:
                    self.num = int(args[0].split('/')[0])
                    self.denum = int(args[0].split('/')[1])
                else:
                    self.num = int(args[0])
                    self.denum = 1
       else :
            self.num = args[0]
            self.denum = args[1]  
       Fraction.change(self)

  def change(self, num=None, denum=None):
        if num is None:
            num = self.num
        if denum is None:
            denum = self.denum
        if ((self.denum % 2 == 0) and (self.num % 2 == 0)) or ((self.denum % 3 == 0) and (self.num % 3 == 0)) :
            self.denum = int('{:.0f}'.format(self.denum / self.num))
            self.num = int('{:.0f}'.format(self.num / self.num))  
        if self.num < 0 or self.denum < 0:
            self.num = -1 * abs(self.num)
            self.denum = abs(self.denum) 
        return self

  def check_other(other):
     if isinstance(other, int):
        other.num = other
        other.denum = 1


  def numerator(self, number=None):
    if not number:
      if self.denum % self.num == 0:
        self.denum = int('{:.0f}'.format(self.denum / self.num))
        self.num = int('{:.0f}'.format(self.num / self.num))
        return self.num
    else:
      self.num = number
      if self.denum % number == 0:
        self.denum =int('{:.0f}'.format(self.denum / number))        
        self.num = int('{:.0f}'.format(number/ number))
        return self.num
      

  def denominator(self, number=None):
    if not number:
      if self.denum % self.num == 0:
        self.denum = int('{:.0f}'.format(self.denum / self.num))
        self.num = int('{:.0f}'.format(self.num / self.num))
        return self.denum 
    else:
      self.denum = number
      if  self.denum % self.num == 0:
         self.denum =int('{:.0f}'.format(self.denum / self.num)) 
         self.num = int('{:.0f}'.format(self.num/ self.num))      
         return self.denum

  def __str__(self):
    return f"{self.num}/{self.denum}"

  def __repr__(self):
    return f"Fraction({self.num}/{self.denum})"
  
  def __add__(self,other):
    Fraction.check_other(other)
    common_denum = self.denum * other.denum
    new_num = (self.num * other.denum) + (other.num * self.denum)
    new_denum = common_denum
    result_fraction = Fraction(new_num, new_denum)
    result_fraction.change()  
    return f"{result_fraction.num}/{result_fraction.denum}"
    
  
  def __sub__(self,other):
    common_denum = self.denum * other.denum
    new_num = (self.num * other.denum) - (other.num * self.denum)
    new_denum = common_denum
    result_fraction = Fraction(new_num, new_denum)
    result_fraction.change()  
    return f"{result_fraction.num}/{result_fraction.denum}"
  
  def __iadd__ (self,other):
    common_denum = self.denum * other.denum
    self.num = int((self.num * other.denum) + (other.num * self.denum))
    self.denum = int((common_denum))
    Fraction.change(self)
    return self
  
  def __isub__ (self,other):
    common_denum = self.denum * other.denum
    self.num = int((self.num * other.denum) - (other.num * self.denum))
    self.denum = int((common_denum))
    Fraction.change(self)
    return self
  
  def __mul__(self,other):
    new_num = (self.num * other.num) 
    new_denum = (other.denum * self.denum)
    result_fraction = Fraction(new_num, new_denum)
    result_fraction.change()  
    return f"{result_fraction.num}/{result_fraction.denum}"
  
  def __truediv__(self,other):
    new_num = (self.num * other.denum) 
    new_denum = (other.num * self.denum)
    result_fraction = Fraction(new_num, new_denum)
    result_fraction.change()  
    return f"{result_fraction.num}/{result_fraction.denum}"

  def __imul__(self,other):
    self.num = (self.num * other.num) 
    self.denum = (other.denum * self.denum)
    Fraction.change(self) 
    return self
  
  def __itruediv__(self,other):
    self.num = (self.num * other.denum) 
    self.denum = (other.num * self.denum)
    Fraction.change(self) 
    return self
  
  def reverse(selt):
     selt.num = selt.denum
     selt.denum = selt.num
     return selt
  
  def __lt__(self,other):
    return (self.num / self.denum) < (other.num / other.denum)
  
  def __gt__(self,other):
    return (self.num / self.denum) > (other.num / other.denum)
  
  def __le__(self,other):
    return (self.num / self.denum) <= (other.num / other.denum)
  
  def __ge__(self,other):
    return (self.num / self.denum) >= (other.num / other.denum)
  
  def __eq__(self,other):
   return (self.num / self.denum) == (other.num / other.denum) 
  
  def __ne__(self,other):
    return (self.num / self.denum) != (other.num / other.denum) 
  

  

     
a = Fraction(1)
b = Fraction('2')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)


