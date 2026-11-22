# Programowanie w Pythonie cz. II, ćwiczenia z dnia drugiego: context managery, SQLAlchemy, Alembic.

## 1. Spis plików
- cw1_kontekst.py — ćwiczenie 1 (Logger, FileWriter, SafeDivision)
- models.py — modele Experiment, DataPoint, Subject i tabela łącząca (ćwiczenia 2, 4, 6)
- main.py — operacje na bazie: dodawanie, odczyt, aktualizacja, agregacje, usuwanie (ćwiczenia 3, 4, 5)
- migracje/ — dwie migracje Alembica (ćwiczenie 6)

## 2. Uruchomienie
```
git clone https://github.com/kicrazom/k036556_python.git
cd k036556_python
uv sync --all-packages
cd dzien2
uv run alembic upgrade head
uv run python main.py
uv run python cw1_kontekst.py
```


## 3. plik bazy danych ```ekpreymenty.db``` nie jest w repozytorium tworzy go ```alembic upgrade head``` 
