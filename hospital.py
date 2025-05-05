print("Welcome to the Medical Diagnosis Expert System!")

# Collect symptoms from user
fever = input("Do you have a fever? (yes/no): ").lower()
cough = input("Do you have a cough? (yes/no): ").lower()
headache = input("Do you have a headache? (yes/no): ").lower()
fatigue = input("Do you feel tired or fatigued? (yes/no): ").lower()
rash = input("Do you have a skin rash? (yes/no): ").lower()

# Rule-based diagnosis
if fever == "yes" and cough == "yes" and fatigue == "yes":
    diagnosis = "You may have the flu."
elif fever == "yes" and headache == "yes" and rash == "yes":
    diagnosis = "You may have dengue fever."
elif cough == "yes" and headache == "yes" and fever == "no":
    diagnosis = "You may have a common cold."
elif rash == "yes" and fever == "no" and cough == "no":
    diagnosis = "You may have an allergic reaction."
else:
    diagnosis = "Unable to determine illness. Please consult a doctor."

# Output result
print("\nDiagnosis Result:")
print(diagnosis)

# Advice
if "flu" in diagnosis:
    print("Advice: Drink fluids, rest well, and consult a doctor if symptoms worsen.")
elif "dengue" in diagnosis:
    print("Advice: Seek immediate medical attention.")
elif "common cold" in diagnosis:
    print("Advice: Rest, stay hydrated, and take over-the-counter medicines.")
elif "allergic" in diagnosis:
    print("Advice: Avoid allergen exposure and consider antihistamines.")
else:
    print("Advice: Please visit a healthcare facility for a proper diagnosis.")

