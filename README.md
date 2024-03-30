# Lista 3

Każde zadanie należy rozwiązać w osobnym pliku `zadX.py`, gdzie `X` to numer zadania.

Dodatkowo, w przypadku zadań 4 i 5 pojawiają się jeszcze dodatkowe wymagania.

## Zadanie 4

Plik `zad4.py` powinien zawierać dwie funkcje o podanych niżej sygnaturach:

```python
def encode_qr(message: str, qr_code_path: str) -> None:
    ...


def decode_qr(qr_code_path: str) -> str:
    ...
```


## Zadanie 5

Funkcja powinna mieć sygnaturę:

```python   
def is_balanced(input: str) -> bool:
    ...
```

## Uruchominie testów

W celu uruchomienia testów należy wywołać w katalogu głównym polecenie:

```bash
pytest tests
```
Oczywiście wymaga to zainstalowania paczki [`pytest`](https://docs.pytest.org/en/7.1.x/getting-started.html#install-pytest).

Oczekiwanym rezultatem jest 5 sukcesów. :)

