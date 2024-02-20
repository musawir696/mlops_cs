class mlops:
    def _init_(self,totalStudents):
        self.totalSTudents=totalStudents
        
    def getTotalStudents(self):
        return self.totalSTudents
    
    def addStudents(self):
         self.totalSTudents=self.totalSTudents+1
    
    def removeStudent(self):
        self.totalSTudents=self.totalSTudents-1
        
    def getClassName(self):
        return "Machine learning Operations CS-B"    
    
mlops_class=mlops()
mlops_class.addStudents()
mlops_class.removeStudent()
print(mlops_class.getTotalStudents())
print(mlops_class.getClassName())

