import streamlit as st

def calculate_bmi(weight, height_m):
    return weight / (height_m ** 2)

def convert_height_to_meters(feet, inches):
    return (feet * 0.3048) + (inches * 0.0254)

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
feet = st.number_input("Enter your height (feet)", min_value=0, step=1)
inches = st.number_input("Enter your height (inches)", min_value=0, max_value=11, step=1)

if st.button("Calculate BMI"):
    height_m = convert_height_to_meters(feet, inches)
    bmi = calculate_bmi(weight, height_m)
    
    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
