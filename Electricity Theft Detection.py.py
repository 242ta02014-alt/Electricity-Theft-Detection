# Electricity Theft Detection
# Easy Python Code

supply_power = float(input("Enter supply power (W): "))
consumer_power = float(input("Enter consumer power (W): "))

# Calculate difference
difference = supply_power - consumer_power

print("\n--- ELECTRICITY THEFT DETECTION ---")
print("Supply Power   :", supply_power, "W")
print("Consumer Power :", consumer_power, "W")
print("Power Difference:", difference, "W")

# Theft detection
if difference > 50:
    print("WARNING: Possible Electricity Theft!")
else:
    print("Status: No Theft Detected")
