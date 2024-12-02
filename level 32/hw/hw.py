def check_exam(arr1, arr2):
    score = 0
    for correct, student in zip(arr1, arr2):
        if student == correct:
            score += 4  # Correct answer
        elif student == "":
            score += 0  # Blank answer
        else:
            score -= 1  # Incorrect answer
    
    return max(score, 0)  # Ensure the score doesn't go below 0
