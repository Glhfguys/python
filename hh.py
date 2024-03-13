class GymExercise:
    def __init__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps
    
    def display(self):
        print(f"Exercise: {self.name}")
        print(f"Sets: {self.sets}")
        print(f"Reps: {self.reps}")

class GymWorkout:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def display_workout(self):
        if not self.exercises:
            print("No exercises added yet.")
            return
        print("Today's Gym Workout:")
        for exercise in self.exercises:
            exercise.display()
            print()

# Example usage:

workout = GymWorkout()

while True:
    print("\nMenu:")
    print("1. Add Exercise")
    print("2. Display Workout")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter exercise name: ")
        sets = int(input("Enter number of sets: "))
        reps = int(input("Enter number of reps: "))
        exercise = GymExercise(name, sets, reps)
        workout.add_exercise(exercise)
        print("Exercise added successfully!")

    elif choice == "2":
        workout.display_workout()
    elif choice == "3":
        print("Exiting program. Have a great workout!")
        break
    else:
        print("Invalid choice. Please choose again.")