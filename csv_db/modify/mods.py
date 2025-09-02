from pandas import DataFrame

def add_excercise(df: DataFrame, mode: str = 'm', row_a: list = []):
    """
    
    Adds an excercise to a DataFrame.

    Args:
        df (DataFrame): The DataFrame to which the excercise will be added.
        mode (str, optional): The mode in which the function is used.
            Must be either:
            - "m" : Manual mode. The information about the excercise to add is manually entered by the user.
            - "a" : Auto mode. The information about the excercise to add is automatically added by the program.
            Defaults to "m".
        row_a (list, optional): A list containing the excercise information to add when auto mode. Defaults to [].
    
    Returns:
        None
    """

    # If the function is used to add a new excercise it asks the user to enter the information about it.
    if mode == 'm':
        e_muscle = input('Enter the muscle trained by the excercise to add: ')
        e_name = input('Enter the excercise name: ')
        e_series = input('Enter the number of series done for the excercise: ')
        e_reps = input('Enter the number of reps done in each serie: ')
        e_weight = input('Enter the weight used for the exccercise: ')
        date = input(
            'Enter the date in where you first did the excercise\n'
            'Use the following syntax YYYY-MM-DD: '
        )
        row = [e_muscle, e_name, e_series, e_reps, e_weight, date]
    
    # If the function is used to update an existing excercise the information is automatically added.
    elif mode == 'a':
        row = row_a
    
    # Add the excercise information to the DataFrame
    df.loc[len(df)] = row

def remove_excercise(df):
    pass

def update_val(df):
    pass