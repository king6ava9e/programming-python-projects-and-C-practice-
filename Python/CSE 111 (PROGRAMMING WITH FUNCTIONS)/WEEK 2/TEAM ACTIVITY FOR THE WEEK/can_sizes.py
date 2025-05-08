import math

def compute_volume(radius, height):
    """Calculate the volume of a cylinder."""
    return math.pi * radius**2 * height

def compute_surface_area(radius, height):
    """Calculate the surface area of a cylinder."""
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume, surface_area):
    """Calculate the storage efficiency of a can."""
    return volume / surface_area

def main():
    """Compute and print the storage efficiency of each can size."""
    cans = [
        ("#1 Picnic", 6.83, 10.16),
        ("#1 Tall", 7.78, 11.91),
        ("#2", 8.73, 11.59),
        ("#2.5", 10.32, 11.91),
        ("#3 Cylinder", 10.79, 17.78),
        ("#5", 13.02, 14.29),
        ("#6Z", 5.40, 8.89),
        ("#8Z short", 6.83, 7.62),
        ("#10", 15.72, 17.78),
        ("#211", 6.83, 12.38),
        ("#300", 7.62, 11.27),
        ("#303", 8.10, 11.11),
    ]

    for name, radius, height in cans:
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        efficiency = compute_storage_efficiency(volume, surface_area)

        # Print the name and storage efficiency only, formatted to 2 decimal places
        print(f"{name} {efficiency:.2f}")

# Run the program
main()