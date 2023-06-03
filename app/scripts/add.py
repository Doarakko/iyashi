import argparse
import os
import sys

sys.path.append(os.path.abspath("."))
import animal
from db import Database
from file import File

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", help="url")
    parser.add_argument("-a", help="animal")
    args = parser.parse_args()

    Database.initialise()
    file = File()
    file.add(url=args.u, animal=args.a)
