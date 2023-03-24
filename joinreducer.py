#!/usr/bin/python3
"""reducer.py"""
import operator
import json
import sys
import yaml

a1 = []
col = ()

class Reducer:

    def __init__(self, element):
        self.elements = element
        self.data = {}

    def performOperation(self, data):
        # print(str(data))
        colNames = []
        with open('/home/kashyapmantri/PycharmProjects/Zenoh/Dependencies/joinschema.yaml', 'r') as file:
            schema = yaml.load(file, Loader=yaml.FullLoader)
        with open('/home/kashyapmantri/PycharmProjects/Zenoh/Dependencies/joinselect.yaml', 'r') as file:
            joinselect = yaml.load(file, Loader=yaml.FullLoader)
        for column in joinselect:
            colNames.append(str(schema[column]))
        length = len(colNames)
       
        for row in data:
            # if len(colNames) == len(row):
            #     print('---------------EQUAL--------------------')
            temp = {colNames[i]: row[i] for i in range(0, length)}
            # temp = {i : row[i] for i in range(0, length)}
            # print("\t".join(column))
            print(str(temp))

    def reduce(self):
        # print('---------------------ABOUT TO READ FROM STDIN-----------------------------')
        for row in sys.stdin:
            row = row.strip().split('\t')
            a1.append(row)
        with open('/home/kashyapmantri/PycharmProjects/Zenoh/Dependencies/reduceroutput.yaml', 'w') as file:
            schema = yaml.dump(a1, file)
        self.performOperation(a1)


if __name__ == '__main__':
    with open('/home/kashyapmantri/PycharmProjects/Zenoh/Dependencies/joinElements.json', 'r') as file:
        elements = json.load(file)

    reducer = Reducer(elements)
    reducer.reduce()

