import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Преобразование и очистка данных.

    Этап Transform в ETL-пайплайне. Функция:
    - приводит типы данных
    - обрабатывает пропущенные значения
    - рассчитывает дополнительные признаки
    - подготавливает данные к анализу и визуализации

    Параметры
    ----------
    df : pd.DataFrame
        DataFrame с исходными данными после этапа Extract.

    Возвращает
    ----------
    pd.DataFrame
        Преобразованный DataFrame.
    """
    df_transformed = df.copy()

    

    return df_transformed
