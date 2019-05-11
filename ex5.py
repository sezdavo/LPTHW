# initial variables
name = 'Eliot Serrano-Davey'
age = 21
height_in = 70.0 # inches
weight_kg = 76.0 # kg
eyes = 'Green'
teeth = 'Yellow'
hair = 'Brown'
# conversion variables to 2dp
height_cm = round(height_in * 2.54, 2)
weight_lb = round(weight_kg * 2.2, 2)
#print discussion
print(f"Let's talk about {name}.")
print(f"He's {height_in} inches tall or {height_cm} centimeters tall.")
print(f"He's {weight_kg} kilograms heavy or {weight_lb} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the smoking.")
# defining totals for metric and imperial measurements
total_metric = age + height_cm + weight_kg
total_imperial = age + height_in + weight_lb
#printing different totals for metric and imperial
print(f"Imperial: If I add {age}, {height_in}, and {weight_lb} I get {total_imperial}.")
print(f"Metric: If I add {age}, {height_cm}, and {weight_kg} I get {total_metric}.")
