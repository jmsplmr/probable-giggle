import csv


class FileHandler:
    @staticmethod
    def read_csv(file_path):
        with open(file_path, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            return [row for row in csv_reader]

    @staticmethod
    def write_to_org(file_path, content):
        with open(file_path, 'w', encoding='utf-8') as orgfile:
            orgfile.write(content)
