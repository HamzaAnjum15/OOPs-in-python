class employee:
    salary=30000
    increment=1.5
    @property
    def salaryafterincrement(self):
        return self.salary*self.increment
    @salaryafterincrement.setter
    def salaryafterincrement(self, sai):
        self.increment=sai/self.salary
e = employee()
print(e.salaryafterincrement)
e.salaryafterincrement=50000
print(e.increment)
