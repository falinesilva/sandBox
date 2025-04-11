import inflect

def main():
    """
    Prompts the user to input names until 'exit' is input, then 
    prints a farewell message with the names joined by commas and 'and'.
    """
    
    p = inflect.engine()
    names = list()

    print ("Type 'exit' and press Enter when done.")
    while True:
        name = input("Name: ").strip()
        if name.lower() == 'exit':
            break
        names.append(name)
    
    names = p.join(names)
    print(f"Adieu, adieu, to {names}")

main()
