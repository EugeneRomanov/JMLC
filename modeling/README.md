# Modelling

## Описание данных
The dataset contains satellite images of nature representing 17 classes.  Each photo is presented in jpg format. An example of each class can be found in the folder artifacts/class_examples.jpeg

## Структура проекта
First of all, you need to upload the project to your working directory using GIT. 
Run the following command: git clone https://gitlab.deepschool.ru/cvr-dec23/e.romanov/hw_01_modeling.git

The project structure contains the following modules:

- configs: config file foy your work.
- src: main modules used for modeling and inference.

## Подготовка окружения
Makefile allows you to simply get started with this project.

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
4. Настройка параметров в [config.yaml](configs/config.yaml) for you training model.

5. ClearML:
    - Регистрация в [ClearML](https://app.community.clear.ml/).
    - [In your profile ClearML](https://app.community.clear.ml/profile) press "Create new credentials"
    - Run `clearml-init` in you console.
    - Fill out credentials

## Обучение модели

```bash
make train
```

## Проверка кода на styleguide
You can also check your code using linters. Run the command:

```bash
make lint 
```
If you want to change the linter parameters, then configure [setup.cfg](setup.cfg) for yourself

