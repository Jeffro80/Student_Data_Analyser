# Overview

The Student Data Analyser app analyses data extracted from the Student
Database. It returns statistics on the supplied data points.

## Inputs

The app takes in csv files containing raw data extracted from the Student
Database that is to be analysed.

## Outputs

The app outputs xls files containing the analysis results. Some data is also
printed to the screen.

## Version

Version Number 0.2  

App last updated 17 October 2018  
Readme last updated 2 November 2018

# Operation

- Place the required data files into the same directory as the app file
- Run the Student_Data_Analyser.py file from within Spyder or from the command
line
- Select the desired function from the menu
- Provide the names for any required files or press enter to open the Open file 
dialog
- Select the filtering option if one is required.

# Functions

## Age data

Analyses age data from the Student Database and returns statistics regarding
student age such as average, percentage of students in each age band and total
number of students in each age band.

### Required Files

- Student Data File
- Student Data Headings File

## Location Data

Analyses location data from the Student Database and returns statistics regarding
percentage of students in each city and the number of students.

### Required Files

- Student Data File
- Student Data Headings File

## Ethnicity Data

Analyses ethnicity data from the Student Database and returns statistics regarding
percentage of students in each ethnicity group and the number of students.

### Required Files

- Student Data File
- Student Data Headings File
- Pacific Island Nations File

## Employment Data

Analyses employment data from the Student Database and returns statistics regarding
percentage of students in each employment category and the number of students.

### Required Files

- Student Data File
- Student Data Headings File

## Study Reason Data

Analyses study reason data from the Student Database and returns statistics
regarding percentage of students identifying each study reason category and the
number of students.

### Required Files

- Student Data File
- Student Data Headings File

## How Heard Data

Analyses how heard data from the Student Database and returns statistics
regarding percentage of students identifying each category and the number of
students.

### Required Files

- Student Data File
- Student Data Headings File

## Average Length of Study

Analyses the average length of study for Online and Part time students and returns
the mean, median, max and min values for each.

### Required Files

- Enrolments File
- Graduates File

# Files used

## Enrolments File

### File Name

enrolments_XXX.csv where XXX is the sample source.

### Contents

Enrolment details for each student in the filtered group.

### Structure

CSV file with EnrolmentFK, StudentFK, TutorFK, ExpiryDate, Status and Tag for
each student.

### Source

qryXXXEnrolmentsData query from the Student Database. The XXX is the target
filtered group, e.g. All, Active, Maori etc.

### Notes

Make sure the StartDate and ExpiryDate columns are in the format DD/MM/YYYY.

## Graduates File

### File Name

graduates.csv

### Contents

Graduates details.

### Structure

CSV file with GraduateFK, EnrolmentFK, GraduationDate and CertificateNumber.

### Source

Graduates table of the Student Database.

### Notes

Make sure the GraduationDate column is in the format DD/MM/YYYY.

## Pacific Island Nations File

### File Name

pacific_island_nations.txt

### Contents

Each Pacific Island nation.

### Structure

TXT file with each Pacific Island nation listed in a single line, separated by
commas with no spaces after the comma.

### Source

Created at app set up and updated as required.

## Student Data File

### File Name

XXX_student_data.csv where XXX is the sample source.

### Contents

Data on each student enrolment taken from the database.

### Structure

CSV file with the following column headings: StudentPK,NameGiven,NameSurname,
Gender,DateOfBirth,AddressCity,AddressCountry,Ethnicity,EnrolmentPK,CourseFK,
StartDate,ExpiryDate,Status,Employment,ReasonForStudy,HowHeard

### Source

qryXXXStudentsData query from the Student Database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

### Notes

Make sure the DateOfBirth, StartDate and ExpiryDate columns are in the format
DD/MM/YYYY.

## Student Data Headings File

### File Name

data_headings.txt

### Contents

Each column heading for data in XXX_student_data file.

### Structure

TXT file with each column heading on one line, separated by commas.

### Source

Column headings extracted from qryXXXStudentsData query from the Student
Database. 

# Dependencies

The following third-party libraries are imported and therefore are required for
the app to run:

- admintools from custtools
- databasetools from custtools
- datetools from custtools
- filetools from custtools

# Development

## Known bugs

## Items to fix

## Current development step

- Combine count and % outputs into one save file: item - % - #

## Required development steps

- 

## Future additions

- Function that generates the age band values (currently done manually)
- Move calculate_percent to a module and add check that values are int
- Move total_dict_values to a module and add check that values are int
- Calculations of age at enrolment - use enrolment date rather than today