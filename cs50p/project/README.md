# To-Do List Creator
#### Video Demo:  <https://youtu.be/7PEm38U3a_k>
#### Description:
Here's a breakdown of how the program works:

1. **Importing Necessary Libraries:**

   - `tabulate`: This library is used for formatting and displaying task data in a tabular format. It helps to present the task list in a structured and visually appealing way.

   - `datetime`: The `datetime` module is used for handling date and time-related data. It is essential for recording both the registration time and the reminder time for tasks.

   - `re`: The `re` module is employed for regular expression matching. In this program, it is used to validate the format of the reminder time input to ensure it adheres to the expected format.

   - `csv`: The `csv` module is used for reading and writing CSV (Comma-Separated Values) files. This functionality allows the program to save and load tasks to and from a file for persistence.

   - `sys`: The `sys` module provides access to some variables used for interacting with the Python runtime environment. In this program, it is used to handle special key combinations for program termination (Ctrl+D).

2. **Main Function:**

   - The `main` function serves as the entry point of the program.

   - It initializes a list called `table` with a header row that defines the columns for the task data (Title, Register Time, Reminder Time, and Description). This list will be used to store task information.

   - It then calls the `task` function to start the task management process.

3. **Task Function:**

   - The `task` function is responsible for task creation and management. It operates in an infinite loop, allowing the user to create tasks until they decide to exit.

   - In each iteration of the loop, the user is prompted to enter a title and description for the task.

   - The function calls the `time` function to get the reminder time, which the user inputs in a specific format.

   - The task data (title, register time, reminder time, and description) is added to the `table` list.

   - After adding a task, the `ftable` function is called to display the table of tasks, showing all previously entered tasks.

   - The user can exit the program and save the tasks by pressing Ctrl+D, which is a special key combination that can be detected by the program.

4. **Time Function:**

   - The `time` function handles the input of reminder times in a specific format.

   - It prompts the user to input a reminder time in the format "day-month-year" and optionally with a 24-hour time. For example, "25-10-2023 14:30" might represent October 25, 2023, at 2:30 PM.

   - To ensure that the input matches the expected format, the function uses a regular expression to validate the input.

   - If the input is valid, it converts the input to a `datetime` object, which allows for easy manipulation of date and time data, and returns the current time and the reminder time.

5. **Ftable Function:**

   - The `ftable` function takes the `table` list, which holds the task data, and uses the `tabulate` library to format and display the tasks in a grid format.

   - When displaying the tasks, it skips the header row, which contains column names, to provide a clean and easy-to-read presentation of the tasks.

6. **Checking if the Script is the Main Program:**

   - Before defining functions, the program checks if it is being executed directly (not imported as a module).

   - If the script is run directly, it calls the `main` function to start the task manager.

In summary, this program serves as a basic task manager with a text-based interface. Users can create and manage tasks, specifying titles, descriptions, and reminder times. The tasks are displayed in a table format and can be saved to a CSV file upon exiting the program, allowing for task persistence between program runs. The program ensures that the user's input follows specific formats and provides a structured interface for task management.