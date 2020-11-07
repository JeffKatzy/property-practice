class Employee:
    # class variable
    positions = ['junior level', 'senior level']

    def __init__(self, name, hometown = 'nyc'):
        self.name = name
        self.hometown = hometown

    @property
    def age(self): 
        return self._age

    @age.setter
    def age(self, age): 
        self._age = int(age)







