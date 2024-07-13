# Service
 
После того, как было обучена модель в данном [репозитории](https://github.com/EugeneRomanov/JMLC_ITMO_2024/tree/main/modelling), можно перейти перейти к созданию и деплою сервиса в Gitlab.

Основные технологии: FastAPI, Docker, Flake8, Pytest, Gitlab CI/CD, DVC.

## Структура репозитория

Репозиторий содержит несколько модулей:
- config: файл с конфигом для запуска сервиса.
- deploy/ansible: вспомогательные команды для деплоя сервиса.
- example_ansible: модуль для тестирования сервиса.
- src: основные модули, которые описывают функционал сервиса.
- tests: unit/integration тесты для кода сервиса.
- weights: папка, куда скачиваются веса модели из DVC. 


## Запуск и деплой сервиса
Основные этапы деплоя сервиса описаны в файле [.gitlab-ci.yml](https://github.com/EugeneRomanov/JMLC_ITMO_2024/blob/main/service/.gitlab-ci.yml) и представлены на схеме: 

![image](https://github.com/EugeneRomanov/JMLC_ITMO_2024/assets/72860505/66ed7890-6fbf-4f03-84f3-c902ba60f694)

Список основных этапов и их краткое содержание: 
  - prepare: загрузка весов модели из DVC.
  - build: сбор образа Docker-контейнера. 
  - lint: проверка кода на style guide при помощи Flake8.
  - tests: проверка кода на unit/integration тестах. 
  - deploy: деплой сервиса в FastAPI. 

## Сервис
Задеплоенный сервис доступен по ссылке: http://91.206.15.25:1001/docs

Сервис имеет 3 метода: 

- прогнозирование класса.
- прогнозирование вероятности.
- вывод списка классов.

Пример работы сервиса:
![Мультимедиа3](https://github.com/user-attachments/assets/a7794565-186e-416f-bfd6-c7df6fcb35f0)
