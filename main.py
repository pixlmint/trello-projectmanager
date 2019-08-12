import os
import auth
import csv_reader
import models


class Trello:
    def __init__(self, name, extension, separator):
        self.extension = extension
        self.name = name
        self.separator = separator
        self.file = os.path.join("csv", name + "." + extension)
        self.client = auth.authorize()
        self.project = models.TrelloProject(self.name, self.client)
        self.csv = None

    def add_board_from_csv(self, file):
        head = csv_reader.read(file)[0]
        for board in head:
            full_board = self.name + " - " + board
            if "NR" not in str(board) and "id" not in str(board) and "Anforderung" not in str(board):
                self.project.add_board(full_board, board)

    def add_list_from_csv(self, file):
        lists = []
        if self.csv is None:
            for line in self.csv:
                for item, key in line:
                    board = self.project.get_board(line[0][key])
                    print(board)


name = input("please enter the project's name (and make sure the file has the same name)")
extension = input("Enter the file extension you'd like to use (default: csv)")
separator = input("Please enter the csv separator (default: ,)")
if not extension:
    extension = "csv"
if not separator:
    separator = ","
project = Trello(name, extension, separator)
# project.add_board_from_csv(project.file)
project.add_list_from_csv(project.file)
