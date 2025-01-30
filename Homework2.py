def calculate_net_salary():
    try:
        gross_salary = float(input("What is the gross salary ?: "))
        number_of_children = int(input("How many children ?: "))

        if gross_salary<1000:
            tax_rate=10
        elif gross_salary<2000:
            tax_rate=12
        elif gross_salary<4000:
            tax_rate=14
        else:
            tax_rate=18

        if gross_salary<2000:
            tax_cut=number_of_children*1
        else:
            tax_cut=number_of_children*0.5

        final_tax_rate=tax_rate-tax_cut
        net_salary=gross_salary * (1 - final_tax_rate / 100)

        print(f"Net salary: {net_salary:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for salary and number of children.")

calculate_net_salary()