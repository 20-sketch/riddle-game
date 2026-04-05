import random

def riddle_game():
    levels = {
        1: {
            "riddles": {
                "What has to be broken before you can use it?": "egg",
                "What has many keys but can’t open a single lock?": "piano",
                "in chair but we can't see": "kunji podiyaal",
                "there is two guys one with more money and happiness and one with no money and lot of unsolvable problems which guy did you choose guy one or two ?": "guy one"
            },
            "required_correct": 2
        },
        2: {
            "riddles": {
                "The more of me you take, the more you leave behind. What am I?": "footsteps",
                "Who is with a lot of  golden money in her chaakk?": "veru pottal",
                "What has hands but can’t clap?": "clock",
                "there is a guy who swallows tapioca who is it?": "kooi kooi maman"
            },
            "required_correct": 2
        },
        3: {
            "riddles": {
                "who is aguy who swallows banana?": "pakki",
                "The person who makes it, sells it. The person who buys it never uses it. The person who uses it never knows they’re using it. What is it?": "coffin",
                "What can travel around the world while staying in a corner?": "stamp",
                "it is a human with who is priceless and property of kerala government": "s.i ratnam"
            },
            "required_correct": 2
        }
    }

    print("🎯 Welcome to the Riddle Game with tiny kuttyappams!")
    print("Answer riddles correctly to advance. Type 'veru pottal' to exit.\n")

    for level, data in levels.items():
        riddles = list(data["riddles"].items())
        random.shuffle(riddles)
        score = 0

        print(f"--- tiny kuttyappams {level} ---")
        for question, answer in riddles:
            print(question)
            user_answer = input("Your answer: ").strip().lower()

            if user_answer == "verupottal":
                print("You quit the game because you are a narinth. Goodbye!")
                return
            elif user_answer == answer:
                print("✅ srakkutty unni!\n")
                score += 1
            else:
                print(f"❌ you proven that you are a tapioca swallow guy! The correct answer was '{answer}'.\n")

        if score >= data["required_correct"]:
            print(f"🎉 You passed one tiny kuttyappam {level}!\n")
        else:
            print(f"get off cow dung! You needed {data['required_correct']} correct answers to pass these tiny kuttyappams {level}.")
            return
        
    print("🏆 Congratulations! You won a gosala chaakk for completing all levels!")

if __name__ == "__main__":
    riddle_game()