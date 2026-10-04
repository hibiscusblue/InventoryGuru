# ========================================
# INVENTORYGURU - FUNCTIONS
# ========================================


def get_quantity(question):
    while True:
        try:
            return int(input(question))

        except ValueError:
            print("Enter a number.")


def ask_yes_no(question):
    while True:
        answer = input(question + " (Y/N): ").strip().upper()

        if answer == "Y":
            return True

        elif answer == "N":
            return False

        else:
            print("Enter Y or N.")


def calculate_difference(system_quantity, counted_quantity):
    return counted_quantity - system_quantity


def show_stock_status(difference):
    if difference < 0:
        print("STOCK SHORTAGE")
        print("Missing:", abs(difference))

    elif difference > 0:
        print("STOCK OVERAGE")
        print("Extra:", difference)

    else:
        print("STOCK OK")


# ========================================
# INVENTORYGURU - START
# ========================================

print("InventoryGuru(^_^)")
print("Simple answers. Clear actions.")
print()

sku = input("SKU: ")
system_quantity = get_quantity("System quantity: ")
counted_quantity = get_quantity("Counted quantity: ")

difference = calculate_difference(
    system_quantity,
    counted_quantity,
)

print()
show_stock_status(difference)


# ========================================
# SHORTAGE WORKFLOW
# ========================================

if difference < 0:
    print()

    counted_again = ask_yes_no("Counted again?")

    if not counted_again:
        print()
        print("Count the stock again.")

        counted_quantity = get_quantity("New count: ")

        difference = calculate_difference(
            system_quantity,
            counted_quantity,
        )

        print()
        show_stock_status(difference)

    if difference != 0:
        check_open_movement()