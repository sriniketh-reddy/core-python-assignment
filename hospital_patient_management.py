class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def get_patients_of_disease(self,disease):
        return [patient.get_name() for patient in self.patients if patient.get_disease() == disease]
    
class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def get_disease(self): 
        return self.disease
    
    def get_name(self):
        return self.name
    

n = int(input("Enter the number of Patients: "))

hospital = Hospital()

for i in range(n):
    name=input("\n\tEnter Name: ")
    age=int(input("\tEnter Age: "))
    disease=input("\tEnter Disease: ")
    patient = Patient(name, age, disease)
    hospital.add_patient(patient)

disease = input("\nEnter the Disease for which you want to get Patients: ")
patients_with_disease=hospital.get_patients_of_disease(disease)

if patients_with_disease:
    print("\nPatients with", disease, "are:",patients_with_disease)
else:
    print("\nNo patients found with", disease)