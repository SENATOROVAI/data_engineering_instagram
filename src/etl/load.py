import pandas as pd
from pathlib import Path


def load_data(
    df: pd.DataFrame,
    output_dir: str | Path,
    file_name: str = "instagram_usage_lifestyle_processed"
) -> None:
    """
    Сохранение обработанных данных.

    Этап Load в ETL-пайплайне. Функция:
    - создаёт директорию для processed-данных (если её нет)
    - сохраняет DataFrame в форматах CSV и Parquet

    Параметры
    ----------
    df : pd.DataFrame
        DataFrame после этапа Transform.
    output_dir : str | Path
        Директория для сохранения processed-данных.
    file_name : str
        Базовое имя выходных файлов (без расширения).
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / f"{file_name}.csv"
    parquet_path = output_dir / f"{file_name}.parquet"

    df.to_csv(csv_path, index=False)
    df.to_parquet(parquet_path, index=False)

    print(
        f"Данные сохранены:\n"
        f"- CSV: {csv_path}\n"
        f"- Parquet: {parquet_path}"
    )
