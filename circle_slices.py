import math

def compute_slices_and_remaining_area():
 
    diameter = 10.0
    radius = diameter / 2.0
    circle_area = math.pi * (radius ** 2)

    # Generate slices
    slices = []
    slice_value = 10.0
    total_angle = 0.0

    while total_angle + slice_value <= 360.0:
        slices.append(slice_value)
        total_angle += slice_value
        slice_value *= 1.22

    total_slices = len(slices)

    # Sum the area of every 4th slice
    removed_area = 0.0
    for i, angle in enumerate(slices, start=1):
        if i % 4 == 0:  # remove every 4th slice
            removed_area += (angle / 360.0) * circle_area

    # Remaining area after removing every 4th slice
    area_remaining = circle_area - removed_area
    
    print(f"Circle area: {circle_area}")
    print(f"Total number of slices: {total_slices}")
    print(f"Remaining area after removing every 4th slice: {round(area_remaining)} square inches")

    return total_slices, round(area_remaining)

if __name__ == "__main__":
    compute_slices_and_remaining_area()

