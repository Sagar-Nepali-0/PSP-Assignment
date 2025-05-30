'''
Functions for managing daily temperature records.
'''

def add_daily_temp(temp_dict, day, temp):
    """
    Adds temperature to dictionary if day doesn't exist.
    
    Args:
        temp_dict (dict): Existing temperature dictionary
        day (str): Day of week
        temp (float): Temperature value
        
    Returns:
        dict: Updated temperature dictionary
    """
    if day not in temp_dict:
        temp_dict[day] = temp
    return temp_dict

def get_daily_temps():
    """
    Prompts user for daily temperatures and returns dictionary.
    
    Returns:
        dict: Dictionary with daily temperatures
    """
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", 
            "Friday", "Saturday", "Sunday"]
    temp_dict = {}
    
    for day in days:
        while True:
            try:
                temp = float(input(f"Enter temperature for {day}: "))
                temp_dict[day] = temp
                break
            except ValueError:
                print("Please enter a valid number")
                
    return temp_dict

# Test cases
temps = {}
temps = add_daily_temp(temps, "Monday", 72.5)
print(temps)

weekly_temps = get_daily_temps()
print(weekly_temps)