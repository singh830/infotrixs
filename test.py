import requests
import time

API_KEY = "59aa5970bd354a1695983211240201" 
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching weather data.")
        return None

def display_weather(weather_data):
    if weather_data:
        print("\nWeather Information:")
        print(f"Location: {weather_data['location']['name']}")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Condition: {weather_data['current']['condition']['text']}")
    else:
        print("\nError fetching weather information.")

def add_favorite(city, favorites):
    if city not in favorites:
        favorites.append(city)
        print(f"\n'{city}' added to favorites.")
    else:
        print(f"\n'{city}' is already in favorites.")

def remove_favorite(city, favorites):
    if city in favorites:
        favorites.remove(city)
        print(f"\n'{city}' removed from favorites.")
    else:
        print(f"\n'{city}' is not in favorites.")

def list_favorites(favorites):
    print("\nFavorite Cities:")
    for city in favorites:
        print(f"- {city}")

def main():
    favorites = []
    refresh_interval = 15  # default refresh interval in seconds

    print("Welcome to the Weather Checking Application!")

    while True:
        print("\nOptions:")
        print("1. Check weather by city")
        print("2. Add city to favorites")
        print("3. Remove city from favorites")
        print("4. List favorite cities")
        print("5. Set auto-refresh interval")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            city_name = input("Enter city name: ")
            weather_data = get_weather(city_name)
            display_weather(weather_data)

        elif choice == "2":
            city_name = input("Enter city name to add to favorites: ")
            add_favorite(city_name, favorites)

        elif choice == "3":
            city_name = input("Enter city name to remove from favorites: ")
            remove_favorite(city_name, favorites)

        elif choice == "4":
            list_favorites(favorites)

        elif choice == "5":
            try:
                refresh_interval = int(input("Enter auto-refresh interval (in seconds): "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "6":
            print("Exiting the Weather Checking Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        time.sleep(refresh_interval)

if __name__ == "__main__":
    main()