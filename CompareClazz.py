'''
    This examples shows the hospital domain where wards and patients. Dynamically
    wards can be filled by patients.
    Used the total_ordering decorator and __eq__ and __lt__ minimum requirments
    to implement the comparisons for the ==, >=, <=  and so on.
'''
from functools import total_ordering

class Patient(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

@total_ordering
class Ward(object):
    def __init__(self, ward_no):
        self.ward_no = ward_no
        self.patients = list()

    def add_patient(self, patient):
        self.patients.append(patient)

    def __str__(self):
        return 'Ward {} has {} patients'.format(self.ward_no, len(self.patients))

    #current capacity is decide by the number of patients in the ward
    @property
    def capacity(self):
        return len(self.patients)

    #minimum required functions
    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

# This is ward no# 1
ward_1 = Ward(1)
ward_1.add_patient(Patient('A',25)) # add patients to wards
ward_1.add_patient(Patient('B',26))
ward_1.add_patient(Patient('C',27))
ward_1.add_patient(Patient('D',28))

# ward no# 2
ward_2 = Ward(2)
ward_2.add_patient(Patient('X',25)) # add patients to wards
ward_2.add_patient(Patient('Y',26))
ward_2.add_patient(Patient('Z',27))

# As you see you can do all the comparisons
ward_1 < ward_2 # False
ward_1 <= ward_2 # False
ward_1 == ward_2 # False
ward_1 >= ward_2 # True
ward_1 > ward_2 # True
