import pandas as pd
from pathlib import Path


def main():
    # Load the template and create your own file
    file = Path('Gym-trackup/csv_db/data/tracks.csv')

    if not file.exists():
        template = pd.read_csv('Gym-trackup/csv_db/data/template.csv')
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
                print(action)
            case "A":
                print(action)
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