import csv
with open('insurance.csv', newline='') as csvfile:
    reader =csv.DictReader(csvfile)
    for row in reader:
        ages = []
        sexes = []
        bmis = []
        num_children = []
        smoker_statuses = []
        regions = []
        insurance_charges = []
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    def __init__(self, patient_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_insurance_charges):
        self.patients_ages = patient_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_insurance_charges

    def analyze_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return ("Average Patient Age: " + str(round(total_age/len(self.patients_ages), 2)) + " years")

    def analyze_sexes(self):

        females = 0
        males = 0
        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            elif sex == 'male':
                males +=  1
        print("Number of females: ", females)
        print("Number of males: ", males)

    def unique_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions:
                unique_regions.append(region)
        return unique_regions

    def average_charges(self):
        total_charges = 0
        for charge in self.patients_charges:
            total_charges = float(charge)
        return ("Average Yearly Medical Insurance Charges: " +
                str(round(total_charges/len(self.patients_charges), 2)) + " dollars.")

    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary['age'] = [int(age) for age in self.patients_ages]
        self.patients_dictionary['sexes'] = self.patients_sexes
        self.patients_dictionary['bmi'] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary['smoker'] = self.patients_smoker_statuses
        self.patients_dictionary['regions'] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary

patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

patient_info.analyze_ages()

patient_info.analyze_sexes()

patient_info.unique_regions()

patient_info.average_charges()

patient_info.create_dictionary()
