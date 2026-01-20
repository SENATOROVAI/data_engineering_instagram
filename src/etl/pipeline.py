from pathlib import Path

from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_data


def run_pipeline(
    input_path: str | Path,
    output_dir: str | Path
) -> None:
    """
    Запуск полного ETL-пайплайна.

    Функция последовательно выполняет этапы:
    Extract → Transform → Load.

    Параметры
    ----------
    input_path : str | Path
        Путь к CSV-файлу с исходными данными.
    output_dir : str | Path
        Директория для сохранения обработанных данных.
    """
    df_raw = extract_data(input_path)
    df_transformed = transform_data(df_raw)
    load_data(df_transformed, output_dir)
