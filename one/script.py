import requests


def main():
    url = "https://swapi.dev/api/vehicles/"
    manufacturers = []
    while url:
        response = requests.get(url)
        data = response.json()
        vehicles = data["results"]
        for vehicle in vehicles:
            if vehicle["manufacturer"].title() not in manufacturers:
                manufacturers.append(vehicle["manufacturer"])
        url = data.get("next")

    print("The first 5 unique manufacturers are:")
    for i, manufacturer in enumerate(manufacturers):
        print(f"{i + 1}. {manufacturer}")
        if i == 4:
            break


if __name__ == "__main__":
    main()
