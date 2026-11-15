import streamlit as st
import math

# --- Page Configuration ---
st.set_page_config(page_title="Advanced ESD Flooring Estimator", layout="wide")
st.title("Smart Infrastructure Calculator 🌌")
st.markdown("Precision tool for ESD flooring requirements: Earth Laboratories vs. Lunar Habitats.")

# --- Sidebar Inputs ---
st.sidebar.header("Input Parameters")

environment = st.sidebar.radio(
    "Select Operating Environment:",
    ["Earth Lab (Butyl Rubber + Biochar + Bronze)", "Lunar Habitat (Ceramic + Silicone + Mylar + Graphene)"]
)

target_area = st.sidebar.number_input("Target Total Area (sq meters)", min_value=1.0, value=90.0)
base_side_mm = st.sidebar.slider("Base Geometric Side Length (mm)", 50, 500, 150)

st.divider()

# --- Geometry Calculations (Pythagoras & Thales Principles) ---
# Hexagonal/Star pattern base area calculation using trigonometric ratios
area_per_piece_sqm = (3 * math.sqrt(3) / 2 * (base_side_mm / 1000)**2)

# Calculate total pieces required (rounded up for full coverage)
total_pieces = math.ceil(target_area / area_per_piece_sqm)
actual_covered_area = total_pieces * area_per_piece_sqm

# --- Material Quantities & Cost Estimations ---
if "Earth" in environment:
    # Earth Laboratory calculations
    base_material_qty = total_pieces * 0.85  # kg of Butyl + Biochar per piece
    joints_qty = total_pieces * 3            # Bronze joints count
    
    material_name = "Butyl Rubber & Biochar Mixture"
    joint_name = "Bronze Grounding Joints"
    joint_unit = "joints"
    
    # Earth Cost Estimation (USD)
    material_cost = base_material_qty * 5.0
    joints_cost = joints_qty * 1.5
    labor_and_install = target_area * 20.0
    total_estimated_cost = material_cost + joints_cost + labor_and_install
    
    cost_breakdown = f"""
    * **Base Material (Butyl+Biochar):** ${material_cost:,.2f} (approx. $5/kg)
    * **Grounding Joints (Bronze):** ${joints_cost:,.2f} (approx. $1.5/joint)
    * **Labor & Installation:** ${labor_and_install:,.2f} (approx. $20/m²)
    """
else:
    # Lunar Habitat calculations
    base_material_qty = total_pieces * 1.2   # kg of Ceramic/Mylar per piece
    joints_qty = actual_covered_area * 2.5   # grams of ISRU Graphene + Silicone
    
    material_name = "Ceramic, Silicone & Mylar Composite"
    joint_name = "Graphene Network (ISRU)"
    joint_unit = "grams"
    
    # Lunar Cost Estimation (USD)
    material_cost = base_material_qty * 150.0 
    shipping_cost = base_material_qty * 10000.0  # High shipping cost from Earth
    graphene_isru_cost = joints_qty * 0.10       # Ultra-low cost due to local ISRU production
    
    total_estimated_cost = material_cost + shipping_cost + graphene_isru_cost
    
    cost_breakdown = f"""
    * **Lunar Materials (Ceramic/Mylar):** ${material_cost:,.2f}
    * **Graphene (Local ISRU Production):** ${graphene_isru_cost:,.2f} (Massive savings vs shipping!)
    * **Earth-to-Moon Payload Shipping:** ${shipping_cost:,.2f} (approx. $10,000/kg)
    *💡 *Note: Utilizing ISRU (In-Situ Resource Utilization) for Graphene drasically reduces aerospace logistics costs.*
    """

# --- Dashboard Output ---
st.header("Final Output & Estimation")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📏 Area Coverage")
    st.metric(label="Actual Covered Area", value=f"{actual_covered_area:.2f} m²")
    st.caption(f"Initial Target: {target_area} m²")

with col2:
    st.success("🧩 Geometry Units")
    st.metric(label="Total Pieces Required", value=f"{total_pieces:,}")
    st.caption(f"Geometric Side: {base_side_mm} mm")

with col3:
    st.warning("⚖️ Material Requirements")
    st.metric(label=material_name, value=f"{base_material_qty:.2f} kg")
    st.metric(label=joint_name, value=f"{joints_qty:.2f} {joint_unit}")

st.subheader("💰 Cost Estimation & Feasibility")
col_cost1, col_cost2 = st.columns([1, 2])

with col_cost1:
    st.metric(
        label="Total Estimated Cost (USD)", 
        value=f"${total_estimated_cost:,.2f}"
    )
    
with col_cost2:
    st.markdown(f"**Cost Breakdown for {target_area} m²:**")
    st.markdown(cost_breakdown)
