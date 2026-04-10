"""
Welcome message generator for the space mission program.
"""


def welcome_message(name, course):
    """
    Generate a personalized welcome message.
    
    Args:
        name (str): The person's name
        course (str): The course name
        
    Returns:
        str: A formatted welcome message
    """
    return f"Welcome, {name}! You are enrolled in {course}."


# Test calls with different names and courses
if __name__ == "__main__":
    print(welcome_message("Alice", "Advanced Spacecraft Navigation"))
    print(welcome_message("Bob", "Interstellar Communication Systems"))
