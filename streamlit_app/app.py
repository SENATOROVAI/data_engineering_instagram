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

    st.dataframe(df.head())


if __name__ == "__main__":
    main()
