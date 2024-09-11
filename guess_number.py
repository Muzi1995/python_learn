import sys
import random


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name  # Make sure we're using the correct name passed to the game
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, Guess the number I am thinking... 1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()

        computerchoice = random.choice("123")
        print(f"\n{name}, you chose {playerchoice}.")
        print(f"Sorry I thought of {computerchoice}.\n")

        player = int(playerchoice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!"
            else:
                return f"Sorry, {name}. Better luck next time. 😢"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_guess_number  # Ensure the correct personalized function is returned


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Guess the Number Game")
    parser.add_argument('-n', '--name', metavar='name', required=True,
                        help='The name of the person playing the game.')

    args = parser.parse_args()
    # Ensure we pass the player's name correctly
    guess_number_game = guess_number(args.name)
    guess_number_game()
