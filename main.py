def show_stock_status(difference):
    if difference < 0:
        print("STOCK SHORTAGE")
        print("Missing:", abs(difference))

    elif difference > 0:
        print("STOCK OVERAGE")
        print("Extra:", difference)

    else:
        print("STOCK OK")


print("INVENTORYMIND")
print("Simple answers. Clear actions.")
print()

sku = input("SKU: ")
system_quantity = int(input("System quantity: "))
counted_quantity = int(input("Counted quantity: "))

difference = counted_quantity - system_quantity

print()
show_stock_status(difference)


if difference < 0:
    print()

    while True:
        counted_again = input("Counted again? (Y/N): ").strip().upper()

        if counted_again == "Y":
            print("Continue to the next check.")
            break

        elif counted_again == "N":
            print()
            print("Count the stock again.")

            counted_quantity = int(input("New count: "))
            difference = counted_quantity - system_quantity

            print()
            show_stock_status(difference)
            break

        else:
            print("Enter Y or N.")