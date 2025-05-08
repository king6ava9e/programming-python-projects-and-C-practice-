# water_flow.py

# Constants
WATER_DENSITY = 998.2  # kg/m^3
GRAVITY = 9.80665  # m/s^2
WATER_VISCOSITY = 0.001001  # Pa·s

def water_column_height(tower_height, tank_height):
    """Calculates the height of a column of water in a tank."""
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    """Calculates the pressure gain from the height of water in a tank."""
    return (WATER_DENSITY * GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates pressure loss due to pipe friction."""
    return - (friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fitting_count, fluid_velocity):
    """Calculates pressure loss due to pipe fittings."""
    K = 0.04  # Typical loss coefficient per fitting
    return - (K * fitting_count * WATER_DENSITY * fluid_velocity**2) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculates the Reynolds number to determine flow type."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, smaller_diameter, fluid_velocity):
    """Calculates pressure loss due to pipe size reduction."""
    return - ((0.5 * WATER_DENSITY * fluid_velocity**2) * ((1 - (smaller_diameter / larger_diameter) ** 4)) / 1000)

def kpa_to_psi(kpa):
    """Converts kilopascals (kPa) to pounds per square inch (psi)."""
    return kpa * 0.145038

def main():
    """Gets input from the user, calls functions, and prints results."""
    print("Water Flow System Calculator")

    tower_height = float(input("Enter tower height (m): "))
    tank_height = float(input("Enter tank height (m): "))
    height = water_column_height(tower_height, tank_height)
    print(f"Water Column Height: {height:.2f} m")

    pressure = pressure_gain_from_water_height(height)
    print(f"Pressure Gain from Water Height: {pressure:.2f} kPa ({kpa_to_psi(pressure):.2f} psi)")

    pipe_diameter = float(input("Enter pipe diameter (m): "))
    pipe_length = float(input("Enter pipe length (m): "))
    friction_factor = float(input("Enter pipe friction factor: "))
    fluid_velocity = float(input("Enter fluid velocity (m/s): "))

    pressure_loss_pipe = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity)
    print(f"Pressure Loss from Pipe: {pressure_loss_pipe:.2f} kPa")

    fitting_count = int(input("Enter number of fittings: "))
    pressure_loss_fittings = pressure_loss_from_fittings(fitting_count, fluid_velocity)
    print(f"Pressure Loss from Fittings: {pressure_loss_fittings:.2f} kPa")

    hydraulic_diameter = pipe_diameter  # Assuming it's the same as pipe diameter
    reynolds = reynolds_number(hydraulic_diameter, fluid_velocity)
    print(f"Reynolds Number: {reynolds:.2f}")

    larger_diameter = float(input("Enter larger pipe diameter (m): "))
    smaller_diameter = float(input("Enter smaller pipe diameter (m): "))
    pressure_loss_reduction = pressure_loss_from_pipe_reduction(larger_diameter, smaller_diameter, fluid_velocity)
    print(f"Pressure Loss from Pipe Reduction: {pressure_loss_reduction:.2f} kPa")

if __name__ == "__main__":
    main()
