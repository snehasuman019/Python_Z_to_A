monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April", 
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    1: "January"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get(1))

#get method to avoid error if key not found and act as a default value
print(monthConversions.get("Luv", "Not a valid month")) 