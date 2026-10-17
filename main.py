import requests

import csv


class DownloadError(Exception):
    pass

class NotFoundError(DownloadError):
    pass

class AccessDeniedError(DownloadError):
    pass


def download_file(url, filename="latest.txt"):
    response = requests.get(url, stream=True)

    if response.status_code == 400:
        response = requests.get(url, stream=True)

    if response.status_code == 404:
        raise NotFoundError("Nie ma takiego pliku: :" + url)

    if response.status_code == 403:
        raise AccessDeniedError("Nie wolno pobrać tego pliku: " + url)

    with open(filename, "wb") as file:
        file.write(response.content)


class SimpleETL:
    def __init__(self, input_file):
        self.input_file = input_file

    def extract(self):
        with open(self.input_file, newline="", encoding="utf-8") as file:
            for row in csv.reader(file):
                yield row

    def transform(self, rows):
        for row in rows:
            row_id = row[0]
            cells = row[1:]

            missing = [index for index, cell in enumerate(cells, start=1)  if cell == "-"]
            numbers = [float(cell) for cell in cells if cell != "-"]

            if numbers:
                total = sum(numbers)
                mean = sum(numbers) / len(numbers)
            else:
                total = ""
                mean = ""

            yield row_id, total, mean, missing

    def load(self, results):
        with open("values.csv", "w", newline="", encoding="utf-8") as values_file:
            with open("missing_values.csv", "w", newline="", encoding="utf-8") as missing_file:
                values_writer = csv.writer(values_file)
                missing_writer = csv.writer(missing_file)

                values_writer.writerow(["numer", "suma", "srednia"])
                missing_writer.writerow(["numer", "brakujace_kolumny"])

                for row_id, total, mean, missing in results:
                    values_writer.writerow([row_id, total, mean])
                    if missing:
                        missing_writer.writerow([row_id] + missing)

    def run(self):
        self.load(self.transform(self.extract()))

addresses = [
    "https://oleksandr-fedoruk.com/sggw/podyplomowe/file",
    "https://oleksandr-fedoruk.com/sggw/podyplomowe/404",
    "https://oleksandr-fedoruk.com/sggw/podyplomowe/403",
]

for address in addresses:
    try:
        download_file(address)
        print("Sukces!", address)
    except NotFoundError as error:
        print("Mamy problem, nie ma pliku :(", error)
    except AccessDeniedError as error:
        print("Mamy problem, nie masz uprawnień di tego pliku :(", error)

etl = SimpleETL("latest.txt")
etl.run()
print("Gotowe: zapisano values.csv i missing_values.csv")