# Student Data Analyser
# Version 0.21 15 November 2018
# Created by Jeff Mitchell
# Analyses student data extracted from the Student Database


import custtools.admintools as ad
import custtools.databasetools as db
import custtools.datetools as da
import custtools.filetools as ft
import numpy as np
import pandas as pd
import re
import sys


def calculate_percent(source_dict):
    """Calculate the percentage value of each key.
    
    Calcualtes the % value of each key value within the whole dictionary.
    Adds all of the key values together to get the total and then divides each
    key value by this total to get its % of the whole. Returns the results
    in a dictionary that has its keys copied from the source_dict and its
    values as the repsective percentages.
    
    Args:
        source_dict (dict): Dictionary that has int for each key value.
        
    Returns:
        percentage_dict (dict): Dictionary holding the % of each key value.
        total (int): Total number of students in sample.
    """
    # Create a copy of the source_dict with each key value set to 0
    percent_dict = ad.copy_dict_reset(source_dict)
    # Get the total of all key values
    total = total_dict_values(source_dict)
    # Get percentage for each key value
    for key, value in source_dict.items():
        if ad.check_is_int(value):
            percent_dict[key] = round(((value/total)*100), 2)
    return percent_dict, total
    

def convert_ages(ages, age_bands, age_band_values):
    """Convert a list of ages to a list of age band values.
    
    Takes each age item in a list and appends it to a new list as an age band
    value that it correspnds to.
    
    Args:
        ages (list): List of age values.
        age_bands (list): List of age bands as strings. Age bands must be
        discrete e.g. 0-17, 18-24,...
        age_band_values (list): List of age band values to be used. The final
        age (which is followed by a '+', e.g. 65+ is ignored). 
    
    Returns:
        converted_ages (list): List of converted age band values.
    """
    # Get the number of age bands
    num_bands = int(len(age_band_values)/2)
    # Get position of final 
    final_band = len(age_bands) - 1
    converted_ages = []
    # Find the band for each age value and add to list
    for age in ages: 
        band = 0
        lower = 0
        upper = 1
        while band < num_bands:
            # Check if age is in current age band range
            if age >= age_band_values[lower] and age <= age_band_values[upper]:
                converted_ages.append(age_bands[band])
                #print('Age {} is in age band {}'.format(age, age_bands[band]))
                break
            else:
                # Check for next age band
                band += 1
                # Increase lower limit by 2 to check next age band
                lower += 2
                # Increase upper limit by 2 to check next age band
                upper += 2
        # Check if age is higher than upper limit of last band range
        if band == num_bands:
            converted_ages.append(age_bands[final_band])
            #print('Age {} is in age band {}'.format(age,
                  #age_bands[final_band]))
    return converted_ages   


def get_course_type(course_code):
    """Returns course type.
    
    Returns the course type that is the two letter code in the middle of the
    course code.
    
    Args:
        course_code (str): Code for the course.
        
    Returns:
        type (str): Two letter course type code.
    """
    if re.search('.+-ON-.+', course_code):
        return 'ON'
    elif re.search('.+-PT-.+', course_code):
        return 'PT'
    else:
        return ''


def get_sample():
    """Return user input for source of data.
    
    Returns:
        source (str): User selection for source of data.
    """
    repeat = True
    high = 8
    while repeat:
        sample_menu()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between 1 and {}.'.format(high))
        else:
            if action < 1 or action > high:
                print('\nPlease select from the available options (1 - {})'
                      .format(high))
            elif action == 1:
                return 'All'
            elif action == 2:
                return 'Active'
            elif action == 3:
                return 'Expired'
            elif action == 4:
                return 'Maori'
            elif action == 5:
                return 'Pasifika'
            elif action == 6:
                return 'Graduated'
            elif action == 7:
                return 'Withdrawn'
            elif action == 8:
                return 'Other'


def get_threshold_items(data, threshold, above=True):
    """Return a list of keys and values that have value above a threshold.
    
    Returns those keys that are equal or above a threshold. If above=False then
    returns those keys whose values are equal or below the threshold. Threshold
    must be an int or float.
    
    Args:
        data (list): List of tuples that has int or floats for values.
        threshold (int / float): Threshold to check against. Values equal to
        the threshold are also returned.
        above (bool): Whether to return values above or below the threshold.
    
    Returns:
        threshold_items (list): List of tuples containing the returned values.
    """
    threshold_list = []
    # Return values equal or above threshold
    if above:
        for pair in data:
            if pair[1] >= threshold: # Check value higher than threshold
                threshold_list.append(pair)
    # Return values equal or below threshold
    else:
        for pair in data:
            if pair[1] <= threshold: # Check value lower than threshold
                threshold_list.append(pair)
    return threshold_list


def get_threshold_items_old(data, threshold, above=True):
    """Return a dictionary with keys that have value above a threshold.
    
    Returns those keys that are equal or above a threshold. If above=False then
    returns those keys whose values are equal or below the threshold. Threshold
    must be an int or float.
    
    Args:
        data (dict): Dictionary that has int or floats for values.
        threshold (int / float): Threshold to check against. Values equal to
        the threshold are also returned.
        above (bool): Whether to return values above or below the threshold.
    
    Returns:
        threshold_items (dict): Dictionary containing the returned values.
    """
    threshold_dict = {}
    # Return values equal or above threshold
    if above:
        for k, v in data.items():
            if v >= threshold:
                threshold_dict[k] = v
    # Return values equal or below threshold
    else:
        for k, v in data.items():
            if v <= threshold:
                threshold_dict[k] = v
    return threshold_dict


def help_age_data():
    """Print Age Data help information"""
    # To be written


def help_employment_data():
    """Print Employment Data help information"""
    # To be written


def help_ethnicity_data():
    """Print Ethnicity Data help information"""
    # To be written


def help_heard_data():
    """Print How Heard Data help information"""
    # To be written


def help_location_data():
    """Print Location Data help information"""
    # To be written


def help_menu():
    """Display the requested help information."""
    repeat = True
    low = 1
    high = 7
    while repeat:
        try_again = False
        help_menu_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                help_age_data()
            elif action == 2:
                help_location_data()
            elif action == 3:
                help_ethnicity_data()
            elif action == 4:
                help_employment_data()
            elif action == 5:
                help_reason_study_data()
            elif action == 6:
                help_heard_data()
            elif action == high:
                repeat = False
        if not try_again:
            repeat = ad.check_repeat_help()


def help_menu_message():
    """Display the help menu options."""
    print('\nPlease enter the number for the item you would like help on:\n')
    print('1: Age Data')
    print('2: Location Data')
    print('3: Ethnicity Data')
    print('4: Employment Data')
    print('5: Reason for Study Data')
    print('6: How Heard Data')
    print('7: Exit Help Menu')
                
                
def help_reason_study_data():
    """Print Reason for Study Data help information"""
    # To be written


def list_nan(item):
    """Return NaN if item is empty.
    
    Args:
        item (str): Item to be checked.
        
    Returns:
        (str): NaN if item is empty, item otherwise.
    """
    if item in (None, ''):
        return np.nan
    else:
        return item


def list_unknown(item):
    """Return 'Unknown' if item is empty.
    
    Args:
        item (str): Item to be checked.
        
    Returns:
        (str): 'Unknown' if item is empty, item otherwise.
    """
    if item in (None, ''):
        return 'Unknown'
    else:
        return item


def main():
    repeat = True
    low = 1
    high = 9
    while repeat:
        try_again = False
        main_message()
        try:
            action = int(input('\nPlease enter the number for your '
                               'selection --> '))
        except ValueError:
            print('Please enter a number between {} and {}.'.format(low, high))
            try_again = True
        else:
            if action < low or action > high:
                print('\nPlease select from the available options ({} - {})'
                      .format(low, high))
                try_again = True
            elif action == low:
                help_menu()
            elif action == 2:
                process_age_data()
            elif action == 3:
                process_location_data()
            elif action == 4:
                process_ethnicity_data()
            elif action == 5:
                process_employment_data()
            elif action == 6:
                process_study_reason_data()
            elif action == 7:
                process_how_heard_data()
            elif action == 8:
                process_study_length()
            elif action == high:
                print('\nIf you have generated any files, please find them '
                      'saved to disk. Goodbye.')
                sys.exit()
        if not try_again:
            repeat = ad.check_repeat()
    print('\nPlease find your files saved to disk. Goodbye.')


def main_message():
    """Print the menu of options."""
    print('\n\n*************==========================*****************')
    print('\nStudent Data Analyser version 0.21')
    print('Created by Jeff Mitchell, 2018')
    print('\nOptions:')
    print('\n1. Help Menu')
    print('2. Age Data')
    print('3. Location Data')
    print('4. Ethnicity Data')
    print('5. Employment Data')
    print('6. Study Reason Data')
    print('7. How Heard Data')
    print('8. Average Length of Study')
    print('9. Exit')


def process_age_data():
    """Process Age Data."""
    warnings = ['\nProcessing Age Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing Age Data.')
    # Confirm the required files are in place
    required_files = ['Student Data File', 'Student Data Headings File']
    ad.confirm_files('Student Data', required_files)
    # Load Student data
    student_data = ft.get_csv_fname_load('Student Data File')
    # Load headings file
    data_headings = ft.load_headings('data_headings.txt')
    # Place data into a DataFrame
    birth_df = pd.DataFrame(data = student_data, columns = data_headings)
    # Drop unnecessary columns
    age_col = 'Age'
    sid_col = 'StudentPK'
    dob_col = 'DateOfBirth'
    headings = [sid_col, dob_col]
    birth_df =  birth_df[headings]
    # Remove duplicate Student ID Numbers
    birth_df.drop_duplicates(sid_col, 'first', True)
    # Remove students without a Date of Birth
    # Set empty Date of Birth values to NaN and then drop
    birth_df[dob_col] = birth_df[dob_col].apply(list_nan)
    birth_df.dropna(subset=[dob_col], inplace=True)
    # Convert Date of Birth column to timestamps
    birth_df[dob_col] = birth_df[dob_col].apply(da.convert_to_datetime, args=
            ('%d/%m/%Y',))
    # Convert Date of Birth column to Age and rename column
    birth_df[dob_col] = birth_df[dob_col].apply(da.calculate_age)
    birth_df = birth_df.rename(columns = {dob_col:age_col})
    # Calculate average age
    average_age = int(birth_df[age_col].mean())
    # Create a dictionary to hold the number of students in each age group
    age_bands = ['0-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    age_band_values = [0, 17, 18, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65]
    count_ages_dict = ad.create_dict(age_bands)
    # Update ages_dict with counts for each age
    # Get each age value in a list
    ages = birth_df[age_col].tolist()
    # Convert ages to age bands
    converted_ages = convert_ages(ages, age_bands, age_band_values)
    # print(converted_ages)
    # Update the ages_dict
    count_ages_dict = update_dict_counts(count_ages_dict, converted_ages)
    # print(count_ages_dict)
    # Create dict to hold the percentages of each age group
    percent_ages_dict, total = calculate_percent(count_ages_dict)
    # Get from user the sample source
    sample = get_sample()
    # Display results
    print('\nAverage age of {} students: {}'.format(sample, average_age))
    print('\nTotal number of {} students in sample: {}'.format(sample, total))
    print('\nPercentage of {} students by Age Group:\n'.format(sample))
    print("{:10} {:7}".format('Age Band', 'Percent'))
    for k, v in percent_ages_dict.items():
        print("{:10} {:7}%".format(k, v))
    # Save percentage results
    perc_name = '{}_Ages_Percentage_{}.csv'.format(sample,
                 ft.generate_time_string())
    ft.csv_dict_save_single_row(percent_ages_dict, perc_name)
    # State name of saved file
    print('\nPercentage results saved to {}'.format(perc_name))
    # Save group totals results
    total_name = '{}_Ages_Group_Totals_{}.csv'.format(sample,
                 ft.generate_time_string())
    ft.csv_dict_save_single_row(count_ages_dict, total_name)
    # State name of saved file
    print('Group Total results saved to {}'.format(total_name))
    ft.process_warning_log(warnings, warnings_to_process)


def process_employment_data():
    """Process Employment Data."""
    warnings = ['\nProcessing Employment Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing Employment Data.')
    # Confirm the required files are in place
    required_files = ['Student Data File', 'Student Data Headings File']
    ad.confirm_files('Student Data', required_files)
    # Load Student data
    student_data = ft.get_csv_fname_load('Student Data File')
    # Load headings file
    data_headings = ft.load_headings('data_headings.txt')
    # Place data into a DataFrame
    employment_df = pd.DataFrame(data = student_data, columns = data_headings)
    # Drop unnecessary columns
    sid_col = 'StudentPK'
    employment_col = 'Employment'
    headings = [sid_col, employment_col]
    employment_df = employment_df[headings]
    # Remove duplicate Student ID Numbers
    employment_df.drop_duplicates(sid_col, 'first', True)
    # Convert students without an Employment entry to 'Unknown'
    employment_df[employment_col] = employment_df[employment_col].apply(
            list_unknown)
    # Get a list of unique employment entries
    unique_emp = employment_df[employment_col].unique()
    # Create a dictionary to hold count of employment types and populate
    count_employ_dict = ad.create_dict(unique_emp)
    # Get each employment type in a list
    employment = employment_df[employment_col].tolist()
    count_employ_dict = update_dict_counts(count_employ_dict, employment)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    count_employ_list = ad.sort_dict_values(count_employ_dict,'descending')
    # Create dict to hold the percentages of each employment type
    percent_employ_dict, total = calculate_percent(count_employ_dict)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    percent_employ_list = ad.sort_dict_values(percent_employ_dict,'descending')
    # Get from user the sample source
    sample = get_sample()
    # Display results
    print('\nPercentage of {} students by Emplyment Type:\n'.format(sample))
    print("{:20} {:7}".format('Employment', 'Percent'))
    for x in percent_employ_list:
        print("{:20} {:7}%".format(x[0], x[1]))
    # Get a list of tuples with just results over 1%
    threshold = 1
    threshold_employ_list = get_threshold_items(percent_employ_list, threshold)
    print('\nThe Employment Types above the {}% threshold are as follows:\n'
          .format(threshold))
    print("{:20} {:7}".format('Employment', 'Percent'))
    for x in threshold_employ_list:
        print("{:20} {:7}%".format(x[0], x[1]))
    print('\nTotal number of {} students in sample: {}\n'.format(sample, total))
    # Save all employment % to a CSV file, each key:value on a separate line
    headings = ['Employment', 'Percent']
    f_name = '{}_Employment_Percentage_'.format(sample) 
    ft.save_list_csv(percent_employ_list, headings, f_name)
    print('')
    # Save threshold employment type with each key:value on a separate line
    f_name = '{}_Top_Employment_Percentage_'.format(sample) 
    ft.save_list_csv(threshold_employ_list, headings, f_name)
    print('')
    # Save all employment type counts to a CSV file
    headings = ['Employment', 'Count']
    f_name = '{}_Employment_Count_'.format(sample) 
    ft.save_list_csv(count_employ_list, headings, f_name)
    ft.process_warning_log(warnings, warnings_to_process)


def process_ethnicity_data():
    """Process Ethnicity Data."""
    warnings = ['\nProcessing Ethnicity Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing Ethnicity Data.')
    # Confirm the required files are in place
    required_files = ['Student Data File', 'Student Data Headings File',
                      'Pacific Island Nations File']
    ad.confirm_files('Student Data', required_files)
    # Load Pacific Island Nations File
    island_nations = ft.load_headings('pacific_island_nations.txt')
    # Load ethincities data
    student_data = ft.get_csv_fname_load('Student Data File')
    # Load headings file
    data_headings = ft.load_headings('data_headings.txt')
    # Place data into a DataFrame
    ethnicities_df = pd.DataFrame(data = student_data, columns = data_headings)
    # Drop unnecessary columns
    sid_col = 'StudentPK'
    eth_col = 'Ethnicity'
    headings = [sid_col, eth_col]
    ethnicities_df = ethnicities_df[headings]
    # Remove duplicate Student ID Numbers
    ethnicities_df.drop_duplicates(sid_col, 'first', True)
    # Remove students without an Ethnicity
    # Set empty Ethnicity values to NaN and then drop
    ethnicities_df[eth_col] = ethnicities_df[eth_col].apply(list_nan)
    ethnicities_df.dropna(subset=[eth_col], inplace=True)
    # Convert all Pacific Island nations to 'Pacific Island'
    ethnicities_df[eth_col] = ethnicities_df[eth_col].apply(db.convert_pacific,
                  args=(island_nations,))
    # print(ethnicities_df)
    # Get a list of unique ethnicities
    unique_eth = ethnicities_df[eth_col].unique()
    # Create a dictionary to hold count of ethnicities and populate
    count_eths_dict = ad.create_dict(unique_eth)
    # Get each ethnicity in a list
    ethnicities = ethnicities_df[eth_col].tolist()
    count_eths_dict = update_dict_counts(count_eths_dict, ethnicities)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    count_eths_list = ad.sort_dict_values(count_eths_dict, 'descending')
    # Create dict to hold the percentages of each ethnicity
    percent_eths_dict, total = calculate_percent(count_eths_dict)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    percent_eths_list = ad.sort_dict_values(percent_eths_dict, 'descending')
    # Get from user the sample source
    sample = get_sample()
    # Display results
    print('\nPercentage of {} students by ethnicity:\n'.format(sample))
    print("{:40} {:7}".format('Ethnicity', 'Percent'))
    for x in percent_eths_list:
        print("{:40} {:7}%".format(x[0], x[1]))
    # Get a list of tuples with just results over 1%
    threshold = 1
    threshold_eths_list = get_threshold_items(percent_eths_list, threshold)
    print('\nThe ethnicities above the {}% threshold are as follows:\n'.format(
            threshold))
    print("{:20} {:7}".format('Ethnicity', 'Percent'))
    for x in threshold_eths_list:
        print("{:20} {:7}%".format(x[0], x[1]))
    print('\nTotal number of {} students in sample: {}'.format(sample, total))
    print('\nTotal number of ethnicities in {} student sample: {}'.format(
            sample, len(unique_eth)))
    print('')
    # Save all ethnicities % to a CSV file, each key:value on a separate line
    headings = ['Ethnicity', 'Percent']
    f_name = '{}_Ethnicities_Percentage_'.format(sample) 
    ft.save_list_csv(percent_eths_list, headings, f_name)
    print('')
    # Save threshold ethnicities with each key:value on a separate line
    f_name = '{}_Top_Ethnicities_Percentage_'.format(sample) 
    ft.save_list_csv(threshold_eths_list, headings, f_name)
    print('')
    # Save all ethnicities counts to a CSV file
    headings = ['Ethnicity', 'Count']
    f_name = '{}_Ethnicities_Count_'.format(sample) 
    ft.save_list_csv(count_eths_list, headings, f_name)
    ft.process_warning_log(warnings, warnings_to_process)


def process_how_heard_data():
    """Process How Heard Data."""
    warnings = ['\nProcessing How Heard Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing How Heard Data.')
    # Confirm the required files are in place
    required_files = ['Student Data File', 'Student Data Headings File']
    ad.confirm_files('Student Data', required_files)
    # Load Student data
    student_data = ft.get_csv_fname_load('Student Data File')
    # Load headings file
    data_headings = ft.load_headings('data_headings.txt')
    # Place data into a DataFrame
    heard_df = pd.DataFrame(data = student_data, columns = data_headings)
    # Drop unnecessary columns
    sid_col = 'StudentPK'
    heard_col = 'HowHeard'
    headings = [sid_col, heard_col]
    heard_df = heard_df[headings]
    # Remove duplicate Student ID Numbers
    heard_df.drop_duplicates(sid_col, 'first', True)
    # Convert students without a How Heard entry to 'Unknown'
    heard_df[heard_col] = heard_df[heard_col].apply(list_unknown)
    # Get a list of unique how heard entries
    unique_heard = heard_df[heard_col].unique()
    # Create a dictionary to hold count of how heard types and populate
    count_heard_dict = ad.create_dict(unique_heard)
    # Get each how heard type in a list
    heard = heard_df[heard_col].tolist()
    count_heard_dict = update_dict_counts(count_heard_dict, heard)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    count_heard_list = ad.sort_dict_values(count_heard_dict,'descending')
    # Create dict to hold the percentages of each how heard type
    percent_heard_dict, total = calculate_percent(count_heard_dict)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    percent_heard_list = ad.sort_dict_values(percent_heard_dict,'descending')
    # Get from user the sample source
    sample = get_sample()
    # Display results
    print('\nPercentage of {} students by How Heard Type:\n'.format(sample))
    print("{:40} {:7}".format('How Heard', 'Percent'))
    for x in percent_heard_list:
        print("{:40} {:7}%".format(x[0], x[1]))
    # Get a list of tuples with just results over 1%
    threshold = 1
    threshold_heard_list = get_threshold_items(percent_heard_list, threshold)
    print('\nThe How Heard Types above the {}% threshold are as follows:\n'
          .format(threshold))
    print("{:40} {:7}".format('How Heard', 'Percent'))
    for x in threshold_heard_list:
        print("{:40} {:7}%".format(x[0], x[1]))
    print('\nTotal number of {} students in sample: {}'.format(sample, total))
    # Save all how heard % to a CSV file, each key:value on a separate line
    headings = ['How Heard', 'Percent']
    f_name = '{}_How_Heard_Percentage_'.format(sample)
    print('')
    ft.save_list_csv(percent_heard_list, headings, f_name)
    # Save threshold how heard with each key:value on a separate line
    f_name = '{}_Top_How Heard_Percentage_'.format(sample)
    print('') 
    ft.save_list_csv(threshold_heard_list, headings, f_name)
    # Save all how heard counts to a CSV file
    headings = ['How Heard', 'Count']
    f_name = '{}_How_Heard_Count_'.format(sample)
    print('') 
    ft.save_list_csv(count_heard_list, headings, f_name)
    ft.process_warning_log(warnings, warnings_to_process)


def process_location_data():
    """Process Location Data."""
    warnings = ['\nProcessing Location Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing Location Data.')
    # Confirm the required files are in place
    required_files = ['Cities File']
    ad.confirm_files('Location Data', required_files)
    # Load cities data
    cities_data = ft.get_csv_fname_load('Location Data')
    # Place data into a DataFrame
    sid_col = 'StudentID'
    city_col = 'AddressCity'
    country_col = 'AddressCountry'
    headings = [sid_col, city_col, country_col]
    cities_df = pd.DataFrame(data = cities_data, columns = headings)
    # Remove duplicate Student ID Numbers
    cities_df.drop_duplicates(sid_col, 'first', True)
    # Remove students without an AddressCity
    # Set empty AddressCity values to NaN and then drop
    cities_df[city_col] = cities_df[city_col].apply(list_nan)
    cities_df.dropna(subset=[city_col], inplace=True)
    # Remove students without New Zealand in AddressCountry
    # Set non-New Zealand values to NaN and then drop
    cities_df[country_col] = cities_df[country_col].apply(ad.convert_to_nan, 
             args=(['New Zealand'], False,))
    cities_df.dropna(subset=[country_col], inplace=True)
    # Get a list of unique cities
    unique_cities = cities_df[city_col].unique()
    # Create a dictionary to hold count of cities and populate
    count_cities_dict = ad.create_dict(unique_cities)
    # Get each city in a list
    cities = cities_df[city_col].tolist()
    count_cities_dict = update_dict_counts(count_cities_dict, cities)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    count_cities_list = ad.sort_dict_values(count_cities_dict,'descending')
    # Create dict to hold the percentages of each city
    percent_cities_dict, total = calculate_percent(count_cities_dict)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    percent_cities_list = ad.sort_dict_values(percent_cities_dict,'descending')
    # Get from user the sample source
    sample = get_sample()
    # Display results
    print('\nPercentage of {} students by City:\n'.format(sample))
    print("{:20} {:7}".format('City', 'Percent'))
    for x in percent_cities_list:
        print("{:20} {:7}%".format(x[0], x[1]))
    # Get a list of tuples with just results over 1%
    threshold = 1
    threshold_cities_list = get_threshold_items(percent_cities_list, threshold)
    print('\nThe cities above the {}% threshold are as follows:\n'.format(
            threshold))
    print("{:20} {:7}".format('City', 'Percent'))
    for x in threshold_cities_list:
        print("{:20} {:7}%".format(x[0], x[1]))
    print('\nTotal number of {} students in sample: {}'.format(sample, total))
    print('\nTotal number of cities in {} student sample: {}'.format(
            sample, len(unique_cities)))
    # Save all cities % to a CSV file with each key:value on a separate line
    headings = ['City', 'Percent']
    f_name = '{}_Cities_Percentage_'.format(sample)
    print('') 
    ft.save_list_csv(percent_cities_list, headings, f_name)
    # Save threshold cities with each key:value on a separate line
    f_name = '{}_Top_Cities_Percentage_'.format(sample)
    print('') 
    ft.save_list_csv(threshold_cities_list, headings, f_name)
    # Save all cities counts to a CSV file
    headings = ['City', 'Count']
    f_name = '{}_Cities_Count_'.format(sample)
    print('')
    ft.save_list_csv(count_cities_list, headings, f_name)
    ft.process_warning_log(warnings, warnings_to_process)


def process_study_length():
    """Process time taken to graduate on average."""
    warnings = ['\nProcessing Length of Study Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing Length of Study Data.')
    # Confirm the required files are in place
    required_files = ['Enrolments File', 'Graduates File']
    ad.confirm_files('Length of Study Data', required_files)
    # Load enrolment data
    enrolment_data = ft.get_csv_fname_load('Enrolment Data')
    # Place data into a DataFrame
    enrolpk_col = 'EnrolmentPK'
    sid_col = 'StudentFK'
    course_col = 'CourseFK'
    tutor_col = 'TutorFK'
    start_col = 'StartDate'
    expiry_col = 'ExpiryDate'
    status_col = 'Status'
    tag_col = 'Tag'
    en_headings = [enrolpk_col, sid_col, course_col, tutor_col, start_col,
                expiry_col, status_col, tag_col]
    enrolment_df = pd.DataFrame(data = enrolment_data, columns = en_headings)
    en_headings = [enrolpk_col, course_col, start_col, status_col]
    enrolment_df = enrolment_df[en_headings]
    # Load graduates data
    graduate_data = ft.get_csv_fname_load('Graduates Data')
    # Place data into a DataFrame
    gradpk_col = 'GraduatePK'
    grad_date_col = 'GraduationDate'
    cert_col = 'CertificateNumber'
    type_col = 'Type'
    length_col = 'LengthOfStudy'
    grad_headings = [gradpk_col, enrolpk_col, grad_date_col, cert_col]
    grads_df = pd.DataFrame(data = graduate_data, columns = grad_headings)
    # Merge the two dataframes and keep required columns
    updated_grads = pd.merge(enrolment_df, grads_df, on=enrolpk_col,
                             how='inner')
    grad_headings = [enrolpk_col, course_col, start_col, grad_date_col]
    updated_grads = updated_grads[grad_headings]
    # Add column for course type and populate
    updated_grads[type_col] = updated_grads[course_col].apply(get_course_type)
    # Add column for length of study and populate
    updated_grads[length_col] = updated_grads.apply(lambda x: 
        da.calculate_days(x[start_col], x[grad_date_col]), axis=1)
    # Group data by course Type
    grouped_grads = updated_grads.groupby(type_col)
    stats = grouped_grads.aggregate([np.mean, np.median, np.max, np.min])
    # Get from user the sample source
    sample = get_sample()
    print('\nStatistics for {}:\n'.format(sample))
    print(stats)
    # Save data to file
    f_name = '{}_Graduates_Statistics_{}{}'.format(sample,
              ft.generate_time_string(), '.xls')
    stats.to_excel(f_name)
    print('\nData saved to {}'.format(f_name))
    # print('Groups: {}'.format(grouped_grads.groups.keys()))
    # print(updated_grads)
    ft.process_warning_log(warnings, warnings_to_process)
    

def process_study_reason_data():
    """Process Study Reason Data."""
    warnings = ['\nProcessing Reason for Study Data Warnings:\n']
    warnings_to_process = False
    print('\nProcessing Reason for Study Data.')
    # Confirm the required files are in place
    required_files = ['Study Reason File']
    ad.confirm_files('Study Reason Data', required_files)
    # Load study reason data
    study_data = ft.get_csv_fname_load('Study Reason Data')
    # Place data into a DataFrame
    sid_col = 'StudentID'
    reason_col = 'Study Reason'
    headings = [sid_col, reason_col]
    study_df = pd.DataFrame(data = study_data, columns = headings)
    # Remove duplicate Student ID Numbers
    study_df.drop_duplicates(sid_col, 'first', True)
    # Convert students without a study reason entry to 'Unknown'
    study_df[reason_col] = study_df[reason_col].apply(list_unknown)
    # Get a list of unique study reason entries
    unique_reason = study_df[reason_col].unique()
    # Create a dictionary to hold count of study reason types and populate
    count_reason_dict = ad.create_dict(unique_reason)
    # Get each study reason type in a list
    reason = study_df[reason_col].tolist()
    count_reason_dict = update_dict_counts(count_reason_dict, reason)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    count_reason_list = ad.sort_dict_values(count_reason_dict,'descending')
    # Create dict to hold the percentages of each study reason type
    percent_reason_dict, total = calculate_percent(count_reason_dict)
    # Convert to an ordered list of tuples (allow ordered display and saving)
    percent_reason_list = ad.sort_dict_values(percent_reason_dict,'descending')
    # Get from user the sample source
    sample = get_sample()
    # Display results
    print('\nPercentage of {} students by Study Reason Type:\n'.format(sample))
    print("{:50} {:7}".format('Study Reason', 'Percent'))
    for x in percent_reason_list:
        print("{:50} {:7}%".format(x[0], x[1]))
    # Get a list of tuples with just results over 1%
    threshold = 1
    threshold_reason_list = get_threshold_items(percent_reason_list, threshold)
    print('\nThe Study Reason Types above the {}% threshold are as follows:\n'
          .format(threshold))
    print("{:50} {:7}".format('Study Reason', 'Percent'))
    for x in threshold_reason_list:
        print("{:50} {:7}%".format(x[0], x[1]))
    print('\nTotal number of {} students in sample: {}'.format(sample, total))
    # Save all study reasons % to a CSV file, each key:value on a separate line
    headings = ['Study Reason', 'Percent']
    f_name = '{}_Study_Reason_Percentage_'.format(sample)
    print('') 
    ft.save_list_csv(percent_reason_list, headings, f_name)
    # Save threshold study reason with each key:value on a separate line
    f_name = '{}_Top_Study_Reason_Percentage_'.format(sample)
    print('')
    ft.save_list_csv(threshold_reason_list, headings, f_name)
    # Save all study reason counts to a CSV file
    headings = ['Study Reason', 'Count']
    f_name = '{}_Study_Reason_Count_'.format(sample)
    print('')
    ft.save_list_csv(count_reason_list, headings, f_name)
    ft.process_warning_log(warnings, warnings_to_process)


def sample_menu():
    """Display the sample menu options."""
    print('\nPlease enter the number for the source of the data:\n')
    print('1: All Students')
    print('2: Active Students')
    print('3: Expired Students')
    print('4: Maori Students')
    print('5: Pasifika Students')
    print('6: Graduated Students')
    print('7: Withdrawn Students')
    print('8: Other Students')


def total_dict_values(source_dict):
    """Return the total of all values in a dictionary.
    
    Counts up the values of each key to generate a total. All values must be
    an int.
    
    Args:
        source_dict (dict): Dictionary to be tallied.
        
    Returns:
        total (int): Total of all values.
    """
    total = 0
    for key, value in source_dict.items():
        if ad.check_is_int(value):
            total += value
            # Skip if not an int
    return total


def update_dict_counts(dictionary, values):
    """Updates key values in dictionary based on counts of items.
    
    Args:
        dictionary (dict): Dictionary to update. Values should be ints.
        values (list): List of values. Values should appear in dictionary as
        keys. If not, they will be added as a key.
    
    Returns:
        updated_dict (dict): dictionary with key values updated.
    """
    for item in values:
        if item in dictionary.keys():
            dictionary[item] = dictionary[item] + 1
        else:
            dictionary[item] = 1
    return dictionary


if __name__ == '__main__':
    main()