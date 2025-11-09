# computer-infrastructure-assessment
Faolán Hamilton's Computer Infrastructure Assessment repository 2025

## To view this repository in codesspaces, follow the steps below:

1. Go to the repository page in your browser (https://github.com/FaolanH/computer-infrastructure-assessment)
2. At the top right of the page you will see an option to Sign in or Sign up. If you don't have one already, sign up for a free GitHub account.
3. Click the green 'Code' button.
4. Click the 'Codespaces' tab
5. Click 'Create New Codespace' on main

## Technologies used

- Python
- ipython (https://ipython.readthedocs.io/en/stable/)
- Git
- GitHub
- Codespaces
- Jupyter

## Modules used

For more information on the modules, please click on the documentation links below
- datetime - used to format dates and time inputs (https://docs.python.org/3/library/datetime.html)
- Pandas - used to create dataframes (https://pandas.pydata.org/docs/)
- Matplotlib - used to plot data (https://matplotlib.org/stable/api/pyplot_summary.html)
- yfinance - used to generate stock data (https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html)

## Problems

There were 4 problems to be solved in this assignment, broken down into three steps: 
- Name the Problem, 
- Describe the Problem,
- Solve the Problem.

These problems are outlined below:

### Problem 1: Data from yfinance
Using the yfinance Python package, write a function called get_data() that downloads all hourly data for the previous five days for the five FAANG stocks:

Facebook (META)
Apple (AAPL)
Amazon (AMZN)
Netflix (NFLX)
Google (GOOG)
The function should save the data into a folder called data in the root of your repository using a filename with the format YYYYMMDD-HHmmss.csv where YYYYMMDD is the four-digit year (e.g. 2025), followed by the two-digit month (e.g. 09 for September), followed by the two digit day, and HHmmss is hour, minutes, seconds. Create the data folder if you don't already have one.

### Problem 2: Plotting Data
Write a function called plot_data() that opens the latest data file in the data folder and, on one plot, plots the Close prices for each of the five stocks. The plot should include axis labels, a legend, and the date as a title. The function should save the plot into a plots folder in the root of your repository using a filename in the format YYYYMMDD-HHmmss.png. Create the plots folder if you don't already have one.

### Problem 3: Script
Create a Python script called faang.py in the root of your repository. Copy the above functions into it and it so that whenever someone at the terminal types ./faang.py, the script runs, downloading the data and creating the plot. Note that this will require a shebang line and the script to be marked executable. Explain the steps you took in your notebook.

### Problem 4: Automation
Create a GitHub Actions workflow to run your script every Saturday morning. The script should be called faang.yml in a .github/workflows/ folder in the root of your repository. In your notebook, explain each of the individual lines in your workflow.
