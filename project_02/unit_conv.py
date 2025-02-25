import streamlit as st

# 🛠 Function to convert length and weight
def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

# 🔥 Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    return None

# 📏 Length conversion dictionary
length_conversion = {
    "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
    "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
}

# ⚖ Weight conversion dictionary
weight_conversion = {
    "Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274
}

# 🎨 Streamlit UI
st.set_page_config(page_title="Unit Converter", page_icon="⚖", layout="wide")
st.title("🛠 Unit Converter App")
st.write("### Made by Hammad 🚀")

# 📌 Sidebar for Navigation
st.sidebar.header("⚙️ Select Conversion Type")
unit_type = st.sidebar.radio("Choose unit type", ["Length", "Weight", "Temperature"])

# 🔹 Main Section
col1, col2 = st.columns([2, 3])

with col1:
    st.header("Input Values")
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

    if unit_type == "Length":
        from_unit = st.selectbox("From", list(length_conversion.keys()))
        to_unit = st.selectbox("To", list(length_conversion.keys()))
    elif unit_type == "Weight":
        from_unit = st.selectbox("From", list(weight_conversion.keys()))
        to_unit = st.selectbox("To", list(weight_conversion.keys()))
    elif unit_type == "Temperature":
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    convert_button = st.button("Convert")

with col2:
    st.header("Conversion Result")
    if convert_button:
        if unit_type == "Length":
            result = convert_units(value, from_unit, to_unit, length_conversion)
        elif unit_type == "Weight":
            result = convert_units(value, from_unit, to_unit, weight_conversion)
        elif unit_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.error("Invalid conversion!")
