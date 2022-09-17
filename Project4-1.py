# Programmer Name : Ani Ohanian
# Date: 8/13/22
# Description: This Program computes and displays the charges for a patient’s hospital stay.
# First, the program should ask if the patient was admitted as an in-patient or an out-patient. 

# If the patient was an in-patient the following data should be entered:
# • The number of days spent in the hospital
# • The daily rate
# • Charges for hospital services (lab tests, etc.)
# • Hospital medication charges.

# If the patient was an out-patient the following data should be entered:
# • Charges for hospital services (lab tests, etc.)
# • Hospital medication charges.

# Use a single, separate function to validate that no input is less than zero. 
# If it is, it should be re-entered before being returned.
# Once the required data has been input and validated, the program should use two
# separate functions to calculate the total charges. One of the functions should accept
# arguments for the in-patient data, while the other function accepts arguments for out-
# patient data. Both functions should return the total charges.



# this function calculates the patients charges 
def totalChargesInPatient(Days, Rate, ServiceCharges, MedicationCharges):
    inPatientTotalCharges = (Days*Rate)+ ServiceCharges + MedicationCharges 
    return inPatientTotalCharges

# this function calculates the out-patient charges
def totalChargesOutPatient(ServicesCharges, MedicationCharges):
    outPatientTotalCharges = ServicesCharges + MedicationCharges
    return outPatientTotalCharges

# this function validates negative user input 
def validateInput(userInput):
    if userInput < 0:
        print("Please re-enter the number.")
        return False
    else:
        return True
    
# this function validates user input for integer 
def getAndValidateInputForInt(inputString):
    while(True):
        userInput = int(input(inputString))
        if (validateInput(userInput)):
            return userInput

# this function validates user input for float
def getAndValidateInputForFloat(inputString):
    while(True):
        userInput = float(input(inputString))
        if (validateInput(userInput)):
            return userInput

# to keep the program running until the user enters the correct input
toContinue = True
while(toContinue):
    try:
        patientAdmission = input("Please enter if the patient is in-patient or out-patient? ").lower()
        # to check user input for in-patient
        if patientAdmission == "in-patient":
            # calling functions to get data for in-patient admission
            numberOfDays = getAndValidateInputForInt("Please enter the number of days spent in the hospital: ")
            dailyRate = getAndValidateInputForFloat("Please enter daily rate: $")
            inPatientHospitalServiceCharges = getAndValidateInputForFloat("Please enter charges for hospital services (lab tests, etc.): $")
            inPatientHospitalMedicationCharges = getAndValidateInputForFloat("Please enter hospital medication charges: $")

            # calculating total charges
            inPatientHospitalCharge = totalChargesInPatient(numberOfDays, dailyRate, inPatientHospitalServiceCharges, inPatientHospitalMedicationCharges)
            print("In-patient total charges is:" , inPatientHospitalCharge)
            toContinue = False
        # to check user input for out-patient
        elif patientAdmission == "out-patient":

            # calling functions to get data for out-patient admission
            outPatientHospitalServicesCharges = getAndValidateInputForFloat("Please enter charges for hospital services (lab tests, etc.): $")
            outPatientHospitalMedicationCharges = getAndValidateInputForFloat("Please enter hospital medication charges: $")
            
            # calculating total charges
            outPatientHospitalCharge = totalChargesOutPatient(outPatientHospitalServicesCharges,outPatientHospitalMedicationCharges)
            print("Out-patient total charges is: " , outPatientHospitalCharge)
            toContinue = False
        else:
            print("Wrong input")
    except:
        print("Wrong input")
