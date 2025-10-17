from mood_detection import detect_mood
from recommend import recommend_song

def main():
    print("Choose option:")
    print("1. Detect mood via webcam")
    print("2. Enter mood manually")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        mood = detect_mood()
        if mood:
            print(f"Mood detected: {mood}")
            recommend_song(mood)
        else:
            print("Could not detect mood.")
    elif choice == "2":
        mood = input("Enter your mood (happy/sad/relaxed/angry): ")
        recommend_song(mood)
    else:
        print("Invalid choice.")

if _name_ == "_main_":
    main()
