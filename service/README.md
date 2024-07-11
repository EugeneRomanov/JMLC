# Service

После того, как было обучена модель в данном [репозитории](https://github.com/EugeneRomanov/JMLC_ITMO_2024/tree/main/modelling), можно перейти перейти к созданию и деплою сервиса в Gitlab.

Основные технологии: FastAPI, Docker, Flake8, Pytest, Gitlab CI/CD, DVC.

## Deploy
Основные этапы деплоя сервиса описаны в файле [.gitlab-ci.yml](https://github.com/EugeneRomanov/JMLC_ITMO_2024/blob/main/service/.gitlab-ci.yml) и представлены на схеме: 

![image](https://github.com/EugeneRomanov/JMLC_ITMO_2024/assets/72860505/66ed7890-6fbf-4f03-84f3-c902ba60f694)



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


## Сервис
Задеплоенный сервис доступен по ссылке: http://91.206.15.25:1001/docs
