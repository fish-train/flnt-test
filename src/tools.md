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

Описание настроек MkDocs:

- [Документация Foliant](https://foliant-docs.github.io/docs/backends/mkdocs/)
- [Документация MkDocs](https://www.mkdocs.org/user-guide/configuration/)