import streamlit as st
from math import pi, sqrt

def Resonance(R, L, C):
    FR = 1 / (2 * pi * sqrt(L * C)) 
    BW = R / (2 * pi * L)           
    Q = FR / BW                    
    FL = FR - (BW / 2)             
    FU = FR + (BW / 2)             
    return FR, BW, Q, FL, FU

st.title("2205A21015-PS3")

st.write("Calculate the resonance frequency,bandwidt,quality factor,upper cutoff frequency,and lower cut off frequency based on R,L,and C values for series resonance circuit")

R = st.number_input("Resistance (R) in Ω:",value=1)
L = st.number_input("Inductance (L) in H:",value=1)
C = st.number_input("Capacitance (C) in F:",value=1)

if st.button("Calculate"):
    if L > 0 and C > 0:
        FR, BW, Q, FL, FU = Resonance(R, L, C)
        st.write(f"Resonance Frequency (FR): {FR:.2f} Hz")
        st.write(f"Bandwidth (BW): {BW:.2f} Hz")
        st.write(f"Quality Factor (Q): {Q:.2f}")
        st.write(f"Lower Cutoff Frequency (FL): {FL:.2f} Hz")
        st.write(f"Upper Cutoff Frequency (FU): {FU:.2f} Hz")
    else:
        st.write("L and C values must be greater than 0.")