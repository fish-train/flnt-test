# Использование Foliant через Docker

Docker – это технология создания контейнеров с открытым исходным кодом, предназначенная для автоматизации развёртывания и управления приложениями. Позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер.

Установка Docker выполнялась на Windows 7, поэтому потребовался **Docker Toolbox**.

## Быстрый старт

1. Скачайте дистрибутив [Docker Toolbox](https://github.com/docker/toolbox/releases).
2. Установите по [инструкции](https://docs.docker.com/toolbox/toolbox_install_windows/).
3. Убедитесь, что в BIOS включена виртуализация.
4. Запустите **Docker Quickstart Terminal** и выполните команду:

    ```powershell
    docker run hello-world
    ```

## Установка Foliant через Docker

```powershell
docker pull foliant/foliant:full
```

Страница Foliant на [Docker Hub](https://hub.docker.com/r/foliant/foliant).

## Запуск Foliant через Docker

1. Заполнить dockerfile:

    ```
    FROM foliant/foliant:full
    COPY requirements.txt .
    RUN pip3 install -r requirements.txt
    COPY ./ /usr/src/app/
    ```

2. Заполнить docker-compose.yaml:

    ```
    version: '3'
    services:
      foliant:
        build:
          context: ./
          dockerfile: ./Dockerfile
      bash:
        build:
          context: ./
          dockerfile: ./Dockerfile
        entrypoint: /bin/bash
    ```

3. Собрать образ: `docker-compose build`.

4. Создать сайт: `docker-compose run --rm foliant make site --with mkdocs`.

5. Посмотреть ИД последнего контейнера: `docker ps -a`.

6. Скопировать папку с сайтом из контейнера: `docker cp <ИД контейнера>:flnt-test.mkdocs \<Папка на локальном компьютере>`.

## Команды Docker

### Посмотреть образы

```powershell
docker images
```

### Посмотреть контейнеры

```powershell
docker ps
```

### Создать образ

```powershell
docker build [OPTIONS] PATH | URL | -
```

### Удалить образ

```powershell
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

### Удалить все образы

```powershell
docker rmi $(docker images -q)
```

### Запустить приложение

```powershell
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

### Удалить контейнер

```powershell
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```

### Удалить все контейнеры

```powershell
docker rm $(docker ps -a -q)
```

### Запустить приложение и удалить контейнер

```powershell
docker run --rm IMAGE
```

### Запустить приложение с указанием порта на компьютере, где запускается docker, и порта в контейнере

```powershell
docker run --rm --name ИМЯ -p 8081:8081 IMAGE
```

## Видео об основах Docker

<iframe width="1583" height="620" src="https://www.youtube.com/embed/QF4ZF857m44" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
