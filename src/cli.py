import argparse
from pathlib import Path

from src.etl.pipeline import run_pipeline


def parse_arguments() -> argparse.Namespace:
    """
    Разбор аргументов командной строки.

    Возвращает
    ----------
    argparse.Namespace
        Объект с аргументами командной строки.
    """
    parser = argparse.ArgumentParser(
        description="Запуск ETL-пайплайна для анализа Instagram-данных"
    )

    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Путь к CSV-файлу с исходными данными"
    )

    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Директория для сохранения обработанных данных"
    )

    return parser.parse_args()


def main() -> None:
    """
    Точка входа для CLI.
    """
    args = parse_arguments()

    run_pipeline(
        input_path=Path(args.input),
        output_dir=Path(args.output)
    )


if __name__ == "__main__":
    main()
