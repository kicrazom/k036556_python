import requests


def download_file(url, filename="latest.txt"):
    response = requests.get(url, stream=True)
    with open(filename, "wb") as file:
        file.write(response.content)


download_file("https://oleksandr-fedoruk.com/sggw/podyplomowe/file")
