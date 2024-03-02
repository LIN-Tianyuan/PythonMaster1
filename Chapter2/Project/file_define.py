"""
Définition des classes relatives aux documents
"""

# Commencez par définir une classe abstraite
# pour la conception de haut niveau et déterminez les fonctionnalités à mettre en oeuvre

import json
from data_define import Record


class FileReader:
    def read_data(self):
        pass


class TextFileReader(FileReader):

    path = None

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list:
        f = open(self.path, 'r', encoding='UTF-8')
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip() # Eliminer l'\n de chaque ligne de données lues
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], data_list[2], data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JSONFileReader(FileReader):
    path = None

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list:
        f = open(self.path, 'r', encoding='UTF-8')
        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("January2023SalesData.txt")
    json_file_reader = JSONFileReader("February2023SalesData.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for data in list1:
        print(data)

    print("------------------------------------------------------------")

    for data in list2:
        print(data)
