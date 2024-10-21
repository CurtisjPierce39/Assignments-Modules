#Question 1 Task 1

def mood_response(mood):

    if mood.lower() in ["happy", "cheerful", "excited"]:
        return "That is great to hear!"
    if mood.lower() in ["sad", "depressed", "upset"]:
        return "Keep your head up! Things will get better!"
    if mood.lower() in ["mad", "frustrated", "angry"]:
        return "Take a breath! Count to 10!"
    return "I don't know what you mean. Can you be more specific?"