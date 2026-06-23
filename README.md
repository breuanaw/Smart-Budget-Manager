Smart Budget Manager
Video Demo: ???
Description:

Smart Budget Manager is a Python application designed to help users manage their personal finances by tracking income, expenses, and monthly budgets. The purpose of this project is to provide a simple but effective way for users to monitor their spending habits and better understand where their money is going. Many people struggle with budgeting, and this application helps organize financial information in one convenient location.

The program begins with a menu-driven interface that allows the user to select different options. Users can add their monthly income, record expenses, view a budget summary, and save their information for future use. The application uses file handling to store information in a JSON file, which allows the data to remain available even after the program closes.

The project was created using Python and incorporates several programming concepts learned throughout the course. These concepts include functions, loops, conditionals, dictionaries, lists, file handling, exception handling, and user input validation. The project is more advanced than the individual labs completed during the course because it combines multiple concepts into a complete working application.

Files Included

TermProject.py

This is the main Python program file. It contains all functions used by the application, including the menu system and budgeting features. The file contains the following functions:

main()
load_data()
save_data()
add_income()
add_expense()
view_summary()

The main function controls the program flow and presents the user menu. The additional functions each perform a specific task to keep the program organized and easy to maintain.

requirements.txt

This file lists any required libraries. Since the project only uses Python's built-in json module, no additional external libraries are required.

budget_data.json

This file is automatically created by the application when data is saved. It stores the user's income and expense information between sessions.

README.md

This file explains the purpose of the project, describes the files included, and discusses important design decisions.

Design Decisions

One of the most important design decisions was selecting a project that would be practical and useful in everyday life. Personal budgeting is a challenge for many people, making it an ideal topic for a software project. The application was designed to be simple enough for beginners to use while still demonstrating multiple programming skills.

Functions were used extensively throughout the program because they improve readability and organization. Instead of placing all code inside the main function, separate functions were created to handle loading data, saving data, adding income, adding expenses, and generating reports. This modular approach makes the code easier to understand and maintain.

JSON was selected as the storage format because it is lightweight, human-readable, and easy to work with in Python. Using JSON eliminates the need for a database while still allowing data to persist between program executions.

Exception handling was added when loading data. If the data file does not exist, the program automatically creates a default structure instead of crashing. This improves the user experience and makes the application more reliable.

Future Improvements

There are many possible improvements that could be added to future versions of the project. Expense categories could be added to organize spending into groups such as food, transportation, utilities, and entertainment. Graphical charts could be generated to visualize spending habits. The application could also support recurring bills, monthly reports, and exporting information to Excel spreadsheets.

Another possible enhancement would be the addition of a graphical user interface using Tkinter. This would make the application more visually appealing and easier for non-technical users to navigate.

Overall, Smart Budget Manager demonstrates the practical application of Python programming concepts while providing a useful financial management tool for users.