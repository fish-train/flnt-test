# Сборка и публикация документации

## HTML

### Выбор и настройка шаблона MkDocs

По умолчанию проект **Foliant** конвертируется в HTML с помощью шаблона **mkdocs**.

Чтобы сменить шаблон:

1. Выберите шаблон на странице [MkDocs Themes](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes).
2. Установите шаблон. Например, шаблон **Materials**:

    ```
    pip install mkdocs-material
    ```

3. Откройте конфигурационный файл **foliant.yml** и добавьте строки:

    ```
    theme:
          name: 'material'
    ```

Шаблон настраивается в файле **foliant.yml**. Описание параметров см. в документации для конкретного шаблона. Например, для шаблона **Materials** см. статью [Getting Started](https://squidfunk.github.io/mkdocs-material/getting-started/#configuration).

При необходимости можно создать собственный шаблон. Подробнее см. статью [Custom themes](https://www.mkdocs.org/user-guide/custom-themes/).

### Локальная сборка сайта

Чтобы локально собрать сайт:

1. Выполните команду: 

     ```
     foliant make site --with mkdocs
     ```

    В папке проекта создается папка "<Название проекта>.mkdocs".

2. Перейдите в папку с сайтом: 
    
    ```
    cd flnt-test.mkdocs
    ```

3. Запустите веб-сервер:
    
    ```
    python -m http.server
    ```

4. В браузере откройте страницу: <http://localhost:8000/>.

### Публикация на GitHub

Чтобы опубликовать сайт на GitHub:

1. Откройте настройки репозитория и перейдите в раздел **Danger Zone**.
2. Убедитесь, что ваш репозиторий публичный. Если нет, нажмите на кнопку **Make public**.
3. Перейдите в раздел **GitHub Pages** и в выпадающем списке **Source** выберите ветку **gh-pages branch**.

    ![](img/publishing-source-drop-down.png)

1. Выполните команду:

   ```
   foliant make ghp -p \my-project
   ```

## PDF

### md-to-pdf

Библиотека [md-to-pdf](https://github.com/simonhaenisch/md-to-pdf) генерирует PDF-файлы, которые можно настроить с помощью CSS и [highlight.js](https://github.com/highlightjs/highlight.js).

Чтобы создать PDF-файл, выполните команду:

```
foliant make pdf --with mdtopdf
```

### Pandoc

[Pandoc](https://pandoc.org/) — универсальная утилита для работы с текстовыми форматами.

Чтобы создать PDF-файл, выполните команду:
```
foliant make docx -p \my-project --with pandoc
```

## DOCX

DOCX-файлы создаются с помощью Pandoc.

Чтобы создать DOCX-файл, выполните команду:

```
foliant make docx -p my-project
```
