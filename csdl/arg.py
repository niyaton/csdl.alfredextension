import argparse

def create_parser():
    description = 'Open IEEE CSDL'

    parser = argparse.ArgumentParser(description=description)
    
    parser = argparse.ArgumentParser(description='Open IEEE CSDL')
    parser.add_argument('conference_abbrev', help='path of repository dir')
    parser.add_argument('year', nargs='?', type=int)

    return parser
