john = 3
mary = 5
adam = 6

def somatorio (x,y,z):
    total_apples = x + y + z
    return f"Total Apples was: {total_apples}\n Being {x} of John, {y} of Mary, {z} of Adam"

def main():
    resultado = somatorio(john,mary,adam)
    print(resultado)

if __name__ == "__main__":
    main()