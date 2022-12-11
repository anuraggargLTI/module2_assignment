# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path
import questionary


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
"""
helper function to save qualifying loan data to a csv file
function takes user input for the file location and saves the data
"""
def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    #Given that no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit
    if(len(qualifying_loans)>0):
        #AC1: Given that I’m using the loan qualifier CLI, when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.
        decision_to_save = questionary.text("do you want to save qualifying loans in a csv file - y/n?").ask()
        #AC3 : Given that I have a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file
        if(decision_to_save=='y' or decision_to_save=='Y'):
          #AC4: Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.
          location_to_save = questionary.text("please provide the file location").ask()
          #AC5: Given that I’m using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.
          csvpath = Path(location_to_save)
          with open(csvpath,'w') as csvfile:
                csvwriter = csv.writer(csvfile) 
                header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
                csvwriter.writerow(header)
                for row_items in qualifying_loans:
                    csvwriter.writerow(row_items)
        else:
            print("Thank you for using the loan qualifier application")
    else:
        print("Sorry there is no qualifying bank loan")
 