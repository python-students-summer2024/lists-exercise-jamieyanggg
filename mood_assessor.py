import datetime
import os

def assess_mood():
    happy = str(2)
    relaxed = str(1)
    apathetic = str(0)
    sad = str(-1)
    angry = str(-2)
    valid_moods = ['happy', 'relaxed', 'apathetic', 'sad', 'angry']

    data_dir = 'data'
    file_path = os.path.join(data_dir, 'mood_diary.txt')

    date_today = datetime.date.today()
    date_today_str = str(date_today)

    file = open(file_path, 'r')
    for line in file:
        if line.startswith(date_today_str):
            print("Sorry, you have already entered your mood today.")
            return None
    

    curr_mood = ''
    while curr_mood not in valid_moods:
        curr_mood = input("What is your current mood? ('happy', 'relaxed', 'apathetic', 'sad', 'angry'): ").strip().lower()
        if curr_mood in valid_moods:
            if curr_mood == 'happy':
                mood_value = happy
            elif curr_mood == 'relaxed':
                mood_value = relaxed
            elif curr_mood == 'apathetic':
                mood_value = apathetic
            elif curr_mood == 'sad':
                mood_value = sad
            elif curr_mood == 'angry':
                mood_value = angry
            with open(file_path, "a") as file:
                file.write(date_today_str + ": " + mood_value + '\n')
            print("Mood recorded.")
        else:
            print("Invalid mood. Please enter one of the following: 'happy', 'relaxed', 'apathetic', 'sad', 'angry'.")

    file = open(file_path, 'r')
    lines = file.readlines()
    mood_sum = 0
    happy_count = 0
    relaxed_count = 0
    apathetic_count = 0
    sad_count = 0
    angry_count = 0
    if len(lines) >= 7:
        last_entries = lines[-7:]
        for line in last_entries:
            date, value = line.strip().split(':')
            mood_sum += int(value)
        avg_mood = round(mood_sum / 7)
        if mood_value == happy:
            happy_count += 1
        elif mood_value == relaxed:
            relaxed_count += 1
        elif mood_value == apathetic:
            apathetic_count += 1
        elif mood_value == sad:
            sad_count += 1
        elif mood_value == angry:
            angry_count += 1
        diagnosis = ''
        if happy_count >= 5:
            diagnosis = 'manic'
        elif sad_count >= 4:
            diagnosis = 'depressive'
        elif apathetic_count >= 6:
            diagnosis = 'schizoid'
        else:
            diagnosis = avg_mood
        if avg_mood == 2:
            diagnosis = 'happy'
        elif avg_mood == 1:
            diagnosis = 'relaxed'
        elif avg_mood == 0:
            diagnosis = 'apathetic'
        elif avg_mood == -1:
            diagnosis = 'sad'
        elif avg_mood == -2:
            diagnosis = 'angry'

        print(f"Your diagnosis: {diagnosis}!")