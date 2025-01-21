import requests
import random


def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        exchange_rate = data["rates"]["ILS"]

        return exchange_rate

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        raise ValueError(f"Failed to retrieve exchange rate: {e}")
    except KeyError as e:
        print(f"Error: Missing expected data in response - {e}")
        raise ValueError("Exchange rate data not found in the response")


def get_money_interval(difficulty):
    usd_value = random.randint(1, 100)
    exchange_rate = get_exchange_rate()

    ils_value = usd_value * exchange_rate

    min_value = int(ils_value * 0.9)  # Example min value (10% less)
    max_value = int(ils_value * 1.1)  # Example max value (10% more)

    return min_value, max_value, ils_value


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Guess the value in ILS (Israeli Shekel):\n"))
            return guess
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compare_results(correct_value, user_guess, min_value, max_value, tolerance=0.01):
    if min_value - tolerance <= user_guess <= max_value + tolerance:
        return True
    else:
        return False

def play(difficulty):
    print("Welcome to Currency Roulette!")
    min_value, max_value, correct_value = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    if compare_results(correct_value, user_guess, min_value, max_value):
        print(f"Congratulations! You guessed correctly! The value was {correct_value:.2f} ILS.")
        return True
    else:
        print(f"Sorry, you lost! The correct value was {correct_value:.2f} ILS.")
        print(f"The acceptable range was {min_value:.2f} to {max_value:.2f} ILS.")
        return False
