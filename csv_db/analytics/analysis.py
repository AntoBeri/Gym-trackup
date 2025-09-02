from pandas import DataFrame
import modify as mods

def show_table (df: DataFrame, ordered: DataFrame):
    """
    
    Takes a DataFrame with the registered excercises and selects the most recent register
    of each registered eaxcercise and prints it as a table.

    Args:
        df (DataFrame): DataFrame containing the registered excercises.
        ordered (DataFrame): DataFrame used to store the most recent registrations.
    
    Returns:
        None

    """
    # Iterate through the excercies in the DataFrame
    for excercise in df.itertuples(index=False):

        # If the current excercise has already been filtered it continues to the next excercise
        if excercise.Excercise in ordered['Excercise'].values:
            continue
        else:
            for other_excercise in df.itertuples(index=False):
                if (excercise.Excercise == other_excercise.Excercise) and (excercise.Date != other_excercise.Date):
                    e_date = excercise.Date.split('-')
                    eo_date = other_excercise.Date.split('-')

                    for e, eo in zip(e_date, eo_date):
                        n_e = int(e)
                        n_eo = int(eo)

                        if n_e > n_eo:
                            excercise_list = list(excercise)
                            break
                        elif n_eo > n_e:
                            excercise_list = list(other_excercise)
                            break

                elif excercise.Excercise == other_excercise.Excercise:
                    excercise_list = list(excercise)
            
            mods.add_excercise(ordered, 'a', excercise_list)
    
    print(ordered)
