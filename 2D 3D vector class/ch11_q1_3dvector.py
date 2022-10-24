class c2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
class c3dvec(c2dvec):    
    def __init__(self,i,j,k):
       super().__init__(i,j)    
       self.kcap=k
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"
c2=c2dvec(1,2)
c3=c3dvec(2,3,4)
print(c2)
print(c3)