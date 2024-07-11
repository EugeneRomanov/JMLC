# Service

После того, как было обучена модель в данном [репозитории](https://github.com/EugeneRomanov/JMLC_ITMO_2024/tree/main/modelling), мы можем перейти к созданию и деплою сервиса в Gitlab.

Этапы деплоя сервиса представлены на рисунке: 
![image](https://github.com/EugeneRomanov/JMLC_ITMO_2024/assets/72860505/66ed7890-6fbf-4f03-84f3-c902ba60f694)

Основные технологии: FastAPI, Docker, Flake8, Pytest, Gitlab CI/CD, DVC.

## Подготовка окружения
Освновные команды для запуска сервиса реализованы в Makefile.

1. Установка environment.
```bash
make venv
```

2. Установка requirements.
```bash
make install_requirements
```

## Запуск сервиса

```bash
make run_app
```

## Сбор образа

```bash
make build
```

*******


## Linter style code
You can also check your code using linters. Run the command:

```bash
make lint 
```
If you want to change the linter parameters, then configure [setup.cfg](setup.cfg) for yourself


## Service
The launched service is available via this [link]([http://localhost:2444/docs](http://91.206.15.25:1001/docs))
