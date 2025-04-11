"""Functions for calculating tips and totals."""

def dollars_to_float(d):
    """Return the tip based on amount and percentage."""
    d = d.replace("$", "")
    d = float(d)
    return d


def percent_to_float(p):
    """Return the total bill including tip."""
    p = p.replace("%", "")
    p = float(p) / 100
    return p


if __name__ == "__main__":
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")