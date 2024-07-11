# Modeling

Данный репозиторий позволяет обучить модель машинного обучения для классификации спутниковых снимков, способную идентифицировать участки незаконной вырубки лесов в бассейне Амазонки.

Структура обучения выглядит следующим образом: 
![image](https://github.com/EugeneRomanov/JMLC_ITMO_2024/assets/72860505/efa21b3d-e0eb-4a79-b1e7-7b8c696d8127)

Основные технологии: Pytorch, OpenCV, Augmentation, Pytorch Lightning, Clear ML, DVC, Flake8. 

## Описание данных
Датасет состоит из 4000 снимков формата .jpg бассейна Амазонки со спутника Planet's Flock 2 станции International Space. Всего на снимках представлено 17 классов явлений, описывающих состояние леса. 

Необходимо решить задачу мульти-классовой классификации снимков. 

## Структура репозитория

Репозиторий содержит несколько модулей:
- configs: файл с конфигом для установки параметров обучения модели.
- src: основные модули используемые для обучения модели.

## Подготовка к обучению модели
Основные команды для запуска обучения модели реализованы в Makefile, что позволяет удобно запускать обучение модели. 

0. Начало работы.

В первую очередь нужно загрузить репозиторий в свою рабочую директорию при помощи GIT.
```bash
git clone https://github.com/EugeneRomanov/JMLC_ITMO_2024.git
```

1. Установка environment.
```bash
make venv
```

2. Установка requirements.
```bash
make install_requirements
```

3. Загрузка данных.
```bash
make download_dataset
```

4. Настройка параметров в [config.yaml](configs/config.yaml) для обучения модели.

5. Настройка логирования экспериментов в ClearML:
    - Регистрация в [ClearML](https://app.community.clear.ml/).
    - [В профиле ClearML](https://app.clear.ml/settings/workspace-configuration) нажми "Create new credentials" и скопируй содержимое.
    - Запусти команду `clearml-init` в твоем терминале.
    - Вставь содержимое credentials

6. Проверка кода на styleguide.

Дополнительно можно проверить код на styleguide при помощи библиотеки Flake8. Для этого установи параметры для [setup.cfg](setup.cfg) и запусти проверку. 
```bash
make lint 
```

## Обучение модели
Запуск обучения модели.
```bash
make train
```

После окончания обучения модели можно посмотреть всю необходимую информацию по эксперименту в личном кабинете [ClearML](https://app.community.clear.ml/). 

Лучший эксперимент можно посмотреть [здесь](https://app.clear.ml/projects/6af89bf5de40410faba201b8130632ce/experiments/07ff5733d5034edea427f7fae84914b2/output/execution).

ЛУчшая модель загружена в DVC и будет использована для создания и деплоя сервиса в данном [репозитории](https://github.com/EugeneRomanov/JMLC_ITMO_2024/tree/main/service).
