def kalkulyator():
    birinchi_son = float(input("Birinchi sonni kiriting: "))
    ikkinchi_son = float(input("Ikkinchi sonni kiriting: "))
    amal = input("Amalni tanlang (+, -, *, /): ")

    if amal == "+":
        print(f"Natija: {birinchi_son + ikkinchi_son}")
    elif amal == "-":
        print(f"Natija: {birinchi_son - ikkinchi_son}")
    elif amal == "*":
        print(f"Natija: {birinchi_son * ikkinchi_son}")
    elif amal == "/":
        if ikkinchi_son != 0:
            print(f"Natija: {birinchi_son / ikkinchi_son}")
        else:
            print("Bo'lish amali nolga bo'lish mumkin emas!")
    else:
        print("Noto'g'ri amal tanlandi!")

if __name__ == "__main__":
    kalkulyator()