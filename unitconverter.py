import streamlit as st

# Title of the application
st.title('Unit Converter')

# Conversion functions
def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def miles_to_kilometers(miles):
    return miles * 1.60934

def kilometers_to_miles(kilometers):
    return kilometers / 1.60934

# Sidebar menu for unit selection
unit_option = st.sidebar.selectbox(
    'Select unit to convert:',
    ('Meters', 'Kilometers', 'Feet', 'Miles')
)

# Input field for user to enter value to convert
input_value = st.number_input(f'Enter value in {unit_option.lower()}')

# Initialize variable to store converted value
converted_value = 0.0

# Convert based on selected unit
if unit_option == 'Meters':
    st.write('### Conversion Result:')
    st.write(f'{input_value} meters = {meters_to_kilometers(input_value)} kilometers')
    st.write(f'{input_value} meters = {meters_to_feet(input_value)} feet')

elif unit_option == 'Kilometers':
    st.write('### Conversion Result:')
    st.write(f'{input_value} kilometers = {kilometers_to_meters(input_value)} meters')
    st.write(f'{input_value} kilometers = {kilometers_to_miles(input_value)} miles')

elif unit_option == 'Feet':
    st.write('### Conversion Result:')
    st.write(f'{input_value} feet = {feet_to_meters(input_value)} meters')

elif unit_option == 'Miles':
    st.write('### Conversion Result:')
    st.write(f'{input_value} miles = {miles_to_kilometers(input_value)} kilometers')

