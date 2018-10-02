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
App last updated 25 September 2018  
Readme last updated 3 October 2018

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

- Date of birth file

## Location Data

Analyses location data from the Student Database and returns statistics regarding
percentage of students in each city and the number of students.

### Required Files

- Cities file

## Ethnicity Data

Analyses ethnicity data from the Student Database and returns statistics regarding
percentage of students in each ethnicity group and the number of students.

### Required Files

- Ethnicities file
- Pacific Island Nations file

## Employment Data

Analyses employment data from the Student Database and returns statistics regarding
percentage of students in each employment category and the number of students.

### Required Files

- Employment file

## Study Reason Data

Analyses study reason data from the Student Database and returns statistics
regarding percentage of students identifying each study reason category and the
number of students.

### Required Files

- Study Reason file

## How Heard Data

Analyses how heard data from the Student Database and returns statistics
regarding percentage of students identifying each category and the number of
students.

### Required Files

- How Heard file

## Average Length of Study

Analyses the average length of study for Online and Part time students and returns
the mean, median, max and min values for each.

### Required Files

- Enrolments file
_ Graduates file

# Files used

## Cities file

### File Name

cities_XXX.csv where XXX is the sample source.

### Structure

CSV file with the Student ID, AddressCity and AddressCountry for each student.

### Contents

Student ID, AddressCity and AddressCountry for each student in the filtered group.

### Source

qryXXXStudentsData query from the Student Database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

## Date of Birth file

### File Name

births_XXX.csv where XXX is the sample source.

### Structure

CSV file with the Student ID and DateOfBirth for each student.

### Contents

Student ID and DateOfBirth for each student in the filtered group.

### Source

qryXXXStudentsData query from the Student Database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

### Notes

Make sure the DateOfBirth column is in the format DD/MM/YYYY.

## Employment file

### File Name

employment_XXX.csv where XXX is the sample source.

### Structure

CSV file with the Student ID and Employment for each student.

### Contents

Student ID and Employment for each student in the filtered group.

### Source

qryXXXStudentsData query from the Student Database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

## Enrolments file

### File Name

enrolments_XXX.csv where XXX is the sample source.

### Structure

CSV file with EnrolmentFK, StudentFK, TutorFK, ExpiryDate, Status and Tag for
each student.

### Contents

Enrolment details for each student in the filtered group.

### Source

qryXXXEnrolmentsData query from the Student Database. The XXX is the target
filtered group, e.g. All, Active, Maori etc.

### Notes

Make sure the StartDate and ExpiryDate columns are in the format DD/MM/YYYY.

## Ethnicities file

### File Name

ethnicity_XXX.csv where XXX is the sample source.

### Structure

CSV file with the Student ID and Ethnicity for each student.

### Contents

Student ID and Ethnicity for each student in the filtered group.

### Source

qryXXXStudentsData query from the Student Database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

## Graduates file

### File Name

graduates.csv

### Structure

CSV file with GraduateFK, EnrolmentFK, GraduationDate and CertificateNumber.

### Contents

Graduates details.

### Source

Graduates table of the Student Database.

### Notes

Make sure the GraduationDate column is in the format DD/MM/YYYY.

## How Heard file

### File Name

how_heard_XXX.csv where XXX is the sample source.

### Structure

CSV file with the Student ID and HowHeard for each student.

### Contents

Student ID and HowHeard for each student in the filtered group.

### Source

qryXXXStudentsData query from the student database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

## Pacific Island Nations file

### File Name

pacific_island_nations.txt

### Structure

TXT file with each Pacific Island nation listed in a single line, separated by
commas with no spaces after the comma.

### Contents

Each Pacific Island nation.

### Source

Created at app set up and updated as required.

## Study Reason file

### File Name

study_reason_XXX.csv where XXX is the sample source.

### Structure

CSV file with the Student ID and ReasonForStudy for each student.

### Contents

Student ID and ReasonForStudy for each student in the filtered group.

### Source

qryXXXStudentsData query from the Student Database. The XXX is the target filtered
group, e.g. All, Active, Maori etc.

# Dependencies

The following third-party libraries are imported and therefore are required for
the app to run:

- admintools from custtools
- databasetools from custtools
- datetools from custtools
- filetools from custtools

# Development

## Known bugs

- Doubling up of print statements for saved files
- How Heard output is garbled

## Items to fix

- Remove doubling up of saved file print statements
- Correct How Heard output

## Current development step

- Fix bugs

## Required development steps

- 

## Future additions

- Function that generates the age band values (currently done manually)
- Move calculate_percent to a module and add check that values are int
- Move total_dict_values to a module and add check that values are int
- Calculations of age at enrolment - use enrolment date rather than today