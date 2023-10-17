"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}
print(CODE_TO_NAME)

while True:
    state_code = input("Enter short state: ").upper()
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    elif state_code == "":
        break
    else:
        print("Invalid short state")
