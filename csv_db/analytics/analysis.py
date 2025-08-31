import modify as mods

def show_table (df, ordered):
    for excercise in df.itertuples(index=False):

        if excercise.Excercise in ordered['Excercise']:
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
                            ordered.loc[len(ordered)] = list(excercise)
                        elif n_eo > n_e:
                            ordered.loc[len(ordered)] = list(other_excercise)
                    
                    continue

                ordered.loc[len(ordered)] = list(excercise)
    
    print(ordered)
