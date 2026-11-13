import math

class GlassFactorySimulator:
    def __init__(self):
        # 85% of stabilized dry regolith can be fused into usable lunar glass
        self.regolith_to_glass_ratio = 0.85 
        self.melting_point_c = 1700 # Quartz/Glass melting point
        self.solar_concentration_efficiency = 0.75 # Passive solar concentrator efficiency

    def calculate_yield(self, dry_regolith_kg):
        """Calculates the mass of glass blocks produced from dry regolith."""
        return dry_regolith_kg * self.regolith_to_glass_ratio

    def calculate_solar_energy_required(self, mass_kg):
        """Calculates solar energy needed to melt the regolith using ISRU thermal dynamics."""
        specific_heat = 800 # J/(kg*K) approximate for regolith
        delta_t = self.melting_point_c - (-150) # Assuming ambient lunar PSR temp of -150C
        energy_joules = mass_kg * specific_heat * delta_t
        energy_kwh = energy_joules / 3.6e6
        return energy_kwh / self.solar_concentration_efficiency

    def run_simulation(self, daily_regolith_input):
        print("==================================================")
        print("🌖 SIFI LUNAR GLASS FACTORY SIMULATION (Flashcube 110)")
        print("==================================================")
        print(f"[INPUT] Stabilized Dry Regolith: {daily_regolith_input} kg")
        
        output_glass = self.calculate_yield(daily_regolith_input)
        energy_req = self.calculate_solar_energy_required(daily_regolith_input)
        
        print(f"[OUTPUT] High-Purity Glass Blocks: {output_glass:.2f} kg")
        print(f"[ENERGY] Passive Solar Thermal Required: {energy_req:.2f} kWh")
        print("[STATUS] Ready for habitat construction & radiation shielding.")
        print("==================================================")
        return output_glass

if __name__ == "__main__":
    # Test simulation with 1000 kg of daily dry regolith tailings
    sim = GlassFactorySimulator()
    sim.run_simulation(1000)
