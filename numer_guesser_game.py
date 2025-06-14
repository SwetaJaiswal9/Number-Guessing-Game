import random

print("Welcome to the Number Guesser Game!")

def choose_difficulty():
    print("Select Difficulty Level:")
    print("1. Beginner (1-10)")
    print("2. Intermediate (1-50)")
    print("3. Pro (1-100)")


    while True:
        choice = input("Enter your choice (1 / 2 / 3): ").strip()
        if choice == "1":
            return 10
        elif choice == "2":
            return 50
        elif choice == "3":
            return 100
        else:
            print("⚠️ Invalid choice. Try again.")


def play_game():
    print("🎮 Let's play: **Guess the Number**!")

    upper_limit = choose_difficulty()
    secret_number = random.randint(1, upper_limit)
    attempts = 0

    while True:
        guess_input = input(f"\nEnter a number between 1 and {upper_limit}: ").strip()
        if not guess_input.isdigit():
            print("❌ That's not a number. Please try again.")
            
        attempts += 1
        guess = int(guess_input)

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

    print("Thanks for playing! 🧡 Come back soon.")

if __name__ == "__main__":
    play_game()