# Docker

Docker - это технология создания контейнеров с открытым исходным кодом, предназначенная для автоматизации развёртывания и управления приложениями. Позволяет «упаковать» приложение со всем его окружением и зависимостями в контейнер.

Установка Docker выполнялась на Windows 7, поэтому потребовался **Docker Toolbox**.

## Быстрый старт

1. Скачайте дистрибутив [Docker Toolbox](https://github.com/docker/toolbox/releases).
2. Установите по [инструкции](https://docs.docker.com/toolbox/toolbox_install_windows/).
3. Убедитесь, что в BIOS включена виртуализация.
4. Запустите **Docker Quickstart Terminal** и выполните команду:
    
    ```
    docker run hello-world
    ```

## Команды

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

## Видео

<iframe width="1583" height="620" src="https://www.youtube.com/embed/QF4ZF857m44" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>