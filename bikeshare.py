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
    cities = ['chicago','new york city','washington']
    city = ''

    print('Enter city name to be analysed (chicago, new york city, washington): ')
    city = input()
    while city not in cities:
        print('Enter city name to be analysed (chicago, new york city, washington): ')
        city = input()

    # get user input for filtering or not (none, both, month, day)
    filters = ["none", "both", "month", "day"]
    filter_crit = 'none'

    print('Would you like to filter by month, date, both or none?: ')
    filter_crit = input()
    while filter_crit not in filters:
        print('Would you like to filter by month, date, both or none?: ')
        filter_crit = input()

    if filter_crit == "none":
        month = "all"
        day = "all"
    elif filter_crit == "both":
        # get user input for month (all, january, february, ... , june)
        months = ["all", "january", "february", "march", "april", "may", "june"]
        month = ''

        print('Enter month name to be analysed (january, february, ... , june): ')
        month = input()
        while month not in months:
            print('Enter month name to be analysed (january, february, ... , june): ')
            month = input()   

        # get user input for day of week (all, monday, tuesday, ... sunday)
        days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day = ''

        print('Enter day name to be analysed (monday, tuesday, ... sunday): ')
        day = input()
        while day not in days:
            print('Enter day name to be analysed (monday, tuesday, ... sunday): ')
            day = input()

    elif filter_crit == "month":
        # get user input for month (all, january, february, ... , june)
        months = ["all", "january", "february", "march", "april", "may", "june"]
        month = ''

        print('Enter month name to be analysed (january, february, ... , june): ')
        month = input()
        while month not in months:
            print('Enter month name to be analysed (january, february, ... , june): ')
            month = input() 

    elif filter_crit == "day":
        # get user input for day of week (all, monday, tuesday, ... sunday)
        days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day = ''

        print('Enter day name to be analysed (january, february, ... , june): ')
        day = input()
        while day not in days:
            print('Enter day name to be analysed (monday, tuesday, ... sunday): ')
            day = input()



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
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['','january', 'february', 'march', 'april', 'may', 'june']

    popular_month = df['month'].mode()[0]
    
    print('Most Common Month:', months[popular_month].title())

    # display the most common day of week
    
    popular_day = df['day_of_week'].mode()[0]
    
    print('Most Common Day of the Week:', popular_day)

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Commonly Used Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('Most Commonly Used End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip

    df['trip'] = df['Start Station'] +' - '+ df['End Station']

    popular_stations = df['trip'].mode()[0]
    
    print('Most Frequent Combination of Start Station and End Station Trip:', popular_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    df['duration'] = pd.to_datetime(df['End Time']) - df['Start Time']

    total_duration = df['duration'].sum()
    
    print('Total travel time:', total_duration)


    # display mean travel time
    mean_duration = df['duration'].mean()
    
    print('Mean travel time:', mean_duration)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()

    print('\nCounts of Users Types:\n', user_types)

    # Display counts of gender
    genders = df['Gender'].value_counts()

    print('\nCounts of Gender:\n', genders)

    # Display earliest, most recent, and most common year of birth

    earliest, recent, common = df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode()[0] 

    print('\nYears of Birth Earlieat = {}, Most recent = {}, Most common = {}:'.format(earliest, recent, common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
