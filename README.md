# Programowanie w Pythonie – SGGW 2026/27

Zadanie 1

## Instalacja środowiska

Instalacja uv:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Instalacja Git:

```powershell
winget install --id Git.Git -e
```

```powershell
uv --version
git --version
```

## Utworzeie projektu

```powershell
git clone https://github.com/kicrazom/k036556_python.git
cd k036556_python
uv sync
uv run python main.py
```

## Utwirzenie projektu w IDE PyCharm

1. **File → Open** → folder projektu.
2. Interpreter (prawy dolny róg): `.venv\Scripts\python.exe`.
3. Prawy przycisk na `main.py` → **Run 'main'**.