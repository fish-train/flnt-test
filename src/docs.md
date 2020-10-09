# Разработка текстов

## Markdown

Документация разрабатывается на языке разметки Markdown.

Подробнее о синтаксисе см. статьи:

- [Официальный сайт](https://daringfireball.net/projects/markdown/syntax)
- [Использование языка разметки Markdown для написания документации](https://docs.microsoft.com/ru-ru/contribute/markdown-reference)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Python-Markdown](https://python-markdown.github.io/)

<anchor>editor_id1</anchor>
Для работы с Markdown можно использовать любой текстовый редактор.
<anchor>editor_id2</anchor>

## Visual Studio Code

При создание этого проекта использовался редактор **Visual Studio Code** с [плагинами](#docs-authoring-pack).

Полезные ссылки:

- [Официальная документация](https://code.visualstudio.com/docs);
- [Вебинар "Настройте Visual Studio Code под свои предпочтения"](https://gitlab.com/svetlnovikova/webinar/-/blob/master/post-webinar-materials.md).

### Плагины

#### Docs Authoring Pack

Набор плагинов содержит:

- [Docs Markdown](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-markdown)
- [Docs Preview](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-preview)
- [Docs YAML](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-yaml)
- [Docs Images](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-images)
- [Docs Metadata](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-metadata)
- [Docs Article Templates](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-article-templates)
- [Docs Linting](https://marketplace.visualstudio.com/items?itemName=docsmsft.docs-linting)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
- [LinkCheckMD](https://marketplace.visualstudio.com/items?itemName=blackmist.LinkCheckMD)

Документация: <https://docs.microsoft.com/en-us/contribute/how-to-write-docs-auth-pack>.

#### Для Markdown

- [HTTP/s and relative link checker](https://marketplace.visualstudio.com/items?itemName=blackmist.LinkCheckMD). Проверяет ссылки;
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one). Горячие клавиши, содержание, превью;
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced). Превью;
- [Markdown Table Formatter](https://marketplace.visualstudio.com/items?itemName=fcrespo82.markdown-table-formatter). Форматирование таблиц;
- [Markdown Table Prettifier](https://marketplace.visualstudio.com/items?itemName=darkriszty.markdown-table-prettify). Форматирование таблиц;
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint). Линтер;
- [Vale](https://marketplace.visualstudio.com/items?itemName=errata-ai.vale-server). Линтер.

#### Для Git

- [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github). Управляет ревью и пулл реквестами;
- [GitLens — Git supercharged](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens). Визуализирует изменения в коде.

#### Остальные

- [colorize](https://marketplace.visualstudio.com/items?itemName=kamikillerto.vscode-colorize). Визуализирует CSS-цвета;
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker). Проверяет орфографию;
- [Russian - Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker-russian). Словарь русского языка для проверки орфографии;
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker);
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio);
- [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop). Поддержка работы с LaTeX;
- [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml);
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python);
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml).

## Добавление страниц

Чтобы добавить страницу в проект **Foliant**:

1. Перейдите в папку **src**.
2. Создайте файл с расширением *.md.
3. Откройте конфигурационный файл **foliant.yml**.
4. Добавьте имя созданного файла в список **chapters**.
