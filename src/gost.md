# Создание документов по ГОСТ

Для создания документов по ГОСТ предназначен набор шаблонов и скриптов **GOSTdown**.

**GOSTdown** создает документы по ГОСТ 19.xxx (ЕСПД) и ГОСТ 7.32 (отчёт о научно-исследовательской работе) в форматах docx из файлов текстовой разметки Markdown.

Подробнее о **GOSTdown** см. в [репозитории](https://gitlab.iaaras.ru/iaaras/gostdown).

## Установка и настройка

1. Убедитесь, что на компьютере установлен Microsoft Word 2010 или выше.
2. Убедитесь, что на компьютере установлен [Pandoc](http://pandoc.org/). По умолчанию **Pandoc** устанавливается в папку `С:\Users\user\AppData\Local\Pandoc`.
3. Откройте компонент «Система» в панели управления: `Панель управления\Все элементы панели управления\Система`.
4. Нажмите на ссылку **Дополнительные параметры системы** в левой панели.
5. Нажмите на кнопку **Переменные среды...**.
6. Убедитесь, что переменная **PATH** содержит путь к папке, в которой установлен **Pandoc**.
7. Скачайте фильтр **pandoc-crossref** из [репозитория](https://github.com/lierdakil/pandoc-crossref/releases).
8. Распакуйте архив и поместите файл **pandoc-crossref.exe** в папку с **Pandoc**.
9. Установите шрифты компании «Паратайп»: [PT Serif, PT Sans и PT Mono](http://rus.paratype.ru/pt-sans-pt-serif).
10. Убедитесь, что на компьютере установлена систем контроля версий [Git](https://git-scm.com/).
11. Запустите **PowerShell** с правами администратора и выполните команду:

    ```
    set-executionpolicy remotesigned
    ```

12. Перейдите в папку, в которую необходимо установить **GOSTdown**, и склонируйте [репозиторий](https://gitlab.iaaras.ru/iaaras/gostdown):

    ```
    git clone https://gitlab.iaaras.ru/iaaras/gostdown.git
    ```

13. Запустите **build-demo-report.bat** и **build-demo-espd.bat**.
14. Убедитесь, что скрипты 

## Создание документов

Чтобы создать документ по ГОСТ 19.xxx (ЕСПД):

1. Скопируйте разработанные MD-файлы в папку с **GOSTdown**.
2. Отредактируйте файлы:

    - **demo-template-espd.docx** - шаблон документа, который содержит титульный лист;
    - **demo-espd-beginning.md** – первая часть документа, которая содержит аннотацию и содержание;
    - **demo-espd-end.md** – последняя часть документа, которая содержит приложения, обозначения и сокращения, список использованных источников.

3. В файле **build-demo-espd.bat**:

    1. Между **demo-espd-beginning.md** и **demo-espd-end.md** перечислите MD-файлы, которые необходимо включить в итоговый документ.
    2. Укажите шаблон. По умолчанию используется файл **demo-template-espd.docx**.
    3. Укажите названия итоговых DOCX- и PDF-файлов.
    4. Чтобы внедрить шрифты в итоговые файлы файл, укажите параметр **embedfonts**.
    
        Пример файла:

        ```
        powershell.exe -command .\build.ps1 ^
        -md demo-espd-beginning.md,index.md,start.md,docs.md,git.md,publish.md,demo-espd-end.md ^
        -template demo-template-espd.docx ^
        -docx test.docx ^
        -pdf test.pdf ^
        -embedfonts
        ```

4. Чтобы включить cdrdjpye. нумерацию рисунков и таблиц, в файле **demo-espd-beginning.md** удалите `chapters: true` из заголовка файла.
5. Запустите **PowerShell** с правами администратора и запустите **build-demo-espd.bat**:

    ```
    .\build-demo-espd.bat
    ```
