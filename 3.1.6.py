if __name__ == '__main__':
    weight = int(input('Enter your weight (kg): '))
    height = int(input('Enter your height (cm): '))
    # BMI = [weight (kg) / height (cm) / height (cm)] x 10,000
    BMI = (weight / height / height) * 10000

    if BMI <= 18.5:
        print("Underweight")
    elif BMI < 25:
        print("Normal Weight")
    elif BMI < 30:
        print("Overweight")
    else:
        print("Obesity")
