"""Retail point-of-sale: checkout, promo codes and receipt logging."""

PRICE_LIST = {"pen": 10, "notebook": 45, "bag": 799, "bottle": 150}
PROMO_CODES = {"SAVE10": ("mul", 0.9), "FLAT50": ("sub", 50)}
STOCK = {name: 100 for name in PRICE_LIST}
STATE = {"sales_total": 0.0, "receipt_no": 1000}
RECEIPT_LINES = []


def process_checkout(cart_items, tax_rate=0.05, receipts=None):
    """Total a cart with tax; raise ValueError on invalid input."""
    if receipts is None:
        receipts = []
    if not 0 <= tax_rate <= 1:
        raise ValueError(f"Invalid tax rate: {tax_rate}")
    subtotal = 0
    for name, qty in cart_items:
        if name not in PRICE_LIST:
            raise ValueError(f"Unknown item: {name}")
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError(f"Invalid quantity for {name}: {qty}")
        subtotal += PRICE_LIST[name] * qty
    total = round(subtotal * (1 + tax_rate), 2)
    receipts.append(total)
    STATE["sales_total"] += total
    STATE["receipt_no"] += 1
    RECEIPT_LINES.append(f"Receipt #{STATE['receipt_no']} total={total:.2f}")
    return total


def apply_promo_code(code):
    """Apply a promo code to the running sales total."""
    kind, value = PROMO_CODES.get(code, (None, None))
    if kind == "mul":
        new_total = STATE["sales_total"] * value
    elif kind == "sub":
        new_total = max(STATE["sales_total"] - value, 0)
    else:
        raise ValueError("Invalid promo code")
    STATE["sales_total"] = round(new_total, 2)
    return STATE["sales_total"]


def update_stock(item, qty):
    """Add qty units to the stock of an item."""
    if item not in STOCK:
        raise ValueError(f"Unknown item: {item}")
    STOCK[item] += qty
    print("Stock updated for", item, "by", qty)


def save_receipt_log(file="pos_log.txt"):
    """Append all receipt lines to a log file."""
    with open(file, "a", encoding="utf-8") as log:
        for line in RECEIPT_LINES:
            log.write(line + "\n")


def print_sales():
    """Print the running sales total."""
    print("Sales so far: " + str(STATE["sales_total"]))


def main():
    """Run a demo session."""
    bills = [
        ([("pen", 3), ("notebook", 2)], 0.05),
        ([("bag", 1), ("laptop", 1)], 0.05),
        ([("bottle", -4)], 0.05),
        ([("pen", "2")], -1),
    ]
    for number, (cart, tax) in enumerate(bills, start=1):
        try:
            print(f"Bill {number}:", process_checkout(cart, tax_rate=tax))
        except ValueError as err:
            print(f"Bill {number} rejected: {err}")
    update_stock("pen", 5)
    print("After promo:", apply_promo_code("SAVE10"))
    code = input("Enter promo code (SAVE10/FLAT50): ") or "FLAT50"
    try:
        print("After your promo:", apply_promo_code(code))
    except ValueError as err:
        print(err)
    save_receipt_log()
    print_sales()


if __name__ == "__main__":
    main()
