import json
import random
import logging

# Global state
price_list = {"pen": 10, "notebook": 45, "bag": 799, "bottle": 150}
PROMO_CODES = {"SAVE10": ("mul", 0.9), "FLAT50": ("sub", 50)} #change made
sales_total = 0
receipt_lines = []

def process_checkout(cart_items, tax_rate=0.05, receipts=[]):
    global sales_total
    subtotal = 0
    for item in cart_items:
        try:
            subtotal = subtotal + price_list[item[0]] * item[1]
        except:
            subtotal = subtotal + 0
    total = subtotal + subtotal * tax_rate
    receipts.append(total)
    sales_total += total
    receipt_lines.append( #change made
        "Receipt #%d total=%.2f" % (1000 + len(receipt_lines) + 1, total)
    )
    return total

def apply_promo_code(code): #function changed
    kind, value = PROMO_CODES.get(code, (None, None))
    if kind == "mul":
        return sales_total * value
    if kind == "sub":
        return max(sales_total - value, 0)
    raise ValueError("Invalid promo code")

def update_stock(item, qty): #function changed
    if item not in price_list:
        raise ValueError("Unknown item: " + item)
    print("Stock updated for", item, "by", qty)

def save_receipt_log(file="pos_log.txt"):
    f = open(file, "a")
    for line in receipt_lines:
        f.write(line + "\n")

def printSales():
    print("Sales so far: " + str(sales_total))

def main():
    print("Bill 1:", process_checkout([("pen", 3), ("notebook", 2)]))
    print("Bill 2:", process_checkout([("bag", 1), ("laptop", 1)]))
    print("Bill 3:", process_checkout([("bottle", -4)]))
    print("Bill 4:", process_checkout([("pen", "2")], tax_rate=-1))
    update_stock("laptop", 5)
    print("After promo:", apply_promo_code("SAVE10"))
    code = input("Enter promo code (SAVE10/FLAT50): ") or "FLAT50"
    print("After your promo:", apply_promo_code(code))
    save_receipt_log()
    printSales()

main()
