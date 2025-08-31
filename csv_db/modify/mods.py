def addExcercise(df):
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

    df.loc[len(df)] = row

def removeExcercise(df):
    pass

def updateVal(df):
    pass