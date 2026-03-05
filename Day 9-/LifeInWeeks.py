
age=int(input("Enter your age: ")) 

def life_in_weeks(age):
    year_left= 90 - age
    weeks = year_left * 52
    print(f"You have {weeks} left to live")


life_in_weeks(age)