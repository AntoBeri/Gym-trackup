import pandas as pd
import modify as mod
import analytics as any
from pathlib import Path


def main():
    # Load the template and the path were the database should be
    file = Path('Gym-trackup/csv_db/data/tracks.csv')
    template = pd.read_csv('Gym-trackup/csv_db/data/template.csv')

    # Check if the database exist, if not create it
    if not file.exists():
        tracks = pd.DataFrame(columns=template.columns)
        tracks.to_csv('Gym-trackup/csv_db/data/tracks.csv', index=False)
    else:
        tracks = pd.read_csv(file)

    while True:
        action = input(
            'What do you want to do?\n' 
            'Consult progress (P)\n'
            'Add excercise (A)\n'
            'Delete excercise (D)\n'
            'Update excercise weigth/reps (U)\n'
            'Change excercise name (C)\n'
            'Exit (E)\n'
            'Selection: '
            ).upper()

        match action:
            case "P": 
                decision = input(
                    'What you want to check from your excercises:\n'
                    'Print excercises table (P)\n'
                ).upper()
                
                match decision:
                    case 'P':
                        ordered_t = pd.DataFrame(columns=template.columns)
                        any.show_table(tracks, ordered_t)
                    case _:
                        print('Not valid selection entered!')
            case "A":
                mod.add_excercise(tracks)

                tracks.to_csv('Gym-trackup/csv_db/data/tracks.csv', index=False)
            case "D":
                print(action)
            case "U":
                print(action)
            case 'U':
                print(action)
            case "E":
                break
            case _:
                print('No valid selection entered!')

if __name__ == '__main__':
    main()