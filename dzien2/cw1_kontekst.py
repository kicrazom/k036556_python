
class Logger:
    def __enter__(self):
        print("Start sekcji logowania")

    def __exit__ (self, exc_type, exc_value, exc_tb):
        print("Koniec sekcji logowania")

class FileWriter:
    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.plik = None

    def __enter__(self):
        self.plik = open(self.sciezka, "w")
        return self.plik

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is not None:
            print("Błąd podczas zapisu:", exc_value)
        self.plik.close()

class SafeDivision:
    def __enter__(self):
        return self

    def divide(self, a, b):
        return a / b

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is ZeroDivisionError:
            print("Nie można dzielić przez zero")
            return True


with Logger():
    print ("jestem w środku:")

with FileWriter("cos.txt") as f:
    f.write("tekst testowy\n")

with SafeDivision() as sd:
    print(sd.divide(10, 2))
    print(sd.divide(1, 0))
    print("ta linia sie nie wykona")

print("program doszedl do konca")
