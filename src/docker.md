# Использовани Foliant через Docker

Docker – это технология создания контейнеров с открытым исходным кодом, предназначенная для автоматизации развёртывания и управления приложениями. Позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер.

Установка Docker выполнялась на Windows 7, поэтому потребовался **Docker Toolbox**.

## Быстрый старт

1. Скачайте дистрибутив [Docker Toolbox](https://github.com/docker/toolbox/releases).
2. Установите по [инструкции](https://docs.docker.com/toolbox/toolbox_install_windows/).
3. Убедитесь, что в BIOS включена виртуализация.
4. Запустите **Docker Quickstart Terminal** и выполните команду:
    
    ```
    docker run hello-world
    ```

## Установка Foliant через Docker

```
docker pull foliant/foliant:full
```

Страница Foliant на [Docker Hub](https://hub.docker.com/r/foliant/foliant).

## Запуск Foliant через Docker

1. Заполнить dockerfile:

    ```dockerfile
    FROM foliant/foliant:full
    
    RUN mkdir -p /usr/src/app/
    WORKDIR /usr/src/app/
    
    COPY . /usr/src/app/
    COPY foliant.yml /usr/src/app/
    
    COPY requirements.txt .
    RUN pip3 install -r requirements.txt
    
    ```

2. Заполнить docker-compose.yaml:

    ```dockerfile
    version: '3'
    services:
      site:
        build:
          context: .
        working_dir: /usr/src/app
        command: make site
      pdf:
        build:
          context: .
        working_dir: /usr/src/app
        command: make pdf
    ```

3. Собрать образ: `docker-compose build`.
4. Создать сайт: `docker-compose run --rm site make site --with mkdocs`.
5. Создать PDF-файл: `docker-compose run --rm pdf make pdf`.

## Команды Docker

### Посмотреть образы

```
docker images
```

### Посмотреть контейнеры

```
docker ps
```

### Создать образ

```
docker build [OPTIONS] PATH | URL | -
```

### Удалить образ

```
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

### Удалить все образы

```
docker rmi $(docker images -q)
```

### Запустить приложение

```
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

### Удалить контейнер

```
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

### Удалить все контейнеры

```
docker rm $(docker ps -a -q)
```

### Запустить приложение и удалить контейнер

```
docker run --rm IMAGE
```

### Запустить приложение с указанием порта на компьютере, где запускается docker, и порта в контейнере

```
docker run --rm --name ИМЯ -p 8081:8081 IMAGE
```

## Видео об основах Docker

<iframe width="1583" height="620" src="https://www.youtube.com/embed/QF4ZF857m44" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>