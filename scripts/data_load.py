import logging
import re
from pathlib import Path

import pandas as pd

DATA_DIR = Path("/app/data")

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def preprocess_data(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Предобработка сырых данных из CSV
    :param input_path: Путь к исходному файлу
    :param output_path: Путь для сохранения обработанных данных
    :return: Очищенный DataFrame
    """
    try:
        # Загрузка данных
        df = pd.read_csv(input_path, sep=';', parse_dates=['Date'], date_format='%d.%m.%Y')

        # Преобразование названий столбцов
        df.columns = [clean_column_name(col) for col in df.columns]
        df['oil_volume_tonn'] = df['oil_volume'] * 900 / 1000 # перевод нефти в тонны
        df = df.sort_values('date')

        # Сохранение
        df.to_csv(output_path, index=False)
        logging.info(f'Data saved to {output_path}')
        return df

    except Exception as e:
        logging.error(f'Processing failed: {str(e)}')
        raise


def clean_column_name(col):
    """
    Функция для преобразования названий полей в snake_case без единиц измерений
    """
    col = re.sub(r'\s*\([^)]*\)', '', col)
    col = col.lstrip('\n').lower().replace(' ', '_')
    return col

if __name__ == '__main__':
    preprocess_data(
        input_path=f'{DATA_DIR}/raw/production_raw.csv',
        output_path=f'{DATA_DIR}/processed/production_clean.csv'
    )