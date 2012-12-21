from csdl.arg import create_parser
import sys

def test_create_parser_01():
    args = ['Test']

    parser = create_parser()
    parsed_args = parser.parse_args(args)
    assert parsed_args.conference_abbrev == 'Test'
    assert parsed_args.year == None

def test_create_parser_02():
    args = ['Test', 'year']

    parser = create_parser()
    try:
        parsed_args = parser.parse_args(['Test', 'year'])
        assert False
    except SystemExit:
        pass
