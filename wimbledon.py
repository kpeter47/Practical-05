import csv

def read_wimbledon_data(filename):
    champions = []
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        csv_reader = csv.DictReader(in_file, delimiter='\t')
        for row in csv_reader:
            name, year, country = row['Champion'], int(row['Year']), row['Country']
            champions.append([name, year])
            countries.add(country)
    return champions, countries

def count_wimbledon_wins(champions):
    win_count = {}
    for name, year in champions:
        if name in win_count:
            win_count[name] += 1
        else:
            win_count[name] = 1
    return win_count

def display_champions(win_count):
    print("Wimbledon Champions:")
    for name, wins in sorted(win_count.items()):
        print(f"{name} {wins}")

def display_countries(countries):
    sorted_countries = sorted(countries)
    print("\nThese countries have won Wimbledon:")
    countries_str = ", ".join(sorted_countries)
    print(countries_str)

def main():
    filename = "wimbledon.csv"
    champions, countries = read_wimbledon_data(filename)
    win_count = count_wimbledon_wins(champions)
    display_champions(win_count)
    display_countries(countries)

if __name__ == "__main__":
    main()
