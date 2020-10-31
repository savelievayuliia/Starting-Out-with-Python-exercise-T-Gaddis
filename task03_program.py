INSURANCE_COEFF = 0.8
def insurance():
    object_value = float(input("Enter the object's value: "))
    insurance_value = object_value * INSURANCE_COEFF
    print("The minimum insured amount of the object is: $",format(insurance_value,",.2f"))
insurance()