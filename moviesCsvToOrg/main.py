# Save this code in a file, e.g., MovieConverter.py

import argparse

from MovieConverter import MovieConverter


def main():
    parser = argparse.ArgumentParser(description="Convert CSV file to Org file.")
    parser.add_argument("input", help="Input CSV file")
    parser.add_argument("--output", help="Output Org file")

    args = parser.parse_args()
    converter = MovieConverter(args.input, args.output)
    converter.convert_csv_to_org()


if __name__ == "__main__":
    main()
