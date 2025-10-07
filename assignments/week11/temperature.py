"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
    

def get_temperatures():
    x = [32, 30, 31, 33, 30, 31, 34]
    return x

def analyze(temp_list):
    sum = 0
    for temp in temp_list:
        sum += temp
    average = sum / len(temp_list)
    max_temp = max(temp_list)
    min_temp = min(temp_list)
    return (average, max_temp, min_temp)

def display_analysis(avg, high, low):
    print("Temperature Analysis for the week:")
    print("Average: " + str(avg) + " C")
    print(f"Highest: {high} C")
    print(f"Lowest: {low} C")

temp_list = get_temperatures()
result = analyze(temp_list)
display_analysis(result[0], result[1], result[2])

