class EmpleadorClass: 
    def __init__(self,fullname,salary,id_employee,job):
        self.fullname = fullname
        self.salary = salary
        self.id_employee = id_employee
        self.job = job
        
        ##getter method##
        ##es un metodo publido que me devuelve un dato privado /protegido##
        
        def getFullname(self):
            return self.fullname
        
        def getSalary(self):
            return self.salary
        
        def getId_employee(self):
            return self.id_employee
        
        def getJob(self):
            return self.job  
        
        ##iniciacion de los "metodos" set #
        def setFullname(self,newFullname):
            self.fullname = newFullname
            
        def getSalary(self,newSalary):
            self.salary = newSalary
            
        def setId_employee(self,newId_employee):
            self.id_employee = newId_employee
            
        def setJob(self,newJob):
                self.job = newJob
        
                 