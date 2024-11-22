import streamlit as st
st.title("Thevenins theorem - 2205A21068 _____________GANESH AZMEERA________________")  
def calculate(Vth, Rth, RL):
    IL = Vth / (Rth + RL)  
    PL = IL * IL * RL      
    return IL, PL
Vth = st.number_input("Enter Vth (Volts):", value=0.0)
Rth = st.number_input("Enter Rth (Ohms):", value=0.0)
RL = st.number_input("Enter RL (Ohms):", value=0.0)
if st.button("Calculate"):
    IL, PL = calculate(Vth, Rth, RL)
    st.write(f"Load Current (IL): {IL:.4f} A")
    st.write(f"Load Power (PL): {PL:.4f} W")
