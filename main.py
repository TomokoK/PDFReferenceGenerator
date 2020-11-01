#
# Generates a collection of references in PDF files
# Continuation of PDFAnalytics program
# 2020=11=01
# Contact: TomokoK @ Github
#

# from PyPDF2 import PdfFileReader
from os import listdir
from os.path import isfile, join
import sys
import csv


def main():
    # Verify we have all the data
    # Get a list of files in the pdfs dir
    pdfsInDirectory = [f for f in listdir("./pdfs") if isfile(join("./pdfs", f))]

    # Remove non-pdfs from pdf list
    for i in pdfsInDirectory:
        if i == "mvPDFs.sh" or i == "getPDFs.sh":
            pdfsInDirectory.remove(i)

    # Format list to just the year value
    for i in range(len(pdfsInDirectory)):
        pdfsInDirectory[i] = pdfsInDirectory[i].split("-")[0]

    # Get a list of the years of our reference PDF data
    referenceDataYears = []
    with open('referenceData.csv') as csvInput:
        csvReader = csv.reader(csvInput, delimiter=',')
        for lines in csvReader:
            yearData = lines[0]  # Get first column data
            referenceDataYears.append(yearData)
    referenceDataYears.remove(referenceDataYears[0])  # Remove 'years' descriptor

    # Format list to just the year value
    for i in range(len(referenceDataYears)):
        referenceDataYears[i] = referenceDataYears[i].split("-")[0]

    # Order each list from old to new
    referenceDataYears.sort()
    pdfsInDirectory.sort()

    # Make sure our data matches
    if pdfsInDirectory == referenceDataYears:
        print("Data looks to be okay...")
    else:
        print("ERROR: Data mismatch.")
        sys.exit()


if __name__ == "__main__":
    main()
