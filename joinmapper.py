#!/usr/bin/python3
"""joinmapper.py"""
import json
import sys
import operator
import yaml


class Mapper:

    def __init__(self, element, schema):
        self.fromTableColumns = element['fromTableColumns']
        self.joinTableColumns = element['joinTableColumns']
        self.whereColumnIndex = []
        self.joinType = element['joinType']
        self.selectColumnIndex = []
        self.whereLValue = element['wherelval']
        self.whereValue = element['whererval']
        self.whereOperator = element['whereop']
        self.operate = {
            '=': operator.eq,
            '<': operator.lt,
            '>': operator.gt,
            '<=': operator.le,
            '>=': operator.ge,
            '!=': operator.ne
        }
        self.schema = schema
        self.mergedColList = list(self.schema)

    def frameSelectColumns(self):
        if self.joinType == 'natural':
            for column in self.fromTableColumns:
                self.selectColumnIndex.append(self.mergedColList.index(column))
            for column in self.joinTableColumns:
                self.selectColumnIndex.append(self.mergedColList.index(column))
        else:
            for column in self.fromTableColumns:
                if column+'_1' in self.mergedColList:
                    self.selectColumnIndex.append(self.mergedColList.index(column+'_1'))
                elif column in self.mergedColList:
                    self.selectColumnIndex.append(self.mergedColList.index(column))

            for column in self.joinTableColumns:
                if column+'_2' in self.mergedColList:
                    self.selectColumnIndex.append(self.mergedColList.index(column+'_2'))
                elif column in self.mergedColList:
                    self.selectColumnIndex.append(self.mergedColList.index(column))
        # print('---------------------------JOIN SELECT COLUMN INDEXS---------------------------------')
        # print(self.selectColumnIndex)
        col_list = list(self.selectColumnIndex)
        with open('/home/kashyapmantri/PycharmProjects/Zenoh/Dependencies/joinselect.yaml', 'w') as file:
            col = yaml.dump(col_list, file)
    def getWhereColumn(self):
        temp = self.whereLValue.strip()
        wherecol = temp.split('.')[1].strip()
        for column in self.mergedColList:
            if (wherecol==column) or (wherecol+'_1'==column) or (wherecol+'_2'==column):
                self.whereColumnIndex.append(self.mergedColList.index(column))
                # print('---------------------------JOIN WHERE COLUMN INDEXS---------------------------------')
                # print(self.whereColumnIndex)
                break

    def execute(self):

        # file1 = open('join.csv', 'r')
        # Lines = file1.readlines()
        for row in sys.stdin:
            # row = row.replace('"', '')
            row = row.strip().split("\t")
            # print(str(row))
            if self.operate[self.whereOperator](row[self.whereColumnIndex[0]], self.whereValue):
                selectColumns = [row[index] for index in self.selectColumnIndex]
                selectColumns = '\t'.join(selectColumns)
                print(selectColumns)


if __name__ == '__main__':
    with open('joinElements.json', 'r') as file:
        elements = json.load(file)
    with open('/home/kashyapmantri/PycharmProjects/Zenoh/Dependencies/joinschema.yaml', 'r') as file:
        schema = yaml.load(file, Loader=yaml.FullLoader)
    mapper = Mapper(elements, schema)
    mapper.frameSelectColumns()
    mapper.getWhereColumn()
    mapper.execute()
