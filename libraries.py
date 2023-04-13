# dictionaries are used to access data by referencing a key
# the value on the left is the KEY, and on the right is the VALUE
# dictionaries consist of KEY-VALUE pairs
# KEYs have to be unique, there can't be duplicate keys


day_abbreviations = {
    "mon": "monday",
    "tue": "tuesday",
    "wed": "wednesday",
    "thu": "thursday",
    "fri": "friday",
    "sat": "saturday",
    "sun": "sunday"
}

abb_day = "MON"
full_day = "MONDAY"
type = "WEEKDAY"

# we can update a dictionary by using the update method, where we'll have to entere a new key-value pair
day_abbreviations.update({abb_day: f"{full_day} is a {type}"})

# one way to access the dictionary is to use "[]" and type in the key inside it
print(day_abbreviations["mon"])
print(day_abbreviations["sun"])

# another way to access dictionary is to use the "get" function
print(day_abbreviations.get("tue"))
print(day_abbreviations.get("thu"))
# using the get function we can handle cases where the key entered is invalid,in which case by default it outputs "none"
# by passing a second parameter, we can display a custom message if the key entered is invalid
print(day_abbreviations.get("Hello"))
print(day_abbreviations.get("jan", "invalid key entered !"))
print(day_abbreviations.get("WED", "key entered is not valid !"))

# we can access both the kley and value in a dictionary inorder to print them using the items() methods as shown below
for key, value in day_abbreviations.items():
    print(f"{key} : {value}")
