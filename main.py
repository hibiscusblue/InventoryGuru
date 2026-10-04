print("INVENTORYMIND")
print("Simple answers. Clear actions.")
print()

# Get inventory information
sku = input("SKU: ")
system_quantity = int(input("System quantity: "))
counted_quantity = int(input("Counted quantity: "))

# Calculate the difference
difference = counted_quantity - system_quantity

print()

# Check the inventory
if difference < 0:
    print("STOCK SHORTAGE")
    print("Missing:", abs(difference))
    print()

    # Ask until the user enters yes or no
    while True:
        counted_again = input(
            "Did you count again? (Y/N): "
        ).strip().upper()

        if counted_again == "Y":
            print("Good. Continue to the next check.")
            break

        elif counted_again == "N":
            print("Count the stock again first.")
            break

        else:
            print("I don't understand. Please enter Y or N.")
            print()

elif difference > 0:
    print("STOCK OVERAGE")
    print("Extra:", difference)

else:
    print("STOCK OK")