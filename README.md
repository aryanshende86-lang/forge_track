# forge_track
week 1 "personal tracker"
# PERSONAL EXPENSE TRACKER
 This is a simple command-line expense tracker written in Python. No apps, no internet, no account — you just run the script and start logging your spending. It's meant to be quick and no-nonsense.
# HOW TO USE IT ??
 Make sure you have Python installed, then just run:
    python expense_tracker-2.py
That's it. A small menu shows up and you can start from there.
# STORAGE OF DATA
Everything gets saved in a plain text file called data.txt in the same folder as the script. Each expense is written as one line in comma-separated format — date, category, amount, note. Nothing gets sent anywhere. Your data stays on your machine.
# FEATURES
1. Add an expense
2. View all expense
3. Filter by category
4. Exit

# ADD AN EXPENSE
You'll be asked to fill in four things:
•	Date (in DD/MM/YY format)
•	Amount — if you type something that isn't a number, it'll ask you to try again
•	Category — pick from Food, Transport, Entertainment, or Other. Type anything outside these and it defaults to Other
•	Note — optional. Just hit 'n' to skip it and a dash gets saved instead.

<img width="650" height="328" alt="image" src="https://github.com/user-attachments/assets/62d92a61-08f9-4be0-bdb2-b4103ef74ef5" />

# VIEW ALL EXPENSE
Pulls up every expense you've ever logged in a clean bordered table — date, category, amount, and note all lined up neatly. The grand total shows at the bottom.

<img width="1396" height="367" alt="image" src="https://github.com/user-attachments/assets/89f18102-db2d-47d5-8953-511f79095852" />

# FILTER BY CATEGORY
If you only want to see what you spent on food, or just transport — this is the option. Type the category name and it shows only those entries with a subtotal at the bottom. Pretty handy for checking where most of your money is leaking.

<img width="946" height="377" alt="image" src="https://github.com/user-attachments/assets/ada8650c-040d-4da2-897d-5968b36adb12" />

# EXIT
Closes the program. 

# REQUIREMNTS TO USE THIS TRACKER
•	Python 3.x
•	No external libraries needed — runs on Python's built-in tools only
•	A terminal / command prompt

# FILE STRUCTURE
After running the script at least once, your folder will look like this:
    expense_tracker-2.py    ← the main script
    data.txt                ← where all your expenses get saved




