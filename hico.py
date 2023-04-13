import logging
import os

import pandas as pd

from functions import *

Filepath = os.path.join(ROOT_DIR, 'Hico Group/data', 'Hico.csv')
df = readfile(Filepath)


def ReadData(rowIndex):
    global Exe
    Exe = df.Exe.values[rowIndex]
    logging.info("Exe: {}".format(Exe))

    global ID
    ID = df.ID.values[rowIndex]
    logging.info("ID: {}".format(ID))

    global PreID
    PreID = df.PreID.values[rowIndex]
    logging.info("PreID: {}".format(PreID))

    global PreReqStep
    PreReqStep = df.PreReqStep.values[rowIndex]
    logging.info("PreReqStep: {}".format(PreReqStep))

    global Description
    Description = df.Description.values[rowIndex]
    logging.info("Description: {}".format(Description))

    global Btn_AddEmployee
    Btn_AddEmployee = df.Btn_AddEmployee.values[rowIndex]
    logging.info("Btn_AddEmployee: {}".format(Btn_AddEmployee))

    global Btn_RemoveEmployee
    Btn_RemoveEmployee = df.Btn_RemoveEmployee.values[rowIndex]
    logging.info("Btn_RemoveEmployee: {}".format(Btn_RemoveEmployee))

    global Slc_EmployeeByNum
    Slc_EmployeeByNum = df.Slc_EmployeeByNum.values[rowIndex]
    logging.info("Slc_EmployeeByNum: {}".format(Slc_EmployeeByNum))

    global Fld_FirstNames
    Fld_FirstNames = df.Fld_FirstNames.values[rowIndex]
    logging.info("Fld_FirstNames: {}".format(Fld_FirstNames))

    global Fld_Surname
    Fld_Surname = df.Fld_Surname.values[rowIndex]
    logging.info("Fld_Surname: {}".format(Fld_Surname))

    global Drp_Salutation
    Drp_Salutation = df.Drp_Salutation.values[rowIndex]
    logging.info("Drp_Salutation: {}".format(Drp_Salutation))

    global Chk_Male
    Chk_Male = df.Chk_Male.values[rowIndex]
    logging.info("Chk_Male: {}".format(Chk_Male))

    global Chk_Female
    Chk_Female = df.Chk_Female.values[rowIndex]
    logging.info("Chk_Female: {}".format(Chk_Female))

    global Chk_Unspecified
    Chk_Unspecified = df.Chk_Unspecified.values[rowIndex]
    logging.info("Chk_Unspecified: {}".format(Chk_Unspecified))

    global Fld_EmployeeNum
    Fld_EmployeeNum = df.Fld_EmployeeNum.values[rowIndex]
    logging.info("Fld_EmployeeNum: {}".format(Fld_EmployeeNum))

    global Vld_FullName
    Vld_FullName = df.Vld_FullName.values[rowIndex]
    logging.info("Vld_FullName: {}".format(Vld_FullName))

    global Fld_GrossSalary
    Fld_GrossSalary = df.Fld_GrossSalary.values[rowIndex]
    logging.info("Fld_GrossSalary: {}".format(Fld_GrossSalary))

    global Chk_Green
    Chk_Green = df.Chk_Green.values[rowIndex]
    logging.info("Chk_Green: {}".format(Chk_Green))

    global Chk_Blue
    Chk_Blue = df.Chk_Blue.values[rowIndex]
    logging.info("Chk_Blue: {}".format(Chk_Blue))

    global Chk_Red
    Chk_Red = df.Chk_Red.values[rowIndex]
    logging.info("Chk_Red: {}".format(Chk_Red))

    global Chk_Default
    Chk_Default = df.Chk_Default.values[rowIndex]
    logging.info("Chk_Default: {}".format(Chk_Default))

    global Btn_Cancel
    Btn_Cancel = df.Btn_Cancel.values[rowIndex]
    logging.info("Btn_Cancel: {}".format(Btn_Cancel))

    global Btn_Save
    Btn_Save = df.Btn_Save.values[rowIndex]
    logging.info("Btn_Save: {}".format(Btn_Save))

    global Employee_UnqNum
    Employee_UnqNum = df.Employee_UnqNum.values[rowIndex]
    logging.info("Employee_UnqNum: {}".format(Employee_UnqNum))

    global EmployeesNum_table
    EmployeesNum_table = df.EmployeesNum_table.values[rowIndex]
    logging.info("EmployeesNum_table: {}".format(EmployeesNum_table))

    global FirstName_table
    FirstName_table = df.FirstName_table.values[rowIndex]
    logging.info("FirstName_table: {}".format(FirstName_table))

    global LastName_table
    LastName_table = df.LastName_table.values[rowIndex]
    logging.info("LastName_table: {}".format(LastName_table))

    global Salutation_table
    Salutation_table = df.Salutation_table.values[rowIndex]
    logging.info("Salutation_table: {}".format(Salutation_table))

    global ProfileColour_table
    ProfileColour_table = df.ProfileColour_table.values[rowIndex]
    logging.info("ProfileColour_table: {}".format(ProfileColour_table))


def Framework():
    if Exe == "P":
        logging.critical("What is happening? (Description) : {}".format(Description))
        logging.info("Do Something with Exe")
    else:
        logging.info("Exit loop Exe != P")
        return

    if pd.notna(Btn_AddEmployee):
        logging.info("Do Something with Btn_AddEmployee: {}".format(Btn_AddEmployee))
        clickOnElement("/html/body/div[1]/div/div/div/div[1]/div[2]/button[2]", By.XPATH, Btn_AddEmployee)

    if pd.notna(Btn_RemoveEmployee):
        logging.info("Do Something with Btn_RemoveEmployee: {}".format(Btn_RemoveEmployee))
        clickOnElement("/html/body/div[1]/div/div/div/div[1]/div[2]/button[1]", By.XPATH, Btn_RemoveEmployee)

    if pd.notna(Slc_EmployeeByNum):
        logging.info("Do Something with Slc_EmployeeByNum: {}".format(Slc_EmployeeByNum))
        clickOnElement(f"//td[normalize-space()='{Slc_EmployeeByNum}']", By.XPATH, Slc_EmployeeByNum)

    if pd.notna(Fld_FirstNames):
        logging.info("Do Something with Fld_FirstNames: {}".format(Fld_FirstNames))
        typeInElement("firstNames", By.ID, Fld_FirstNames)

    if pd.notna(Fld_Surname):
        logging.info("Do Something with Fld_Surname: {}".format(Fld_Surname))
        typeInElement("surname", By.ID, Fld_Surname)

    if pd.notna(Drp_Salutation):
        logging.info("Do Something with Drp_Salutation: {}".format(Drp_Salutation))
        selectFromDrpDwn("title", By.ID, Drp_Salutation)

    if pd.notna(Chk_Male):
        logging.info("Do Something with Chk_Male: {}".format(Chk_Male))
        clickOnElement("formHorizontalRadiosGender1", By.ID, Chk_Male)

    if pd.notna(Chk_Female):
        logging.info("Do Something with Chk_Female: {}".format(Chk_Female))
        clickOnElement("formHorizontalRadiosGender2", By.ID, Chk_Female)

    if pd.notna(Chk_Unspecified):
        logging.info("Do Something with Chk_Unspecified: {}".format(Chk_Unspecified))
        clickOnElement("formHorizontalRadiosGender3", By.ID, Chk_Unspecified)

    if pd.notna(Fld_EmployeeNum):
        logging.info("Do Something with Fld_EmployeeNum: {}".format(Fld_EmployeeNum))
        typeInElement("employeeNumber", By.ID, Fld_EmployeeNum)

    if pd.notna(Vld_FullName):
        logging.info("Do Something with Vld_FullName: {}".format(Vld_FullName))
        validateFldValue("fullName", By.ID, Vld_FullName)

    if pd.notna(Fld_GrossSalary):
        logging.info("Do Something with Fld_GrossSalary: {}".format(Fld_GrossSalary))
        typeInElement("salary", By.ID, Fld_GrossSalary)

    if pd.notna(Chk_Green):
        logging.info("Do Something with Chk_Green: {}".format(Chk_Green))
        clickOnElement("formHorizontalRadiosProfile1", By.ID, Chk_Green)

    if pd.notna(Chk_Blue):
        logging.info("Do Something with Chk_Blue: {}".format(Chk_Blue))
        clickOnElement("formHorizontalRadiosProfile2", By.ID, Chk_Blue)

    if pd.notna(Chk_Red):
        logging.info("Do Something with Chk_Red: {}".format(Chk_Red))
        clickOnElement("formHorizontalRadiosProfile3", By.ID, Chk_Red)

    if pd.notna(Chk_Default):
        logging.info("Do Something with Chk_Default: {}".format(Chk_Default))
        clickOnElement("formHorizontalRadiosProfile4", By.ID, Chk_Default)

    if pd.notna(Btn_Cancel):
        logging.info("Do Something with Btn_Cancel: {}".format(Btn_Cancel))
        clickOnElement("/html/body/div[1]/div/div/div/div[3]/div[2]/button[2]", By.XPATH, Btn_Cancel)

    if pd.notna(Btn_Save):
        logging.info("Do Something with Btn_Save: {}".format(Btn_Save))
        clickOnElement("/html/body/div[1]/div/div/div/div[3]/div[2]/button[1]", By.XPATH, Btn_Save)

    if pd.notna(EmployeesNum_table):
        logging.info("Do Something with EmployeesNum_table: {}".format(EmployeesNum_table))
        validateValue(f"//td[normalize-space()='{Employee_UnqNum}']", By.XPATH, EmployeesNum_table)

    if pd.notna(FirstName_table):
        logging.info("Do Something with FirstName_table: {}".format(FirstName_table))
        validateValue(f"//td[normalize-space()='{Employee_UnqNum}']/following-sibling::td", By.XPATH, FirstName_table)

    if pd.notna(LastName_table):
        logging.info("Do Something with LastName_table: {}".format(LastName_table))
        validateValue(f"//td[normalize-space()='{Employee_UnqNum}']/following-sibling::td/following-sibling::td", By.XPATH, LastName_table)

    if pd.notna(Salutation_table):
        logging.info("Do Something with Salutation_table: {}".format(Salutation_table))
        validateValue(f"//td[normalize-space()='{Employee_UnqNum}']/following-sibling::td/following-sibling::td/following-sibling::td", By.XPATH, Salutation_table)

    if pd.notna(ProfileColour_table):
        logging.info("Do Something with ProfileColour_table: {}".format(ProfileColour_table))
        validateValue(f"//td[normalize-space()='{Employee_UnqNum}']/following-sibling::td/following-sibling::td/following-sibling::td/following-sibling::td", By.XPATH, ProfileColour_table)


logging.info(
    "****************************************************************************     HICO START        ****************************************************************************")
# Get PreID RowIndex Number to use to speed up lookup for ReadData function.
PreID = sys.argv[0]
y = str(PreID)
logging.info("PREID TO USE: {}".format(PreID))
for i, cell in enumerate(df.PreID.values):
    if cell == y:
        rowIndex = i
        rowindex_print = rowIndex + 2  # this is to account for the two rows on top that are not used / you can tell which tow is running because of this
        ID = df.ID.values[rowIndex]
        # This print is to show where rowIndex x starts - reading data
        logging.info("\n ****** TEST CASE: {} ; TEST DATA ROW INDEX: {} START ****** \n".format(ID, rowindex_print))
        ReadData(rowIndex)
        # This print is to show where rowIndex x ends - reading data
        logging.info("\n ###### TEST CASE: {} ; TEST DATA ROW INDEX: {} END ###### \n".format(ID, rowindex_print))
        # This print is to show where rowIndex x starts - executing data
        logging.info("\n ****** TEST CASE: {} ; FRAMEWORK ROW INDEX: {} START ****** \n".format(ID, rowindex_print))
        Framework()
        # This print is to show where rowIndex x starts - executing data
        logging.info("\n ###### TEST CASE: {} ; FRAMEWORK ROW INDEX: {} END ###### \n".format(ID, rowindex_print))

logging.critical(
    "############################################################################            HICO COMPLETE              ############################################################################\n")
