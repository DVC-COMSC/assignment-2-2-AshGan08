def main():
    celcius = int(input("Please enter Celcius degrees: "))
    fahrenheit = (9/5*celcius)+32
    return celcius, fahrenheit


if __name__ == '__main__':
    celcius, fahrenheit = main()
    print(f'Here is the Fahrenheit converted from celcius \t {fahrenheit: .2f}')
    