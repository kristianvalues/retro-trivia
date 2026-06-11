# My database of retro trivia questions and answers
trivia_bank = {
    "What 90s digital pet had to be fed, cleaned up after, and kept alive?": "tamagotchi",
    "In what vintage video game do you control a yellow circle eating dots?": "pac-man",
    "What popular 90s toy featured collectible cardboard discs played with a slammer?": "pogs",
    "What was the name of the green slime famously dumped on people on Nickelodeon?": "gak"
}
# 1. Initialize the player's score
score = 0

print("Welcome to the Retro Trivia Challenge!")
print("-------------------------------------")

# 2. Loop through the dictionary using .items()
for question, correct_answer in trivia_bank.items():
    print(question)
    
    # 3. Take the player's guess
    player_guess = input("Your answer: ")
    
    # 4. Check the answer (ignoring capitalization!)
    if player_guess.lower() == correct_answer.lower():
        print("Correct! 🎉\n")
        score += 1
    else:
        print(f"Not quite! The correct answer was: {correct_answer}.\n")

# 5. Show final results
print("-------------------------------------")
print(f"Game Over! Your final score is: {score}/{len(trivia_bank)}")