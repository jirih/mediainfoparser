# -*- coding: utf-8 -*-
import argparse
import json
import os
import sys

from mparser import MParser

NOT_AVAILABLE = "Unavailable"
INDENT = 2


def create_parser():
    parser = argparse.ArgumentParser(description='Parse mediainfo output')
    parser.add_argument('--file', help='input file, instead of stardard input',
                        dest="file", default=None, action='store')
    parser.add_argument('--dir', help='input directory, instead of stardard input',
                        dest="dir", default=None, action='store')

    parser.add_argument('--json-all', help='print all as Json',
                        dest="print_all", default=False, action='store_true')
    parser.add_argument('--json-general-only', help='print General section only as Json',
                        dest="print_general_only", default=False, action='store_true')

    parser.add_argument('--track-type', help='track type of interest',
                        dest="track_type", default=None, choices={"Audio", "Video", "Text"}, action='store')
    parser.add_argument('--track-numbers', nargs='+', help='Track numbers of interest',
                        dest="track_numbers", default=[], action='store')

    parser.add_argument('--number-of-tracks', help='returns number of tracks of given type',
                        dest="number_of_tracks", default=False, action='store_true')

    parser.add_argument('--fields', nargs='+', help='fields to output, one per line',
                        dest="fields", default=[], action='store')
    return parser


def run_for_file(args, file):
    mparser = MParser(file)
    mparser.parse()

    print_all = args.print_all
    print_general_only = args.print_general_only
    track_numbers = args.track_numbers
    track_type = args.track_type
    number_of_tracks = args.number_of_tracks
    fields = args.fields

    if not print_all and not print_general_only and track_type is None and not fields:
        print_all = True

    if print_general_only:
        print(json.dumps(mparser.regrouped["General"], indent=INDENT))
        sys.exit(0)

    if print_all:
        if track_type is not None:
            track_numbers = expand_track_numbers(track_numbers, mparser, track_type)
            output = {k: v for k, v in mparser.regrouped[track_type].items() if k in track_numbers}
            print(json.dumps(output, indent=INDENT))

        else:
            print(json.dumps(mparser.regrouped, indent=INDENT))
    else:
        if track_type is not None:
            if number_of_tracks:
                print(len(mparser.regrouped[track_type]))
            else:
                track_numbers = expand_track_numbers(track_numbers, mparser, track_type)
                for interested_track in track_numbers:
                    for field in fields:
                        if field in mparser.regrouped[track_type][interested_track]:
                            print(mparser.regrouped[track_type][interested_track][field])
                        else:
                            print(NOT_AVAILABLE)
        else:
            for field in fields:
                if field in mparser.regrouped["General"]:
                    print(mparser.regrouped["General"][field])
                else:
                    print(NOT_AVAILABLE)


def main():
    parser = create_parser()
    args = parser.parse_args()
    directory = args.dir

    if directory:
        for root, dirs, files in os.walk(directory):
            for name in files:
                run_for_file(args, os.path.join(root, name))
    else:
        file = args.file
        run_for_file(args, file)
    sys.exit(0)


def expand_track_numbers(track_numbers, mparser, track_type):
    if not track_numbers:
        track_numbers = list(range(len(mparser.regrouped[track_type])))
    else:
        track_numbers = list(map(int, track_numbers))
    return track_numbers


if __name__ == "__main__":
    main()
