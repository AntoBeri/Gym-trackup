import pandas as pd
from pathlib import Path


def main():
    # Load the template and create your own file
    file = Path('Gym-trackup/data/tracks.csv')

    if not file.exists():
        template = pd.read_csv('Gym-trackup/data/template.csv')
        tracks = pd.DataFrame(columns=template.columns)
        tracks.to_csv('Gym-trackup/data/tracks.csv', index=False)
    else:
        tracks = pd.read_csv(file)

    print(tracks.head)

if __name__ == '__main__':
    main()