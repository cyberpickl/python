
#input fields for collecting name and place
name = input("Hi What's your name?: ")
place = input ("Where do you live?: ")



#creating a function that takes name and place variables as parameters
def greet (name, place):
    print(f"Hello {name}")
    print(f"How do you do!You live in {place}")
    print ("Isn't the weather nice")

#calling the function and passing arguments 
greet(name, place)