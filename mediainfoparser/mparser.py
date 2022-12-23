# -*- coding: utf-8 -*-
import re
import sys


def parse_section(reader):
    section = {}
    line = reader.readline()
    while line != '' and line not in ['\n', '\r\n']:
        result = re.search(r"^(.+)\s+:\s+(.+)$", line)
        section[result.group(1).strip()] = result.group(2)
        line = reader.readline()
    return section


class MParser:
    def __init__(self, file):
        self.file = file
        self.parsed = {}
        self.regrouped = {}

    def regroup(self):
        self.regrouped["General"] = self.parsed["General"]

        self.regroup_group("Audio")
        self.regroup_group("Video")
        self.regroup_group("Text")

    def regroup_group(self, group):
        self.regrouped[group] = {}

        if "%s" % group in self.parsed or "%s #1" % group in self.parsed:
            if "%s #1" % group not in self.parsed:
                self.regrouped[group][0] = self.parsed[group]
            else:
                for section in self.parsed:
                    r = re.search(r"%s #(\d+)" % group, section)
                    if r is not None:
                        self.regrouped[group][int(r.group(1)) - 1] = self.parsed["%s #%s" % (group, r.group(1))]

    def parse(self):
        with open(self.file, 'r') if self.file is not None else sys.stdin as reader:
            line = reader.readline()
            while line != '':
                self.parsed[line.strip()] = parse_section(reader)
                line = reader.readline()
        self.regroup()
