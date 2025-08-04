import os
import pandas as pd
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
from pathlib import Path
import logging

DATA_DIR = Path("/app/data")

# Загрузка переменных окружения
load_dotenv()

# Настройка подключения
POSTGRES_CONFIG = {
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRES_PORT', '5432'),
    'database': os.getenv('POSTGRES_DB')
}
TABLE_NAME = 'production'


def create_db_engine(): #Создание SQLAlchemy engine
    db_url = f'postgresql://{POSTGRES_CONFIG['user']}:{POSTGRES_CONFIG['password']}@{POSTGRES_CONFIG['host']}:{POSTGRES_CONFIG['port']}/{POSTGRES_CONFIG['database']}'
    return create_engine(db_url)


def load_data_to_db(csv_path: str, engine) -> bool:
    """
    Загрузка данных из CSV в PostgreSQL
    :param csv_path: Путь к CSV-файлу
    :param engine: SQLAlchemy engine
    :return: Статус выполнения
    """
    try:
        df = pd.read_csv(csv_path, parse_dates=['date'], date_format='%Y-%m-%d')

        with engine.connect() as conn:
            # Загрузка данных с заменой существующей таблицы
            df.to_sql(
                name=TABLE_NAME,
                con=conn,
                if_exists='replace',
                index=False,
                method='multi',
                chunksize=1000
            )

        logging.info(f'Successfully loaded {len(df)} rows to {TABLE_NAME}')
        return True

    except exc.SQLAlchemyError as e:
        logging.error(f'Database error: {str(e)}')
        return False
    except Exception as e:
        logging.error(f'Unexpected error: {str(e)}')
        return False


if __name__ == '__main__':
    engine = create_db_engine()
    load_data_to_db(
        csv_path=f'{DATA_DIR}/processed/production_clean.csv',
        engine=engine
    )