#importing the pandas library
import pandas as pd

#getting the list csv file
CSV_dataFrame = pd.read_csv('employeedata.csv')

#getting the list excel file
Excel_dataFrame = pd.read_excel('employeedata.xlsx')


#function for changing the employee emails in both csv and xlsx files respectively
def EmailChanger(Email):
    Email = str(Email[0:Email.index('@')] + '@handsinhands.org')
    return Email


#changing the employee emails in both csv and xlsx files respectively
CSV_dataFrame['Email'] = CSV_dataFrame['Email'].apply(EmailChanger)
Excel_dataFrame['Email'] = Excel_dataFrame['Email'].apply(EmailChanger)


#saving the changes made to both csv and xlsx files respectively
CSV_dataFrame.to_csv('employeedata.csv')
Excel_dataFrame.to_excel('employeedata.xlsx')
