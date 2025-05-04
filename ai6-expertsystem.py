def medical_expert_system():
    print("Welcome to the Smart Health Diagnosis System!")
    
    # Getting the patient's basic info
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    preexisting_conditions = input("Do you have any pre-existing conditions like diabetes, hypertension, asthma? (yes/no): ").lower()

    # Asking about symptoms
    print("\nPlease answer with 'yes' or 'no'.")
    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    fatigue = input("Do you feel tired or have body aches? ").lower()
    sneezing = input("Are you sneezing frequently? ").lower()
    sore_throat = input("Do you have a sore throat? ").lower()
    breath = input("Do you feel shortness of breath? ").lower()
    taste_smell_loss = input("Have you lost your sense of taste or smell? ").lower()
    headache = input("Do you have a headache? ").lower()
    chest_pain = input("Are you experiencing chest pain or tightness? ").lower()
    loss_of_appetite = input("Have you experienced a loss of appetite? ").lower()

    score = 0

    # Scoring logic (more nuanced symptoms)
    symptoms = [fever, cough, fatigue, sneezing, sore_throat, breath, taste_smell_loss, headache, chest_pain, loss_of_appetite]
    for s in symptoms:
        if s == "yes":
            score += 1

    # Diagnosis logic with more conditions
    if score >= 7 and taste_smell_loss == "yes" and breath == "yes":
        diagnosis = "Likely COVID-19"
        advice = "Isolate immediately and consult a doctor. Testing is highly recommended."
    elif fever == "yes" and cough == "yes" and fatigue == "yes" and chest_pain == "yes":
        diagnosis = "Likely Heart-related Issues"
        advice = "Seek immediate medical attention. Chest pain with fatigue and cough is concerning."
    elif fever == "yes" and cough == "yes" and fatigue == "yes":
        diagnosis = "Likely Influenza (Flu)"
        advice = "Take rest, stay hydrated, and monitor temperature. See a doctor if symptoms worsen."
    elif sneezing == "yes" and sore_throat == "yes" and fever == "no":
        diagnosis = "Likely Seasonal Allergies"
        advice = "Avoid allergens, use antihistamines if needed, and stay indoors."
    elif sore_throat == "yes" and cough == "yes" and fever == "no":
        diagnosis = "Likely Common Cold"
        advice = "Warm fluids, rest, and over-the-counter meds can help."
    elif fever == "yes" and sore_throat == "yes" and headache == "yes":
        diagnosis = "Likely Strep Throat"
        advice = "Consult a doctor for a throat culture test. Antibiotics may be needed."
    elif chest_pain == "yes" and breath == "yes":
        diagnosis = "Possible Heart Condition"
        advice = "Chest pain and shortness of breath require immediate medical evaluation."
    else:
        diagnosis = "Unable to determine"
        advice = "Consult a medical professional for proper diagnosis."

    # Severity level
    if score <= 2:
        severity = "Mild"
    elif score <= 4:
        severity = "Moderate"
    else:
        severity = "Severe"

    # Age risk check with pre-existing conditions
    risk_note = ""
    if age >= 60 and score >= 3:
        risk_note = "High-risk age group. Immediate medical attention recommended."
    if preexisting_conditions == "yes":
        risk_note += " Pre-existing conditions detected. Please consult your doctor immediately."

    # Final result
    print(f"\n Patient: {name}")
    print(f"Age: {age} | Symptom Severity: {severity}")
    print(f"\n Diagnosis: {diagnosis}")
    print(f" Advice: {advice}")
    if risk_note:
        print(risk_note)

# Run the system
medical_expert_system()
