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

    # Список колонок, которые должны быть числовыми
    numeric_columns = [
        "age",
        "exercise_hours_per_week",
        "sleep_hours_per_night",
        "daily_active_minutes_instagram",
        "sessions_per_day",
        "followers_count",
        "following_count",
        "user_engagement_score",
    ]

    for column in numeric_columns:
        if column in df_transformed.columns:
            df_transformed[column] = pd.to_numeric(
                df_transformed[column],
                errors="coerce"
            )      
            median_value = df_transformed[column].median()
            df_transformed[column] = df_transformed[column].fillna(median_value)
            
    # Расчёт агрегированного показателя активности пользователя
    activity_columns = [
        "daily_active_minutes_instagram",
        "sessions_per_day",
        "followers_count",
        "following_count",
    ]

    existing_activity_columns = [
        col for col in activity_columns if col in df_transformed.columns
    ]

    if existing_activity_columns:
        df_transformed["activity_score"] = (
            df_transformed[existing_activity_columns].sum(axis=1)
        )
    return df_transformed
