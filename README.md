Data Analysis Python Code Examples

This repository contains a collection of Python code examples for data analysis. The code examples use popular libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.

Code Examples

1. Load and Explore Data
The first code example demonstrates how to load and explore data using the Pandas library. The code loads a CSV file into a Pandas DataFrame and then displays the first few rows and summary statistics for numerical columns in the DataFrame. It also counts the number of rows and selects a subset of the data based on a condition. This code is helpful in getting an initial understanding of the data and its distribution.

2. Data Visualization
The second code example demonstrates how to create visualizations using Matplotlib and Seaborn libraries. The code creates different types of visualizations such as line chart, scatter plot, bar chart, and heatmap. These visualizations help to gain insights and communicate findings from the data analysis.

3. Data Preprocessing
The third code example demonstrates how to preprocess data using Scikit-learn library. The code shows how to standardize the data to have zero mean and unit variance, encode categorical variables as dummy variables, and split the data into training and testing sets. These preprocessing techniques are essential for preparing data to be used in machine learning algorithms.

4. Percentage.  This Python code calculates the weighted grade percentage for a student's midterm and final exam scores, based on the specified weights for each exam type. The program prompts the user to input the two exam scores, and then calculates and displays the weighted percentages and total grade percentage. The program allows the user to input new values and recalculate the grade percentage, or terminate the program.

5. combine_excel_FILE_IN_A_Folder. This code combines multiple Excel files into a single Excel file with one sheet. It does this by first setting the directory path where the Excel files are stored. Then it reads each Excel file and creates a dictionary of DataFrames, one for each sheet. It adds a column to identify the sheet name and file name for each DataFrame, and then appends them to a list. Finally, it concatenates all the DataFrames into a single DataFrame and writes it to a new Excel file. The output file path is specified by the user.

6. Automated Email System.This Python code uses the pandas library to load student grade data from an Excel file, groups the data by student ID and email address, generates an email for each student with their grade report, and sends the email using the smtplib library. The email message is created using the email.mime.text and email.mime.multipart libraries. The code allows for custom email addresses to be used for sending and receiving the emails.
