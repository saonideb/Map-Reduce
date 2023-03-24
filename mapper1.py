#!/usr/bin/python3
"""mapper.py"""
import json
import sys
import operator


class Mapper:

    def __init__(self, element):
        self.selectColumnIndex = element['selectColumnIndex']
        self.whereColumnIndex = element['whereColumnIndex']
        self.whereValue = element['whereValue']
        self.whereOperator = element['whereOperator']
        self.operate = {
            '=': operator.eq,
            '<': operator.lt,
            '>': operator.gt,
            '<=': operator.le,
            '>=': operator.ge,
            '!=': operator.ne
        }

    def execute(self):
        # print('--------------SELECT COLUMNS-------------'+str(self.selectColumnIndex))
        # file1 = open('movies.csv', 'r')
        # Lines = file1.readlines()
        for row in sys.stdin:
            row = row.replace('"', '')
            row = row.strip().split(',')
            #print(str(row))
            test = self.operate[self.whereOperator](row[self.whereColumnIndex], self.whereValue)
            if test:
                selectColumns = [row[index] for index in self.selectColumnIndex]
                selectColumns = '\t'.join(selectColumns)
                print(selectColumns)

if __name__ == '__main__':
    with open('elements.json', 'r') as file:
        elements = json.load(file)
    # print('---------------------------------------ELEMENTS-------------------------------------------')
    # print(elements)
    mapper = Mapper(elements)
    mapper.execute()
