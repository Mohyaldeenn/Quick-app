import os
import json
from datetime import datetime

class HabitTracker:
    def __init__(self, filename="habit_data.json"):
        self.filename = filename
        self.habits = self.load_data()

    def load_data(self):
        """Load habit data from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        else:
            return {}

    def save_data(self):
        """Save habit data to the file."""
        with open(self.filename, "w") as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, habit_name, goal):
        """Add a new habit with a goal."""
        if habit_name not in self.habits:
            self.habits[habit_name] = {"goal": goal, "progress": []}
            self.save_data()
            print(f"Habit '{habit_name}' added with a goal of {goal} days.")
        else:
            print(f"Habit '{habit_name}' already exists.")

    def mark_habit_completed(self, habit_name):
        """Mark the habit as completed today."""
        today = datetime.today().strftime('%Y-%m-%d')
        if habit_name in self.habits:
            self.habits[habit_name]["progress"].append(today)
            self.save_data()
            print(f"Marked '{habit_name}' as completed for {today}.")
        else:
            print(f"Habit '{habit_name}' not found.")

    def view_progress(self):
        """View the progress for all habits."""
        for habit, data in self.habits.items():
            completed_days = len(data["progress"])
            goal = data["goal"]
            print(f"{habit}: Goal = {goal} days, Progress = {completed_days}/{goal} days completed.")
            print(f"Completed on: {', '.join(data['progress'])}\n")

    def view_report(self):
        """View a detailed report of habits' progress."""
        for habit, data in self.habits.items():
            completed_days = len(data["progress"])
            goal = data["goal"]
            completion_percentage = (completed_days / goal) * 100 if goal > 0 else 0
            print(f"{habit}:")
            print(f"  Goal: {goal} days")
            print(f"  Progress: {completed_days}/{goal} days")
            print(f"  Completion: {completion_percentage:.2f}%")
            print(f"  Completed on: {', '.join(data['progress'])}\n")

def print_menu():
    """Print the menu for the user."""
    print("\nHabit Tracker Menu:")
    print("1. View progress of all habits")
    print("2. Add a new habit")
    print("3. Mark a habit as completed today")
    print("4. View detailed report")
    print("5. Exit")

def main():
    tracker = HabitTracker()

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            tracker.view_progress()
        elif choice == "2":
            habit_name = input("Enter the habit name: ").strip()
            goal = int(input("Enter the goal for this habit (number of days): ").strip())
            tracker.add_habit(habit_name, goal)
        elif choice == "3":
            habit_name = input("Enter the habit name to mark as completed today: ").strip()
            tracker.mark_habit_completed(habit_name)
        elif choice == "4":
            tracker.view_report()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please choose a valid option.")

if __name__ == "__main__":
    main()