#!/usr/bin/python3
"""reducer.py"""
import operator
import json
import sys
import collections
import yaml

a1 = []
col = ()
class Reducer:

    def __init__(self, element):
        self.elements = element
        self.data = {}
        self.operate = {
            '=': operator.eq,
            '<': operator.lt,
            '>': operator.gt,
            '<=': operator.le,
            '>=': operator.ge,
            '!=': operator.ne
        }

    # def performOperation(self, data):
    #         # print(str(data))
    #         for column in data:
    #             values = [str(value) for value in data[column]]
    #             print(str(column) + '\t' + str(values))

    def performOperation(self, data):
        # print(str(data))
        with open('/home/kashyapmantri/git_workspace/Zenoh/Dependencies/schema.yaml', 'r') as file:
            schema = yaml.load(file, Loader=yaml.FullLoader)
        table = list(schema[elements['fromTable']])
        colNames = []
        length = len(elements['selectColumnIndex'])
        for i in elements['selectColumnIndex']:
            colNames.append(table[i])
        for row in data:
            temp = {colNames[i]: row[i] for i in range(0, length)}
            # print("\t".join(column))
            print(str(temp))

    def reduce(self):
        # print('---------------------ABOUT TO READ FROM STDIN-----------------------------')
        for row in sys.stdin:
            row = row.strip().split('\t')
            # print(str(row))
            a1.append(row[0:])
            # if row[0] not in self.data:
            #     self.data[row[0]] = row[1].split('\t')
            # else:
            #     self.data[row[0]].append(row[1].split('\t'))
        # self.performOperation(self.data)
        self.performOperation(a1)


if __name__ == '__main__':
    with open('elements.json', 'r') as file:
        elements = json.load(file)

    # print('-------------------ABOUT TO START REDUCE------------------')
    reducer = Reducer(elements)
    reducer.reduce()

