# Service

## Описание 
После того, как было обучена модель в данном [репозитории](https://github.com/EugeneRomanov/JMLC_ITMO_2024/tree/main/modelling), можно перейти перейти к созданию и деплою сервиса в Gitlab.

Основные технологии: FastAPI, Docker, Flake8, Pytest, Gitlab CI/CD, DVC.

## Deploy
Основные этапы деплоя сервиса описаны в файле [.gitlab-ci.yml](https://github.com/EugeneRomanov/JMLC_ITMO_2024/blob/main/service/.gitlab-ci.yml) и представлены на схеме: 

![image](https://github.com/EugeneRomanov/JMLC_ITMO_2024/assets/72860505/66ed7890-6fbf-4f03-84f3-c902ba60f694)

Список основных этапов и их краткое соедржание: 
  - prepare: загрузка весов модели из DVC.
  - build: сбор образа Docker-контейнера. 
  - lint: проверка кода на style guide при помощи Flake8.
  - tests: проверка кода на юнит и интеграционных тестах. 
  - deploy: деплой сервиса в FastAPI. 

## Сервис
Задеплоенный сервис доступен по ссылке: http://91.206.15.25:1001/docs
