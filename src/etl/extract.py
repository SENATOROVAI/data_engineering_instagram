import pandas as pd
from pathlib import Path


def extract_data(file_path: str | Path) -> pd.DataFrame:
    """
    Загрузка исходных данных из CSV-файла.

    Функция отвечает за этап Extract в ETL-пайплайне:
    - проверяет существование файла
    - загружает данные в pandas DataFrame
    - выводит базовую информацию о размере датасета

    Параметры
    ----------
    file_path : str | Path
        Путь к CSV-файлу с исходными (raw) данными.

    Возвращает
    ----------
    pd.DataFrame
        DataFrame с загруженными данными.
    """
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")

    df = pd.read_csv(file_path)

    print(
        f"Данные успешно загружены: "
        f"{df.shape[0]} строк, {df.shape[1]} столбцов"
    )

    return df
