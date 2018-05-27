import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city = input('Enter city (chicago, new york city, washington): ').lower()
            CITY_DATA[city]
            break
        except:
            print("Input not a valid city.")

    # get user input for month (all, january, february, ... , june)
    mo_filter_flag = input('Do you want to filter for a specific month? (y/n): ').lower()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if mo_filter_flag == 'y':
        while True:
            try:
                month = input('Enter month to view (january - june):').lower()
                month = months.index(month) + 1
                break
            except:
                print('Input not valid month.')
    else:
        month = 'all'

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_filter_flag = input('Do you want to filter for a specific day of the week? (y/n): ').lower()
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day_filter_flag == "y":
        while True:
            try:
                day = input('Enter day to view: ').title()
                days_of_week.index(day)
                break
            except:
                print('Input not a valid day.')
    else:
        day = 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['hour'] = df['Start Time'].dt.hour

    df['month'] = df['Start Time'].dt.month

    df['day_name'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        df.loc[(df['month'] == month)]

    if day != 'all':
        df.loc[df['day_name'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Month: ', df['month'].mode()[0])


    # display the most common day of week
    print('Day of week: ', df['day_name'].mode()[0])

    # display the most common start hour
    print('Start hour: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('End station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['station_combo'] = df['Start Station'] + " ==> " + df['End Station']
    print('Station combo: ', df['station_combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time: ', df['Trip Duration'].sum())

    # display mean travel time
    print('Mean travel time: ', df['Trip Duration'].mean())

    print('Median travel time: ', df['Trip Duration'].median())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    user_types = user_types_count.index

    for user in user_types:
        print('{}: {}'.format(user, user_types_count[user]))



    # Display counts of gender
    gender_count = df['Gender'].value_counts()
    genders = gender_count.index

    for gender in genders:
        print('{}: {}'.format(gender, gender_count[gender]))

    # Display earliest, most recent, and most common year of birth
    print('Earliest birth year: ', df['Birth Year'].min())
    print('Recent birth year: ', df['Birth Year'].max())
    print('Most common birth year: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def print_raw_data(df):
    i = input('Would you like to see raw data? (y/n)').lower
    if i == 'y':
        while True:
            num_rows = int(input('Enter # of rows to view: '))
            break
        except:
            print('Input not a valid integer. Try again.')

        print(df.head(num_rows))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
