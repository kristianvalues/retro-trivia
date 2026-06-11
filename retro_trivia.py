import random  #Import Python's built-in random tools

# Our database of retro trivia questions and answers
trivia_bank = {
    "What 90s digital pet had to be fed, cleaned up after, and kept alive?": "tamagotchi",
    "In what vintage video game do you control a yellow circle eating dots?": "pac-man",
    "What popular 90s toy featured collectible cardboard discs played with a slammer?": "pogs",
    "What was the name of the green slime famously dumped on people on Nickelodeon?": "gak"
}

# Extract the questions into a list and scramble them!
questions_list = list(trivia_bank.keys())
random.shuffle(questions_list)

# Initialize game stats
score = 0
lives = 3 

print("Welcome to the Retro Trivia Challenge!")
print("-------------------------------------")

# 🎲 UPDATED: Loop through the shuffled list instead of the dictionary directly
for question in questions_list:
    # Look up the correct answer using the question as the key
    correct_answer = trivia_bank[question]
    
    print(question)
    player_guess = input("Your answer: ")
    
    if player_guess.lower() == correct_answer.lower():
        print("Correct! 🎉\n")
        score += 1
    else:
        lives -= 1  
        print(f"Not quite! The correct answer was: {correct_answer}.")
        print(f"❤️ Lives remaining: {lives}\n")
        
        if lives == 0:
            print("💥 Game Over! You ran out of lives! 💥\n")
            break 

# Show final results
print("-------------------------------------")
print(f"Game Over! Your final score is: {score}/{len(trivia_bank)}")