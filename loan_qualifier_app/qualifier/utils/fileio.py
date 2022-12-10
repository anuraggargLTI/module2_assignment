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
    if(len(qualifying_loans)>0):
        decision_to_save = questionary.text("do you want to save qualifying loans in a csv file - y/n?").ask()
        if(decision_to_save=='y' or decision_to_save=='Y'):
          location_to_save = questionary.text("please provide the file location").ask()
         # if(Path(location_to_save).exists()):
        csvpath = Path(location_to_save)
        with open(csvpath,'w') as csvfile:
                csvwriter = csv.writer(csvfile) 
                header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
                csvwriter.writerow(header)
                for row_items in qualifying_loans:
                    csvwriter.writerow(row_items)
          #else:
          #  print("Sorry you have not specified the location correctly")
 