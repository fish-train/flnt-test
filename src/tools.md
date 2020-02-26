# Настройка инструментов

В разделе описаны текущие настройки инструментов.

## MkDocs

Настройки **MkDocs** хранятся в файле foliant.yml:

``` yml
mkdocs:
    mkdocs_path: mkdocs
    slug: flnt-test
    use_title: true
    use_chapters: true
    use_headings: true
    default_subsection_title: Expand
    mkdocs.yml:
        repo_name: fish-train/flnt-test
        repo_url: https://github.com/fish-train/flnt-test
        edit_uri: edit/master/src/
        site_name: Docs as Code. Учебный проект
        theme:
            name: 'material'
            logo:
                icon: 'keyboard'
            favicon: img/keyboard.png
            language: 'ru'
            palette:
                primary: 'indigo'
                accent: 'indigo'
        extra:
            search:
                language: 'en, ru'
        markdown_extensions:
            - toc:
                toc_depth: '2-6'
                permalink: true
            - admonition
            - codehilite
            - pymdownx.tasklist:
                custom_checkbox: true
            - pymdownx.details
```

**mkdocs_path**. Путь к файлу mkdocs.exe. По умолчанию путь к исполняемому файлу содержится в переменной окружения **PATH**.

**slug**. Название папки без наименования проекта, в которую локально выгружается сайт. Например, если параметр имеет значение «mkdocs», то имя папки: <название проекта>.mkdocs.

**use_title**. Если параметр имеет значение **true**, то для заголовка сайта используется значение параметра **site_name**. Если **false**, укажите заголовок сайта вручную, иначе MkDocs не сможет создать сайт. Значение по умолчанию **true**. 

**use_chapters**. Если параметр имеет значение **true**, то значения **chapters** из foliant.yml используется как значения **pages** в mkdocs.yml.

**use_headings**. 

**default_subsection_title**. 

**mkdocs.yml**. Параметры из [mkdocs.yml](https://www.mkdocs.org/user-guide/configuration/):

- **repo_name**. Логин пользователя и название репозитория в Git. Например, `fish-train/flnt-test`.

- **repo_url**. 

- **edit_uri**.

- **site_name**. 

- **theme**.

  - **name**. 

  - **logo**. 

    - **icon**. 

  - **favicon**. 

  - **language**. 

  - **palette**. 

    - **primary**. 

    - **accent**. 

- **extra**. 

  - **search**. 

    - **language**. 

- **markdown_extensions**. 

  - **toc**. 

    - **toc_depth**. 

    - **permalink**. 

  - **admonition**. 

  - **codehilite**. 

  - **pymdownx.tasklist**. 

    - **custom_checkbox**. 

  - **pymdownx.details**. 
