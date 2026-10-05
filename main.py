# ========================================
# INVENTORYGURU - FUNCTIONS
# ========================================


def get_quantity(question):
    while True:
        try:
            return int(input(question))

        except ValueError:
            print("Enter a number.")


def get_choices(question, number_of_choices):
    while True:
        answer = input(question)

        try:
            choices = [int(choice.strip()) for choice in answer.split(",")]

            if all(1 <= choice <= number_of_choices for choice in choices):
                return choices

            print("Choose numbers from the list.")

        except ValueError:
            print("Enter numbers separated by commas.")


def material_workbench_check():
    print()
    print("STEP 1 - MATERIAL WORKBENCH")
    print()
    print("Check the item in Material Workbench.")
    print()
    print("What do you see?")
    print()
    print("1 - Underdelivery")
    print("2 - Scrap")
    print("3 - Hold")
    print("4 - Oracle / KiSoft discrepancy")
    print("5 - Receiving error")
    print("6 - Everything looks correct")
    print("7 - Other")

    print()


    choices = get_choices("Choice(s): ", 7)

    return choices


def material_transactions_check():
    print()
    print("STEP 2 - MATERIAL TRANSACTIONS")
    print()
    print("Check Material Transactions.")
    print()
    print("What do you see?")
    print()
    print("1 - Cycle count")
    print("2 - Picking exception")
    print("3 - Scrap to DAR")
    print("4 - Open PO")
    print("5 - Nothing relevant")
    print("6 - Other")

    print()

    choice = get_choices("Choice(s): ", 6)

    return choices


# ========================================
# INVENTORYGURU - START
# ========================================

print()
print("InventoryGuru(^_^)")
print("Simple answers. Clear actions.")
print()

print("UNEXPLAINED ITEM")
print()

sku = input("SKU: ").strip().upper()
quantity = get_quantity("Physical quantity: ")

print()
print("SKU:", sku)
print("Quantity:", quantity)


# ========================================
# STEP 1 - MATERIAL WORKBENCH
# ========================================

workbench_result = material_workbench_check()


# ========================================
# WORKBENCH RESULTS
# ========================================

if workbench_result == 1:
    print()
    print("UNDERDELIVERY FOUND")
    print("Investigate the underdelivery.")

elif workbench_result == 2:
    print()
    print("SCRAP FOUND")
    print("Investigate the scrap stock.")

elif workbench_result == 3:
    print()
    print("HOLD FOUND")
    print("Investigate the hold stock.")

elif workbench_result == 4:
    print()
    print("SYSTEM DISCREPANCY FOUND")
    print("Compare Oracle and KiSoft.")

elif workbench_result == 5:
    print()
    print("RECEIVING ERROR FOUND")
    print("Check if the item is hanging in receiving.")

elif workbench_result == 6:
    print()
    print("Material Workbench looks correct.")

    # ========================================
    # STEP 2 - MATERIAL TRANSACTIONS
    # ========================================

    transaction_result = material_transactions_check()

    if transaction_result == 1:
        print()
        print("CYCLE COUNT FOUND")
        print("Investigate the cycle count.")

    elif transaction_result == 2:
        print()
        print("PICKING EXCEPTION FOUND")
        print("Investigate the picking exception.")

    elif transaction_result == 3:
        print()
        print("SCRAP TO DAR FOUND")
        print("Investigate the booking.")

    elif transaction_result == 4:
        print()
        print("OPEN PO FOUND")
        print("Investigate the open PO.")

    elif transaction_result == 5:
        print()
        print("NO EXPLANATION FOUND")
        print("Continue to the next check.")

    else:
        print()
        print("OTHER RESULT")
        print("Ask Inventory Control.")

else:
    print()
    print("OTHER RESULT")
    print("Ask Inventory Control.")
