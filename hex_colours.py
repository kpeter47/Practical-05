# Define a dictionary of color names and their corresponding hexadecimal codes
COLORS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aquamarine": "#7fffd4",
    "blueviolet": "#8a2be2",
    "chartreuse": "#7fff00",
    "cornflowerblue": "#6495ed",
    "darkorange": "#ff8c00",
    "gold": "#ffd700",
    "hotpink": "#ff69b4",
    "limegreen": "#32cd32"
}

def lookup_color():
    while True:
        color_name = input("Enter a color name (or blank to exit): ").strip().lower()

        if not color_name:
            break  # Exit the loop if the user enters a blank line

        # Look up the color name in the dictionary and print the result
        color_code = COLORS.get(color_name, "Color not found")
        print(f"{color_name.capitalize()}: {color_code}")

if __name__ == "__main__":
    lookup_color()
