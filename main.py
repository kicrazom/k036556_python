import requests


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
