import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Flashcube 110 Dashboard", layout="wide")

st.title("🌖 Flashcube 110: Lunar Pyramid ISRU")
st.subheader("Interactive Financial & Production Dashboard")

# Sidebar for Mission Parameters
st.sidebar.header("⚙️ Mission Parameters")
ice_concentration = st.sidebar.slider("Ice Concentration in Regolith (%)", 1.0, 10.0, 5.0)
daily_excavation_kg = st.sidebar.number_input("Daily Excavation via Micro-Poclain (kg)", value=2500)
water_recovery_rate = st.sidebar.slider("Thermal Recovery Efficiency (%)", 50.0, 99.0, 73.0)

# Core Calculations
daily_water_kg = daily_excavation_kg * (ice_concentration / 100.0) * (water_recovery_rate / 100.0)
annual_water_tons = (daily_water_kg * 365) / 1000

# Space Economics (The $5,000/kg Problem)
capex = 50_000_000  # $50 Million Capital Expenditure
traditional_cost_per_kg = 5000
annual_savings = (annual_water_tons * 1000) * traditional_cost_per_kg
roi_months = (capex / annual_savings) * 12 if annual_savings > 0 else 0
ten_year_savings = (annual_savings * 10) - capex

# Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("💧 Annual Water Yield", f"{annual_water_tons:.1f} Tons")
col2.metric("⏱️ ROI Duration", f"{roi_months:.1f} Months")
col3.metric("💰 10-Year Savings", f"${ten_year_savings / 1e9:.2f} Billion")

st.markdown("---")

# Detailed Breakdown
st.markdown("### 📊 Economic Viability & QHSE Architecture")
st.write(f"- **Capital Expenditure (CAPEX):** ${capex:,} (Includes Dual-Robot Fleet & FJH Reactor)")
st.write(f"- **Operating Cost (OPEX):** Near-Zero (Powered by Passive Solar, Vacuum, and Gravity)")
st.write(f"- **Traditional Earth-to-Moon Hauling Cost:** $5,000 per kg")

st.markdown("### 🛡️ Dual-Use Commercialization")
st.success("The **Aegis ESD puzzle-grid** and **anti-static composite fabric** are ready for immediate terrestrial supply to JPL cleanrooms and hospital MRI facilities, generating immediate commercial revenue.")

st.markdown("### ⚡ Flash Joule Heating (FJH)")
st.info("96 plastic trash bags are processed per cycle via massive electrical capacitor discharge, converting waste instantly into high-purity Graphene for quartz pipe defrosters.")
