import requests

def fetch_questions():
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print("Failed to fetch questions")
        return []
import random
import urllib.parse
def play_game():
   import random
import urllib.parse  # Import this at the top of your file

def play_game():
    questions = fetch_questions()
    if not questions:
        return

    score = 0

    for idx, question in enumerate(questions, 1):
        # Decode the question before printing
        decoded_question = urllib.parse.unquote(question['question'])
        print(f"\nQ{idx}: {decoded_question}")
        
        # Decode the options before printing
        options = question['incorrect_answers'] + [question['correct_answer']]
        random.shuffle(options)

        for i, option in enumerate(options, 1):
            decoded_option = urllib.parse.unquote(option)  # Decode each option
            print(f"  {i}. {decoded_option}")

        try:
            answer = int(input("Your answer (1-4): "))
            if options[answer-1] == question['correct_answer']:
                print("Correct! 🎉\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}\n")
        except (ValueError, IndexError):
            print(f"Invalid input! The correct answer was: {question['correct_answer']}\n")

    print(f"\nGame Over! Your Score: {score}/{len(questions)}")


if __name__ == "__main__":
    print("\nWelcome to Fun Trivia Bot! ")
    play_game()
