def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")


def pounds_to_float(d):
    return(float(d.replace('£', '')))# TODO

def percent_to_float(p):
    x = (p.replace('%', ''))# TODO
    x = ((float(x))/100)
    return(x)

main()
