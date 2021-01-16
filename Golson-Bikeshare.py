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
        (str) city - name of the city to analyze (accepts letters in any case!)
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input('Enter city name here, lowercase: \n')
        city = city.lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('try again')
            continue
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month name here, lowercase, or all: \n')
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print('try again')
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day of week here, lowercase, or all: \n')
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print('try again')
            continue

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
    # load data file into a dataframe
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

    # TO DO: display the most common month
    print('The most common month is: ' + str(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most day is: ' + str(df['day_of_week'].mode()[0]))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    # find the most common hour (from 0 to 23)
    print('The most common month is: ' + str(df['hour'].mode()[0]))

    return df

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular Start Station is: ' + df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most popular End Station is: ' + df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Combo'] = df['Start Station'] + ' ' + df['End Station']
    print('The most popular combination is: ' + df['Combo'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(str(df['Trip Duration'].sum() / 60) + ' minutes')
    print(str(df['Trip Duration'].sum() / 360) + ' hours')
    print(str(df['Trip Duration'].sum() / 8640) + ' days!!!')
    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The numbers of subscribers and non-subscribers are:\n' + str(df['User Type'].value_counts()))

    # TO DO: Display counts of gender
    try:
        print('The numbers of men and women are:\n' + str(df['Gender'].value_counts()))
    except KeyError:
        print('(This city does not provide gender data...)')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The oldest birth year is ' + str(int(df['Birth Year'].min())))
    except KeyError:
        print('(This city does not provide birth years...)')

    try:
        print('The most recent birth year is ' + str(int(df['Birth Year'].max())))
    except KeyError:
        print('(This city does not provide birth years...)')

    try:
        print('The most common birth year is ' + str(int(df['Birth Year'].mode()[0])))
    except KeyError:
        print('(This city does not provide birth years...)')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_more(df):
    """Prompts user for 5 lines of data at a time."""

    view_data = input('\nWould you like to view the first 5 rows of data? Enter yes or no\n')
    start_loc = 0
    end_loc = 5
    while True:
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        end_loc += 5
        view_display = input('Do you want to see 5 more? Enter yes or no\n').lower()
        if view_display != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_more(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
