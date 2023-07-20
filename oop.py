class Employee:
    def __init__(self,n,a,p):
        self.name = n
        self.age = a
        self.position = p

    def greet(f):
        def temp(self):
            print("Welcome to Arbisoft!")
            f(self)
            print("We know you grow yourb knowledge working with us!")
        return temp 

    @greet
    def introduction(self):
        print(f'My name is {self.name}. I am {self.age} years and I am currently working as a {self.position}.')
    
    def get_age(self):
        return self.age
    def set_age(self, a):
        self.age = a

class TeamMember(Employee):
    def __init__(self,n,a,p, project):
        super().__init__(n,a,p)
        self.project = project
    def inform(self):
        print(f"I am {self.name} and I am working on {self.project}")
    
    def introduction(self):
        print("hello world")
    

hassaan = Employee("Hassaan", 20, "Fellow")
hassaan.introduction()
print(f"Hassaan's age is: {hassaan.get_age()}")

hassaan.set_age(21)
print(f"Hassaan's age is: {hassaan.get_age()}")


new_obj = TeamMember("Abu Bakar", 20, "fellow","Workstream")
new_obj.inform()
new_obj.introduction()


