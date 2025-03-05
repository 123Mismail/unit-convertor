import streamlit as st

# Categories and units
units = {
    "Length": {
        "Meter (m)": 1,
        "Kilometer (km)": 1000,
        "Centimeter (cm)": 0.01,
        "Millimeter (mm)": 0.001,
        "Mile (mi)": 1609.34,
        "Yard (yd)": 0.9144,
        "Foot (ft)": 0.3048,
        "Inch (in)": 0.0254
    },
    "Mass": {
        "Kilogram (kg)": 1,
        "Gram (g)": 0.001,
        "Milligram (mg)": 0.000001,
        "Pound (lb)": 0.453592,
        "Ounce (oz)": 0.0283495
    },
    "Temperature": {
        "Celsius (°C)": "C",
        "Fahrenheit (°F)": "F",
        "Kelvin (K)": "K"
    },
    "Time": {
        "Second (s)": 1,
        "Minute (min)": 60,
        "Hour (h)": 3600,
        "Day (d)": 86400
    },
    "Speed": {
        "Meter/second (m/s)": 1,
        "Kilometer/hour (km/h)": 0.277778,
        "Mile/hour (mph)": 0.44704,
        "Foot/second (ft/s)": 0.3048
    }
}

# Page config
st.set_page_config(page_title="Universal Unit Converter", page_icon="🛠️", layout="centered")

# Inject custom CSS for unique glassmorphism styling
st.markdown("""
    <style>
        .glass {
            background: rgba(255, 255, 255, 0.25);
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        }
        .history-item {
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <h1 style='text-align: center; color: #6A5ACD;'>✨ Universal Unit Converter ✨</h1>
    <p style='text-align: center;'>Convert units effortlessly with style, and track your recent conversions!</p>
""", unsafe_allow_html=True)

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Category selection
category = st.selectbox("📂 Choose Category:", list(units.keys()))

# Unit selections
col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("🔻 From:", list(units[category].keys()))
with col2:
    unit_to = st.selectbox("🔺 To:", list(units[category].keys()))

# Input value
value = st.number_input("✏️ Enter value to convert:", min_value=0.0)

# Temperature conversion logic
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "C":
        return (value * 9/5 + 32) if to_unit == "F" else value + 273.15
    if from_unit == "F":
        return (value - 32) * 5/9 if to_unit == "C" else (value - 32) * 5/9 + 273.15
    if from_unit == "K":
        return value - 273.15 if to_unit == "C" else (value - 273.15) * 9/5 + 32

# Conversion action
if st.button("🚀 Convert"):
    if category == "Temperature":
        from_symbol = units[category][unit_from]
        to_symbol = units[category][unit_to]
        result = convert_temperature(value, from_symbol, to_symbol)
    else:
        result = value * (units[category][unit_from] / units[category][unit_to])
    
    # Store result in history (limit 5 items)
    st.session_state.history.insert(0, f"{value} {unit_from} ➡️ {result:.4f} {unit_to}")
    if len(st.session_state.history) > 5:
        st.session_state.history.pop()

    # Display result with glass effect
    st.markdown(f"""
        <div class="glass">
            <h2 style='color: #483D8B;'>✅ Result</h2>
            <h3 style='color: #4B0082;'>{value} {unit_from} = {result:.4f} {unit_to}</h3>
        </div>
    """, unsafe_allow_html=True)

# Display recent history
if st.session_state.history:
    st.markdown("""
        <div class="glass">
            <h3 style='color: #6A5ACD;'>🕒 Recent Conversions</h3>
    """, unsafe_allow_html=True)

    for item in st.session_state.history:
        st.markdown(f"<div class='history-item'>{item}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
