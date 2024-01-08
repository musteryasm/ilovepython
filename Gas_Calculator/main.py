def ideal_gas_calculator():
    while True:
        print("Choose the variable you want to calculate:")
        print("1. Pressure (P)")
        print("2. Mass (m)")
        print("3. Molar Mass (M)")
        print("4. Gas Constant (R)")
        print("5. Temperature (T)")
        print("6. Volume (V)")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            N_known = input("Is N known? (yes/no): ")
            if N_known.lower() == 'yes':
                N = float(input("Enter N: "))
                R = float(input("Enter gas constant (kJ/kg.K): "))
                T = float(input("Enter temperature (K): "))
                V = float(input("Enter volume (m^3): "))
                P = N*R*T/V
            else:
                density_known = input("Is density known? (yes/no): ")
                if density_known.lower() == 'yes':
                    density = float(input("Enter density (kg/m^3): "))
                    m = 1/density
                else:
                    m = float(input("Enter mass (kg): "))
                M = float(input("Enter molar mass (kg/kmol): "))
                R = float(input("Enter gas constant (kJ/kg.K): "))
                T = float(input("Enter temperature (K): "))
                V = float(input("Enter volume (m^3): "))
                P = (m/M)*R*T/V
            print(f"Pressure (P) = {P} kPa")
        elif choice == '2':
            P = float(input("Enter pressure (kPa): "))
            M = float(input("Enter molar mass (kg/kmol): "))
            R = float(input("Enter gas constant (kJ/kg.K): "))
            T = float(input("Enter temperature (K): "))
            V = float(input("Enter volume (m^3): "))
            m = (P * M * V) / (R * T)
            print(f"Mass (m) = {m} kg")
        elif choice == '3':
            P = float(input("Enter pressure (kPa): "))
            m = float(input("Enter mass (kg): "))
            R = float(input("Enter gas constant (kJ/kg.K): "))
            T = float(input("Enter temperature (K): "))
            V = float(input("Enter volume (m^3): "))
            M = (m * R * T) / (P * V)
            print(f"Molar Mass (M) = {M} kg/kmol")
        elif choice == '4':
            P = float(input("Enter pressure (kPa): "))
            m = float(input("Enter mass (kg): "))
            M = float(input("Enter molar mass (kg/kmol): "))
            T = float(input("Enter temperature (K): "))
            V = float(input("Enter volume (m^3): "))
            R = (P * V) / ((m/M) * T)
            print(f"Gas Constant (R) = {R} kJ/kg.K")
        elif choice == '5':
            P = float(input("Enter pressure (kPa): "))
            m = float(input("Enter mass (kg): "))
            M = float(input("Enter molar mass (kg/kmol): "))
            R = float(input("Enter gas constant (kJ/kg.K): "))
            V = float(input("Enter volume (m^3): "))
            T = (P * V) / ((m/M) * R)
            print(f"Temperature (T) = {T} K")
        elif choice == '6':
            P = float(input("Enter pressure (kPa): "))
            m = float(input("Enter mass (kg): "))
            M = float(input("Enter molar mass (kg/kmol): "))
            R = float(input("Enter gas constant (kJ/kg.K): "))
            T = float(input("Enter temperature (K): "))
            V = (m/M) * R * T / P
            print(f"Volume (V) = {V} m^3")

        again = input("Do you want to calculate again? (yes/no): ")
        if again.lower() != 'yes':
            break

ideal_gas_calculator()
