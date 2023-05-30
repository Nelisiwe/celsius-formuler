def convert_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9


def find_coldest_day(temperatures):
  coldest_day = 0
  for i in range(1, len(temperatures)):
    if temperatures[i] < temperatures[coldest_day]:
      coldest_day = i

  return coldest_day


def main():
  fahrenheit_1 = float(input("Enter the maximum temperature for day 1 in degrees Fahrenheit: "))
  fahrenheit_2 = float(input("Enter the maximum temperature for day 2 in degrees Fahrenheit: "))

  celsius_1 = convert_to_celsius(fahrenheit_1)
  celsius_2 = convert_to_celsius(fahrenheit_2)

  print("The maximum temperature for day 1 in degrees Celsius is", celsius_1)
  print("The maximum temperature for day 2 in degrees Celsius is", celsius_2)

  coldest_day = find_coldest_day([celsius_1, celsius_2])

  if coldest_day == 0:
    print("Day 1 was the coldest day.")
  else:
    print("Day 2 was the coldest day.")


if __name__ == "__main__":
  main()
