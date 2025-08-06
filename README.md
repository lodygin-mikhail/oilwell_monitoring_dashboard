# 🛢️ Oil Production Data Pipeline | Визуализация данных добычи


Этот проект представляет собой **конвейер данных** для обработки и анализа показателей добычи нефти. Данные загружаются из CSV, обрабатываются Python-скриптами, сохраняются в **PostgreSQL** и визуализируются в **Metabase**.  

---

## 📌 О проекте

Автоматизированный пайплайн для работы с данными месторождений:
- 📂 Загрузка "грязных" CSV из различных источников
- 🧹 Предобработка (очистка, нормализация)
- 🗄️ Загрузка в PostgreSQL и визуализация в Metabase
- 📊 Готовые дашборды для анализа динамики

---

## Структура проекта

```text
oil-production-pipeline/
├── 📂 data/                    
│   ├── 📂 raw/                 # Исходные CSV-файлы
│   └── 📂 processed/           # Предобработанные данные
├── 📂 scripts/
│   ├── 🐍 data_load.py         # Очистка и трансформация данных
│   └── 🐍 load_to_postgres.py  # Загрузка в PostgreSQL
├── 📂 dashboards               # Примеры визуализаций
├── 🐳 docker-compose.yml       # Конфигурация сервисов
├── 🐋 Dockerfile               # Образ приложения
├── 📜 requirements.txt         # Зависимости Python
└── 📖 README.md                # Документация
```

---

⚙️ Технологии
- Python (Pandas, SQLAlchemy, Psycopg2)
- PostgreSQL (хранение данных)
- Metabase (визуализация)
- Docker (контейнеризация)

---
## 🚀 Быстрый старт

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/lodygin-mikhail/oilwell_production_data_pipeline.git
cd oilwell_production_data_pipeline
```

2. **Поместите CSV-файл в `data/raw/` с именем `production_raw.csv`**
Формат данных:
```csv
Date;Oil volume (m3/day);Volume of liquid (m3/day);Gas volume (m3/day);Water volume (m3/day);Water cut (%);Working hours;Dynamic level (m);Reservoir pressure (atm);
01.01.2017;49;70;13055;21;29;24;1819;214;
02.01.2017;49;70;13055;21;29;24;1836;214;
```

3. **Запустите контейнеры**
```bash
docker-compose up --build
```
---

🔐 Конфигурация окружения (.env)
Проект использует переменные окружения для безопасного хранения чувствительных данных. Для работы проекта необходимо создать файл `.env` на основе шаблона `.env.example`

**Как использовать:**
1. **Скопируйте шаблон:**
   ```bash
   cp .env.example .env
   ```
2. **Заполните переменные** в созданном .env файле:
- Откройте файл в текстовом редакторе
- Замените значения-заглушки (например `your_db_username`) на реальные данные
- Сохраните файл

---

📈Пример дашборда в Metabase

![Dashboard Preview](dashboards/oil_production_dashboard.png)
