import streamlit as st
import pandas as pd
from pathlib import Path


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    """
    Загрузка обработанных данных для Streamlit-приложения.
    """
    return pd.read_csv(path)


def main() -> None:
    st.title("Анализ пользовательской активности в Instagram")

    st.markdown(
        """
        Дашборд демонстрирует основные характеристики и паттерны
        пользовательской активности на основе синтетических данных.
        """
    )

    data_path = Path("data/processed/instagram_usage_lifestyle_processed.csv")

    if not data_path.exists():
        st.error("Файл с обработанными данными не найден. Сначала запустите ETL.")
        return

    df = load_data(data_path)

    st.success(f"Данные загружены: {df.shape[0]} строк, {df.shape[1]} столбцов")
    st.subheader("Фильтр пользователей по уровню активности")

    min_activity = int(df["activity_score"].dropna().min())
    max_activity = int(df["activity_score"].dropna().max())

    activity_range = st.slider(
        "Выберите диапазон activity_score",
        min_value=min_activity,
        max_value=max_activity,
        value=(min_activity, max_activity)
    )

    filtered_df = df[
        (df["activity_score"] >= activity_range[0]) &
        (df["activity_score"] <= activity_range[1])
    ]

    st.write(f"Выбрано пользователей: {filtered_df.shape[0]}")
    st.subheader("Распределение времени в Instagram")

    st.bar_chart(
        filtered_df["daily_active_minutes_instagram"]
        .value_counts()
        .head(20)
    )

    st.dataframe(filtered_df.head())


if __name__ == "__main__":
    main()
